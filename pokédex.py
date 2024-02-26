import tkinter as tk
from tkinter import Tk, Button 
from tkinter import messagebox
import pickle

# PARAMETRE DE LA PAGE
window = tk.Tk()
window.title("Pokédex")
window.geometry("1024x768")


#CRÉATION DES FONCTIONS 
#sauvegarde dans la listbox le nom du pokemon
def ajoute_list():
    type_pokemon = type_text.get()
    life_pokemon = life_text.get()
    name_pokemon = name_text.get()
    pokedex[name_pokemon] = type_pokemon, life_pokemon
    liste_pokemon.insert(tk.END, name_pokemon)
    messagebox.showinfo("Sauvegarde", "Pokémon sauvegardé !")

def afficher_entree():
    index = liste_pokemon.curselection()
    if index:
        index = int(index[0])
        test = liste_pokemon.get(index)
        entree = pokedex.get(test, "")
        messagebox.showinfo("Info", f"Élément : {entree[0]}\n Type : {entree[1]}")


# DONNÉES UTILISATEUR 
liste_pokemon = tk.Listbox(window)
liste_pokemon.bind("<<ListboxSelect>>")
liste_pokemon.pack()
button_info = tk.Button(window, text="Plus d'information", command=afficher_entree)
button_info.pack()
#-----
label1 = tk.Label(window, text="Nom de votre pokemon :")
label1.pack()
name_text = tk.Entry(window)
name_text.pack()
#-----
label2 = tk.Label(window, text="Élément de votre pokemon :")
label2.pack()
type_text = tk.Entry(window)
type_text.pack()
#-----
label3 = tk.Label(window, text="Type de votre pokemon :")
label3.pack()
life_text = tk.Entry(window)
life_text.pack()
#-----
bouton_envoi = tk.Button(window, text ="Envoyer",command=ajoute_list)
bouton_envoi.pack()
pokedex = {}


# FIN DU PROGRAMME
window.mainloop()