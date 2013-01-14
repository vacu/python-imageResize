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
    if imageType == 'image':
      if len(sys.argv) > 4:
        # if the 4th param is not null then append it to the filename
        if sys.argv[4] is not None:
          imageFile.save(
            os.path.splitext(sys.argv[2])[0] + '.thumb.' + sys.argv[4] + os.path.splitext(sys.argv[2])[1],
            imageFile.format,
            quality=100
          );
      # if there are not more than 4 params than create the thumb
      else:
        imageFile.save(
          os.path.splitext(sys.argv[2])[0] + '.thumb' + os.path.splitext(sys.argv[2])[1],
          imageFile.format,
          quality=100
        );
    else:
      if len(sys.argv) > 4:
        # if the 4th param is not null then append it to the filename
        if sys.argv[4] is not None:
          imageFile.save(
            sys.argv[2] + os.path.splitext(imageType)[0] + '.thumb.' + sys.argv[4] + os.path.splitext(imageType)[1],
            imageFile.format,
            quality=100
          );
      # if there are not more than 4 params than create the thumb
      else:
        imageFile.save(
          sys.argv[2] + os.path.splitext(imageType)[0] + '.thumb' + os.path.splitext(imageType)[1],
          imageFile.format,
          quality=100
        );
