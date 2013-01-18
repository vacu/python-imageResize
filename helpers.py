import sys, os, Image, ExifTags

class ImageHelper:
  def __init__(self):
    self.data = [];

  def createThumb(self, imageFile):
    # landscape
    if imageFile.size[0] > imageFile.size[1]:
      if sys.argv[3] < imageFile.size[1]:
        if imageFile.format is 'JPEG':
          imageFile = imageFile.rotate(180, expand=True);

      imageFile.thumbnail((int(sys.argv[3]), int(imageFile.size[1])), Image.ANTIALIAS);
    # portrait
    else:
      imageFile.thumbnail((int(imageFile.size[0]), int(sys.argv[3])), Image.ANTIALIAS);

  # imageType can be image (by default) or the filename in case we are passing the folder
  def saveFile(self, imageFile, imageType = 'image'):
    if len(sys.argv) > 4:
      if sys.argv[4] is not None: filename = '.thumb.' + sys.argv[4];
    else:
      filename = '.thumb';

    if imageType == 'image':
      imageFile.save(
        os.path.splitext(sys.argv[2])[0] + filename + os.path.splitext(sys.argv[2])[1],
        imageFile.format,
        quality=100
      );
    else:
      imageFile.save(
        sys.argv[2] + os.path.splitext(imageType)[0] + filename + os.path.splitext(imageType)[1],
        imageFile.format,
        quality=100
      );
