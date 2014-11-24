"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""
"""Filter 1:  CSUMBify"""

def CSUMBify():
  """Adds CSUMB-esque features to image: Wave border, school colors, otter mascot, and text"""
  pic = makePicture(pickAFile())
  #return error if chosen image dimensions are less than 200 pixels
  if (getWidth(pic) < 200) or (getHeight(pic) < 200):
    print "I'm sorry. Picture dimensions must be greater than 200 pixels."
    return 1 
  pic = CSUMBBlend(pic)
  pic = dkbCopy(makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\otter.jpg"), pic, 20, getHeight(pic)-77)
  pic = addBorder(pic)
  pic = text(pic)
  show(pic)
  return pic

def addBorder(pic):
  """adds wave border to pic"""
  #load border images
  border = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\waveborder.jpg")
  bottomLeft = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\bottomleft.jpg")
  bottomRight = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\bottomright.jpg")
  topLeft = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\topleft.jpg")
  topRight = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\topright.jpg")
  borderDim=getHeight(border) #square image
  cornerDim=getHeight(bottomLeft) #square image
  #bottom border
  targetX = 0
  targetY = getHeight(pic)-getHeight(border)
  for i in range(int(getWidth(pic)/borderDim)): #int to prevent image falling out of range
    for x in range (0, getWidth(border)):
      for y in range (0, getHeight(border)):
        color = getColor(getPixel(border, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + borderDim
  #rotate wave border for top border
  border180 = makeEmptyPicture(getWidth(border), getHeight(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(border180, getWidth(border)-x-1, getHeight(border)-y-1), px)
  #topborder
  targetX = 0
  targetY = 0
  for i in range(0, int(getWidth(pic)/borderDim)): #int to prevent image falling out of range
    for x in range(0, getWidth(border180)):
      for y in range(0, getHeight(border180)):
        color = getColor(getPixel(border180, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + borderDim
  #rotate wave border for right border
  borderCW = makeEmptyPicture(getHeight(border), getWidth(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(borderCW, y, getWidth(border)-x-1), px)
  #rightborder
  targetX = getWidth(pic) - borderDim
  targetY = 0
  for i in range(0, int(getHeight(pic)/borderDim)): #int to prevent image falling out of range
    for x in range(0, getWidth(borderCW)):
      for y in range(0, getHeight(borderCW)):
        color = getColor(getPixel(borderCW, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetY = targetY + borderDim
  #rotate wave border for right border
  borderCCW = makeEmptyPicture(getHeight(border), getWidth(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(borderCCW, getHeight(border)-y-1, x), px)
  #leftborder
  targetX = 0
  targetY = 0
  for i in range(0, int(getHeight(pic)/borderDim)): #int to prevent image falling out of range
    for x in range(0, getWidth(borderCCW)):
      for y in range(0, getHeight(borderCCW)):
        color = getColor(getPixel(borderCCW, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetY = targetY + borderDim
  #add corner images
  #top left
  targetX = 0
  targetY = 0
  for x in range(0, getWidth(topLeft)):
    for y in range(0, getHeight(topLeft)):
      color = getColor(getPixel(topLeft, x, y))
      if distance(color, white) > 200.0:
        setColor(getPixel(pic, x+targetX, y+targetY), color)
  #top right
  targetX = getWidth(pic)-cornerDim
  targetY = 0
  for x in range(0, getWidth(topRight)):
    for y in range(0, getHeight(topRight)):
      color = getColor(getPixel(topRight, x, y))
      if distance(color, white) > 200.0:
        setColor(getPixel(pic, x+targetX, y+targetY), color)
  #bottom left
  targetX = 0
  targetY = getHeight(pic)-cornerDim
  for x in range(0, getWidth(bottomLeft)):
    for y in range(0, getHeight(bottomLeft)):
      color = getColor(getPixel(bottomLeft, x, y))
      if distance(color, white) > 200.0:
        setColor(getPixel(pic, x+targetX, y+targetY), color)
  #bottom right
  targetX = getWidth(pic)-cornerDim
  targetY = getHeight(pic)-cornerDim
  for x in range(0, getWidth(bottomRight)):
    for y in range(0, getHeight(bottomRight)):
      color = getColor(getPixel(bottomRight, x, y))
      if distance(color, white) > 200.0:
        setColor(getPixel(pic, x+targetX, y+targetY), color)
  return pic

def CSUMBBlend(pic):  
  #blends CSUMB school colors into image in 3 vertical stripes
  bayBlue = makeColor(0, 34, 84)
  goldenSand = makeColor(143, 134, 79)
  valleyGreen = makeColor(0, 119, 81)
  amount = 0.5
  for x in range(0, getWidth(pic)/3):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newBBRed = 0*amount + getRed(pixel)*(1-amount)
      newBBGreen = 34*amount + getGreen(pixel)*(1-amount)
      newBBBlue = 84*amount + getBlue(pixel)*(1-amount)
      newColor = makeColor(newBBRed, newBBGreen, newBBBlue)
      setColor(pixel, newColor)
  for x in range(getWidth(pic)/3, getWidth(pic)*2/3):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newGSRed = 143*amount + getRed(pixel)*(1-amount)
      newGSGreen = 134*amount + getGreen(pixel)*(1-amount)
      newGSBlue = 79*amount + getBlue(pixel)*(1-amount)
      newColor = makeColor(newGSRed, newGSGreen, newGSBlue)
      setColor(pixel, newColor)
  for x in range(getWidth(pic)*2/3, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newVGRed = 0*amount + getRed(pixel)*(1-amount)
      newVGGreen = 110*amount + getGreen(pixel)*(1-amount)
      newVGBlue = 81*amount + getBlue(pixel)*(1-amount)
      newColor = makeColor(newVGRed, newVGGreen, newVGBlue)
      setColor(pixel, newColor)
  return pic
  
def dkbCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding dark blue"""
  dkblue = makeColor(25, 49, 75)
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, dkblue) > 50.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target  
  
#Text
def text(pic):
  #define style for images with width < 300
  if getWidth(pic) < 300:
    text = makeStyle(sansSerif, bold, 20)
    addTextWithStyle(pic, getWidth(pic)-110 , getHeight(pic)-25, "CSUMB", text, black) 
    addTextWithStyle(pic, getWidth(pic)-106, getHeight(pic)-29, "CSUMB", text, white)
  #define style for images with width >= 300
  else:
    text = makeStyle(sansSerif, bold, 40)
    addTextWithStyle(pic, getWidth(pic)-194, getHeight(pic)-30, "CSUMB", text, black) 
    addTextWithStyle(pic, getWidth(pic)-190, getHeight(pic)-34, "CSUMB", text, white)
  return pic
