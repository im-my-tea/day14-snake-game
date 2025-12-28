import turtle as t
from snake import Snake
import time

# 1. Setup Screen
S = t.Screen()
S.title("Snake Xenzia")
S.bgcolor("aqua")
S.setup(width=600, height=600)
S.tracer(0)

# 2. Create Snake
snake = Snake()

S.listen()
S.onkey(snake.up, "Up")
S.onkey(snake.down, "Down")
S.onkey(snake.left, "Left")
S.onkey(snake.right, "Right")

# 3. Game Loop
game_is_on = True
while game_is_on:
    S.update() # Refresh screen
    time.sleep(0.1) # Delay
    
    snake.move() # Move snake




S.mainloop()