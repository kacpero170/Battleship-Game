from random import randint
print("")
print("The numbers of rows and columns are 0-4.")
board = []

size = 5
for x in range(0, size):
  board.append(["O"] * size)

def print_board(board):
  for row in board:
    print(" ".join(row))
print("")
print_board(board)
print("")

def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print("Turn", turn + 1)
  print("")

  while True:
    try:
      guess_row = int(input("Please enter a row number: "))
      guess_col = int(input("Please enter a column number: "))
      print("")
    except ValueError:
      print("Please enter a valid integer row and column number.")
      print("")
    break

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(size) or \
      guess_col not in range(size):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print("")
    print_board(board)
    print("")

    if turn == 3:
      print("Game Over.")
      print("")
