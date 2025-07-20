class Tile:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain

    def draw(self, screen, assets):
        pass  # TODO: Add drawing logic

class GameMap:
    def __init__(self):
        self.tiles = []  # TODO: Generate or load map

    def draw(self, screen, assets):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen, assets)