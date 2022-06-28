from tkinter import *
import random
GAME_WIDTH=1200
GAME_HEIGHT=700
SPEED=200
SPACE_SIZE=50 
BODY_PARTS=1
SNAKE_COLOR="#0099ff"
FOOD_COLOR="#cc3300"
BACKGROUN_COLOR="#333"
class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.cordenadas=[]
        self.esquare=[]
        for i in range(0,BODY_PARTS):
            self.cordenadas.append([0,0]) 
        for x,y in self.cordenadas:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag='snake')
            self.esquare.append(square)
class Food:
    def __init__(self):
        x=random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.cordenadas=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

def next_turn(snake,food):
    x,y=snake.cordenadas[0]
    if direction=='up':
        y-=SPACE_SIZE
    elif direction=='down':
        y+=SPACE_SIZE
    elif direction=='left':
        x-=SPACE_SIZE
    elif direction=='right':
        x+=SPACE_SIZE
    snake.cordenadas.insert(0,(x,y))
    squere=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.esquare.insert(0,squere)
    if x==food.cordenadas[0] and y==food.cordenadas[1]:
        global score
        score+=1
        label.config(text=f"PONTOS: {score}")
        canvas.delete('food')
        food=Food()
    else:
        del snake.cordenadas[-1]
        canvas.delete(snake.esquare[-1])
        del snake.esquare[-1]
    if check_collisetion(snake):
        game_over()
    else:
        app_game.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
    global direction
    if new_direction=='left':
        if direction!='right':
            direction=new_direction
    if new_direction=='right':
        if direction!='left':
            direction=new_direction
    if new_direction=='down':
        if direction!='up':
            direction=new_direction
    if new_direction=='up':
        if direction!='down':
            direction=new_direction
            
def check_collisetion(snake):
    x,y=snake.cordenadas[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    if y<0 or y>=GAME_HEIGHT:
        return True
    for body_parts in snake.cordenadas[1:]:
        if x==body_parts[0] and y==body_parts[1]:
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('roboto',40),text="GAME OVER",fill='red',tag='gameover')
if __name__=='__main__':
    app_game=Tk()
    app_game.title("JOGUINHO DE COBRA")
    app_game.state("zoomed")
    app_game.resizable(0,0)
    score=0
    direction='down'
    label=Label(app_game,text='PONTOS: {}'.format(score),font=('roboto',30))
    label.pack()
    canvas=Canvas(app_game,bg=BACKGROUN_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
    canvas.pack()
    app_game.update()
    app_game_width=app_game.winfo_width()
    app_game_height=app_game.winfo_height()
    screen_width=app_game.winfo_screenwidth()
    screen_height=app_game.winfo_screenheight()
    #
    x=int((screen_width/2)-(app_game_width/2))
    y=int((screen_height/2)-(app_game_height/2))
    #
    #app_game.geometry(f"{app_game_width}X{app_game_height}+{x}+{y}")
    app_game.bind('<Left>',lambda event:change_direction('left'))
    app_game.bind('<Up>',lambda event:change_direction('up'))
    app_game.bind('<Right>',lambda event:change_direction('right'))
    app_game.bind('<Down>',lambda event:change_direction('down'))
    snake=Snake()    
    food=Food()
    next_turn(snake, food)
    app_game.mainloop()

