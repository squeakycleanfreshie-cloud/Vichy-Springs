define mu = Character("Josette")
define nar = Character("Narrator")
define pl = Character("[name]")
define l = Character("Lucien")
define a = Character("Arthur")
define j = Character("Jaques")
define p = Character("Paul")
define v = Character("Verrain")
define b = Character("Budak")
define t = Character("Mr Pernette")

default paul = 0
default lucien = 0
default arthur = 0
default jaques = 0
default name = "Player"
default icecream = "vanilla"

# The game starts here.

label start:
    nar "You wake up. Lips dry, confused about where you are."
    nar "You suddenly remember — you're in your new exchange family's house."
    nar "You get out of bed and get ready to walk downstairs."
    nar "You walk down the stairs, and catch a glimpse of your exchange family's mum."
    # place new acene here (living room)
    mu "How did you sleep, darling!"
    pl "Okay... I woke up a couple of times."
    mu "Lucien is still in his room, but he should be coming down soon."
    pl "Great."
    mu "Also, I'm making pancakes to celebrate your first day of school in France."
    nar "You don't like pancakes, but you don't show it."
    pl "Delicious."
    nar "You sit down at the table. It's awkward — you only met your family last night."
    nar "After what feels like 30 minutes of silence, Lucien finally walks down the stairs."
    l "Hello... what was your name again?"
    nar "Lucien's mum gives him a stern look."

    $ name = renpy.input("Sorry, I forgot, what is your name?")
    $ name = name.strip()

    l "Well... hello, [name]."
    pl "Hello Lucien."
    l "Are you exited for your first day of school? You will get to meet all of my freinds!"
    pl "Cool. What are there names?"
    l "There is Arthur, Jaques & Paul"
    l "Also, we have to leave for school in 10 mins, so finish your pancakes!"
    nar "You finish your pancakes and pack your bag, meeting Lucien at the door."
    l "Took you long enough! We are late, lets go!"
    # make the scene outdoors street
    nar "You and lucien walk to school"
    l "Why did you choose to exchange to france?"
    pl "I wanted to get away from my family for a year."
    l "Oh."
    l "Well you will have lots of fun in Vichy."
    l "I just found this really cool spot we can go after school"
    pl "What is is?"
    l "The old, abandoned Vichy Springs"
    l "Vichy used to a tourism town. But as time passed, and the owners stopped caring for the natural baths, tourists stopped coming in"
    l "Now its hidden away in the trees. And nobody knows about it."
    pl "Then how did you find it?"
    l "My grandfather used to talk about it. Said his father used to take the family there before the war. I went looking, and... it's still there"
    pl "Cool"
    nar "You and Lucien finish walking to school" 
    # place new school scene here
    nar "Eventually, you arrive at school. You and Lucien have been split up, because you are in seperate classes, so you are all alone"
    nar "The teacher walks into the class. He is wearing glasses, has a round face and messy hair"
    t "Hello class, sorry I'm late."
    t "We have a new exchange student today. His name is [name]. He will be in this History Class until the end of the year."










    l "Guys, I found this really cool spot we can go after school."
    l "It's the abandoned Vichy Springs."
    j "Sounds fun, I'm in."
    p "Sorry guys, I can't come. I'm busy."

    menu:
        "Convince Paul to come":
            pl "Paul, please come. It'll be fun."
            $ paul += 1
            p "...Fine. I guess I can make time."

        "Let him do his own thing":
            pl "We'll see you tomorrow, Paul."
            $ paul -= 1
            p "Yeah... see you soon."

    j "[name], what's your favourite ice-cream?"

    $ icecream = renpy.input("What is your favourite flavour of ice-cream?")
    $ icecream = icecream.strip()

    j "[icecream]? Never would've guessed."

    # This ends the game.

    return