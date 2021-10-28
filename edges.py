from PIL import Image, ImageFilter
before = Image.open('justine.jpg')
after = before.filter(ImageFilter.FIND_EDGES)
after.save('test.jpg')