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


#MIT License

Copyright (c) 2013

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        
          
