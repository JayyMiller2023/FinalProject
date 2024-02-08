
# TODO: Pick a theme, then create a battle sequence, finally have choices for the player.
#       - Make enemies fair to the player
#       - Make as many quests as you can
#       - make a reasonable Game Over Select

import time
import random
import tkinter as tk
from tkinter import messagebox

name = input("Enter your character's name: ")

def game_over():
    print("\nGame Over!")
    choice = input("Do you want to start over? (yes/no): ").lower()
    if choice == "yes":
        CollapsedBuilding()
    if choice == "no":
        print("Farewell")
        exit()


def introduction():
    print("Hello there! Welcome to my final game in this subject, AFTERLIFE SPECTRUM (I know, a cheesy name but just roll with it)")
    time.sleep(3)
    print("To start, How about we pick a name for your character?")
    time.sleep(1)


def create_character():
    # Character Creation Prompt
    print(f"\"{name}\". What an interesting name...")
    time.sleep(1)
    print("Applying updated information")
    time.sleep(3)
    print("Applied!")
    time.sleep(1)
    print("Running...")
    time.sleep(1)
    
    return name

def Run_Savestate() :
    print("Cycle complete! before we go, do you wish to upload a save state?")
    choice0 = ("! (Yes/No) !")
    if choice0 == "yes" : 
        code = input("! Please Insert Code !")
        if code == "104" : 
            Chapter2()
        else : 
            print("Sorry, the corrisponding code is not available, please try again")
            exit()
    else:
        CollapsedBuilding()


def CollapsedBuilding():
    print("You awaken in a desoulate world, the sand kicks along with the wind and you can see pieces of metal scattered around")
    time.sleep(1)
    print("Come to think of it... You seem to be in a building.")
    time.sleep(1)
    print("? How on earth did you survive that fall anyways ?")
    time.sleep(1)
    messagebox.showerror("Notice", "? This is known as a clue about this lore and maybe the character ?", icon=messagebox.INFO, type=messagebox.OK)
    time.sleep(1)
    Choice1 = input("! There are two ways to go, one in front of you and one that leads to a garden. Where do you go? (Front/ Back) !")
    if Choice1 == "Front": 
        Streets()
    if Choice1 == "Back":
        Garden()

def Streets() :
    time.sleep(1)
    print("Before you go, you take a piece of cloth that was exposed to water dripping from a pipe earlier and used it to cover your face and eyes")
    time.sleep(1)
    print("You begin to walk the once thriving streets, now empty, the sand kick on your feet as you rush to find source of water to restock your cloth")
    time.sleep(1)
    print("instead, you find a house in the middle of nowhere.")
    Chapter2()

def Garden() :
    print("Before you go, you take a piece of cloth that was exposed to water dripping from a pipe earlier and used it to cover your face and eyes")
    time.sleep(1)
    print("you walk to the back to find a secret tunnel, there you wonder the empty corridor, until you see a light at the end")
    time.sleep(1)
    print("you walk you walk into a house from the painting")
    Chapter2()

def Chapter2() :
    time.sleep(1)
    print("Saving state...")
    time.sleep(3)
    print("Saved!")
    time.sleep(2)
    print("! Save state code is 104 !")
    time.sleep(2)
    print("You wander the strange house, It seemed like ages sense you've seen a house like this")
    time.sleep(1)
    print("? But why put it in the middle of the city, and in such a familiar manner, like you've been here before ?")
    time.sleep(1)
    print("Regardless, you know someone lives here, the only question is...")
    time.sleep(1)
    Choice2 = messagebox.showinfo("Notice", "! Do you find the owner? !", icon=messagebox.INFO, type=messagebox.YESNO)
    if Choice2 == messagebox.YES:
        time.sleep(1)
        print("You look around for the owner of the estate and find noone, so you just go out when you stumble apon a guy")
        time.sleep(1)
        print("He then urges you back inside.")
        time.sleep(1)
        print("\n\n???: You really shouldn't be out here, especially at night!")
        time.sleep(1)
        print(f"\n{name}: What? Why?")
        time.sleep(1)
        print("\n\n???: Theres a HUGE tornado out there, and the sand is intoxicated, how on earth didn't you die?")
        time.sleep(1)
        print(f"\n{name}: I don't know!")
    if Choice2 == messagebox.NO:
        time.sleep(1)
        print("You don't want to waste their time anyways, but the moment you do get outside, the wind pick up a whole bunch.")
        time.sleep(1)
        print("You then rush back inside, just in time for the owner to rush back inside the house.")
        time.sleep(1)
        print("\n\n???: You really shouldn't be out here, especially at night!")
        time.sleep(1)
        print(f"\n{name}: What? Why?")
        time.sleep(1)
        print("\n\n???: Theres a HUGE tornado out there, and the sand is intoxicated, how on earth didn't you die?")
        time.sleep(1)
        print(f"\n{name}: I don't know!")

def main():
    introduction()
    player = create_character()
    Run_Savestate()
    


if __name__ == "__main__":
    main()