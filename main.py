from dataclasses import dataclass
import tkinter as tk


# Create main window
root = tk.Tk()
root.title("Stats Page")
root.geometry("400x300")  

# Example labels
# ----- R Player Labels -----
R_name_label = tk.Label(root, text="R")
R_name_label.grid(row=0, column=0, sticky="w", padx=50)

R_wins_label = tk.Label(root, text="Wins:")
R_wins_label.grid(row=1, column=0, sticky="w", padx=50)

R_win_rate_label = tk.Label(root, text="Win Rate:")
R_win_rate_label.grid(row=2, column=0, sticky="w", padx=50)

R_accuracy_label = tk.Label(root, text="Accuracy:")
R_accuracy_label.grid(row=3, column=0, sticky="w", padx=50)

# ----- G Player Labels -----
G_name_label = tk.Label(root, text="G")
G_name_label.grid(row=0, column=1, sticky="w", padx=50)

G_wins_label = tk.Label(root, text="Wins:")
G_wins_label.grid(row=1, column=1, sticky="w", padx=50)

G_win_rate_label = tk.Label(root, text="Win Rate:")
G_win_rate_label.grid(row=2, column=1, sticky="w", padx=50)

G_accuracy_label = tk.Label(root, text="Accuracy:")
G_accuracy_label.grid(row=3, column=1, sticky="w", padx=50)



# Run the application
root.mainloop()

@dataclass
class PlayerStats:
    name: str
    win_rate: float = 0
    wins: int = 0
    accuracy: float = 0

# Creates player objects
r_stats = PlayerStats(name="r")
g_stats = PlayerStats(name="g")

# Updates win rates
def update_win_rates():
    r_stats.win_rate=r_stats.wins/g_stats.wins
    g_stats.win_rate=g_stats.wins/r_stats.wins

# Print stats
print(r_stats)
print(g_stats)
