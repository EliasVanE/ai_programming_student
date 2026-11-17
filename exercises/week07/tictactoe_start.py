"""
Oefening: TicTacToe met Minimax & Alpha-Beta
==============================================
"""
import copy


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def possible_moves(self):
        """Geef lijst van (rij, kolom)-tupels van lege velden."""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def is_valid_move(self, x, y):
        pass

    def make_move(self, x, y, player):
        pass

    def undo_move(self, x, y):
        self.board[x][y] = ' '

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                return self.board[0][2]
        return None

    def is_draw(self):
        return len(self.possible_moves()) == 0 and not self.check_winner()
    def evaluate(self,board,depth):
        winner = self.check_winner(board)

        if winner == 'X':
            return 10
        elif winner == 'O':
            return -10
        elif self.is_draw(board) or depth == 0:
            return 0
        

    def minimax(self, board, depth, is_maximizing, alpha, beta):

        if depth == 0 or self.check_winner_board(board) or self.is_draw():
            return self.evaluate(board)
        if is_maximizing:
            best = -float('inf')
            for zet in self.possible_moves():
                x, y = zet

                new_board = [row.copy() for row in board]
                new_board[x][y] = 'X'

                score = self.minimax(new_board, depth - 1, False, alpha, beta)

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

            return best

        else:
            best = float('inf')

            for zet in self.possible_moves():
                x, y = zet

                new_board = [row.copy() for row in board]
                new_board[x][y] = 'O'

                score = self.minimax(new_board, depth - 1, True, alpha, beta)

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

            return best
  
  
  
    def find_best_move(self):
        best_score = -float('inf')
        best_move = None

        for zet in self.possible_moves():
            x, y = zet

            new_board = [row.copy() for row in self.board]
            new_board[x][y] = 'X'

            score = self.minimax(
                new_board,
                9,
                False,
                -float('inf'),
                float('inf')
            )

            if score > best_score:
                best_score = score
                best_move = zet

        return best_move

    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def play(self):
        pass


if __name__ == "__main__":
    game = TicTacToe()
   
    game.print_board()