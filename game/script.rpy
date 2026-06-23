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
define ta = Character("Ms Dubois")

default paul = 0
default lucien = 0
default arthur = 0
default jaques = 0
default name = "Player"
default icecream = "vanilla"
default run = False

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
    t "We have a new exchange student today. Their name is [name]. They will be in this History Class until the end of the year."
    t "Please give him a warm welcome"
    nar "The class stays silent. Its really awkward"
    nar "The class countinues, and the teachers talks about WW1 tactics. Before you know it, the bell rings."
    nar "In the next class, you are with Lucien."

    menu:
        "Sit next to Lucien?"

        "Sit next to him.":
            $ lucien += 1
            jump label_one

        "Sit by yourself.":
            jump label_two

label label_one:
    nar "You sit next to Lucien"
    l "Hey [name] how was history?"
    pl "It was ok. What about you?"
    l "Great! I love history lots. And I am with Arthur"
    pl "Ohh Arthur."
    nar "You remember lucien breifly talking about arthur earlier"
    pl "Whats he like?"
    l "He is really smart, Like really smart."
    pl "I'm sure i will meet him soon."
    l "You will! and for recess we are having croissonts which are my favourite."
    pl "Great"
    l "Let me ask you a random question before class starts"
    pl "Sure"
    l "If you could live in any year in the past, what would it be?"

    $ lucien_answer = renpy.input("What year in the past would you live in?")
    $ lucien_answer = lucien_answer.strip()

    pl "[lucien_answer]"
    l "Oh, thats crazy! Most of Vichy was built and established in [lucien_answer]"
    ta "Welcome everyone to English"
    nar "Mrs Dubois writes something on the board"
    nar "{i}The Invisible Man{/i}"
    ta "Today we are discussing {i}The Invisible Man{/i}, who is by the end of the novel, completley invisible to the other characters in the book"
    l "Thats kinda sad."
    ta "It is"
    ta "Today I'm giving you your books, please read to chapter three now, before the bell goes."
    nar "She hands everybody a book"
    nar "You start reading"
    nar "ring ring ring - the bell rings"
    nar "Everybody storms out the door, eager to go to recess"

    jump morning_tea

label label_two:
    nar "You sit by yourself."
    nar "Lucien looks back at you."
    l "Why aren't you sitting next to me?"
    menu:
        "What do you tell him?"

        "Make up a nice lie":
            nar "You walk over to him and whisper in his ear"
            pl "Well, the girl sitting next to me, looks nice and I though i'd get to know her, you know"
            l "Ohhh [name], I fully understand! Charlotte is a very pretty girl!"
            nar "You walk back to your seat, and Lucien watches you sit next to Charlotte, grinning."
            nar "He winks at you, and turns back to focus."
            ta "Welcome everyone to English"
            nar "Mrs Dubois writes something on the board"
            nar "{i}The Invisible Man{/i}"
            ta "Today we are discussing {i}The Invisible Man{/i}, who is by the end of the novel, completley invisible to the other characters in the book"
            pl "Thats kinda sad."
            ta "It is"
            ta "Today I'm giving you your books, please read to chapter three now, before the bell goes."
            nar "She hands everybody a book"
            nar "You start reading"
            nar "ring ring ring - the bell rings"
            nar "Everybody storms out the door, eager to get to recess"
            nar "You catch up with lucien to walk with him to recess"
            jump morning_tea

        "Tell him you don't feel like sitting next to him":
            pl "Listen lucien, I don't feel like sitting next to you."
            l "Oh. Ok."
            nar "You walk back to your seat. Lucien looks like he is about to cry."
            nar "The class continues on as usual, and you zone out looking out the window"
            nar "The clouds drift slowly."
            nar "Before you know it, it is time for recess"
            nar "You catch up with Lucien, before he walks out the door"
            pl "I'm sorry."
            l "Why would you ditch me like that. What did I even do?"
            pl "I just wanted to meet new people you know. I'm sorry."
            pl "Can we please, forget about this?"
            l "Okay."
            l "And I'm fine with you sitting away from me next time"
            l "We don't have to next to eachother 24/7 to still be freinds"
            l "It was just - unexpected"
            jump morning_tea
    
label morning_tea:
    nar "You and Lucien walk to the outdoor playground"
    l "This is the Quad. Everyone plays soccer, handball and basketball here"
    pl "Do you like any of thoose sports?"
    l "Nah, I'm not a very sporty person. I like going on runs though"
    pl "Cool."
    menu:
        "will you ask Lucien to go on a run with him some time?"

        "Ask him to go on a run":
            $ run = True
            pl "We should go on a run sometime."
            l "Thats a great idea, and I can take you around the town."
            pl "Yeah."
            jump morning_tea_1
        "Don't Ask him to go on a run":
            $ run = False
            jump morning_tea_1

label morning_tea_1:
    nar "Lucien waves at a group of three boys sitting down at a bench."
    nar "You walk over to the group."
    l "Hey Guys, this is [name], hes the exchange student my family is hosting for a year."
    a "Hello!"
    j "Hello!"
    p "Hello."
    pl "Hey everyone."