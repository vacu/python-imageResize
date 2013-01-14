def createThumb(imageFile, newFile, fileFormat):
  return imageFile.save(newFile, fileFormat, quality=100);
