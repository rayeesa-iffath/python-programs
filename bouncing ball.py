import tkinter as tk

window = tk.Tk()
window.title("Bouncing Ball")

canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="red")

x_speed = 3
y_speed = 3

while True:

    canvas.move(ball, x_speed, y_speed)

    position = canvas.coords(ball)

    if position[3] >= 400 or position[1] <= 0:
        y_speed = -y_speed

    if position[2] >= 600 or position[0] <= 0:
        x_speed = -x_speed

    window.update()

    canvas.after(10)

window.mainloop()
