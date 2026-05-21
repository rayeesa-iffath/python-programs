
import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=500, bg="black")
canvas.pack()

ball = canvas.create_oval(290,250,310,270, fill="white")

paddle = canvas.create_rectangle(250,450,350,470, fill="blue")

bricks = []

for i in range(5):
    for j in range(8):
        brick = canvas.create_rectangle(
            j*75, i*30,
            j*75+70, i*30+20,
            fill="red"
        )
        bricks.append(brick)

x_speed = 3
y_speed = 3

def move_left(event):
    canvas.move(paddle, -30, 0)

def move_right(event):
    canvas.move(paddle, 30, 0)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

while True:

    canvas.move(ball, x_speed, y_speed)

    pos = canvas.coords(ball)
    paddle_pos = canvas.coords(paddle)

    if pos[0] <= 0 or pos[2] >= 600:
        x_speed = -x_speed

    if pos[1] <= 0:
        y_speed = -y_speed

    if pos[3] >= 500:
        break

    if (pos[2] >= paddle_pos[0] and
        pos[0] <= paddle_pos[2] and
        pos[3] >= paddle_pos[1]):

        y_speed = -y_speed

    for brick in bricks:
        brick_pos = canvas.coords(brick)

        if (pos[2] >= brick_pos[0] and
            pos[0] <= brick_pos[2] and
            pos[1] <= brick_pos[3]):

            canvas.delete(brick)
            bricks.remove(brick)

            y_speed = -y_speed
            break

    window.update()
    canvas.after(10)

window.mainloop()
