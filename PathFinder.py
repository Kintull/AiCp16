import time
import math

class PathFinder:
    def __init__(self, wizard):
        #init_point = (1,1)
        #dest_point = (1000,1000)                 
        #zone = (0,0,1000,1000)
        
        self.init_point = (wizard.x, wizard.y)
        neighbour = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        distance = 0
    
    def goTo(self, dest_point):
        init_point = self.init_point
        path_pool = init_pathfinder(init_point, dest_point)
        final_path = getPathInPool(path_pool,init_point, dest_point)
        return final_path
        
    def init_pathfinder(self, init_point, dest_point):  
        unchecked_pool = []
        checked_pool = {}
        checked_pool[init_point] = 0
        unchecked_pool.append(init_point)
        for point in unchecked_pool: 
            if dest_point in checked_pool:
                break #reached last point
            self.checkNeighbours(point, checked_pool, unchecked_pool, dest_point) 
        return checked_pool

            
    def inSquare(self, point, square): 
        (xp,yp),(x1,y1,x2,y2) = point, square
        if (x2 >= xp >= x1)&(y2 >= yp >= y1):
            return True
        return False
        
    def checkNeighbours(self, (x,y),checked_pool, unchecked_pool, dest_point):
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
        

    def getPathInPool(self, checked_pool, dest_point, init_point):
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
    
       
