import sys, os, Image

class ImageHelper:
  def __init__(self):
    self.data = [];

  def createThumb(self, imageFile, thumbSize):
    # landscape
    if imageFile.size[0] > imageFile.size[1]:
      if int(thumbSize) > imageFile.size[1]:
        if imageFile.format is 'JPEG':
          imageFile = imageFile.rotate(180, expand=True);

      imageFile.thumbnail((int(thumbSize), int(imageFile.size[1])), Image.ANTIALIAS);
    # portrait
    else:
      imageFile.thumbnail((int(imageFile.size[0]), int(thumbSize)), Image.ANTIALIAS);

    return imageFile;

  # imageType can be image (by default) or the filename in case we are passing the folder
  def saveFile(self, imageFile, filePath, customName, imageType = 'image'):
    if customName is not None:
      filename = '.thumb.' + customName;
    else:
      filename = '.thumb';

    if imageType == 'image':
      return imageFile.save(
        os.path.splitext(filePath)[0] + filename + os.path.splitext(filePath)[1],
        imageFile.format,
        quality=100
      );
    else:
      return imageFile.save(
        sys.argv[2] + os.path.splitext(imageType)[0] + filename + os.path.splitext(imageType)[1],
        imageFile.format,
        quality=100
      );
