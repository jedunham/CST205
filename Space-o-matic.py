"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""
"""Filter 2:  Space-o-matic"""

def spaceomatic():
  """Creates a space-themed image"""
  pic = makePicture(pickAFile()) #REMOVE AND ADD PIC TO PARAMETER BEFORE SUBMITTING ASSIGNMENT
  #return error if chosen image dimensions are above maximum tolerance
  if (getWidth(pic) > 1700) or (getHeight(pic) > 1071):
    print "I'm sorry. Picture dimensions must be less than 1700 pixels width and 1071 pixels height."
    return 1 
  pic = spaceBlend(pic)
  ulplanet = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\planetul.jpg")
  urplanet = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\planetur.jpg")
  llplanet = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\planetll.jpg")
  lrplanet = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\planetlr.jpg")
  pic = grCopy(ulplanet, pic, 20, 20)
  pic = grCopy(urplanet, pic, getWidth(pic)-20-getWidth(urplanet), 20)
  pic = grCopy(llplanet, pic, 20, getHeight(pic)-20-getHeight(llplanet))
  pic = grCopy(lrplanet, pic, getWidth(pic)-20-getWidth(lrplanet), getHeight(pic)-20-getHeight(lrplanet))
  pic = addBorder(pic)
     
  show(pic)
  return pic

def spaceBlend(pic):  
  """Blends source image with a space image"""
  width = getWidth(pic)
  height = getHeight(pic)
  spacePic = makePicture(r"C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\spacebg.jpg")
  blendPic = makeEmptyPicture(width, height)
  for x in range(0, width):
    for y in range(0, height):
      targetPx = getPixel(blendPic, x, y)
      px1 = getPixel(pic, x, y)
      px2 = getPixel(spacePic, x, y)
      r1 = getRed(px1)
      g1 = getGreen(px1)
      b1 = getBlue(px1)
      r2 = getRed(px2)
      g2 = getGreen(px2)
      b2 = getBlue(px2)
      blendColor = makeColor((r1+r2)/2, (g1+g2)/2, (b1+b2)/2)
      setColor(targetPx, blendColor)
  return blendPic
  
def addBorder(pic):
  """Adds a border to an image"""
  #main border 
  mainBorder = makeColor(0, 42, 225)
  #top border
  for x in range (0, getWidth(pic)):
    for y in range (0, 15):
      px = getPixel(pic, x, y)
      setColor(px, mainBorder)
  #bottom border
  for x in range (0, getWidth(pic)):
    for y in range (getHeight(pic)-15, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, mainBorder)
  #left border
  for x in range (0, 15):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, mainBorder)
  #right border
  for x in range (getWidth(pic)-15, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, mainBorder)
  #Inner accent border 
  innerBorder = makeColor(0, 204, 204)
  #top border
  for x in range (0, getWidth(pic)):
    for y in range (6, 10):
      px = getPixel(pic, x, y)
      setColor(px, innerBorder)
  #bottom border
  for x in range (0, getWidth(pic)):
    for y in range (getHeight(pic)-10, getHeight(pic)-6):
      px = getPixel(pic, x, y)
      setColor(px, innerBorder)
  #left border
  for x in range (6, 10):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, innerBorder)
  #right border
  for x in range (getWidth(pic)-10, getWidth(pic)-6):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      setColor(px, innerBorder)
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
                  