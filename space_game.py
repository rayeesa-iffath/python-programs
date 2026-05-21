import tkinter as tk
import random

window = tk.Tk()
window.title("Space Shooter")

canvas = tk.Canvas(window, width=600, height=600, bg="black")
canvas.pack()

player = canvas.create_rectangle(270, 550, 330, 580, fill="blue")

bullets = []
enemies = []

score = 0

def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

def shoot(event):
    x1, y1, x2, y2 = canvas.coords(player)
    bullet = canvas.create_rectangle(x1+25, y1-10, x1+35, y1, fill="yellow")
    bullets.append(bullet)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<space>", shoot)

while True:

    if random.randint(1, 20) == 1:
        x = random.randint(50, 550)
        enemy = canvas.create_oval(x, 0, x+40, 40, fill="red")
        enemies.append(enemy)

    for bullet in bullets:
        canvas.move(bullet, 0, -15)

    for enemy in enemies:
        canvas.move(enemy, 0, 5)

    for bullet in bullets:
        bullet_pos = canvas.coords(bullet)

        for enemy in enemies:
            enemy_pos = canvas.coords(enemy)

            if bullet_pos and enemy_pos:
                if (bullet_pos[0] < enemy_pos[2] and
                    bullet_pos[2] > enemy_pos[0] and
                    bullet_pos[1] < enemy_pos[3] and
                    bullet_pos[3] > enemy_pos[1]):

                    canvas.delete(bullet)
                    canvas.delete(enemy)

                    bullets.remove(bullet)
                    enemies.remove(enemy)

                    score += 1
                    window.title(f"Score: {score}")

    window.update()
    canvas.after(30)

window.mainloop()
