from PIL import Image

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

im = Image.open("C:\\Users\\Maxime Zehnder\\Desktop\\Pictures\\picture1.jpg")
print(im.size, im.format, im.mode)
print(im.format)

im = rotate_box(im)

im2 = Image.open("C:\\Users\\Maxime Zehnder\\Desktop\\Pictures\\picture1.jpg")
im2 = rotate_box(im2)

im.show()
im2.show()

#exercise -> opem all 4 images, rotete them or make them gray

import code

def to_grayscale(an_image):
    grayscale_im = an_image.convert("L")
    return grayscale_im

pic_list = code.get_filenames("C:\\Users\\Maxime Zehnder\\Desktop\\pictures")
for pic_name in pic_list:
    im = Image.open(pic_name)
    im = rotate_box(im) #or im = to_grayscale(im) -> to make the picture gray
    im = to_grayscale(im) # function that turns the image gray
    im.show()

#opening an image, turn it gray and safe it somewhere else
im = Image.open("C:\\Users\\Maxime Zehnder\\Desktop\\pictures\\picture1.jpg")
im = to_grayscale(im)
im.show