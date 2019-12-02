import queue
def createMaze():
    maze = []
    maze.append(["#","O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"])
    return maze


def printMaze(maze, path=""): #Print maze and solution from correct path
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i += 1

        elif move == "R":
            i -= 1

        elif move == "U":
            j += 1

        elif move == "D":
            j -= 1
        pos.add((j, i)) #add path to array range.
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves): #Check obstacle and out of range of map from each of path.
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
    i = start
    j = 0 
    for move in moves:
        if move == "L":
            i += 1

        elif move == "R":
            i -= 1

        elif move == "U":
            j += 1

        elif move == "D":
            j -= 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    return True


def findGoal(maze, moves):  #Check path to goal from queue.  if path is correct this function will be return True.
    #initial Start point
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    #Move follow queue(moves)
    for move in moves:
        if move == "L":
            i += 1

        elif move == "R":
            i -= 1

        elif move == "U":
            j += 1

        elif move == "D":
            j -= 1
    #check goal from last point after move. 
    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True
    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()
count = 0
while not findGoal(maze, add): 
    print(add)
    add = nums.get()
    for j in ["L", "R", "U", "D"]: #try to put Direction to queue
        put = add + j
        if valid(maze, put):   # Check obstacle with each of j from queue(put).
            nums.put(put) #put Direction to queue.
    count = count + 1