#!/usr/bin/env python

import sys, os, Image, ExifTags
# custom functions
import helpers

# instantiate the class
imgHelper = helpers.ImageHelper();

if len(sys.argv) > 1:
  # image file
  if sys.argv[1] != '-folder':
    imageFile = Image.open(sys.argv[2]);
    imageX = imageFile.size[0] / 2;
    imageY = imageFile.size[1] / 2;

  # SINGLE FILE
  if sys.argv[1] == '-image':
    imgHelper.createThumb(imageFile);
    imgHelper.saveFile(imageFile);
  # FOLDER
  elif sys.argv[1] == '-folder':
    for root, dirs, files in os.walk(sys.argv[2]):
      for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
          imageFile = Image.open(sys.argv[2] + file);
          imgHelper.createThumb(imageFile);
          imgHelper.saveFile(imageFile, file);
  # CROP
  elif sys.argv[1] == '-crop':
    size = sys.argv[3];
    box = (imageX - (int(size) / 2), imageY - (int(size) / 2), imageX + int(size), imageY + int(size));
    region = imageFile.crop(box);

    region.save(
      os.path.splitext(sys.argv[2])[0] + '.thumb' + os.path.splitext(sys.argv[2])[1],
      imageFile.format
    );
