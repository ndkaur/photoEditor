from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

# take all the images from imgs floder 
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    edit = img.filter(ImageFilter.MedianFilter)

    # increasing the contrast 
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')



# autocontrast()
# colorize()
# crop()
# scale()
# SupportsGetMesh
# deform()
# equalize()
# expand()
# flip()
# grayscale()
# invert()
# mirror()
# posterize()
# solarize()
# exif_transpose()