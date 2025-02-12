"""
I am bored to get up and close my pc
"""
import subprocess
import customtkinter as ctk


class Sleeper(ctk.CTk):
    """Time for sleep"""
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("System Timer")
        self.geometry("1300x700")
        ctk.set_appearance_mode("system")  # Light/Dark/System
        ctk.set_default_color_theme("blue")

        # Grid layout
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Buttons
        self.button1 = ctk.CTkButton(self, text="30 min",
                                     font=("Arial", 45, "bold"),
                                     command=lambda: self.schedule_shutdown(30)
                                     )
        self.button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.button2 = ctk.CTkButton(self, text="60 min",
                                     font=("Arial", 55, "bold"),
                                     command=lambda: self.schedule_shutdown(60)
                                     )
        self.button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.button3 = ctk.CTkButton(self, text="90 min",
                                     font=("Arial", 65, "bold"),
                                     command=lambda: self.schedule_shutdown(90)
                                     )
        self.button3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.button4 = ctk.CTkButton(self, text="120 min",
                                     font=("Arial", 75, "bold"),
                                     command=lambda: self.schedule_shutdown(120)
                                     )
        self.button4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.cancel_button = ctk.CTkButton(self, text="Cancel Shutdown",
                                           font=("Arial", 35, "bold"),
                                           command=self.cancel_shutdown,
                                           fg_color="red"
                                           )
        self.cancel_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.error_label = ctk.CTkLabel(self, text="No shutdown is scheduled.", fg_color="red", font=("Arial", 30, "bold"))
        self.error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def schedule_shutdown(self, minutes: int) -> None:
        """Schedule system shutdown after the given minutes."""
        command = subprocess.Popen(
            ["shutdown", "-P", f"+{minutes}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = command.communicate()
        self.update_error_label(stderr)

    def cancel_shutdown(self) -> None:
        """Cancel a scheduled shutdown."""
        subprocess.run(["shutdown", "-c"], check=True)
        self.update_error_label("No shutdown is scheduled.")

    def update_error_label(self, message: str) -> None:
        """Update the error label with a new message."""
        self.error_label.configure(text=message)


if __name__ == "__main__":
    app = Sleeper()
    app.mainloop()
