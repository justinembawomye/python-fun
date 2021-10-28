from PIL import Image, ImageFilter
before = Image.open('justine.jpg')
after = before.filter(ImageFilter.BoxBlur(50))
after.save('out.jpg')