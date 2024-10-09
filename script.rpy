# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    $ refuse_drink = False
    $ drank_tea = False
    $ right_pocket = True
    $ the_bag = True
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "i am escaping the range, i have found some keys!"

    e "can you help me choose a key?"

    

    # test branching
menu:
     "what one chould i choose?"

     "gold key.":
         "i have chosen the gold key, but it was not quite the right choice"

     "silver key.":
         $ drank_tea = True
         "i have chosen the silver key, this seems to be the right key, but what could it open?"

     "bronze key.":
         $ refuse_drink = True
         jump ending

label after_menu:
     "i need to keep the key safe, where should i keep it?"
menu:
     "right pocket.":
         $ right_pocket = True
         " this pocket is perfect, the key is definitley safe here"

     "left pocket.":
         "This pocket has a hole in it!, i cannot use this pocket"

     "the bag.":
         $ the_bag = False
         "the bag is too big and i have lost the key"
         jump ending

label after_menu2:

     "after choosing the key, i found myself infront of three doors, not knowing which one to open."
menu:
    "yellow door.":
        "wrong door, you are in the sargents office and got told off  '"
        
    "red door.":
        "not quite right, try again "
        
    "green door." if drank_tea:
        "YES!, you have chosen the right door, you can now go to target practice '"

label ending:
    if refuse_drink:
        "you chose the bronze key, the sargent caught you, you now have to leave! "
    else:
        "The end."
return