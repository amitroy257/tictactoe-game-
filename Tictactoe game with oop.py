class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # initialize board with empty spaces
        self.current_player = 'X'  # player 'X' starts the game

    def print_board(self):
        print(f'| {self.board[0]} | {self.board[1]} | {self.board[2]} |')
        print(f'| {self.board[3]} | {self.board[4]} | {self.board[5]} |')
        print(f'| {self.board[6]} | {self.board[7]} | {self.board[8]} |')

    def make_move(self, position):
        if self.board[position] == ' ':  # check if the position is empty
            self.board[position] = self.current_player  # place the current player's symbol on the board
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # switch to the other player
        else:
            print('Position already occupied. Try again.')
            return False
        return True

    def check_winner(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        # check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        # check if the game is a tie
        if ' ' not in self.board:
            return 'Tie'

    def play(self):
        while True:
            self.print_board()
            position = int(input(f'{self.current_player}, enter a position (1-9): ')) - 1
            if not (0 <= position <= 8):
                print('Invalid position. Try again.')
                continue
            if self.make_move(position):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == 'Tie':
                        print('The game is a tie!')
                    else:
                        print(f'{winner} wins!')
                    break


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
