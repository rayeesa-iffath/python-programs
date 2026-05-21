import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

ball = canvas.create_oval(290,190,310,210, fill="white")

paddle = canvas.create_rectangle(250,370,350,390, fill="blue")

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

    if pos[3] >= 400:
        canvas.create_text(300,200,text="GAME OVER",fill="red",font=("Arial",30))
        break

    if (pos[2] >= paddle_pos[0] and
        pos[0] <= paddle_pos[2] and
        pos[3] >= paddle_pos[1]):

        y_speed = -y_speed

    window.update()
    canvas.after(10)

window.mainloop()

