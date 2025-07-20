class Unit:
    def __init__(self, x, y, unit_type, owner):
        self.x = x
        self.y = y
        self.unit_type = unit_type
        self.owner = owner

    def move(self, dx, dy):
        pass  # TODO: Movement logic