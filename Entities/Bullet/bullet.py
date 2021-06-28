from Entities.game_object import GameObject

class Bullet(GameObject):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy