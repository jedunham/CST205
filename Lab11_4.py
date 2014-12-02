# Lab #11
# Wannabe Zork game


def game():
  welcome()
  gameOver = false
  global gameOver
  userInput = requestString("Type 'play' to begin or 'exit' to leave")
  global userInput
  inventory = ""
  global inventory
  lockedDoor = "locked"
  global lockedDoor
  
  while not gameOver:
    if userInput.lower() == "play":
      porch()
    elif userInput.lower() == "exit":
      exit()
      gameOver = true
    elif userInput.lower() == "help":
      welcome()
      game()
    else:
      printNow("")
      printNow("Invalid command")
      game()
  else:
    gameOver = true
    

def welcome():
  printNow("") 
  printNow("*** Welcome to Lost Land ***")
  printNow("Choose a direction to begin your adventure")
  printNow("Type north, south, east, or west to move in those directions")
  printNow("Type help to redisplay this introduction")
  printNow("Type exit to quit at any time")

   
def exit():
  printNow("")
  printNow("Better luck next time")
  

def porch():
  printNow("") 
  printNow("----------PORCH----------")
  printNow("You are at the front door of dark house")
  printNow("A pack of hungry dogs are barking and running towards you")
  printNow("You can go north into the house or fight off the pack of hungry dogs")
  
  userInput = requestString("Choose your direction wisely")
  global gameOver
  global inventory
  
  while not gameOver:
    if userInput.lower() == "north":
      printNow("")
      printNow("Good choice!")
      livRoom()
    elif userInput.lower() == "exit":
      exit()
      gameOver = true
    elif userInput.lower() == "help":
      welcome()
      porch()
    else:
      printNow("")
      printNow("No time to hesitate")
      printNow("You have been eaten by the pack of hungry dogs!")
      game()
  else:
    gameOver = true
  
  
def livRoom():
  global gameOver
  global inventory
  global lockedDoor
  printNow("")
  printNow("--------LIVING ROOM--------")
  printNow("You are in the living room")   
  printNow("To the east is the kitchen")
  printNow("To the north is a staircase")
  if lockedDoor == "locked":
    printNow("To the west is a locked door")
    
    userInput = requestString("Choose your direction wisely")

  
    while not gameOver:  
      if userInput.lower() == "north":
        printNow("")
        printNow("You are going up the stairs")
        upstairs()
      elif userInput.lower() == "east":
        printNow("")
        printNow("You are walking east")
        kitchen()
      elif userInput.lower() == "west":
        printNow("")
        printNow("The door is locked")
        livRoom()
      elif userInput.lower() == "south":
        printNow("")
        printNow("You went back outside to the hungry dogs")
        porch()
      elif userInput.lower() == "exit":
        exit()
        gameOver = true      
      elif userInput.lower() == "help":
        welcome()
        livRoom()  
      elif (userInput.lower() == "unlock door" or userInput.lower() == "unlock door with key" or userInput.lower() == "use key on door"):
        if "key" in inventory:
          printNow("\nThe bloody key fits nicely in this lock.")
          printNow("The door unlocks!")
          lockedDoor = "unlocked"
          livRoom()
        else:
          printNow("\nThis lock does not appear to be influenced by wishful thinking.")
          livRoom()
      else:
        printNow("")
        printNow("Invalid command")
        livRoom()
    else:
      gameOver = true
  else:
    printNow("To the west is an unlocked door")
    
    userInput = requestString("Choose your direction wisely")

  
    while not gameOver:  
      if userInput.lower() == "north":
        printNow("")
        printNow("You are going up the stairs")
        upstairs()
      elif userInput.lower() == "east":
        printNow("")
        printNow("You are walking east")
        kitchen()
      elif userInput.lower() == "west":
        printNow("")
        printNow("You open the door and are walking west")
        #library() 
        kitchen() #temporarily redirecting to kitchen until library function is ready.
      elif userInput.lower() == "south":
        printNow("")
        printNow("You went back outside to the hungry dogs")
        porch()
      elif userInput.lower() == "exit":
        exit()
        gameOver = true      
      elif userInput.lower() == "help":
        welcome()
        livRoom()  
      else:
        printNow("")
        printNow("Invalid command")
        livRoom()
    else:
      gameOver = true
  
def kitchen():
  printNow("")
  printNow("----------KITCHEN----------")
  printNow("You are in the kitchen.")
  printNow("On the floor is a streak of blood that leads east to an open door.")
  printNow("The blood is very slippery. You see something laying in it. It looks like a key.")
  printNow("To go back to the living room go west")
  # add room that attaches to kitchen
  
  userInput = requestString("Choose your direction wisely")
  global gameOver
  global inventory
  
  while not gameOver:
    if userInput.lower() == "east":
      backyard()
    elif userInput.lower() == "west":
      livRoom()
    elif userInput.lower() == "south":
      printNow("")
      printNow("There's a wall there")
      kitchen()
    elif userInput.lower() == "north":
      printNow("")
      printNow("There's a wall there")
      kitchen()
    elif userInput.lower() == "exit":
      exit()
      gameOver = true      
    elif userInput.lower() == "help":
      welcome()
      kitchen()
    elif ((userInput.lower() == "take key") or (userInput.lower() == "get key") or (userInput.lower() == "key")):
      inventory += " " + "key"
      printNow("\nYou pick up the bloody key.")
      printNow(inventory) #test print
      kitchen()
    else:
      printNow("")
      printNow("Invalid command")
      kitchen()
  else:
   gameOver = true   
  

def backyard():
  printNow("")
  printNow("----------BACKYARD----------")
  printNow("You went outside to the backyard and were eaten by the pack of hungry dogs")
  # create objective to close door to stop dogs from coming into house
  game()
  
def upstairs():
  printNow("")
  printNow("----------UPSTAIRS----------")
  printNow("You are upstairs")
  printNow("Oddly there is only one door to the north")
  printNow("To go back downstairs head south")
  
  userInput = requestString("Choose your direction wisely")
  global gameOver
  global inventory
  
  while not gameOver:
    if userInput.lower() == "north":
      upstairsRoom()
    elif userInput.lower() == "south":
      livRoom()
    elif userInput.lower() == "east":
      printNow("")
      printNow("There's a wall there")
      upstairs()
    elif userInput.lower() == "west":
      printNow("")
      printNow("There's a wall there")
      upstairs()
    elif userInput.lower() == "exit":
      exit()
      gameOver = true      
    elif userInput.lower() == "help":
      welcome()
      upstairs()
    else:
      printNow("")
      printNow("Invalid command")
      upstairs()
  else:
    gameOver = true
  
def upstairsRoom():
  printNow("")
  printNow("-------UPSTAIRS BEDROOM-------")
  printNow("You are in the bedroom upstairs")
  printNow("There appears to be nothing here, but a bed and nightstand")
  printNow("Go south to get back to the living room")
  # create objective to find key on nightstand to open locked door in livRoom
  # add additional bedroom that attaches to this one
  
  userInput = requestString("Choose your direction wisely")
  global gameOver
  global inventory
  
  while not gameOver:
    if userInput.lower() == "south":
      livRoom()
    elif userInput.lower() == "north":
      printNow("")
      printNow("There's a wall there")
      upstairsRoom() 
    elif userInput.lower() == "east":
      printNow("")
      printNow("There's a wall there")
      upstairsRoom()    
    elif userInput.lower() == "west":
      printNow("")
      printNow("There's a wall there")
      upstairsRoom()
    elif userInput.lower() == "exit":
      exit()
      gameOver = true      
    elif userInput.lower() == "help":
      welcome()
      upstairsRoom()
    else:
      printNow("")
      printNow("Invalid command")
      upstairsRoom()
  else:
    gameOver = true
      
      
  
  
