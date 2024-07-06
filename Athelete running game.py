import tkinter as tk
import random

my_root = tk.Tk()
my_root.title("Athlete Running Game")

my_canvas = tk.Canvas(my_root, width=800, height=400, bg="white")
my_canvas.pack()

my_finish_line = 750
my_canvas.create_line(my_finish_line, 0, my_finish_line, 400, fill="red", width=5)

my_athlete1 = my_canvas.create_rectangle(50, 100, 100, 150, fill="blue")
my_athlete2 = my_canvas.create_rectangle(50, 250, 100, 300, fill="green")

my_athlete1_name = "Blue Bolt"
my_athlete2_name = "Green Flash"

my_athlete1_score = 0
my_athlete2_score = 0

my_score_label1 = tk.Label(my_root, text=f"{my_athlete1_name}: {my_athlete1_score}", font=("Arial", 14))
my_score_label1.pack()
my_score_label2 = tk.Label(my_root, text=f"{my_athlete2_name}: {my_athlete2_score}", font=("Arial", 14))
my_score_label2.pack()

def my_reset_race():
    my_canvas.coords(my_athlete1, 50, 100, 100, 150)
    my_canvas.coords(my_athlete2, 50, 250, 100, 300)
    my_canvas.delete("winner_text")

def my_start_race():
    my_canvas.move(my_athlete1, random.randint(1, 10), 0)
    my_canvas.move(my_athlete2, random.randint(1, 10), 0)

    my_athlete1_pos = my_canvas.coords(my_athlete1)[2]
    my_athlete2_pos = my_canvas.coords(my_athlete2)[2]

    if my_athlete1_pos >= my_finish_line:
        global my_athlete1_score
        my_athlete1_score += 1
        my_canvas.create_text(400, 200, text=f"{my_athlete1_name} Wins!", font=("Arial", 24), fill="blue", tag="winner_text")
        my_update_scores()
    elif my_athlete2_pos >= my_finish_line:
        global my_athlete2_score
        my_athlete2_score += 1
        my_canvas.create_text(400, 200, text=f"{my_athlete2_name} Wins!", font=("Arial", 24), fill="green", tag="winner_text")
        my_update_scores()
    else:
        my_root.after(50, my_start_race)

def my_update_scores():
    my_score_label1.config(text=f"{my_athlete1_name}: {my_athlete1_score}")
    my_score_label2.config(text=f"{my_athlete2_name}: {my_athlete2_score}")

my_start_button = tk.Button(my_root, text="Start Race", command=my_start_race)
my_start_button.pack()

my_reset_button = tk.Button(my_root, text="Reset Race", command=my_reset_race)
my_reset_button.pack()

my_root.mainloop()
