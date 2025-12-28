# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale, exhale.")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()  # Inherit num_eyes
    
#     def breathe(self):
#         super().breathe()   # Do what Animals do
#         print("doing this underwater.")

#     def swim(self):
#         print("moving in water.")

# # Test it
# nemo = Fish()
# nemo.swim()
# nemo.breathe() 
# print(f"Nemo has {nemo.num_eyes} eyes.")

from turtle import Turtle, Screen

tim = Turtle()
S = Screen()
S.bgcolor("aqua")
S.setup(width=600, height=600)

def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)
    
def clear_screen():
    tim.home()
    tim.clear()

# 1. Start Listening
S.listen()

# 2. Bind Keys to Functions
# Note: No parentheses () after function names!
S.onkey(key="w", fun=move_forwards)
S.onkey(key="a", fun=turn_left)
S.onkey(key="d", fun=turn_right)
S.onkey(key="c", fun=clear_screen)

S.exitonclick()