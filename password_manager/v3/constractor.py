import customtkinter as ctk
from PIL import Image
from widgets import Labels


class MainWindow(ctk.CTk):
    """
    Main window class
    """

    def __init__(self):
        super().__init__()
        # self.geometry('600x600')  # '1280x800'| '1366x768' | '1600x900' | '1920x1080'
        self.resizable(False, False)
        self.title("Password Manager")
        ctk.set_appearance_mode("system")  # Light/Dark/System
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # Grid
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Logo
        image = Image.open("logo2.png")
        ctk_image = ctk.CTkImage(light_image=image, size=(500, 300))

        self.logo = ctk.CTkLabel(self, image=ctk_image, text="")
        # self.logo.pack(padx=20, pady=10)
        self.logo.grid(row=0, column=0,
                       columnspan=2,
                       padx=0,
                       sticky="n")

        # Widgets
        self.labels = Labels(self)
        # self.labels.pack(padx=20, pady=10)
        self.labels.grid(row=1, column=0,
                         columnspan=1,
                         padx=0, pady=0,
                         sticky="nsew")


def main():
    app = MainWindow()
    app.mainloop()


if __name__ == '__main__':
    main()
