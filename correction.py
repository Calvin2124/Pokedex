import tkinter as tk
from tkinter import messagebox
import pickle


fenetre = tk.Tk()
fenetre.title("Pokédex")
class Pokemon:
    def __init__(self, nom, type, capacites):
        self.type = type
        self.nom = nom
        self.capacites = capacites

def sauvegarde_pokedex():
    with open("correction_file.pkl", "wb") as f:
        pickle.dump(pokedex, f)

def charger_pokedex():
    try:
        with open("correction_file.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return[] #SI LE FICHIER N'EST PAS TROUVÉ, ENVOI UNE LISTE VIDE

def afficher_details():
    index = list_pokemon.curselection()
    if index:
        pokemon = pokedex [index[0]]
        messagebox.showinfo("Détail du pokemon :", f"Nom : {pokemon.nom} \n Type : {pokemon.type} \n Capacitée : {pokemon.capacites}")
    else: 
        messagebox.showwarning("Aucune selection", "Aucun pokemon sélectionné")

def ajouter_pokemon():
    nom = entry_nom.get()
    type_pokemon = entry_type.get()
    capacite = entry_capacite.get()
    #ON AJOUTE LE POKEMON A LA LISTE 
    pokedex.append(Pokemon(nom, type_pokemon, capacite))
    #AJOUTE LE POKEMON SUR LA LISTBOX
    list_pokemon.insert(tk.END, nom)
    #SAUVEGARDE LA LISTE NOUVELLEMENT MISE A JOUR 
    sauvegarde_pokedex()
    messagebox.showinfo("Pokemon ajouté !", "Le pokemon a été ajouté !")

pokedex = charger_pokedex()
# lISTE DE POKEMON
list_pokemon = tk.Listbox(fenetre)
#PEUPLER LA LISTE DES POKÉMONS
for pokemon in pokedex: 
    list_pokemon.insert(tk.END, pokemon.nom)
list_pokemon.pack()
#BOUTON QUI AFFICHE 
bouton_detail = tk.Button(fenetre, text="Afficher les détail", command=afficher_details)
bouton_detail.pack()

#AJOUTER FORMULAIRE 
label_nom = tk.Label(fenetre, text="Nom du pokemon : ")
label_nom.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

label_type = tk.Label(fenetre, text="Type du pokemon : ")
label_type.pack()
entry_type = tk.Entry(fenetre)
entry_type.pack()

label_capacite = tk.Label(fenetre, text="Capacité du pokemon : ")
label_capacite.pack()
entry_capacite = tk.Entry(fenetre)
entry_capacite.pack()

bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_pokemon)
bouton_ajouter.pack()





fenetre.mainloop()