# ===== By Harmony ========
import tkinter as tk


class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.game_over = False
        self.play_again_button = None
        self.x_score = 0
        self.o_score = 0

        # Create score labels
        self.x_score_label = tk.Label(master, text="Player X: 0", font=("Arial", 12))
        self.o_score_label = tk.Label(master, text="Player O: 0", font=("Arial", 12))
        self.x_score_label.grid(row=0, column=0)
        self.o_score_label.grid(row=0, column=2)

        # Create buttons for each cell on the board
        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text="", font=("Arial", 36), width=3, height=1,
                               command=lambda i=i: self.play_move(i), bd=8)
            button.grid(row=i // 3 + 1, column=i % 3, pady=0)
            button.configure(bg="yellow")
            self.buttons.append(button)

        # Create button to play again
        self.play_again_button = tk.Button(master, text="Play Again", font=("Arial", 14),
                                           command=self.reset_game, state=tk.DISABLED, bd=5)
        self.play_again_button.grid(row=10, column=0, columnspan=2)

        # Create button to exit the game
        self.exit_button = tk.Button(master, text="Exit", font=("Arial", 14),
                                     command=self.master.quit, bd=5)
        self.exit_button.grid(row=10, column=2, columnspan=2)

    def play_move(self, i):
        if not self.game_over and self.board[i] == "":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_for_winner():
                self.game_over = True
                winner = self.current_player
                if winner == "X":
                    self.x_score += 1
                    self.x_score_label.config(text="PlayerX: {}".format(self.x_score))
                else:
                    self.o_score += 1
                    self.o_score_label.config(text="PlayerO: {}".format(self.o_score))
                self.play_again_button.config(state=tk.NORMAL)
                tk.messagebox.showinfo("Game Over", f"{winner} has won the game!")
            else:
                self.swap_players()

    def check_for_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if (self.board[i] == self.board[i + 1] == self.board[i + 2]) and self.board[i] != "":
                return True

        # Check columns
        for i in range(3):
            if (self.board[i] == self.board[i + 3] == self.board[i + 6]) and self.board[i] != "":
                return True

        # Check diagonals
        if (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != "":
            return True
        if (self.board[2] == self.board[4] == self.board[6]) and self.board[2] != "":
            return True

        # Check for tie
        if "" not in self.board:
            return True

        return False

    def swap_players(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_game(self):
        self.board = ["", "", "", "", "", "", "", "", ""]
        for button in self.buttons:
            button.config(text="")
        self.game_over = False
        self.play_again_button.config(state=tk.DISABLED)

    def run(self):
        self.master.mainloop()


# Create the main window and start the game
root = tk.Tk()
root.configure(bg="white")
root.geometry("320x400")
game = TicTacToe(root)
game.run()

# ===== By Harmony ========