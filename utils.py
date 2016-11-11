def InCircle(self, UnitCenter, CircleCenter, Radius):
    (ux,uy),(cx,cy) = UnitCenter,CircleCenter
    dx = abs(ux-cx)
    dy = abs(uy-cy)
    if dx + dy <= Radius: 
        return True
    elif dx > Radius:
        return False
    elif dy > Radius:
        return False
    elif dx^2 + dy^2 <= Radius^2:
        return True
    else:
        return False

def MyLocation(self):
    return self.me.x,self.me.y


def goTo(self, (x, y)):
    angle = Unit.get_angle_to(self.mywiz, x, y)
    self.movewiz.turn = angle
    if (abs(angle) < self.game.staff_sector / 4.0):
        self.movewiz.speed = self.game.wizard_forward_speed
        
def InitTick(self, mywiz, world, game, move) :
    self.mywiz = mywiz
    self.world = world
    self.game = game
    self.movewiz = move