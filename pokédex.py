import tkinter as tk
from tkinter import messagebox
import pickle
from tkinter import PhotoImage
from PIL import Image, ImageTk

# PARAMETRE DE LA PAGE
window = tk.Tk()
window.title("Pokédex")
window.geometry("1024x695")
# Chemin de l'image PNG
image_path = "/Users/Python/image/PokéBall.png"
# Charger l'image
icon_image = tk.PhotoImage(file=image_path)
# Définir l'icône de la fenêtre
window.iconphoto(True, icon_image)

# Chargement de l'image au format
image_life = "/Users/Python/image/regeneration50x50-effet-minecraft.png"
life_img = tk.PhotoImage(file=image_life)
image_pokemon = "/Users/Python/image/International1_Pokémon_logo.png"
pokemon_img = tk.PhotoImage(file=image_pokemon)
image_type = "/Users/Python/image/pokemon-symbol-png-tra.png"
type_img = tk.PhotoImage(file=image_type)

#FONCTION GIF
class AnimatedGIF(tk.Label):
    def __init__(self, master, path):
        self.master = master
        self.index = 0
        self.gif = Image.open(path)
        self.frames = []
        try:
            while True:
                self.frames.append(self.gif.copy())
                self.gif.seek(len(self.frames))
        except EOFError:
            pass
        self.delay = self.gif.info['duration']
        self.image = ImageTk.PhotoImage(self.frames[0])
        super().__init__(master, image=self.image)

    def update_image(self):
        self.index += 1
        if self.index == len(self.frames):
            self.index = 0
        self.image.paste(self.frames[self.index])
        self.after(self.delay, self.update_image)

# FONCTION POUR CHARGER LES DONNÉES
def charger_donnees():
    try:
        with open('/Users/Python/projetPython/pokemon_file.pkl', 'rb') as f:
            if f.read(1):  # Vérifie si le fichier n'est pas vide
                f.seek(0)  # Réinitialise la position du curseur au début du fichier
                return pickle.load(f)
            else:
                return {}
    except (FileNotFoundError, EOFError):
        return {}

pokedex = charger_donnees()

# FONCTION POUR SAUVEGARDER LES DONNÉES
def sauvegarder_donnees():
    with open('/Users/Python/projetPython/pokemon_file.pkl', 'wb') as f:
        pickle.dump(pokedex, f)

# FONCTION POUR AFFICHER LES INFORMATIONS DU POKÉMON SÉLECTIONNÉ
def afficher_entree():
    index = liste_pokemon.curselection()
    if index:
        index = int(index[0])
        test = liste_pokemon.get(index)
        entree = pokedex.get(test, "")
        messagebox.showinfo("Info", f"Élément : {entree[0]}\nType : {entree[1]}")

# FONCTION POUR SUPPRIMER UN POKÉMON DE LA LISTBOX ET DU FICHIER PKL
def supprimer_pokemon():
    index = liste_pokemon.curselection()
    if index:
        index = int(index[0])
        pokemon_a_supprimer = liste_pokemon.get(index)
        del pokedex[pokemon_a_supprimer]
        liste_pokemon.delete(index)
        sauvegarder_donnees()

frame = tk.Frame(window, padx=5, pady=5)
frame.pack(fill="both", expand=True)

# Première ligne avec 3 éléments centrés
div1 = tk.Frame(frame, bg="#5490d5", pady=32)
div1.grid(row=0, column=0, sticky="nsew")

div2 = tk.Frame(frame, bg="#5490d5", pady=32)
div2.grid(row=0, column=1, sticky="nsew")

div3 = tk.Frame(frame, bg="#5490d5", pady=32)
div3.grid(row=0, column=2, sticky="nsew")

#REMPLIR LES ELEMENTS 
label_pokemon = tk.Label(div1, image=pokemon_img, bg="#5490d5")
label_pokemon.pack()
label1 = tk.Label(div1, text="Nom de votre Pokémon :", bg="#5490d5", fg="black", pady=10, font=("Helvetica", 19))
label1.pack()
name_text = tk.Entry(div1, bg="#5490d5", border=0, fg="#000")
name_text.pack() 

label_type = tk.Label(div2, image=type_img, bg="#5490d5")
label_type.pack()
label2 = tk.Label(div2, text="Type de votre Pokémon :", bg="#5490d5", fg="black", pady=10, font=("Helvetica", 19))
label2.pack()
type_text = tk.Entry(div2, bg="#5490d5", border=0, fg="#000")
type_text.pack()

label_life = tk.Label(div3, image=life_img, bg="#5490d5")
label_life.pack()
label3 = tk.Label(div3, text="Vie de votre Pokémon :", bg="#5490d5", fg="black", pady=10, font=("Helvetica", 19))
label3.pack()
life_text = tk.Entry(div3, bg="#5490d5", border=0, fg="#000")
life_text.pack()

# Deuxième ligne avec un élément qui prend toute la longueur et centré
div4 = tk.Frame(frame)
div4.grid(row=1, column=0, columnspan=3, sticky="nsew")

# Charger et afficher le GIF animé
gif_label = AnimatedGIF(div4, "/Users/Python/image/tumblr_mb7ajc09St1rfjowdo1_500.gif")
gif_label.grid(row=0, column=0)
# gif_label.configure(bg="#316ef3")
# Mettre à jour l'affichage du GIF animé
gif_label.update_image()

# LISTBOX
liste_pokemon = tk.Listbox(div4, bg="#316ef3")
liste_pokemon.grid(row=0, column=1, sticky="nsew")

container_btn = tk.Frame(div4, pady=150, padx=70)
container_btn.grid(row=0, column=2, sticky="nsew")


# BOUTON POUR AVOIR LES INFORMATIONS SUR LE POKEMON
button_info = tk.Button(container_btn, text="Plus d'information", pady=15, padx= 15, command=afficher_entree)
button_info.grid(row=0, column=1, sticky="nsew")
# BOUTON POUR SUPPRIMER UN POKÉMON
bouton_supprimer = tk.Button(container_btn, text="Supprimer Pokémon", pady=15, padx= 15, command=supprimer_pokemon)
bouton_supprimer.grid(row=1, column=1, sticky="nsew", pady=30)
# BOUTON D'ENVOI
bouton_envoi = tk.Button(container_btn, text="Envoyer", pady=15, padx= 15, command=lambda: ajoute_list())
bouton_envoi.grid(row=3, column=1, sticky="nsew")



# FONCTION POUR AJOUTER UN POKÉMON À LA LISTE
def ajoute_list():
    type_pokemon = type_text.get()
    life_pokemon = life_text.get()
    name_pokemon = name_text.get()
    pokedex[name_pokemon] = (type_pokemon, life_pokemon)
    liste_pokemon.insert(tk.END, name_pokemon)
    sauvegarder_donnees()
    type_text.delete(0, tk.END)
    life_text.delete(0, tk.END)
    name_text.delete(0, tk.END)
    messagebox.showinfo("Sauvegarde", "Pokémon sauvegardé !")

# CHARGEMENT INITIAL DES DONNÉES
for pokemon in pokedex:
    liste_pokemon.insert(tk.END, pokemon)

    # Configurer le redimensionnement des cellules de la grille pour qu'elles s'ajustent lors du redimensionnement de la fenêtre
for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

frame.grid_rowconfigure(1, weight=1)

# FIN DU PROGRAMME
window.mainloop()