import random

class LudoPiece:
    def __init__(self, start_position):
        self.position = start_position
        self.distance_from_goal = self.calculate_distance_from_goal()

    def calculate_distance_from_goal(self):
        if self.position == 0:
            # Piece is at home
            return 57  # 56 track positions + 1 to reach the goal
        elif 1 <= self.position <= 56:
            # Piece is on the track
            return 58 - self.position
        elif self.position == 58:
            # Piece has reached the goal
            return 0
        else:
            raise ValueError("Invalid position")

    def move(self, steps):
        self.position += steps
        if self.position > 58:
            self.position = 58  # Ensure the position does not exceed the goal
        self.distance_from_goal = self.calculate_distance_from_goal()

class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.pieces = [LudoPiece(0) for _ in range(4)]

    def move_piece(self, piece_index, steps):
        if 0 <= piece_index < len(self.pieces):
            self.pieces[piece_index].move(steps)
        else:
            raise IndexError("Invalid piece index")

class LudoEngine:
    def __init__(self):
        self.players = [Player(i) for i in range(4)]
        self.current_turn = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_current_player_piece(self, piece_index, steps):
        current_player = self.players[self.current_turn]
        current_player.move_piece(piece_index, steps)
        self.next_turn()

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % 4

    def get_board_state(self):
        board_state = {}
        for player in self.players:
            board_state[player.player_number] = [piece.position for piece in player.pieces]
        return board_state

    def get_engine_state(self):
        return {
            "current_turn": self.current_turn,
            "board_state": self.get_board_state()
        }