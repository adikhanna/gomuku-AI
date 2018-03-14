import Tkinter as tkinter
import random


class Game(object):
    block_size = 100
    def __init__(self, parent):
        parent.title('Gomoku - villasr2 avkhann2 hornits2')
        self.parent = parent

        self.initialize_game()

    def initialize_game(self):
        self.board = [  None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None,\
                        None, None, None, None, None, None, None]
        self.map = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (0, 5): 5, (0, 6): 6,
                    (1, 0): 7, (1, 1): 8, (1, 2): 9, (1, 3): 10, (1, 4): 11, (1, 5): 12, (1, 6): 13,
                    (2, 0): 14, (2, 1): 15, (2, 2): 16, (2, 3): 17, (2, 4): 18, (2, 5): 19, (2, 6): 20,
                    (3, 0): 21, (3, 1): 22, (3, 2): 23, (3, 3): 24, (3, 4): 25, (3, 5): 26, (3, 6): 27,
                    (4, 0): 28, (4, 1): 29, (4, 2): 30, (4, 3): 31, (4, 4): 32, (4, 5): 33, (4, 6): 34,
                    (5, 0): 35, (5, 1): 36, (5, 2): 37, (5, 3): 38, (5, 4): 39, (5, 5): 40, (5, 6): 41,
                    (6, 0): 42, (6, 1): 43, (6, 2): 44, (6, 3): 45, (6, 4): 46, (6, 5): 47, (6, 6): 48}
        self.top_frame = tkinter.Frame(self.parent)
        self.top_frame.pack(side=tkinter.TOP)
        restart_button = tkinter.Button(self.top_frame, text='Restart', width=20,
                                        command=self.restart)
        restart_button.pack()
        self.bottom_frame=tkinter.Frame(self.parent)
        self.bottom_frame.pack(side=tkinter.BOTTOM)
        self.my_lbl=tkinter.Label(self.bottom_frame,text=None)
        self.my_lbl.pack()
        self.canvas = tkinter.Canvas(self.top_frame,
                                     width=self.block_size * 7,
                                     height=self.block_size * 7)
        for ro in range(7):
            for col in range(7):

                self.canvas.create_rectangle(self.block_size * col,
                                             self.block_size * ro,
                                             self.block_size * (col + 1),
                                             self.block_size * (ro + 1),fill='white')
        self.canvas.bind("<Button-1>", self.play)
        self.canvas.pack()

    def board_full(self):
        if None not in self.board:
            return True
        else:
            return False


    def possible_moves(self):
        possible_moves = []
        for i in range(0, 49):
            if self.board[i] is None:
                possible_moves.append(i)
            else:
                pass
        return possible_moves

    def pc_move(self):
        while not self.board_full():
            pc_move = random.randint(0, 48)
            if pc_move in self.possible_moves():
                self.board[pc_move] = 'O'
                self.canvas.itemconfigure(tagOrId=(pc_move+1),fill='blue')
                break
            else:
                continue
        return self

    def draw_out(self):
        print(self.board[0:7])
        print(self.board[7:14])
        print(self.board[14:21])
        print(self.board[21:28])
        print(self.board[28:35])
        print(self.board[35:42])
        print(self.board[42:49])

    def play(self, event):
        print('clicked', event.y, event.x)
        cx = self.canvas.canvasx(event.x)
        cy = self.canvas.canvasy(event.y)
        cid = self.canvas.find_closest(cx,cy)[0]
        my_move = self.map[(cy // self.block_size, cx // self.block_size)]
        if self.board[my_move] is None:
            self.board[my_move] = 'X'
            self.canvas.itemconfigure(cid,fill='red')
        else:
            return None
        self.draw_out()
        if self.check_game()is not None:
            print(self.check_game())
        else:
            pass
        self.possible_moves()
        self.pc_move()
        self.draw_out()
        if self.check_game()is not None:
            print(self.check_game())
        else:
            pass
        return self

    def check_game(self):
        result=None
        if (self.board[0]==self.board[1]==self.board[2]==self.board[3]==self.board[4]=='X') or (self.board[1]==self.board[2]==self.board[3]==self.board[4]==self.board[5]=='X') or (self.board[2]==self.board[3]==self.board[4]==self.board[5]==self.board[6]=='X') or (self.board[7]==self.board[8]==self.board[9]==self.board[10]==self.board[11]=='X') or (self.board[8]==self.board[9]==self.board[10]==self.board[11]==self.board[12]=='X') or (self.board[9]==self.board[10]==self.board[11]==self.board[12]==self.board[13]=='X') or (self.board[14]==self.board[15]==self.board[16]==self.board[17]==self.board[18]=='X') or (self.board[15]==self.board[16]==self.board[17]==self.board[18]==self.board[19]=='X') or (self.board[16]==self.board[17]==self.board[18]==self.board[19]==self.board[20]=='X') or (self.board[21]==self.board[22]==self.board[23]==self.board[24]==self.board[25]=='X') or (self.board[22]==self.board[23]==self.board[24]==self.board[25]==self.board[26]=='X') or (self.board[23]==self.board[24]==self.board[25]==self.board[26]==self.board[27]=='X') or (self.board[28]==self.board[29]==self.board[30]==self.board[31]==self.board[32]=='X') or (self.board[29]==self.board[30]==self.board[31]==self.board[32]==self.board[33]=='X') or (self.board[30]==self.board[31]==self.board[32]==self.board[33]==self.board[34]=='X') or (self.board[35]==self.board[36]==self.board[37]==self.board[38]==self.board[39]=='X') or (self.board[36]==self.board[37]==self.board[38]==self.board[39]==self.board[40]=='X') or (self.board[37]==self.board[38]==self.board[39]==self.board[40]==self.board[41]=='X') or (self.board[42]==self.board[43]==self.board[44]==self.board[45]==self.board[46]=='X') or (self.board[43]==self.board[44]==self.board[45]==self.board[46]==self.board[47]=='X') or (self.board[44]==self.board[45]==self.board[46]==self.board[47]==self.board[48]=='X') or (self.board[0]==self.board[7]==self.board[14]==self.board[21]==self.board[28]=='X') or (self.board[7]==self.board[14]==self.board[21]==self.board[28]==self.board[35]=='X') or (self.board[14]==self.board[21]==self.board[28]==self.board[35]==self.board[42]=='X') or (self.board[1]==self.board[8]==self.board[15]==self.board[22]==self.board[29]=='X') or (self.board[8]==self.board[15]==self.board[22]==self.board[29]==self.board[36]=='X') or (self.board[15]==self.board[22]==self.board[29]==self.board[36]==self.board[43]=='X') or (self.board[2]==self.board[9]==self.board[16]==self.board[23]==self.board[30]=='X') or (self.board[9]==self.board[16]==self.board[23]==self.board[30]==self.board[37]=='X') or (self.board[16]==self.board[23]==self.board[30]==self.board[37]==self.board[44]=='X') or (self.board[3]==self.board[10]==self.board[17]==self.board[24]==self.board[31]=='X') or (self.board[10]==self.board[17]==self.board[24]==self.board[31]==self.board[38]=='X') or (self.board[17]==self.board[24]==self.board[31]==self.board[38]==self.board[45]=='X') or (self.board[4]==self.board[11]==self.board[18]==self.board[25]==self.board[32]=='X') or (self.board[11]==self.board[18]==self.board[25]==self.board[32]==self.board[39]=='X') or (self.board[18]==self.board[25]==self.board[32]==self.board[39]==self.board[46]=='X') or (self.board[5]==self.board[12]==self.board[19]==self.board[26]==self.board[33]=='X') or (self.board[12]==self.board[19]==self.board[26]==self.board[33]==self.board[40]=='X') or (self.board[19]==self.board[26]==self.board[33]==self.board[40]==self.board[47]=='X') or (self.board[6]==self.board[13]==self.board[20]==self.board[27]==self.board[34]=='X') or (self.board[13]==self.board[20]==self.board[27]==self.board[34]==self.board[41]=='X') or (self.board[20]==self.board[27]==self.board[34]==self.board[41]==self.board[48]=='X') or (self.board[0]==self.board[8]==self.board[16]==self.board[24]==self.board[32]=='X') or (self.board[8]==self.board[16]==self.board[24]==self.board[32]==self.board[40]=='X') or (self.board[16]==self.board[24]==self.board[32]==self.board[40]==self.board[48]=='X') or (self.board[1]==self.board[9]==self.board[17]==self.board[25]==self.board[33]=='X') or (self.board[9]==self.board[17]==self.board[25]==self.board[33]==self.board[41]=='X') or (self.board[2]==self.board[10]==self.board[18]==self.board[26]==self.board[34]=='X') or (self.board[7]==self.board[15]==self.board[23]==self.board[31]==self.board[39]=='X') or (self.board[15]==self.board[23]==self.board[31]==self.board[39]==self.board[47]=='X') or (self.board[14]==self.board[22]==self.board[30]==self.board[38]==self.board[46]=='X') or (self.board[6]==self.board[12]==self.board[18]==self.board[24]==self.board[30]=='X') or (self.board[12]==self.board[18]==self.board[24]==self.board[30]==self.board[36]=='X') or (self.board[18]==self.board[24]==self.board[30]==self.board[36]==self.board[42]=='X') or (self.board[5]==self.board[11]==self.board[17]==self.board[23]==self.board[29]=='X') or (self.board[11]==self.board[17]==self.board[23]==self.board[29]==self.board[35]=='X') or (self.board[4]==self.board[10]==self.board[16]==self.board[22]==self.board[28]=='X') or (self.board[13]==self.board[19]==self.board[25]==self.board[31]==self.board[37]=='X') or (self.board[19]==self.board[25]==self.board[31]==self.board[37]==self.board[43]=='X') or (self.board[20]==self.board[26]==self.board[32]==self.board[38]==self.board[44]=='X'):
            result = 'You win!'
            self.my_lbl.configure(text=result)

        elif (self.board[0]==self.board[1]==self.board[2]==self.board[3]==self.board[4]=='O') or (self.board[1]==self.board[2]==self.board[3]==self.board[4]==self.board[5]=='O') or (self.board[2]==self.board[3]==self.board[4]==self.board[5]==self.board[6]=='O') or (self.board[7]==self.board[8]==self.board[9]==self.board[10]==self.board[11]=='O') or (self.board[8]==self.board[9]==self.board[10]==self.board[11]==self.board[12]=='O') or (self.board[9]==self.board[10]==self.board[11]==self.board[12]==self.board[13]=='O') or (self.board[14]==self.board[15]==self.board[16]==self.board[17]==self.board[18]=='O') or (self.board[15]==self.board[16]==self.board[17]==self.board[18]==self.board[19]=='O') or (self.board[16]==self.board[17]==self.board[18]==self.board[19]==self.board[20]=='O') or (self.board[21]==self.board[22]==self.board[23]==self.board[24]==self.board[25]=='O') or (self.board[22]==self.board[23]==self.board[24]==self.board[25]==self.board[26]=='O') or (self.board[23]==self.board[24]==self.board[25]==self.board[26]==self.board[27]=='O') or (self.board[28]==self.board[29]==self.board[30]==self.board[31]==self.board[32]=='O') or (self.board[29]==self.board[30]==self.board[31]==self.board[32]==self.board[33]=='O') or (self.board[30]==self.board[31]==self.board[32]==self.board[33]==self.board[34]=='O') or (self.board[35]==self.board[36]==self.board[37]==self.board[38]==self.board[39]=='O') or (self.board[36]==self.board[37]==self.board[38]==self.board[39]==self.board[40]=='O') or (self.board[37]==self.board[38]==self.board[39]==self.board[40]==self.board[41]=='O') or (self.board[42]==self.board[43]==self.board[44]==self.board[45]==self.board[46]=='O') or (self.board[43]==self.board[44]==self.board[45]==self.board[46]==self.board[47]=='O') or (self.board[44]==self.board[45]==self.board[46]==self.board[47]==self.board[48]=='O') or (self.board[0]==self.board[7]==self.board[14]==self.board[21]==self.board[28]=='O') or (self.board[7]==self.board[14]==self.board[21]==self.board[28]==self.board[35]=='O') or (self.board[14]==self.board[21]==self.board[28]==self.board[35]==self.board[42]=='O') or (self.board[1]==self.board[8]==self.board[15]==self.board[22]==self.board[29]=='O') or (self.board[8]==self.board[15]==self.board[22]==self.board[29]==self.board[36]=='O') or (self.board[15]==self.board[22]==self.board[29]==self.board[36]==self.board[43]=='O') or (self.board[2]==self.board[9]==self.board[16]==self.board[23]==self.board[30]=='O') or (self.board[9]==self.board[16]==self.board[23]==self.board[30]==self.board[37]=='O') or (self.board[16]==self.board[23]==self.board[30]==self.board[37]==self.board[44]=='O') or (self.board[3]==self.board[10]==self.board[17]==self.board[24]==self.board[31]=='O') or (self.board[10]==self.board[17]==self.board[24]==self.board[31]==self.board[38]=='O') or (self.board[17]==self.board[24]==self.board[31]==self.board[38]==self.board[45]=='O') or (self.board[4]==self.board[11]==self.board[18]==self.board[25]==self.board[32]=='O') or (self.board[11]==self.board[18]==self.board[25]==self.board[32]==self.board[39]=='O') or (self.board[18]==self.board[25]==self.board[32]==self.board[39]==self.board[46]=='O') or (self.board[5]==self.board[12]==self.board[19]==self.board[26]==self.board[33]=='O') or (self.board[12]==self.board[19]==self.board[26]==self.board[33]==self.board[40]=='O') or (self.board[19]==self.board[26]==self.board[33]==self.board[40]==self.board[47]=='O') or (self.board[6]==self.board[13]==self.board[20]==self.board[27]==self.board[34]=='O') or (self.board[13]==self.board[20]==self.board[27]==self.board[34]==self.board[41]=='O') or (self.board[20]==self.board[27]==self.board[34]==self.board[41]==self.board[48]=='O') or (self.board[0]==self.board[8]==self.board[16]==self.board[24]==self.board[32]=='O') or (self.board[8]==self.board[16]==self.board[24]==self.board[32]==self.board[40]=='O') or (self.board[16]==self.board[24]==self.board[32]==self.board[40]==self.board[48]=='O') or (self.board[1]==self.board[9]==self.board[17]==self.board[25]==self.board[33]=='O') or (self.board[9]==self.board[17]==self.board[25]==self.board[33]==self.board[41]=='O') or (self.board[2]==self.board[10]==self.board[18]==self.board[26]==self.board[34]=='O') or (self.board[7]==self.board[15]==self.board[23]==self.board[31]==self.board[39]=='O') or (self.board[15]==self.board[23]==self.board[31]==self.board[39]==self.board[47]=='O') or (self.board[14]==self.board[22]==self.board[30]==self.board[38]==self.board[46]=='O') or (self.board[6]==self.board[12]==self.board[18]==self.board[24]==self.board[30]=='O') or (self.board[12]==self.board[18]==self.board[24]==self.board[30]==self.board[36]=='O') or (self.board[18]==self.board[24]==self.board[30]==self.board[36]==self.board[42]=='O') or (self.board[5]==self.board[11]==self.board[17]==self.board[23]==self.board[29]=='O') or (self.board[11]==self.board[17]==self.board[23]==self.board[29]==self.board[35]=='O') or (self.board[4]==self.board[10]==self.board[16]==self.board[22]==self.board[28]=='O') or (self.board[13]==self.board[19]==self.board[25]==self.board[31]==self.board[37]=='O') or (self.board[19]==self.board[25]==self.board[31]==self.board[37]==self.board[43]=='O') or (self.board[20]==self.board[26]==self.board[32]==self.board[38]==self.board[44]=='O'):
            result = 'You lost!'
            self.my_lbl.config(text=result)
        elif self.board_full()is True:
            result = 'A tie!'
            self.my_lbl.configure(text=result)
        else:
            pass
        return result

    def restart(self):
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        self.initialize_game()



def main():
    root = tkinter.Tk()
    my_game = Game(root)
    root.mainloop()
if __name__ == '__main__':
    main()

    #references:
    #https://stackoverflow.com/questions/27288495/python-tictactoe-gui-game-crash-when-tie#27288722
