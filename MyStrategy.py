from model.ActionType import ActionType
from model.Game import Game
from model.Move import Move
from model.Wizard import Wizard
from model.World import World
from model.Unit import Unit
from utils import InCircle, goTo, InitTick, MyLocation


class MyStrategy:
    topWayPoints = []
    midWayPoints = []
    botWayPoints = []
    Grid = []
    GridW = {}
    currentWayPoint = ()
    EnemyTowerWeight = -10
    LivingUnitWeight = -9999
    
    def move(self, mywiz, world, game, move):
        utils.InitTick(self, mywiz, world, game, move)
        utils.InitializeStrategy(game)
        utils.goTo(self, self.topWayPoints[5])
        # move.speed = game.wizard_forward_speed
        # move.strafe_speed = game.wizard_strafe_speed
        # move.turn = game.wizard_max_turn_angle
        # move.action = ActionType.MAGIC_MISSILE
        
            
    def InitializeStrategy(self, game):
        mapSize = game.map_size;        
        self.topWayPoints = [(0.025 * mapSize,0.9 * mapSize),
             (0.05 * mapSize,0.8 * mapSize),
             (0.05 * mapSize,0.7 * mapSize),
             (0.05 * mapSize,0.6 * mapSize),
             (0.05 * mapSize,0.5 * mapSize),
             (0.05 * mapSize,0.4 * mapSize),
             (0.05 * mapSize,0.3 * mapSize),
             (0.05 * mapSize,0.2 * mapSize),
             (0.05 * mapSize,0.05 * mapSize),
             (0.2 * mapSize,0.025 * mapSize),
             (0.3 * mapSize,0.025 * mapSize),
             (0.4 * mapSize,0.025 * mapSize),
             (0.5 * mapSize,0.025 * mapSize),
             (0.6 * mapSize,0.025 * mapSize),
             (0.7 * mapSize,0.025 * mapSize),
             (0.8 * mapSize,0.025 * mapSize),
             (0.9 * mapSize,0.025 * mapSize)]
             
        grid = [(x,y) for x in range(self.me.x-250,self.me.x+250,10) if x>0
              for y in range(self.me.y-250,self.me.y+250,10) if y>0]
            
        for cell in grid:
            for tower in buildings:
                if utils.InCircle(cell, (tower.x,tower.y), tower.radius):
                    gridW[cell] = BuildingWeight
                elif utils.InCircle(cell, (tower.x,tower.y), tower.atack_range):
                    gridW[cell] = LivingUnitWeight
        
        print grid

    
        