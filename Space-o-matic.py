"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""

def spaceomatic():
  """TEXT DESCRIBING FILTER"""
  pic = makePicture(pickAFile())
  pic = spaceBlend(pic)
     
  show(pic)
  return pic

def spaceBlend(pic):  
  width = getWidth(pic)
  height = getHeight(pic)
  spacePic = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\spacebg2.jpg")
  blendPic = makeEmptyPicture(width, height)
  amount = 0.5
  for x in range(0, width):
    for y in range(0, height):
      targetPx = getPixel(blendPic, x, y)
      px1 = getPixel(pic, x, y)
      px2 = getPixel(spacePic, x, y)
      r1, g1, b1 = getRed(px1), getGreen(px1), getBlue(px1)
      r2, g2, b2 = getRed(px2), getGreen(px2), getBlue(px2)
      blendColor = makeColor((r1+r2)/2, (g1+g2)/2, (b1+b2)/2)
      setColor(targetPx, blendColor)
  return blendPic