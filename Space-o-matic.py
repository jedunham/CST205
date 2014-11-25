"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""

def spaceomatic():
  """TEXT DESCRIBING FILTER"""
  pic = makePicture(pickAFile())
  pic = spaceBlend(pic)
  pic = addBorder(pic)
     
  show(pic)
  return pic

def spaceBlend(pic):  
  width = getWidth(pic)
  height = getHeight(pic)
  spacePic = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\spacebg.jpg")
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
  
def addBorder(pic):
  """Adds a border to an image"""
  borderColor = makeColor(0, 42, 225)
  #top border
  for x in range (0, getWidth(pic)):
    for y in range (0, 15):
      px = getPixel(pic, x, y)
      setColor(px, borderColor)
  #bottom border
  for x in range (0, getWidth(pic)):
    for y in range (getHeight(pic)-15, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, borderColor)
  #left border
  for x in range (0, 15):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, borderColor)
  #right border
  for x in range (getWidth(pic)-15, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, borderColor)
  show(pic)
  return pic

def grCopy(source, target, targetX, targetY):
  """copies a picture onto a target picture excluding green"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, green) > 165.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target
                  