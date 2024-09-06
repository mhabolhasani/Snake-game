import consts
from game_manager import GameManager
from cell import Cell 

class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        next_x=self.val(self.cells[-1][0] + Snake.dx[self.direction])
        next_y=self.val(self.cells[-1][1] + Snake.dy[self.direction])
        next_pos=(next_x , next_y)
        next_cell=self.game.get_cell(next_pos)
        if (next_cell.color != consts.fruit_color  and next_cell.color != consts.back_color) or not next_cell:
            self.game.kill(self)
        else :
            if self.game.get_cell(next_pos).color != consts.fruit_color :
                self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)
            self.game.get_cell(next_pos).set_color(self.color)
            self.cells.append(next_pos)
        
    def handle(self, keys):
        for i in keys :
            if i in self.keys.keys() :
                if self.keys[i]=="UP" and self.direction=="DOWN" :
                    pass                  
                elif self.keys[i]=="DOWM" and self.direction=="UP" :
                    pass
                elif self.keys[i]=="RIGHT" and self.direction=="LEFT" :
                    pass
                elif self.keys[i]=="LEFT" and self.direction=="RIGHT" :
                    pass
                else :
                    self.direction=self.keys[i]
                    break        