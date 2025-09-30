#maze = [9][4]
import random
maze = [[-1 for _ in range(4)] for _ in range(9)]

#for x in range(9):
#    for y in range(4):
#        maze[x][y] = -1

maze[0][1] = 1
maze[1][1] = 2
maze[1][2] = 4
maze[1][3] = 0
maze[2][2] = 5
maze[2][3] = 1
maze[3][1] = 4
maze[3][2] = 6
maze[4][0] = 1          
maze[4][3] = 3
maze[5][0] = 2
maze[6][0] = 3
maze[6][1] = 7
maze[7][1] = 8
maze[7][3] = 6
maze[8][3] = 7

room = 0
direction = [0, 1, 2, 3]

def changeRoom(room, direction):
    while room < 8:
        y = random.randrange(4)
        room = 0
        if maze[room][y] == -1:
            print('You have hit a wall.')
            room  # stay in same room
        else:
            newRoom = maze[room][y]
            print(f'You moved from room {room} to room {newRoom}.')
            # return newRoom
            room = newRoom

# Directions: 0 = North, 1 = East, 2 = South, 3 = West
room = changeRoom(room, direction) 