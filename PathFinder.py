import time
import math

class PathFinder:
    def __init__(self):
        init_point = (1,1)
        dest_point = (1000,1000)
        triangle_blocks = [[(1,8),(1,2),(1,4)],
                           [(5,4),(2,1),(8,1)],
                           [(9,8),(6,5),(9,2)],
                           [(2,9),(5,6),(8,9)]]
        """
           #####
        #   #2#   #
        ##   #   ##
        #1#     #3#
        ##   #   ##
        #   #4#   #
           #####
        """        
                           
        zone = (0,0,1000,1000)
        neighbour = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        unchecked_pool = []
        checked_pool = {}
        checked_pool[init_point] = 0
        distance = 0
        
    def getPathTo(init_point, dest_point):   
        unchecked_pool.append(init_point)
        counter = 0
        start = time.time()
        for point in unchecked_pool: 
            if dest_point in checked_pool:
                break
            self.checkNeighbours(point,checked_pool,unchecked_pool,dest_point) 
            #print counter
            counter+=1
        fin = time.time()    
        #print checked_pool
        print self.getPathFrom(checked_pool, dest_point, init_point)
        print fin - start
            
    def inSquare(self,point, square): 
        (xp,yp),(x1,y1,x2,y2) = point, square
        if (x2 >= xp >= x1)&(y2 >= yp >= y1):
            return True
        return False
        
    def checkNeighbours((x,y),checked_pool,unchecked_pool,dest_point):
        distance_sorted_neighbour = sorted(neighbour, key = lambda((xsh,ysh)): math.hypot(abs(x+xsh-dest_point[0]),abs(y+ysh-dest_point[1])))
        #print distance_sorted_neighbour
        good_shifts = 0
        shifts_remain = 2
        for iter in range(8):
            shift = distance_sorted_neighbour[iter]
            pointN = (x + shift[0], y + shift[1]) 
            if pointN not in checked_pool and inSquare(pointN, zone) and not inSquare(pointN, square_block):
                checked_pool[pointN] = checked_pool[(x,y)] + 1
                unchecked_pool.append(pointN)
                #print pointN
                #sleep(0.01)
                good_shifts += 1
            shifts_remain -= 1
            
            if shifts_remain <= 0 and good_shifts < 2:
                shifts_remain += 2
            elif shifts_remain <= 0 and good_shifts >= 2:
                break
                
        unchecked_pool.remove((x,y))
        

    def getPathFrom(self, checked_pool, dest_point, init_point):
        path = []
        corner_sorted_neighbour = sorted(neighbour, key = lambda((x,y)): abs(x*y), reverse=True)
        current_point = dest_point
        if dest_point not in checked_pool:
            return path
        while 1:
            if current_point == init_point:
                path.append(current_point)
                break
            
            for iter in range(8):
                shift = corner_sorted_neighbour[iter]
                next_point = (current_point[0] + shift[0], current_point[1] + shift[1])
                if next_point in checked_pool and checked_pool[next_point] < checked_pool[current_point]:
                    path.append(current_point)
                    current_point = next_point
                    break
                if iter == 8:
                    return path
        return path
    
       
