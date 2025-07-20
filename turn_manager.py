class TurnManager:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0

    def end_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)