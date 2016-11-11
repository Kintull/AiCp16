from time import sleep
import math

init_point = (10,10)
dest_point = (90,90)
square_block = (50,50,70,70)
zone = (0,0,100,100)
neighbour = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
unchecked_pool = []
checked_pool = {}
checked_pool[init_point] = 0
unchecked_pool.append(init_point)
distance = 0
def inSquare(point, square):
    (xp,yp),(x1,y1,x2,y2) = point, square
    if (x2 >= xp >= x1)&(y2 >= yp >= y1):
        return True
    return False
    
def checkNeighbours((x,y),checked_pool,unchecked_pool):
    distance_sorted_neighbour = sorted(neighbour, key = lambda((nx,ny)):math.hypot(nx-x,ny-y))
    print distance_sorted_neighbour
    good_shifts = 0
    shifts_remain = 3
    for shift in neighbour:
        pointN = (x + shift[0], y + shift[1]) 
        if pointN not in checked_pool and inSquare(pointN, zone) and not inSquare(pointN, square_block):
            checked_pool[pointN] = checked_pool[(x,y)] + 1
            unchecked_pool.append(pointN)
            print pointN
            good_shifts += 1
        shifts_remain -= 1
        
        if shifts_remain <= 0 and good_shifts < 2:
            shifts_remain += 2
        elif shifts_remain <= 0 and good_shifts >= 2:
            break
            
    unchecked_pool.remove((x,y))

def getPathTo(checked_pool, dest_point, init_point, path = None):
    if dest_point == init_point:
        path.append(dest_point)
        return path
    if path == None:
        path = []
    corner_sorted_neighbour = sorted(neighbour, key = lambda((x,y)): x*y)
    print corner_sorted_neighbour
    for shift in corner_sorted_neighbour:
        pointN = (dest_point[0] + shift[0], dest_point[1] + shift[1])
        if pointN in checked_pool and checked_pool[pointN] < checked_pool[dest_point]:
            path.append(dest_point)
            return getPathTo(checked_pool, pointN, init_point, path)

            
counter = 0

for point in unchecked_pool:
    if dest_point in checked_pool:
        break
    checkNeighbours(point,checked_pool,unchecked_pool) 
    print counter
    counter+=1
    
print checked_pool
print getPathTo(checked_pool, dest_point, init_point)
  

    