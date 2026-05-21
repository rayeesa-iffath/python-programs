import tkinter as tk
import random

window = tk.Tk()
window.title("Car Racing Game")

WIDTH = 400
HEIGHT = 600

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

car = canvas.create_rectangle(180, 500, 220, 580, fill="blue")

enemy = canvas.create_rectangle(180, 0, 220, 80, fill="red")

score = 0

def move_left(event):
    canvas.move(car, -20, 0)

def move_right(event):
    canvas.move(car, 20, 0)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

while True:

    canvas.move(enemy, 0, 10)

    enemy_pos = canvas.coords(enemy)
    car_pos = canvas.coords(car)

    # Reset enemy
    if enemy_pos[3] > HEIGHT:
        x = random.randint(50, 300)
        canvas.coords(enemy, x, 0, x+40, 80)
        score += 1
        window.title(f"Score: {score}")

    # Collision detection
    if (car_pos[2] > enemy_pos[0] and
        car_pos[0] < enemy_pos[2] and
        car_pos[3] > enemy_pos[1]):

        canvas.create_text(200, 300, text="GAME OVER", fill="white", font=("Arial", 30))
        break

    window.update()
    canvas.after(50)

window.mainloop()
