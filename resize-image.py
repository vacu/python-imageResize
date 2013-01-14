import sys, os, Image, ExifTags

# image file
if sys.argv[1] != '-test':
  imageFile = Image.open(sys.argv[2]);
  imageX = imageFile.size[0] / 2;
  imageY = imageFile.size[1] / 2;

if len(sys.argv) > 1:
  # THUMB
  if sys.argv[1] == '-thumb':
    # landscape
    if imageFile.size[0] > imageFile.size[1]:
      if sys.argv[3] < imageFile.size[1]:
        if imageFile.format is 'JPEG':
          imageFile = imageFile.rotate(180, expand=True);

      imageFile.thumbnail((int(sys.argv[3]), int(imageFile.size[1])), Image.ANTIALIAS);
    # portrait
    else:
      imageFile.thumbnail((int(imageFile.size[0]), int(sys.argv[3])), Image.ANTIALIAS);

    # check if we have more than 4 params
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
  # CROP
  elif sys.argv[1] == '-crop':
    size = sys.argv[3];
    box = (imageX - (int(size) / 2), imageY - (int(size) / 2), imageX + int(size), imageY + int(size));
    region = imageFile.crop(box);

    region.save(
      os.path.splitext(sys.argv[2])[0] + '.thumb' + os.path.splitext(sys.argv[2])[1],
      imageFile.format
    );
  elif sys.argv[1] == '-test':
    for root, dirs, files in os.walk(sys.argv[2]):
      for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
          imageFile = Image.open(sys.argv[2] + file);

          if imageFile.size[0] > imageFile.size[1]:
            if sys.argv[3] < imageFile.size[1]:
              if imageFile.format is 'JPEG':
                imageFile = imageFile.rotate(180, expand=True);

            imageFile.thumbnail((int(sys.argv[3]), int(imageFile.size[1])), Image.ANTIALIAS);
          # portrait
          else:
            imageFile.thumbnail((int(imageFile.size[0]), int(sys.argv[3])), Image.ANTIALIAS);

          imageFile.save(
            sys.argv[2] + os.path.splitext(file)[0] + '.thumb' + os.path.splitext(file)[1],
            imageFile.format,
            quality=100
          );
