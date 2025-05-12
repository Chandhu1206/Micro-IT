import tkinter as tk
from time import strftime

class ClockStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock & Stopwatch")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.clock_label = tk.Label(root, font=("Arial", 18), bg="black", fg="white")
        self.clock_label.pack(pady=10, fill='x')
        self.update_clock()

        self.stopwatch_time = 0
        self.running = False

        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 30), fg="green")
        self.stopwatch_label.pack(pady=10)

        buttons_frame = tk.Frame(root)
        buttons_frame.pack()

        self.start_btn = tk.Button(buttons_frame, text="Start", command=self.start_stopwatch, width=8)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(buttons_frame, text="Stop", command=self.stop_stopwatch, width=8)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(buttons_frame, text="Reset", command=self.reset_stopwatch, width=8)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_clock(self):
        time_string = strftime('%I:%M:%S %p')
        self.clock_label.config(text=f"Current Time: {time_string}")
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            self.stopwatch_time += 1
            mins, secs = divmod(self.stopwatch_time, 60)
            hours, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.root.after(1000, self.update_stopwatch)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_stopwatch()

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.stopwatch_time = 0
        self.stopwatch_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockStopwatchApp(root)
    root.mainloop()
