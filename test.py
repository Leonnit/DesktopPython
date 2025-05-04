from customtkinter import *
from tkinter import *
from database import Database
from PIL import Image, ImageDraw, ImageOps
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def make_rounded_image(image_path, size, radius):
    # Charger l'image
    image = Image.open(image_path).resize(size, Image.Resampling.LANCZOS)

    # Créer un masque arrondi
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    # Appliquer le masque à l'image
    rounded_image = ImageOps.fit(image, size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)
    return rounded_image

application = CTk()
application.geometry("1200x700")
application.title("Mon Application")

set_appearance_mode("Light")  # Mode clair

# Bar de menu avec couleur de fond blanche
bar_menue_top = CTkFrame(application, fg_color="white", height=60)  # Couleur blanche définie
bar_menue_top.pack(fill="x")

Logo = CTkLabel(bar_menue_top, text="logo Me", font=CTkFont(size=40, weight="bold")).pack(padx=20, pady=5, side="left")

bar= CTkFrame(bar_menue_top, height=50, fg_color="white")
bar.pack(side="right", padx=30)
phrase = CTkLabel(bar, text="Tongasoa eto Gestion de Magasin", font=CTkFont(size=16, weight="bold")).pack(side="left", padx=30, pady=20)
bar_recherche = CTkEntry(bar, height=40, width=300, placeholder_text="Recherche ici.....")
bar_recherche.pack(side="left", padx=10, pady=10)
# Panneaux circulaires (bord arrondi) avec couleur grise
pannel1 = CTkFrame(bar, corner_radius=50, width=40, height=40, fg_color="#e0e0e0")  # Gris
pannel1.pack(side="left", padx=10)
pannel2 = CTkFrame(bar, corner_radius=50, width=40, height=40, fg_color="#e0e0e0")  # Gris
pannel2.pack(side="left", padx=10)
panel_connexion = CTkFrame(bar, height=50, fg_color="transparent")
panel_connexion.pack(side="left")

# Charger une image et créer un CTkImage
icon_message = Image.open("icon/icons8-message-ios-17-outlined-120.png")  # Remplacez par le chemin de votre image
message = CTkImage(light_image=icon_message, dark_image=icon_message, size=(25, 25))  # Taille spécifiée Ajouter un widget label pour afficher l'image
label = CTkLabel(pannel1, image=message, text="", fg_color="transparent")  # Pas de fond visible
label.pack(pady=8, padx=10)

# Charger une autre image et créer un CTkImage
icon_notification = Image.open("icon/icons8-notification-ios-17-outlined-120.png")  # Remplacez par le chemin de votre image
notification = CTkImage(light_image=icon_notification, dark_image=icon_notification, size=(25, 25))  # Taille spécifiée
# Ajouter un widget label pour afficher l'image
label = CTkLabel(pannel2, image=notification, text="", fg_color="transparent")  # Pas de fond visible
label.pack(pady=8, padx=10)

# Charger une image arrondie et créer un CTkImage
icon_profile = make_rounded_image("icon/tsaya Man (532).jpg", size=(40, 40), radius=20)
profile = CTkImage(light_image=icon_profile, dark_image=icon_profile, size=(40, 40))  # Taille spécifiée

# Ajouter l'image arrondie
label = CTkLabel(panel_connexion, image=profile, text="", fg_color="transparent")  # Pas de fond visible
label.pack(pady=5, side="left", padx=10)  # Positionnement ajusté

Label_nom=CTkLabel(panel_connexion, text="N.Leonnit",font=CTkFont(size=16, weight="bold")).pack(pady=(10,0))
Connecte=CTkLabel(panel_connexion, text="Connecte",font=CTkFont(size=14,)).pack(pady=(0))

# Bare de menu Verticale
bar_menu=CTkFrame(application, width=200, height=700, fg_color="#0B4B88", border_color=None)
bar_menu.pack(side="left", fill="x")
bar_menu.pack_propagate(False)

Titre_menue = CTkLabel(bar_menu, text="Menue", text_color="white", font=CTkFont("Arial", size=30, weight="bold"))
Titre_menue.pack(padx= 30, pady=(50, 30))

## passe 
def show_frame(frame):
    for f in frames:
        f.pack_forget() # Masquer tous les panneaux
        frame.pack(fill="both", expand=True) # Afficherle panneau sélectionné
    print("mety eee", )
    if frame == pannel_accueil:
        Tire_article= CTkLabel(pannel_accueil, text="Accueil", font=CTkFont(size=30, weight="bold"))
        Tire_article.pack( padx= 20, pady=20,  side="top")
    if frame == pannel_fonction:
        print("mampidtra na mamoka")
        pannel_form = CTkFrame(pannel_fonction, width=500, height=700, fg_color="white",)
        pannel_form.pack(padx = 50, pady=10)
        pannel_form.pack_propagate(False)

        Titre_formulaire = CTkLabel(pannel_form, text="Solde Sortie", font=CTkFont("Arail", size=25, weight="bold"))
        Titre_formulaire.pack(pady =10)

        entre_pannel = CTkFrame(pannel_form, width= 400, height=120, fg_color="transparent")
        entre_pannel.pack(padx=20, pady=(10, 0))
        entre_pannel.pack_propagate(False)
        username = CTkLabel(entre_pannel, text="Nom du Porteur:", font=CTkFont("normal", size=16))
        username.pack(padx=(0, 220))
        username_entre = CTkEntry(entre_pannel, placeholder_text="Entre le nom de porteur..", width=400, height=40, font=CTkFont(size=16))
        username_entre.pack(padx=20)
        texte="ulla praesentium neque assumenda voluptatem quia minus aperiam, est commodi error impedit minima?"
        texte_article= CTkTextbox(entre_pannel, width=700, height=50, font=CTkFont("normal",size=12))
        texte_article.pack( padx= 20)
        texte_article.insert("0.0", texte)

        entre_pannel = CTkFrame(pannel_form, width= 400, height=120, fg_color="transparent")
        entre_pannel.pack(padx=20)
        entre_pannel.pack_propagate(False)
        vola = CTkLabel(entre_pannel, text="Totale du money:", font=CTkFont("normal", size=16))
        vola.pack(padx=(0, 220))
        vola_entre = CTkEntry(entre_pannel, placeholder_text="Nombre du money", width=400, height=40, font=CTkFont(size=16))
        vola_entre.pack(padx=20)
        texte="ulla praesentium neque assumenda voluptatem quia minus aperiam, est commodi error impedit minima?"
        texte_article= CTkTextbox(entre_pannel, width=700, height=50, font=CTkFont("normal",size=12))
        texte_article.pack( padx= 20)
        texte_article.insert("0.0", texte)

        entre_pannel = CTkFrame(pannel_form, width= 400, height=120, fg_color="transparent")
        entre_pannel.pack(padx=20)
        entre_pannel.pack_propagate(False)
        raison = CTkLabel(entre_pannel, text="Raison de sortie:", font=CTkFont("normal", size=16))
        raison.pack(padx=(0, 220))
        raison_entre = CTkEntry(entre_pannel, placeholder_text="Raison de sortie", width=400, height=40, font=CTkFont(size=16))
        raison_entre.pack(padx=20)
        texte="ulla praesentium neque assumenda voluptatem quia minus aperiam, est commodi error impedit minima?"
        texte_article= CTkTextbox(entre_pannel, width=700, height=50, font=CTkFont("normal",size=12))
        texte_article.pack( padx= 20)
        texte_article.insert("0.0", texte)

        entre_pannel = CTkFrame(pannel_form, width= 400, height=120, fg_color="transparent")
        entre_pannel.pack(padx=20)
        Bouton_enregistre = CTkButton(entre_pannel, text="Enregistre", width= 150, height=35, font= CTkFont("normale", size=14 ))
        Bouton_enregistre.pack(side="left")
        Bouton_annule = CTkButton(entre_pannel, text="annule", width= 150, height=35,fg_color="black", font= CTkFont("normale", size=14 ))
        Bouton_annule.pack(side="left", padx=20)
    if frame == pannel_message:
        Tire_article= CTkLabel(pannel_message, text="Message", font=CTkFont(size=30, weight="bold"))
        Tire_article.pack( padx= 20, pady=20,  side="top")
    if frame == pannel_State:
        Tire_article= CTkLabel(pannel_State, text="Message", font=CTkFont(size=30, weight="bold"))
        Tire_article.pack( padx= 20, pady=20,  side="top")
    if frame == pannel_liste:
        Tire_article= CTkLabel(pannel_liste, text="liste", font=CTkFont(size=30, weight="bold"))
        Tire_article.pack( padx= 20, pady=20,  side="top")

    if frame == pannel_parametre:
        Tire_article= CTkLabel(pannel_parametre, text="parametre", font=CTkFont(size=30, weight="bold"))
        Tire_article.pack( padx= 20, pady=20,  side="top")
    def enregistre_entre():
        serveur_data = Database()
        username = username.get()
        vola = vola_entre.get()
        raison = raison_entre.get()
    # Configuration de la fenêtre principale


boutton_home = CTkButton(bar_menu,text="Accueil", command=lambda:show_frame(pannel_accueil), fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white", height=35)
boutton_home.pack(pady=10)
boutton_fonction =CTkButton(bar_menu,text="Fonction", command=lambda:show_frame(pannel_fonction), fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white" , height=35)
boutton_fonction.pack(pady=10)
boutton_message =CTkButton(bar_menu,text="Message", command=lambda:show_frame(pannel_message), fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white" , height=35)
boutton_message.pack(pady=10)
boutton_liste =CTkButton(bar_menu,text="Liste", command=lambda:show_frame(pannel_liste), fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white" , height=35)
boutton_liste.pack(pady=10)
boutton_state =CTkButton(bar_menu,text="Statistique", command=lambda:show_frame(pannel_State),fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white",  height=35)
boutton_state.pack(pady=10)
boutton_parametre =CTkButton(bar_menu,text="Parametre", command=lambda:show_frame(pannel_parametre), fg_color="transparent" , width=200, font= CTkFont("bold", size=14 ), text_color="white", height=35)
boutton_parametre.pack(pady=10)


## Le corps d'application Accueil
pannel=CTkFrame(application, width=1200, height=700, fg_color="black")
pannel.pack(side='left', padx=5, pady=5)
pannel.pack_propagate(False)

pannel_gauche = CTkFrame(pannel, width=600, height=700, fg_color="red",)
pannel_gauche.pack(side="left", fill="x",)
pannel_gauche.pack_propagate(False)

pannel_droite = CTkFrame(pannel, width=600, height=700, fg_color="green",)
pannel_droite.pack(side="right", fill="x",)
pannel_droite.pack_propagate(False)
## Fin creaction du gauche droite

## Creation differente pannel 
pannel_accueil = CTkFrame(pannel_gauche, width=600, height=700, fg_color="white",)
pannel_fonction = CTkFrame(pannel_gauche, width=600, height=700, fg_color="red")
pannel_message = CTkFrame(pannel_gauche, width=600, height=700, fg_color="green")
pannel_liste = CTkFrame(pannel_gauche, width=600, height=700, fg_color="gray")
pannel_State = CTkFrame(pannel_gauche, width=600, height=700, fg_color="yellow")
pannel_parametre = CTkFrame(pannel_gauche, width=600, height=700, fg_color="orange")

frames = [pannel_accueil, pannel_fonction, pannel_message, pannel_liste, pannel_State, pannel_parametre]

application.mainloop()