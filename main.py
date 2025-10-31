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

        # Shared data
        self.r_stats = PlayerStats(name="R")
        self.g_stats = PlayerStats(name="G")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (StatsPage, ActionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StatsPage)

    def show_frame(self, page_class):
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

        tk.Button(self, text="Go to Actions",
                  command=lambda: controller.show_frame(ActionsPage)).grid(row=4, column=0, columnspan=2, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


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
        self.geometry("650x500")

        self.r_stats = PlayerStats(name="R")
        self.g_stats = PlayerStats(name="G")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (StatsPage, ActionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StatsPage)

    def show_frame(self, page_class):
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

        tk.Button(self, text="Go to Actions",
                  command=lambda: controller.show_frame(ActionsPage)).grid(row=4, column=0, columnspan=2, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


class ActionsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.active_player = None
        self.active_type = None
        self.current_player = None
        self.timeline = []
        self.visit_counts = {"R": 0, "G": 0}
        self.shot_counts = {"R": 0, "G": 0}
        self.break_player = None  # which player takes the break
        self.break_shot = True    # break mode is active until next shot or end visit

        tk.Label(self, text="Actions Page", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=15)

        # --- Left column (R player) ---
        tk.Label(self, text="R", font=("Arial", 14, "bold")).grid(row=1, column=0)
        self.r_buttons = [
            tk.Button(self, text="Ball Potted", command=lambda: self.player_action("R", "pot")),
            tk.Button(self, text="Hit & Miss", command=lambda: self.player_action("R", "miss")),
            tk.Button(self, text="Foul", command=lambda: self.player_action("R", "foul")),
            tk.Button(self, text="Snooker Attempt", command=lambda: self.snooker_attempt("R")),
            tk.Button(self, text="Next Shot", command=lambda: self.next_shot("R")),
            tk.Button(self, text="End Visit", command=lambda: self.end_visit("R")),
        ]
        for i, btn in enumerate(self.r_buttons, start=2):
            btn.grid(row=i, column=0, pady=5)

        # --- Right column (G player) ---
        tk.Label(self, text="G", font=("Arial", 14, "bold")).grid(row=1, column=2)
        self.g_buttons = [
            tk.Button(self, text="Ball Potted", command=lambda: self.player_action("G", "pot")),
            tk.Button(self, text="Hit & Miss", command=lambda: self.player_action("G", "miss")),
            tk.Button(self, text="Foul", command=lambda: self.player_action("G", "foul")),
            tk.Button(self, text="Snooker Attempt", command=lambda: self.snooker_attempt("G")),
            tk.Button(self, text="Next Shot", command=lambda: self.next_shot("G")),
            tk.Button(self, text="End Visit", command=lambda: self.end_visit("G")),
        ]
        for i, btn in enumerate(self.g_buttons, start=2):
            btn.grid(row=i, column=2, pady=5)

        # --- Middle column for dynamic action options ---
        self.action_frame = tk.Frame(self)
        self.action_frame.grid(row=2, column=1, rowspan=6, sticky="n")
        self.action_buttons = []

        # Secondary button categories
        self.pot_types = ["Plant", "90–45°", "0–45°", "Rail Shot", "Hit & Hope"]
        self.foul_types = [
            "Hit opponent ball", "Hit black ball", "Ball exit table",
            "Potted opponent ball", "Potted black", "Physical contact",
            "Potted white ball"
        ]

        tk.Button(self, text="Back to Stats",
                  command=lambda: controller.show_frame(StatsPage)).grid(row=8, column=0, columnspan=3, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    # --- Player action handling ---
    def player_action(self, player, action_type):
        # Set current player if first action of visit
        if not self.current_player:
            self.current_player = player
            self.toggle_player_buttons(active_player=player)
            if not self.break_player:
                self.break_player = player  # first player to act takes the break
            self.start_new_visit(player)

        if player != self.current_player:
            print(f"Ignored input: It's currently {self.current_player}'s visit.")
            return

        # Break mode: only break_player can take break, print immediately, no secondary buttons
        if self.break_shot and player == self.break_player and action_type in ("pot", "miss", "foul"):
            shot_num = self.shot_counts[player]
            main_text = {
                "pot": "Ball potted",
                "miss": "Hit & miss",
                "foul": "Foul"
            }[action_type]
            entry = f"Shot {shot_num}: {player} — {main_text} (break)"
            print(entry)
            self.timeline.append(entry)
            return

        # Normal behavior: show secondary buttons
        if action_type in ("pot", "miss", "foul"):
            self.show_action_options(player, action_type)

    def show_action_options(self, player, action_type):
        self.active_player = player
        self.active_type = action_type

        for btn in self.action_buttons:
            btn.grid_forget()
        self.action_buttons.clear()

        if action_type in ("pot", "miss"):
            options = self.pot_types
        else:
            options = self.foul_types

        for i, opt in enumerate(options):
            btn = tk.Button(self.action_frame, text=opt, command=lambda o=opt: self.select_action_type(o))
            btn.grid(row=i, column=0, pady=2, padx=10, sticky="ew")
            self.action_buttons.append(btn)

    def select_action_type(self, selection):
        player = self.active_player
        action_type = self.active_type
        shot_num = self.shot_counts[player]

        main_text = {
            "pot": "Ball potted",
            "miss": "Hit & miss",
            "foul": "Foul"
        }.get(action_type, action_type.capitalize())

        entry = f"Shot {shot_num}: {player} — {main_text}, {selection}"
        print(entry)
        self.timeline.append(entry)

        for btn in self.action_buttons:
            btn.grid_forget()
        self.action_buttons.clear()

    def snooker_attempt(self, player):
        if not self.current_player:
            self.current_player = player
            self.toggle_player_buttons(active_player=player)
            if not self.break_player:
                self.break_player = player
            self.start_new_visit(player)

        if player != self.current_player:
            print(f"Ignored input: It's currently {self.current_player}'s visit.")
            return

        shot_num = self.shot_counts[player]
        entry = f"Shot {shot_num}: {player} — Snooker attempt"
        print(entry)
        self.timeline.append(entry)

    def start_new_visit(self, player):
        self.visit_counts[player] += 1
        self.shot_counts[player] = 1
        header = f"------ {player} Visit {self.visit_counts[player]} ------"
        print(header)
        self.timeline.append(header)

    def next_shot(self, player):
        if player != self.current_player:
            print(f"Ignored input: It's currently {self.current_player}'s visit.")
            return

        self.shot_counts[player] += 1

        # End break only for break_player
        if self.break_shot and player == self.break_player:
            self.break_shot = False

    def end_visit(self, player):
        # End break if break_player ends visit
        if self.break_shot and player == self.break_player:
            self.break_shot = False

        next_player = "G" if player == "R" else "R"
        self.current_player = next_player
        self.start_new_visit(next_player)
        self.toggle_player_buttons(active_player=next_player)

    def toggle_player_buttons(self, active_player):
        if active_player == "R":
            for btn in self.r_buttons:
                btn.config(state="normal")
            for btn in self.g_buttons:
                btn.config(state="disabled")
        elif active_player == "G":
            for btn in self.g_buttons:
                btn.config(state="normal")
            for btn in self.r_buttons:
                btn.config(state="disabled")
        else:
            for btn in self.r_buttons + self.g_buttons:
                btn.config(state="normal")




if __name__ == "__main__":
    app = App()
    app.mainloop()
