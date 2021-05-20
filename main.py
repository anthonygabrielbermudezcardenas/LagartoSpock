import random
import json
import os
import time
from messages import msg


SAVE_ON_EXIT = True
SAVE_EACH_CYCLE = False
SAVEFILE = 'save.json'
victorias = [["P", "T"], ["PA", "P"], ["T", "PA"], ["P", "L"], ["L", "PA"], ["L", "S"], ["S", "T"], ["S", "PA"]]
opciones = ["P", "PA", "T", "L", "S"]
players = {
    "player": 0
}

startTime = None
stats = {
    "inputGood": 0,
    "totalTeclas": 0
}


def updateTimeStats():
    stats['elapsedTime'] = time.time() - startTime


def updatePlayStats(status):
    players[player][status] += 1
    print(msg[status])


def endGame():
    if SAVE_ON_EXIT:
        saveGame(players)

    gmTime = time.gmtime(stats['elapsedTime'])
    print(time.strftime("%H:%M:%S", gmTime))
    exit()


def userInput():
    global stats
    user = None
    firstTime = True
    while user not in opciones:
        if not firstTime:
            print("\nOpcion no valida: elija de nuevo")
        firstTime = False
        user = input("Elije una de estas tres opciones: (P)iedra, (PA)pel , (T)ijeras, (L)agarto, (S)pock y si quiere salir: Salir(SA)")
        stats["totalTeclas"] += 1

        if user == "SA":
            endGame()

    stats["inputGood"] += 1

    return user


def saveGame(players):
    with open(SAVEFILE, "w") as outfile:
        updateTimeStats()
        json.dump(players, outfile, indent=4)


def loadGame(player):
    if os.path.isfile(SAVEFILE):
        with open(SAVEFILE) as json_file:
            players = json.load(json_file)
            if player in players:
                print(players[player])
                inicio()
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


def init():
    global player
    global players
    print("¡BIENVENIDO ESTAS JUGANDO A PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK!")
    print("¿Cómo te llamas?")
    player = input("Ingresa tu nombre: ")
    players = loadGame(player)

    return time.time()


def main():
    global startTime
    startTime = init()
    while True:
        user = userInput()
        pc = random.choice(opciones)
        print(f"La pc ha selecionado {pc}")
        if user == pc:
            updatePlayStats("Empates")
        elif [user, pc] in victorias:
            updatePlayStats("Victorias")
        else:
            updatePlayStats("Derrotas")

        print(players[player])
        if SAVE_EACH_CYCLE:
            saveGame(players)


main()
