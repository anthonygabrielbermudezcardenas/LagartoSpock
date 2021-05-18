import random
import json
import os
from messages import msg

print("¡BIENVENIDO ESTAS JUGANDO A PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK!")

SAVE_ON_EXIT = True
SAVE_EACH_CYCLE = False
SAVEFILE = 'save.json'
victorias = [["P", "T"], ["PA", "P"], ["T", "PA"], ["P", "L"], ["L", "PA"], ["L", "S"], ["S", "T"], ["S", "PA"]]
opciones = ["P", "PA", "T", "L", "S"]
# players = None
players = {
    "juan": {
        "Victorias": 0,
        "Derrotase": 0,
        "Empates": 0
    },
    "manuel": {
        "Victorias": 0,
        "Derrotas": 0,
        "Empates": 0
    }
}


def userWins(msg):
    print(msg)
    players[player]["Victorias"] = players[player]["Victorias"] + 1


def userLoses(msg):
    print(msg)
    players[player]["Derrotas"] = players[player]["Derrotas"] + 1


def userDraw(msg):
    print(msg)
    players[player]["Empates"] = players[player]["Empates"] + 1


def userInput():
    print("Elije una de estas tres opciones: (P)iedra, (PA)pel , (T)ijeras, (L)agarto, (S)pock y si quiere salir: Salir(SA)")
    user = input(opciones)

    if user == "SA":
        if SAVE_ON_EXIT:
            saveGame(players)
        exit()
    while user not in opciones:
        print("\nOpcion no valida: elija de nuevo")
        user = input("Elije: P, PA, T, L, S ")
    return user


def saveGame(players):
    with open(SAVEFILE, "w") as outfile:
        json.dump(players, outfile, indent=4)


def loadGame(player):
    if os.path.isfile(SAVEFILE):
        with open(SAVEFILE) as json_file:
            players = json.load(json_file)
            if player in players:
                print(players[player])
            else:
                players[player] = {
                    "Victorias": 0,
                    "Derrotas": 0,
                    "Empates": 0
                }
            return players

    else:
        return {player: {
            "Victorias": 0,
            "Derrotas": 0,
            "Empates": 0
        }}

print("¿Cómo te llamas?") 
player = input("Ingresa tu nombre: ")
players = loadGame(player)

while True:
    user = userInput()
    pc = random.choice(opciones)
    print(f"La pc ha selecionado  {pc}")
    if user == pc:
        userDraw(msg)
        print(msg["userDraw"])
    elif [user, pc] in victorias:
        userWins(msg)
        print(msg["userWins"])
    else:
        userLoses(msg)
        print(msg["userLoses"])

    print(players[player])
    if SAVE_EACH_CYCLE:
        saveGame(players)
