import random

class LudoPiece:
    def __init__(self, start_position, Pid):
        self.Pid = Pid
        self.position = start_position
        self.distance_from_goal = self.calculate_distance_from_goal()

    def calculate_distance_from_goal(self):
        if self.position == 0:
            # Piece is at home
            return 57  # 56 track positions + 1 to reach the goal
        elif 1 <= self.position <= 56:
            # Piece is on the track
            return 58 - self.position
        else:
            raise ValueError("Invalid position")

    def move(self, steps):
        self.position += steps
        if self.position > 58:
            self.position = 58  # Ensure the position does not exceed the goal
        # self.distance_from_goal = self.calculate_distance_from_goal()

class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.pieces = [LudoPiece(0, i) for i in range(4)]

    def move_piece(self, piece_index, steps):
        if 0 <= piece_index < len(self.pieces):
            self.pieces[piece_index].move(steps)
        else:
            raise IndexError("Invalid piece index")

class LudoEngine:
    def __init__(self, n_players=4): # n players can only be 2, 3, 4
        self.players = [Player(i) for i in range(n_players)]
        self.current_turn = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_current_player_piece(self, piece_index, steps):
        current_player = self.players[self.current_turn]
        current_player.move_piece(piece_index, steps)
        self.next_turn()

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % 4
    
    def step(self):
        self.move_current_player_piece(random.randint(0, 3), 1)
        for player in self.players:
            for pice in player.pieces:
                if pice.position==57:
                    return True
        return False
