###Python image resizer
Creates a thumbnail for the selected image maintaining the ratio.
The generated image will be named as image-name.thumb.ext

###Usage
    python resize-image.py <image file> <height or width> <crop size>

If <b>\<crop size></b> is not specified it will create a thumbnail otherwise it will crop the image

The <b>\<height or width></b> argument is based on the image type.
If the image is landscape then the image will be resized based on the width and the other way around if it's portrait
