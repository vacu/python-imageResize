import sys, os, Image, ExifTags

# image file
imageFile = Image.open(sys.argv[1]);

imageX = imageFile.size[0] / 2;
imageY = imageFile.size[1] / 2;


if len(sys.argv) > 3:
  size = sys.argv[3];
  box = (imageX - (int(size) / 2), imageY - (int(size) / 2), imageX + int(size), imageY + int(size));
  region = imageFile.crop(box);

  region.save(
    os.path.splitext(sys.argv[1])[0] + '.thumb' + os.path.splitext(sys.argv[1])[1],
    imageFile.format
  )
else:
  if imageFile.size[0] > imageFile.size[1]:
    imageFormat = 'landscape';
  else:
    imageFormat = 'portrait';

  if imageFormat == 'landscape':
    if sys.argv[2] < imageFile.size[1]:
      if imageFile.format is 'JPEG':
        imageFile = imageFile.rotate(180, expand=True);

    imageFile.thumbnail((int(sys.argv[2]), int(imageFile.size[1])), Image.ANTIALIAS);
  else:
    imageFile.thumbnail((int(imageFile.size[0]), int(sys.argv[2])), Image.ANTIALIAS);

  imageFile.save(
    os.path.splitext(sys.argv[1])[0] + '.thumb' + os.path.splitext(sys.argv[1])[1],
    imageFile.format,
    quality=100
  )
