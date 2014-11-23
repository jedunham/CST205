"""Midterm Pair Programmers:  Jennifer Dunham and Hyo Lee"""

def CSUMBify():
  """TEXT DESCRIBING FILTER"""
  pic = makePicture(pickAFile())
  border = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 4\midterm\sourceimages\waveborder.jpg")
  pic = addBorder(pic, border)
  #target = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 3\Lab7\Thanksgiving Card\Image Library\leavesbg.jpg")
  
  #target = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 3\Lab7\Thanksgiving Card\Image Library\leavesbg.jpg")
  #target = grCopy(source1, target, 93, 14)
  #source2 = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 3\Lab7\Thanksgiving Card\Image Library\\turkey.jpg")
  #target = grCopy(source2, target, 300, 220)
  #source3 = makePicture("C:\Users\whitenebula\Documents\School\CSUMB\CST 205\Module 3\Lab7\Thanksgiving Card\Image Library\cornucopia.png")
  #target = whCopy(source3, target, 189, 311)
  #myFont1 = makeStyle("Gill Sans Ultra Bold Condensed", bold, 15)
  #fontColor1 = makeColor(204, 102, 0)
  #myFont2 = makeStyle("Lucida Calligraphy", bold, 16)
  #fontColor2 = makeColor(102, 0, 102)
  #str1 = "Thank you for"
  #str2 = "not eating me!"
  #str3 = "Gobble gobble!"
  #addTextWithStyle(target, 350, 264, str1, myFont1, fontColor1)
  #addTextWithStyle(target, 348, 283, str2, myFont1, fontColor1)
  #addTextWithStyle(target, 348, 303, str3, myFont1, fontColor1)
  #str4 = "From Jennifer Dunham"
  #addTextWithStyle(target, 7, 471, str4, myFont2, fontColor2)
  #show(target)
  #return target
  return pic

def addBorder(pic, border):
  """adds wave border to pic"""
  #bottomborder
  targetX = 0
  targetY = getHeight(pic)-getHeight(border)
  for i in range(int(getWidth(pic)/30)):
    for x in range (0, getWidth(border)):
      for y in range (0, getHeight(border)):
        color = getColor(getPixel(border, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + 30
  #rotate wave border 180°
  border180 = makeEmptyPicture(getWidth(border), getHeight(border))
  for x in range(0, getWidth(border)):
    for y in range(0, getHeight(border)):
      px = getColor(getPixel(border, x, y))
      setColor(getPixel(border180, getWidth(border)-x-1, getHeight(border)-y-1), px)
  #topborder
  targetX = 0
  targetY = 0
  for i in range(0, int(getWidth(pic)/30)):
    for x in range(0, getWidth(border180)):
      for y in range(0, getHeight(border180)):
        color = getColor(getPixel(border180, x, y))
        if distance(color, white) > 75.0:
          setColor(getPixel(pic, x+targetX, y+targetY), color)
    targetX = targetX + 30
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