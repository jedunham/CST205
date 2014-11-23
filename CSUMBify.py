"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""

def CSUMBify():
  """TEXT DESCRIBING FILTER"""
  pic = makePicture(pickAFile())
  border = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\waveborder.jpg")
  pic = addBorder(pic, border)
 
  return pic

def addBorder(pic, border):
  """adds wave border to pic"""
  #bottomborder
  borderDim=30
  targetX = 0
  targetY = getHeight(pic)-getHeight(border)
  for i in range(int(getWidth(pic)/borderDim)):
    for x in range (0, getWidth(border)):
      for y in range (0, getHeight(border)):
        color = getColor(getPixel(border, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + borderDim
  #rotate wave border 180°
  border180 = makeEmptyPicture(getWidth(border), getHeight(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(border180, getWidth(border)-x-1, getHeight(border)-y-1), px)
  #topborder
  targetX = 0
  targetY = 0
  for i in range(0, int(getWidth(pic)/borderDim)):
    for x in range(0, getWidth(border180)):
      for y in range(0, getHeight(border180)):
        color = getColor(getPixel(border180, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + borderDim
  #rotate wave border 90° CW
  borderCW = makeEmptyPicture(getHeight(border), getWidth(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(borderCW, y, getWidth(border)-x-1), px)
  #rightborder
  targetX = getWidth(pic) - borderDim
  targetY = 0
  for i in range(0, int(getHeight(pic)/borderDim)):
    for x in range(0, getWidth(borderCW)):
      for y in range(0, getHeight(borderCW)):
        color = getColor(getPixel(borderCW, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetY = targetY + borderDim
  show(pic)
  return pic  

#need to rotatePicLeft(border):

#need to rotatePicRight(border):




def grCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding green"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, green) > 165.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target

def whCopy(source, target, targetX, targetY):
  """copy a picture onto a target picture excluding white"""
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      if distance(color, white) > 125.0:
        setColor(getPixel(target, x+targetX, y+targetY), color)
  return target  