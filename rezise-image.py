import sys, os, Image, ExifTags

# image file
imageFile = Image.open(sys.argv[1])
# set height and width
imageWidth = imageFile.size[0]
imageHeight = imageFile.size[1]

# if second parameter is present
# assign it as width
if len(sys.argv) > 2:
  imageWidth = sys.argv[2]

# if third parameter is present
# assing it as height
if len(sys.argv) > 3:
  imageHeight = sys.argv[3]

if imageHeight is not None and imageWidth is not None:
  # if format of the image is jpg
  if imageFile.format is 'JPEG':
    # rotate the image 180 degrees so we get it straight
    exif = dict((ExifTags.TAGS[k], v) for k, v in imageFile._getexif().items() if k in ExifTags.TAGS)
    if exif['Orientation']:
      imageFile = imageFile.rotate(180, expand=True)

  imageFile.thumbnail((int(imageWidth), int(imageHeight)), Image.ANTIALIAS)
  imageFile.save(
    os.path.splitext(sys.argv[1])[0] + '.thumb' + os.path.splitext(sys.argv[1])[1],
    imageFile.format,
    quality=100
  )

