class City:
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.owner = owner
        self.production_queue = []

    def produce(self):
        pass  # TODO: Handle production over turns