import FrontEnd.CheckerBoard as CheckerBoard
import FrontEnd.CheckerPiece as CheckerPiece
from BackEnd.MoveLogic.Jump import jumps_at
from BackEnd.MoveLogic.LegalMoves import legal_moves
from FrontEnd.ExecuteJump import execute_jump
from FrontEnd.ExecuteSlide import execute_slide
from FrontEnd.HelperFunctions.AddressToLocation import address_to_location
import FrontEnd.EventHandling.SelectAddress as SelectEvent
import FrontEnd.EventHandling.DragPiece as DragEvent
import FrontEnd.EventHandling.DropAddress as DropEvent
from BackEnd.Objects.Player import Player
from FrontEnd.HelperFunctions.CreateRoundedRectangle import create_rounded_rectangle
from FrontEnd.HelperFunctions.OrientedLocation import oriented_location
from playsound import playsound
slide_sound_path = 'Audio/PieceSlide.mp3'
place_sound_path = 'Audio/PlacePiece.mp3'
illegal_sound_path = 'Audio/IllegalMove.mp3'


class GameBoard:
    def __init__(self, canvas, center, size, square_side, square_colors, player_id_to_color, game_text, do_flip=False):
        # internal game logic
        self.logic_board = None
        self.current_player = None
        self.current_opponent = None
        self.selected_address = None
        self.current_legal_moves = None
        self.player_1_id = None
        self.captured_pieces = {}
        for player_id in player_id_to_color.keys():
            self.captured_pieces[player_id] = []

        # drawing
        self.canvas = canvas
        self.board_size = size
        self.center = center
        self.board_image = None
        self.orientation = None
        self.do_flip = do_flip
        self.square_side = square_side
        self.square_colors = square_colors
        self.drawn_pieces = {}
        self.player_id_to_color = player_id_to_color
        self.game_text = game_text

    def game_setup(self, logic_board, player_1_id, player_2_id):
        # handling internal game logic
        self.logic_board = logic_board
        self.current_player = Player(player_1_id, logic_board)
        self.player_1_id = player_1_id
        self.current_opponent = Player(player_2_id, logic_board)
        self.current_legal_moves = legal_moves(logic_board, self.current_player)

        # handling drawing
        self.orientation = 1
        self.draw_game_board()
        self.draw_checker_board()
        for address, logic_piece in logic_board.lookup_entry.items():
            self.draw_piece(address, logic_piece)

    def get_pile_dimensions(self, player_id):
        width, height = self.board_size
        center = self.center
        if self.do_flip and player_id == self.current_player.player_id or (
                not self.do_flip and player_id == self.player_1_id):
            br_x = center[0] + int(0.9 * width) // 2
            br_y = center[1] + int(0.9 * height) // 2
            tl_x = br_x - int(0.6 * width)
            tl_y = br_y - self.square_side
        else:
            tl_x = center[0] - int(0.9 * width) // 2
            tl_y = center[1] - int(0.9 * height) // 2
            br_x = tl_x + int(0.6 * width)
            br_y = tl_y + self.square_side
        return tl_x, tl_y, br_x, br_y

    def add_to_pile(self, player_id, captured_piece):
        self.captured_pieces[player_id].append(captured_piece)
        captured_amount = len(self.captured_pieces[player_id])
        tl_x, tl_y, br_x, br_y = self.get_pile_dimensions(player_id)
        place_x = tl_x
        if captured_amount <= 5:
            place_x += captured_amount * (br_x - tl_x) // 6
        elif captured_amount <= 9:
            border_width = (br_x - tl_x) // 6 - int(0.8 * self.square_side // 2)
            place_x += (captured_amount - 5) * (br_x - tl_x - 2 * border_width) // 5 + border_width
        else:
            border_width = (br_x - tl_x) // 6 + (br_x - tl_x) // 30
            place_x += (captured_amount - 9) * (br_x - tl_x - 2 * border_width) // 4 + border_width
        place_y = tl_y + (br_y - tl_y) // 2
        captured_piece.place(place_x, place_y)

    def draw_game_board(self):
        width, height = self.board_size
        center = self.center
        create_rounded_rectangle(self.canvas, (width, height), center, self.square_side, "#8A360F")
        create_rounded_rectangle(self.canvas, (int(0.95 * width), int(0.95 * height)), center,
                                 int(0.95 * self.square_side), "burlywood3")
        checker_board_side = 8 * self.square_side
        frame_side = int(1.025 * checker_board_side)
        self.canvas.create_rectangle(center[0] - int(frame_side // 2),
                                     center[1] - int(frame_side // 2),
                                     center[0] + int(frame_side // 2),
                                     center[1] + int(frame_side // 2),
                                     fill="lightsteelblue4")

        player_id_to_color = {1: "#7F7F7F", 2: "#C20000"}

        self.canvas.create_rectangle(*self.get_pile_dimensions(self.current_player.player_id),
                                     fill="blanchedalmond")

        current_player_color = player_id_to_color[self.current_player.player_id]
        current_player_br_x = center[0] - int(0.7 * width) // 2
        current_player_br_y = center[1] + int(0.9 * height) // 2
        current_player_tl_x = current_player_br_x - self.square_side
        current_player_tl_y = current_player_br_y - self.square_side
        self.canvas.create_oval(current_player_tl_x, current_player_tl_y,
                                current_player_br_x, current_player_br_y,
                                fill=current_player_color, width=2)

        self.canvas.create_rectangle(*self.get_pile_dimensions(self.current_opponent.player_id),
                                     fill="blanchedalmond")

        current_opponent_color = player_id_to_color[self.current_opponent.player_id]
        current_opponent_tl_x = center[0] + int(0.7 * width) // 2
        current_opponent_tl_y = center[1] - int(0.9 * height) // 2
        current_opponent_br_x = current_opponent_tl_x + self.square_side
        current_opponent_br_y = current_opponent_tl_y + self.square_side
        self.canvas.create_oval(current_opponent_tl_x, current_opponent_tl_y,
                                current_opponent_br_x, current_opponent_br_y,
                                fill=current_opponent_color, width=2)

    def draw_checker_board(self):
        side_length = self.square_side * 8
        CheckerBoard.draw_checker_board(self.canvas, side_length,
                                        self.center, self.square_colors)

    def draw_piece(self, address, logic_piece):
        piece_radius = int(0.8 * (self.square_side // 2))
        if logic_piece.is_king:
            piece_name = self.player_id_to_color[logic_piece.player_id] + "King"
        else:
            piece_name = self.player_id_to_color[logic_piece.player_id] + "Man"
        piece = CheckerPiece.CheckerPiece(self.canvas, piece_radius, piece_name)
        piece.place(*address_to_location(address))
        self.drawn_pieces[address] = piece

    def flip_pieces(self):
        for piece in self.drawn_pieces.values():
            new_location = oriented_location(*piece.location(), self.center, -1)
            piece.place(*new_location)

    def bindings(self):
        self.canvas.bind("<Button-1>", self.select_address)
        self.canvas.bind("<B1-Motion>", self.drag_piece)
        self.canvas.bind("<ButtonRelease-1>", self.drop_piece)

    def oriented_location(self, x, y):
        p = self.center
        t = self.orientation
        oriented_x = (2 * x * t + (1 - t) * p[0]) // 2
        oriented_y = (2 * y * t + (1 - t) * p[1]) // 2
        return oriented_x, oriented_y

    def select_address(self, event):
        x = event.x
        y = event.y
        piece_radius = 0.8 * self.square_side
        oriented_x, oriented_y = oriented_location(x, y, self.center, self.orientation)
        self.selected_address = SelectEvent.select_address(oriented_x, oriented_y, piece_radius)

    def drag_piece(self, event):
        if self.selected_address in self.drawn_pieces.keys():
            selected_piece = self.drawn_pieces[self.selected_address]
            DragEvent.drag_piece(event, selected_piece)

    def change_to_next_player(self):
        temp_player = self.current_player
        self.current_player = self.current_opponent
        self.current_opponent = temp_player
        self.current_legal_moves = legal_moves(self.logic_board, self.current_player)
        self.game_text.config(text=f"Player {self.current_player.player_id}")
        if self.do_flip:
            self.draw_game_board()
            self.draw_checker_board()
            self.flip_pieces()
            self.orientation *= -1

    def drop_piece(self, event):
        if self.selected_address in self.drawn_pieces.keys():
            x = event.x
            y = event.y
            oriented_x, oriented_y = oriented_location(x, y, self.center, self.orientation)
            selected_piece = self.drawn_pieces[self.selected_address]
            drop_address = DropEvent.drop_address(oriented_x, oriented_y, self.current_legal_moves,
                                                  self.selected_address)
            if drop_address == self.selected_address:
                drop_location = oriented_location(*address_to_location(drop_address), self.center, self.orientation)
                selected_piece.place(*drop_location)
                sound_path = illegal_sound_path
            else:
                if abs(self.selected_address[0] - drop_address[0]) == 1:
                    sound_path = slide_sound_path
                    execute_slide(self.current_player, self.logic_board, self.drawn_pieces,
                                  self.selected_address, drop_address, self.orientation, self.center)
                    self.change_to_next_player()
                else:
                    sound_path = place_sound_path
                    jumped_piece = execute_jump(self.current_player, self.current_opponent, self.logic_board,
                                                self.drawn_pieces, self.selected_address, drop_address,
                                                self.orientation, self.center)
                    self.add_to_pile(self.current_player.player_id, jumped_piece)
                    extra_jumps = jumps_at(self.logic_board, drop_address)
                    if len(extra_jumps) > 0:
                        self.current_legal_moves = {drop_address: extra_jumps}
                    else:
                        self.change_to_next_player()
            self.canvas.update()
            playsound(sound_path)
        if (len(self.current_opponent.man_locations) == 0) and (len(self.current_opponent.king_locations) == 0):
            self.game_text.config(text=f"Player {self.current_player.player_id} Wins!")
        elif len(self.current_legal_moves.keys()) == 0:
            self.game_text.config(text=f"Player {self.current_opponent.player_id} Wins!")
        self.selected_address = None
