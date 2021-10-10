#TIC TAC TOE game board Logic 

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
x = "X"
playing = True
winner = None




def game():

  gameboard()
  while playing:
    turn(x)
    gameover()
    switch()
  if winner == "X" or winner == "O":
    print("***  "+winner + " IS THE WINNER !!! *** ")
  elif winner == None:
    print("** IT`S A DRAW !! **")


def gameboard():
  print("\n")
  print ("Select The Number Equivalent To The Spot")
  print("\n")
  print("1|2|3    " + board[0] + " | " + board[1] + " | " + board[2] )
  print("4|5|6    " + board[3] + " | " + board[4] + " | " + board[5] )
  print("7|8|9    " + board[6] + " | " + board[7] + " | " + board[8] )
  print("\n")


def turn(player):
  print(player + "'s turn.")
  position = input("Choose a Spot  :  ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Spot must be from 1-9  : ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("That Spot is Taken !! Go again  :  ")
  board[position] = player
  gameboard()


def gameover():
  victory()
  tie()


def victory():
  global winner
  rwinner = rows()
  cwinner = columns()
  dwinner = diagonals()
  if rwinner:
    winner = rwinner
  elif cwinner:
    winner = cwinner
  elif dwinner:
    winner = dwinner
  else:
    winner = None



def rows():
  global playing
  r1 = board[0] == board[1] == board[2] != "-"
  r2 = board[3] == board[4] == board[5] != "-"
  r3 = board[6] == board[7] == board[8] != "-"
  if r1 or r2 or r3:
    playing = False
  if r1:
    return board[0] 
  elif r2:
    return board[3] 
  elif r3:
    return board[6] 
  else:
    return None

def columns():
  global playing
  c1 = board[0] == board[3] == board[6] != "-"
  c2 = board[1] == board[4] == board[7] != "-"
  c3 = board[2] == board[5] == board[8] != "-"
  if c1 or c2 or c3:
    playing = False
  if c1:
    return board[0] 
  elif c2:
    return board[1] 
  elif c3:
    return board[2] 
  else:
    return None


def diagonals():
  global playing
  d1 = board[0] == board[4] == board[8] != "-"
  d2 = board[2] == board[4] == board[6] != "-"
  if d1 or d2:
    playing = False
  if d1:
    return board[0] 
  elif d2:
    return board[2]
  else:
    return None


def tie():
  global playing
  if "-" not in board:
    playing = False
    return True
  else:
    return False
def switch():
  global x
  if x == "X":
    x = "O"
  elif x == "O":
    x = "X"

print("WELCOME TO TIC TAC TOE")
game()
