import tkinter as tk
from dataclasses import dataclass

@dataclass
class PlayerStats:
    name: str
    win_rate: float = 0
    wins: int = 0
    accuracy: float = 0


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game App")
        self.geometry("600x450")

        # Shared data (like a controller’s model)
        self.r_stats = PlayerStats(name="R")
        self.g_stats = PlayerStats(name="G")

        # Container to hold all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Initialize pages
        for F in (StatsPage, ActionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StatsPage)

    def show_frame(self, page_class):
        """Raise the frame to the front."""
        frame = self.frames[page_class]
        frame.tkraise()


class StatsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Stats Page", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # ---- R ----
        tk.Label(self, text=f"{controller.r_stats.name}", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=5)
        tk.Label(self, text=f"Wins: {controller.r_stats.wins}").grid(row=2, column=0)
        tk.Label(self, text=f"Accuracy: {controller.r_stats.accuracy}%").grid(row=3, column=0)

        # ---- G ----
        tk.Label(self, text=f"{controller.g_stats.name}", font=("Arial", 12, "bold")).grid(row=1, column=1, pady=5)
        tk.Label(self, text=f"Wins: {controller.g_stats.wins}").grid(row=2, column=1)
        tk.Label(self, text=f"Accuracy: {controller.g_stats.accuracy}%").grid(row=3, column=1)

        # Button centered below both
        tk.Button(self, text="Go to Actions", 
                  command=lambda: controller.show_frame(ActionsPage)).grid(row=4, column=0, columnspan=2, pady=20)

        # Adjust spacing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


class ActionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Actions Page", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=15)

        tk.Label(self, text="R", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=5)
        tk.Button(self, text="Ball Potted", command=lambda: print("Ball potted!")).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self, text="Hit & miss", command=lambda: print("Hit & miss")).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(self, text="Foul", command=lambda: print("Foul Committed")).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(self, text="Snooker attempt", command=lambda: print("Snooker attempt...")).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(self, text="Next shot", command=lambda: print("Next shot")).grid(row=6, column=0, padx=10, pady=5)
        tk.Button(self, text="End Visit", command=lambda: print("Next player...")).grid(row=7, column=0, padx=10, pady=5)

        tk.Label(self, text="G", font=("Arial", 14, "bold")).grid(row=1, column=1, padx=10)
        tk.Button(self, text="Ball Potted", command=lambda: print("Ball potted!")).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self, text="Hit & miss", command=lambda: print("Hit & miss")).grid(row=3, column=1, padx=10, pady=5)
        tk.Button(self, text="Foul", command=lambda: print("Foul Committed")).grid(row=4, column=1, padx=10, pady=5)
        tk.Button(self, text="Snooker attempt", command=lambda: print("Snooker attempt...")).grid(row=5, column=1, padx=10, pady=5)
        tk.Button(self, text="Next Shot", command=lambda: print("Next shot...")).grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self, text="End Visit", command=lambda: print("Next player...")).grid(row=7, column=1, padx=10, pady=5)

        tk.Button(self, text="Back to Stats", 
                  command=lambda: controller.show_frame(StatsPage)).grid(row=8, column=0, padx=10, pady=15)


if __name__ == "__main__":
    app = App()
    app.mainloop()
