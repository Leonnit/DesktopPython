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
bar_menu=CTkFrame(application, width=250, height=700, fg_color="#0B4B88")
bar_menu.pack(side="left", fill="x")
bar_menu.pack_propagate(False)

# Function to create a menu title section with an optional bottom border
def create_menu_title(parent, title, include_border=False, border_width=150):
    title_frame = CTkFrame(parent, width=200, height=40, fg_color="transparent")
    title_frame.pack(padx=20, pady=(40 if include_border else 10, 0))
    title_frame.pack_propagate(False)
    # Title text
    CTkLabel(title_frame,text=title,font=CTkFont(size=25, weight="bold"), text_color="white").pack(side="left")

    # Optional bottom border
    if include_border:
        border_frame = CTkFrame(parent, width=border_width, height=10, fg_color="white")
        border_frame.pack(padx=20, pady=0)
        border_frame.pack_propagate(False)
# Function to create a menu item dynamically


def create_menu_item(parent, icon_path, label_text):
    
    item_frame = CTkFrame(parent, width=250, height=40, fg_color="black")
    item_frame.pack(padx=20, pady=(10, 0))
    item_frame.pack_propagate(False)
    # Add icon
    icon_image = Image.open(icon_path).resize((25, 25), Image.Resampling.LANCZOS)
    icon = CTkImage(light_image=icon_image, dark_image=icon_image, size=(25, 25))
    CTkLabel(item_frame, image=icon, text="", fg_color="transparent").pack(pady=8, side="left", padx=10)
    # Add label
    CTkLabel( item_frame,text=label_text, text_color="white",font=CTkFont(size=16, weight="bold")).pack(pady=8, side="left", padx=10)


# Create menu title with bottom border
create_menu_title(bar_menu, "Menue", include_border=True)
# Data for menu items
menu_items = [
    {"icon": "icon/icons8-home-windows-10-310.png", "text": "Dccueil"},
    {"icon": "icon/icons8-message-ios-17-outlined-120.png", "text": "Fonction"},
    {"icon": "icon/icons8-message-ios-17-outlined-310.png", "text": "Message"},
    {"icon": "icon/icons8-list-ios-17-filled-96.png", "text": "Liste Employe"},
    {"icon": "icon/icons8-graph-material-rounded-96.png", "text": "Statistique"},
    {"icon": "icon/icons8-setting-ios-17-outlined-310.png", "text": "Calendrier"}
]
# Generate menu items dynamically
for item in menu_items:
    create_menu_item(bar_menu, item["icon"], item["text"])
# Create another menu title with bottom border
create_menu_title(bar_menu, "A l'instant", include_border=False)

## Le corps d'application Accueil
pannel=CTkFrame(application, width=1200, height=700)
pannel.pack(side='left', padx=10, pady=10)
pannel_gauche = CTkFrame(pannel, width=600, height=700, fg_color="red",)
pannel_gauche.pack(side="left", fill="x",)
pannel_gauche.pack_propagate(False)

def show_frame(frame):
    for f in frames:
        f.pack_forget() # Masquer tous les panneaux
        frame.pack(fill="both", expand=True) # Afficherle panneau sélectionné
    # Configuration de la fenêtre principale

## Creation differente pannel 
pannel_accueil = CTkFrame(pannel, width=600, height=700, fg_color="red",)
pannel_fonction = CTkFrame(pannel, width=600, height=700, fg_color="red")
pannel_message = CTkFrame(pannel, width=600, height=700, fg_color="red")
pannel_liste = CTkFrame(pannel, width=600, height=700, fg_color="red")
pannel_State = CTkFrame(pannel, width=600, height=700, fg_color="red")
pannel_parametre = CTkFrame(pannel, width=600, height=700, fg_color="red")

frames = [pannel_accueil, pannel_fonction, pannel_message, pannel_liste, pannel_State, pannel_parametre]



#Pannel pour le Menue gauche
value = "Accueil"
if value =="Accueil":
    Tire_article= CTkLabel(pannel_gauche, text="Lorem Upsom dollar", font=CTkFont(size=30, weight="bold"))
    Tire_article.pack( padx= 20, pady=20,  side="top")

    texte="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae, culpa vitae saepe quisquam eligendi maiores! Corrupti id nulla praesentium neque assumenda voluptatem quia minus aperiam, est commodi error impedit minima?"
    texte_article= CTkTextbox(pannel_gauche, width=700, height=100, font=CTkFont(size=16))
    texte_article.pack( padx= 20)
    texte_article.insert("0.0", texte)

    Tire_article= CTkLabel(pannel_gauche, text="Evenement du semaine", font=CTkFont(size=25, weight="bold"))
    Tire_article.pack( padx= 20, pady=20,  side="top")

    table_frame= CTkFrame(pannel_gauche, width=600)
    table_frame.pack( padx= 20)
    table_frame.pack_propagate(False)
    # Ajouter les en-têtes des colonnes
    columns = ["Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4"]
    for col, title in enumerate(columns):
        header =CTkLabel(table_frame, text=title, font=("Arial", 16, "bold"))
        header.grid(row=0, column=col, padx=5, pady=5)  # Ligne 0 pour les en-têtes

    # Ajouter les lignes de données
    for row in range(1, 4):  # Lignes 1 à 3
        for col in range(4):  # Colonnes 0 à 3
            cell =CTkLabel(table_frame, text=f"dedabe nohel za wa \n omeo bonbo", font=("Arial", 14))
            cell.grid(row=row, column=col, padx=5, pady=5)  # Remplir chaque cellule

if value == "fonction":
    fonction = "entre"
    if fonction == "sorti":
        pannel_formulaire = CTkFrame(pannel, width=600, height=700, fg_color="red",)
        pannel_formulaire.pack(side="left", fill="x",)
        pannel_formulaire.pack_propagate(False)

        pannel_form = CTkFrame(pannel_formulaire, width=500, height=700, fg_color="white",)
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

    
    def enregistre_entre():
        serveur_data = Database()
        username = username.get()
        vola = vola_entre.get()
        raison = raison_entre.get()

        ## entre dans le base de donne

    if fonction == "entre":
        pannel_formulaire = CTkFrame(pannel, width=600, height=700, fg_color="red",)
        pannel_formulaire.pack(side="left", fill="x",)
        pannel_formulaire.pack_propagate(False)

        pannel_form = CTkFrame(pannel_formulaire, width=500, height=700, fg_color="white",)
        pannel_form.pack(padx = 50, pady=10)
        pannel_form.pack_propagate(False)

        Titre_formulaire = CTkLabel(pannel_form, text="Solde Entre", font=CTkFont("Arail", size=25, weight="bold"))
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
        Bouton_enregistre = CTkButton(entre_pannel, text="Enregistre", width= 150, height=35, font= CTkFont("normale", size=14 ), command=enregistre_entre())
        Bouton_enregistre.pack(side="left")
        Bouton_annule = CTkButton(entre_pannel, text="annule", width= 150, height=35,fg_color="black", font= CTkFont("normale", size=14 ))
        Bouton_annule.pack(side="left", padx=20)






    

#pannel de tous le graphe de statistique
pannel_statistique = CTkFrame(pannel, width=500, height=700, fg_color="white")
pannel_statistique.pack(side="left")
pannel_statistique.pack_propagate(False)

pannel_statistique1 = CTkFrame(pannel_statistique, width=500, height=300, fg_color="white")
pannel_statistique1.pack()

Titre_statistique = CTkLabel(pannel_statistique1, text="Statistique du compte",font=CTkFont(size=20, weight="bold"))
Titre_statistique.pack()
pannel_statistique1.pack_propagate(False)
pannel_graphe = CTkFrame(pannel_statistique1, width=250, height=250)
pannel_graphe.pack(side="left")
pannel_graphe.pack_propagate(False)

pannel_legende = CTkFrame(pannel_statistique1, width=250, height=250, fg_color="white")
pannel_legende.pack(side="left", padx= 20)
pannel_legende.pack_propagate(False)

#Créer un diagramme circulaire
fig, ax = plt.subplots()  # Ajustez la taille de la figure
categories = ['Catégorie A', 'Catégorie B', 'Catégorie C', 'Catégorie D']
sizes = [10, 20, 15, 25]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Créer le graphique avec légendes
ax.pie(sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=colors)

# Ajouter les noms sous le graphique
#ax.legend(categories, loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=2)
# Ajuster manuellement les marges pour supprimer le padding
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Intégrer le graphique dans l'interface CustomTkinter
canvas = FigureCanvasTkAgg(fig, master=pannel_graphe)
canvas.get_tk_widget().pack()

for i, (category, color) in enumerate(zip(categories, colors)):
    # Ajouter un carré coloré pour chaque catégorie
    color_block =CTkLabel(pannel_legende, text=" ", width=20, height=20, fg_color=color)
    color_block.grid(row=i, column=0, padx=5, pady=5)

    # Ajouter le nom de la catégorie à côté du carré coloré
    label =CTkLabel(pannel_legende, text=category, font=CTkFont(size=14))
    label.grid(row=i, column=1, padx=5, pady=5)

# Créer un graphique en bâtons
fig, ax = plt.subplots()
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
ax.bar(categories, values)
ax.set_title("Statistique d'entree et sortie")
# Intégrer le graphique dans la fenêtre CustomTkinter
canvas = FigureCanvasTkAgg(fig, master=pannel_statistique)
canvas.get_tk_widget().pack()

application.mainloop()
