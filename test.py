import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageDraw, ImageOps


def make_rounded_image(image_path, size, radius):
    """Crée une image avec des bords arrondis."""
    image = Image.open(image_path).resize(size, Image.Resampling.LANCZOS)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    rounded_image = ImageOps.fit(image, size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)
    return rounded_image


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("Mon Application")

        ctk.set_appearance_mode("Light")  # Mode clair

        self.setup_menu_top()
        self.setup_sidebar()
        self.setup_main_panel()
        self.setup_frames()

    def setup_menu_top(self):
        """Création de la barre de menu supérieure."""
        self.menu_top = ctk.CTkFrame(self, fg_color="white", height=60)
        self.menu_top.pack(fill="x")
        ctk.CTkLabel(self.menu_top, text="Logo Me", font=ctk.CTkFont(size=40, weight="bold")).pack(side="left", padx=20, pady=5)
        bar = ctk.CTkFrame(self.menu_top, height=50, fg_color="white")
        bar.pack(side="right", padx=30)
        ctk.CTkLabel(bar, text="Tongasoa eto Gestion de Magasin", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=30, pady=20)
        ctk.CTkEntry(bar, height=40, width=300, placeholder_text="Recherche ici...").pack(side="left", padx=10, pady=10)
        self.setup_top_icons(bar)

    def setup_top_icons(self, parent):
        """Ajoute les icônes en haut à droite."""
        icons = [("icon/icons8-message-ios-17-outlined-120.png", "#e0e0e0"),
                 ("icon/icons8-notification-ios-17-outlined-120.png", "#e0e0e0")]

        for icon_path, color in icons:
            pannel = ctk.CTkFrame(parent, corner_radius=50, width=40, height=40, fg_color=color)
            pannel.pack(side="left", padx=10)
            img = Image.open(icon_path)
            icon = ctk.CTkImage(light_image=img, dark_image=img, size=(25, 25))
            ctk.CTkLabel(pannel, image=icon, text="").pack(pady=8, padx=10)

        profile_img = make_rounded_image("icon/tsaya Man (532).jpg", size=(40, 40), radius=20)
        profile = ctk.CTkImage(light_image=profile_img, dark_image=profile_img, size=(40, 40))

        panel_connexion = ctk.CTkFrame(parent, height=50, fg_color="transparent")
        panel_connexion.pack(side="left")

        ctk.CTkLabel(panel_connexion, image=profile, text="").pack(pady=5, side="left", padx=10)
        ctk.CTkLabel(panel_connexion, text="N.Leonnit", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 0))
        ctk.CTkLabel(panel_connexion, text="Connecté", font=ctk.CTkFont(size=14)).pack()

    def setup_sidebar(self):
        """Création de la barre de menu latérale."""
        self.sidebar = ctk.CTkFrame(self, width=200, fg_color="#0B4B88")
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="Menu", text_color="white", font=ctk.CTkFont(size=30, weight="bold")).pack(pady=(50, 30))

        menu_items = [
            ("Accueil", "accueil"), ("Fonction", "fonction"), ("Message", "message"),
            ("Liste", "liste"), ("Statistique", "stat"), ("Paramètre", "parametre")
        ]

        for text, frame_name in menu_items:
            ctk.CTkButton(self.sidebar, text=text, command=lambda f=frame_name: self.show_frame(f),
                          fg_color="transparent", text_color="white",
                          font=ctk.CTkFont(size=14), width=200, height=35).pack(pady=10)

    def setup_main_panel(self):
        """Création du panneau principal."""
        self.main_panel = ctk.CTkFrame(self, width=1200, fg_color="black")
        self.main_panel.pack(side='left', padx=5, pady=5, fill="both", expand=True)

        self.panel_left = ctk.CTkFrame(self.main_panel, width=600, fg_color="red")
        self.panel_left.pack(side="left", fill="both", expand=True)
        self.panel_left.pack_propagate(False)

        self.panel_right = ctk.CTkFrame(self.main_panel, width=600, fg_color="green")
        self.panel_right.pack(side="right", fill="both", expand=True)

    def setup_frames(self):
        """Création des panneaux de contenu."""
        self.frames = {
            "accueil": ctk.CTkFrame(self.panel_left, fg_color="white"),
            "fonction": ctk.CTkFrame(self.panel_left, fg_color="red"),
            "message": ctk.CTkFrame(self.panel_left, fg_color="green"),
            "liste": ctk.CTkFrame(self.panel_left, fg_color="gray"),
            "stat": ctk.CTkFrame(self.panel_left, fg_color="yellow"),
            "parametre": ctk.CTkFrame(self.panel_left, fg_color="orange")
        }
        for frame in self.frames.values():
            frame.pack(fill="both", expand=True)
            frame.pack_forget()  # Masquer toutes les pages au démarrage

        self.show_frame("accueil")  # Afficher l'accueil par défaut

    def show_frame(self, frame_name):
        """Affiche le panneau sélectionné."""
        for frame in self.frames.values():
            frame.pack_forget()

        self.frames[frame_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop() 
