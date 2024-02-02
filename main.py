import os # To import test image files
import cv2 # To work with opencv images
from PIL import Image # Image submodule to work with pillow images
import pytesseract as pt # pytesseract module

test_img_path = "../test images/"
create_path = lambda f : os.path.join(test_img_path, f)

test_image_files = os.listdir(test_img_path)

for f in test_image_files:
    print(f)
    
def show_image(img_path, size=(500, 500)):
    image = cv2.imread(img_path)
    image = cv2.resize(image, size)
    
    cv2.imshow("IMAGE", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # provide full path to tesseract.exe
    
 # using cmd: tesseract --list-langs
avb_langs = pt.get_languages(config='')

for lang in avb_langs:
    print(lang)
image_path = test_image_files[12] # 2, 3, 12, 1, 13, 15
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_string(image)

print(text)
show_image(path)

path = create_path("portu-text-2.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='por')

print(text)
show_image(path)

img_name_txt_file = "../test images/image-paths.txt"
text = pt.image_to_string(img_name_txt_file, lang='jpn')

print(text)

path = create_path("news-2.jpg")

image = Image.open(path)
text = 'NO TEXT TO BE APPEARED'

try:
    text = pt.image_to_string(image, lang='eng', timeout=5)
except RuntimeError as timeout_error:
    print("[TIMEOUT ERROR]")

print(text)
show_image(path)

path = create_path("jap-text-1.png")

image = Image.open(path)
bound_rects = pt.image_to_boxes(image, lang='jpn')

print(bound_rects)
show_image(path)

img = cv2.imread(path)
h, _, _ = img.shape

for b in bound_rects.splitlines():
    b = b.strip().split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow("CHARACTERIZED IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_path = test_image_files[2]
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_data(image)

print(text)
show_image(path)

image_path = "hindi-text-1.jpg" # news-2.jpg hindi-news-1.jpg hindi-news-2.jpg hindi-text-1.jpg
path = create_path(image_path)

print(pt.image_to_osd(path, lang='hin'))

image_path = "news-2.jpg"
path = create_path(image_path)
file_save_path = "../files/"

pdf = pt.image_to_pdf_or_hocr(path, extension='pdf')

file = open(os.path.join(file_save_path, "pdf-content.pdf"), 'w+b')
file.write(pdf)
file.close()

# hocr: open standard of data representation for formatted text obtained from (OCR)
hocr = pt.image_to_pdf_or_hocr(path, extension='hocr')

file = open(os.path.join(file_save_path, "hocr-content.html"), 'w+b')
file.write(hocr)
file.close()

xml = pt.image_to_alto_xml(path)

file = open(os.path.join(file_save_path, "xml-content.xml"), 'w+b')
file.write(xml)
file.close()

image_path = "abc-text.jpg"
path = create_path(image_path)
custom_oem_psm_config = r'--oem 3 --psm 9'

image = Image.open(path)
pt.image_to_string(image, config=custom_oem_psm_config)

   