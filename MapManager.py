
class MapManager:
    def __init__(self, mywiz, world, game):
        if 1:#game.fraction == 'dire':
            self.home = (9,1)
        else:
            self.home = (1,9)
        
        self.mywiz = mywiz
        self.world = world
        self.map_area = [(0,0),(world.width, world.height)]
        self.lanes = ['top', 'mid', 'bot']
        self.area_to_rectangle = {7 :[(0,10),(2,8)],
                                  41:[(0,8),(1,5)],
                                  42:[(0,5),(1,2)],
                                  8 :[(0,2),(2,0)],
                                  11:[(2,1),(5,0)],
                                  12:[(5,1),(8,0)],
                                  5 :[(8,2),(10,0)],
                                  22:[(9,2),(10,5)],
                                  21:[(9,5),(10,8)],
                                  6 :[(8,10),(10,8)],
                                  32:[(5,10),(8,9)],
                                  31:[(5,10),(8,9)]
                                  }
        self.top_blocks = [41,42,8,11,12]
        self.all_blocks = [7,41,42,8,11,12,5,22,21,6,32]
        self.all_blocks_default = [7,41,42,8,11,12,5,22,21,6,32]
        
        self.wood_blocks = [[(1,8),(1,2),(1,4)],
                            [(5,4),(2,1),(8,1)],
                            [(9,8),(6,5),(9,2)],
                            [(2,9),(5,6),(8,9)]]
        self.blocked_area = []
        """ Wood blocks:
               #####
            #   #2#   #
            ##   #   ##
            #1#     #3#
            ##   #   ##
            #   #4#   #
               #####
        """                            
        self.enemy_in_area = {x:0 for block in self.all_blocks}
        
    def blockArea(self, map_blocks = []):
        if map_blocks == []:
            return 
        self.blocked_area.extend(map_blocks)
    
    def unblockArea(self, map_blocks = []):
        if map_blocks == []:
            return 
        self.blocked_area.remove(map_blocks)

    def useDefaultArea():
        self.all_blocks = self.all_blocks_default
        self.blocked_area = []
        
    def getPushPoint(lane):
    #TODO: make lane refactoring (update mid and bot also)
        if lane == 'top':
            enemy_minions = filter(lambda x: x.faction != self.mywiz.faction, self.world.minions)
            enemy_wizards = filter(lambda x: x.faction != self.mywiz.faction, self.world.wizards)
            self.updateAreaDanger(enemy_minions, top_blocks, 1)
            self.updateAreaDanger(enemy_wizards, top_blocks, 4)
                        
        
    def updateAreaDanger(units, blocks, weight):
        for unit in units:
            for area in blocks:
                area_xy = self.area_to_rectangle[area]
                #TODO: CONVERT 1,2,3... T to mapsize / T
                if self.inRectangle((unit.x, unit.y), area_xy):
                    self.enemy_in_area[area] += 1
    
    def inRectangle(self, point, rectangle):
        (x,y), [(x1,y1),(x2,y2)] = point, rectangle
        return ((x1 < x < x2) and (y1 < y < y2))
    
    def inTriangle (self, point, triangle):
        [p1, p2, p3] = triangle
        b1 = self.sign(point, p1, p2) < 0
        b2 = self.sign(point, p2, p3) < 0
        b3 = self.sign(point, p3, p1) < 0
        return ((b1 == b2) and (b2 == b3))   
        
    def sign (self, p1, p2, p3):
        (p1x, p1y) = p1 
        (p2x, p2y) = p2
        (p3x, p3y) = p3
        return (p1x - p3x) * (p2y - p3y) - (p2x - p3x) * (p1y - p3y)