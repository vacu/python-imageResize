###Python image resizer
Creates a thumbnail for the selected image maintaining the ratio.
The generated image will be named as image-name.thumb.ext

###Params
* -thumb - Creates a thumb based on the image type (portrait / landscape)
* -crop - Crops the image

###Usage
    python resize-image.py <param> <image> <size>

The \<size> argument is based on the image type.
If the image is landscape then the image will be resized based on the width and the other way around if it's portrait.
