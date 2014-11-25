"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""
"""Filter 1:  CSUMBerize"""

def CSUMBerize(pic):
  """Adds CSUMB-esque features to image: Wave border, school colors, otter mascot, and text"""
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
  topLeft = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\\topleft.jpg")
  
  #declare variables
  borderDim=getHeight(border)     #square image
  cornerDim=getHeight(topLeft) #square image
  
  #bottom border
  targetX = 0
  targetY = getHeight(pic)-getHeight(border)
  for i in range(int(getWidth(pic)/borderDim)): #int to prevent image falling out of range
    pic = whCopy(border, pic, targetX, targetY, 75.0)
    targetX = targetX + borderDim
  
  #rightborder
  borderRight = rotatePic(border)
  targetX = getWidth(pic) - borderDim
  targetY = 0
  for i in range(0, int(getHeight(pic)/borderDim)): #int to prevent image falling out of range
    pic = whCopy(borderRight, pic, targetX, targetY, 75.0)
    targetY = targetY + borderDim
  
  #topborder
  borderTop = rotatePic(borderRight)
  targetX = 0
  targetY = 0
  for i in range(0, int(getWidth(pic)/borderDim)): #int to prevent image falling out of range
    pic = whCopy(borderTop, pic, targetX, targetY, 75.0)
    targetX = targetX + borderDim
  
  #leftborder
  borderLeft = rotatePic(borderTop)
  targetX = 0
  targetY = 0
  for i in range(0, int(getHeight(pic)/borderDim)): #int to prevent image falling out of range
    pic = whCopy(borderLeft, pic, targetX, targetY, 75.0)
    targetY = targetY + borderDim
  
  #add corner images
  #top left
  targetX = 0
  targetY = 0
  pic = whCopy(topLeft, pic, targetX, targetY, 200.0)
  #bottom left
  targetX = 0
  targetY = getHeight(pic)-cornerDim
  bottomLeft = rotatePic(topLeft)
  pic = whCopy(bottomLeft, pic, targetX, targetY, 200.0)
  #bottom right
  targetX = getWidth(pic)-cornerDim
  targetY = getHeight(pic)-cornerDim
  bottomRight = rotatePic(bottomLeft)
  pic = whCopy(bottomRight, pic, targetX, targetY, 200.0)
  #top right
  targetX = getWidth(pic)-cornerDim
  targetY = 0
  topRight = rotatePic(bottomRight)
  pic = whCopy(topRight, pic, targetX, targetY, 200.0)
  
 
  return pic

def CSUMBBlend(pic):  
  """blends CSUMB school colors into image in 3 vertical stripes"""
  amount = 0.5
  for x in range(0, getWidth(pic)/3):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newBBRed = 0*amount + getRed(pixel)*(1-amount)      #r = 0 in Bay Blue
      newBBGreen = 47*amount + getGreen(pixel)*(1-amount) #g = 47 in Bay Blue
      newBBBlue = 93*amount + getBlue(pixel)*(1-amount)   #b = 93 in Bay Blue
      newColor = makeColor(newBBRed, newBBGreen, newBBBlue)
      setColor(pixel, newColor)
  for x in range(getWidth(pic)/3, getWidth(pic)*2/3):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newGSRed = 132*amount + getRed(pixel)*(1-amount)     #r = 132 in Golden Sand
      newGSGreen = 114*amount + getGreen(pixel)*(1-amount) #g = 114 in Golden Sand
      newGSBlue = 72*amount + getBlue(pixel)*(1-amount)    #b = 72 in Golden Sand
      newColor = makeColor(newGSRed, newGSGreen, newGSBlue)
      setColor(pixel, newColor)
  for x in range(getWidth(pic)*2/3, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      px = getColor(pixel)
      newVGRed = 0*amount + getRed(pixel)*(1-amount)       #r = 0 in Valley Green
      newVGGreen = 120*amount + getGreen(pixel)*(1-amount) #g = 120 in Valley Green
      newVGBlue = 86*amount + getBlue(pixel)*(1-amount)    #b = 86 in Valley Green
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

def whCopy(source, target, targetX, targetY, dist):
  """copy a picture onto a target picture excluding white"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, white) > dist:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target    

def rotatePic(pic):
  """rotates pic 90° counterclockwise"""
  newpic = makeEmptyPicture(getHeight(pic), getWidth(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getColor(getPixel(pic, x, y))
      setColor(getPixel(newpic, y, getWidth(pic)-x-1), px)
  return newpic

#Text
def text(pic):
  """Adds "CSUMB" text to image"""
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
