# textadventure
currentroom = 1

invRoom0 = []
invRoom1 = ["baloon"] 
invRoom2 = ["longsword", "key"]
invRoom3 = []
invRoom4 = ["matches"]
invRoom5 = []
invRoom6 = []


room0 = ["In a dark space. How did you end up here?", "stop", "stop", "stop", "stop", invRoom0]
room1 = ["On a road that goes east and west. There is a shed to the north.", 2, 3, "stop", 4, invRoom1]
room2 = ["In a shed. The shed is empty. There is a road to the south.", "stop", "stop", 1, "stop", invRoom2]
room3 = ["On a road that leads east and west.", "stop", "stop","stop", 1, invRoom3]
room4 = ["On a road that leads east and west.", "stop", 1, "stop", 5, invRoom4]
room5 = ["Outside a cave", "stop", 4, "stop", 6, invRoom5]
room6 = ["In a cave", "stop", 5, "stop", "stop", invRoom6]
rooms = [room0, room1, room2, room3, room4, room5, room6]
playerinventory = []
itemName = "that"


def ChangeRoom(roomnumber):
       global currentroom
       currentroom = roomnumber

def addToInventory(item):
        playerinventory.append(item)

def getDescription(roomnumber):
       return rooms[roomnumber][0]

def describeItems(roomnumber):
       if not (rooms[roomnumber][5] == []):
         print ("You see a")
         for x in range(len(rooms[roomnumber][5] )): 
              print (rooms[roomnumber][5][x],) 

def listInventory():
       if (playerinventory == []):
         print("Your backpack is empty")
       else:
         print ("You have")
         for x in range(len(playerinventory)): 
              print (playerinventory[x],) 



def moveToRoom(movecommand):
          mycurrentroom = currentroom
          if movecommand == "n" or movecommand == "north":
             if rooms[mycurrentroom][1] == "stop":
                print("You can't go that way")
             else:
                  ChangeRoom(rooms[mycurrentroom][1])

#                  print (getDescription(mycurrentroom))
          if movecommand == "e" or movecommand == "east":
               if rooms[mycurrentroom][2] == "stop":
                  print("You can't go that way")
               else:
                   ChangeRoom(rooms[mycurrentroom][2])
                  
          if movecommand == "s" or movecommand == "south":
             if rooms[mycurrentroom][3] == "stop":
                  print("You can't go that way")
             else:
                   ChangeRoom(rooms[mycurrentroom][3])
#                  
          if movecommand == "w" or movecommand == "west":
               if rooms[mycurrentroom][4] == "stop":
                  print("You can't go that way")
               else:
                     ChangeRoom(rooms[mycurrentroom][4])
                   

    
      
numberofmoves = 0
while numberofmoves < 10:     
  print (getDescription(currentroom))
  describeItems(currentroom)
  
  movecommand = input("What do you want to do?")
  if movecommand == "w" or movecommand == "west" or movecommand == "s" or movecommand == "south" or movecommand == "e" or movecommand == "east" or movecommand == "n" or movecommand == "north":
    moveToRoom(movecommand)
  if movecommand[:5] == "take " or movecommand[:5] == "Take ":
    itemName = movecommand[-(len(movecommand)-5):]
    if itemName in rooms[currentroom][5]:
      rooms[currentroom][5].remove(itemName)
      addToInventory(itemName)
      listInventory()
    else:
     print("I cant find " + itemName + " here")
  if movecommand[:10] == "inventory" or movecommand[:5] == "Inventory":
        listInventory()

    
  numberofmoves = numberofmoves + 1


