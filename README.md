###Python image resizer
Creates a thumbnail for the selected image maintaining the ratio.
The generated image will be named as image-name.thumb.ext

###Params
* -image - Creates a thumb based on the image type (portrait / landscape)
* -folder - Creates thumbs for all the images in the specified folder
* -crop - Crops the image

###Usage
    python resize-image.py <param> <image/folder> <size> <string>

If the last parameter is specified then the created thumb will include the string as well:

  Ex: python resize-image.py <param> <image/folder> <size> randomstring

Will generate a file that has \<filename>.thumb.randomstring.\<extension>

The \<size> argument is based on the image type.
If the image is landscape then the image will be resized based on the width and the other way around if it's portrait.

### Notes:
Crop parameter doesn't work with folder or appending a random string to the file.
