from PIL import Image, ImageGrab
from ocr import ocr_baidu as ocr


image = ImageGrab.grabclipboard()
if image is None:
    print("无法从剪贴板获取图片，请先将图片复制到剪贴板")
    exit(0)
if isinstance(image, list):
    image = Image.open(image[0])
result = ocr(image)
if result is None:
    print("识别失败")
    exit(0)
with open("grid-text.txt", "w", encoding="utf-8") as f:
    f.writelines(text + "\n" for text in result)
