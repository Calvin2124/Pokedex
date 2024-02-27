import tkinter as tk
from tkinter import messagebox
import pickle

# PARAMETRE DE LA PAGE
window = tk.Tk()
window.title("Pokédex")
window.geometry("1024x768")
window.iconbitmap('/Users/Python/image/PokéBall.png')

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

# CRÉATION DES WIDGETS
liste_pokemon = tk.Listbox(window)
liste_pokemon.pack()
# BOUTON POUR AVOIR LES INFORMATIONS SUR LE POKEMON
button_info = tk.Button(window, text="Plus d'information", command=afficher_entree)
button_info.pack()
# BOUTON POUR SUPPRIMER UN POKÉMON
bouton_supprimer = tk.Button(window, text="Supprimer Pokémon", command=supprimer_pokemon)
bouton_supprimer.pack()

label1 = tk.Label(window, text="Nom de votre Pokémon :")
label1.pack()
name_text = tk.Entry(window)
name_text.pack()

label2 = tk.Label(window, text="Type de votre Pokémon :")
label2.pack()
type_text = tk.Entry(window)
type_text.pack()

label3 = tk.Label(window, text="Vie de votre Pokémon :")
label3.pack()
life_text = tk.Entry(window)
life_text.pack()

bouton_envoi = tk.Button(window, text="Envoyer", command=lambda: ajoute_list())
bouton_envoi.pack()

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

# FIN DU PROGRAMME
window.mainloop()