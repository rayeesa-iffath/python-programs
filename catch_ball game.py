import tkinter as tk
import random

window = tk.Tk()

canvas = tk.Canvas(window, width=500, height=500, bg="black")
canvas.pack()

basket = canvas.create_rectangle(200,450,300,480, fill="blue")

ball = canvas.create_oval(240,0,270,30, fill="red")

score = 0

def move_left(event):
    canvas.move(basket, -30, 0)

def move_right(event):
    canvas.move(basket, 30, 0)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

while True:

    canvas.move(ball, 0, 10)

    ball_pos = canvas.coords(ball)
    basket_pos = canvas.coords(basket)

    if ball_pos[3] >= 500:

        x = random.randint(50,450)

        canvas.coords(ball, x, 0, x+30, 30)

    if (ball_pos[2] >= basket_pos[0] and
        ball_pos[0] <= basket_pos[2] and
        ball_pos[3] >= basket_pos[1]):

        score += 1

        window.title(f"Score: {score}")

        x = random.randint(50,450)

        canvas.coords(ball, x, 0, x+30, 30)

    window.update()

    canvas.after(30)

window.mainloop()

