class TicTacToe3D:
    def __init__(self):
        self.board = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print('Layer {}: {}'.format(i+1, self.board[i][j]))
            print()

    def is_valid_move(self, layer, row, col):
        if layer < 0 or layer > 2 or row < 0 or row > 2 or col < 0 or col > 2:
            return False
        if self.board[layer][row][col] is not None:
            return False
        return True

    def make_move(self, layer, row, col):
        if self.is_valid_move(layer, row, col):
            self.board[layer][row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_win(self):
        # Check horizontal wins
        for i in range(3):
            for j in range(3):
                if self.board[i][j][0] == self.board[i][j][1] == self.board[i][j][2] and self.board[i][j][0] is not None:
                    return self.board[i][j][0]
                if self.board[j][0][i] == self.board[j][1][i] == self.board[j][2][i] and self.board[j][0][i] is not None:
                    return self.board[j][0][i]

        # Check vertical wins
        for i in range(3):
            if self.board[0][i][0] == self.board[1][i][0] == self.board[2][i][0] and self.board[0][i][0] is not None:
                return self.board[0][i][0]
            if self.board[0][0][i] == self.board[1][0][i] == self.board[2][0][i] and self.board[0][0][i] is not None:
                return self.board[0][0][i]

        # Check diagonal wins
        if self.board[0][0][0] == self.board[1][1][1] == self.board[2][2][2] and self.board[0][0][0] is not None:
            return self.board[0][0][0]
        if self.board[0][2][0] == self.board[1][1][1] == self.board[2][0][2] and self.board[0][2][0] is not None:
            return self.board[0][2][0]
        if self.board[0][0][2] == self.board[1][1][1] == self.board[2][2][0] and self.board[0][0][2] is not None:
            return self.board[0][0][2]
        if self.board[0][2][2] == self.board[1][1][1] == self.board[2][0][0] and self.board[0][2][2] is not None:
            return self.board[0][2][2]

        return None

    def play(self):
        while True:
            self.print_board()
            layer = int(input("Enter the layer (1-3): ")) - 1
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if self.make_move(layer, row, col):
                winner = self.check_win()
                if winner is not None:
                    self.print_board()
                    print("Player {} wins!".format(winner))
                    break
            else:
                print("Invalid move, try again.")


if __name__ == "__main__":
    game = TicTacToe3D()
    game.play()
