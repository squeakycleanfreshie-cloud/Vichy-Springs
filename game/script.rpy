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
define ajp = Character("Arthur, Jaques & Paul")

default paul = 0
default lucien = 0
default arthur = 0
default jaques = 0
default name = "Player"
default icecream = "vanilla"
default run = False

label start:
    # TODO: ADD BACKGROUND — bedroom
    nar "You wake up. Lips dry, confused about where you are."
    nar "You suddenly remember — you're in your new exchange family's house."
    nar "You get out of bed and get ready to walk downstairs."
    nar "You walk down the stairs, and catch a glimpse of your exchange family's mum."
    # TODO: ADD BACKGROUND — living room
    # TODO: ADD SPRITE — Josette
    mu "How did you sleep, darling!"
    pl "Okay... I woke up a couple of times."
    mu "Lucien is still in his room, but he should be coming down soon."
    pl "Great."
    mu "Also, I'm making pancakes to celebrate your first day of school in France."
    nar "You don't like pancakes, but you don't show it."
    pl "Delicious."
    nar "You sit down at the table. It's awkward — you only met your family last night."
    nar "After what feels like 30 minutes of silence, Lucien finally walks down the stairs."
    # TODO: ADD SPRITE — Lucien
    l "Hello... what was your name again?"
    nar "Lucien's mum gives him a stern look."

    $ name = renpy.input("Sorry, I forgot, what is your name?")
    $ name = name.strip()

    l "Well... hello, [name]."
    pl "Hello, Lucien."
    l "Are you excited for your first day of school? You'll get to meet all of my friends!"
    pl "Cool. What are their names?"
    l "There's Arthur, Jaques, and Paul."
    l "Also, we have to leave for school in 10 minutes, so finish your pancakes!"
    nar "You finish your pancakes and pack your bag, meeting Lucien at the door."
    l "Took you long enough! We are late, let's go!"
    # TODO: ADD BACKGROUND — street
    # TODO: REMOVE — Josette sprite
    nar "You and Lucien walk to school."
    l "Why did you choose to exchange to France?"
    pl "I wanted to get away from my family for a year."
    l "Oh."
    l "Well, you'll have lots of fun in Vichy."
    l "I just found this really cool spot we can go to after school."
    pl "What is it?"
    l "The old, abandoned Vichy Springs."
    l "Vichy used to be a tourism town. But as time passed, and the owners stopped caring for the natural baths, tourists stopped coming in."
    l "Now it's hidden away in the trees. And nobody knows about it."
    pl "Then how did you find it?"
    l "My grandfather used to talk about it. Said his father used to take the family there before the war. I went looking, and... it's still there."
    pl "Cool."
    nar "You and Lucien finish walking to school."
    # TODO: ADD BACKGROUND — school exterior
    # TODO: REMOVE — Lucien sprite
    nar "Eventually, you arrive at school. You and Lucien have been split up because you're in separate classes, so you are all alone."
    nar "The teacher walks into the class."
    # TODO: ADD BACKGROUND — classroom
    # TODO: ADD SPRITE — Mr Pernette
    t "Hello class, sorry I'm late."
    t "We have a new exchange student today. Their name is [name]. They will be in this History class until the end of the year."
    t "Please give them a warm welcome."
    nar "The class stays silent. It's really awkward."
    nar "The class continues, and the teacher talks about WWI tactics. Before you know it, the bell rings."
    nar "In the next class, you are with Lucien."
    # TODO: ADD SPRITE — Lucien

    menu:
        "Sit next to Lucien?"

        "Sit next to him.":
            $ lucien += 1
            jump label_one

        "Sit by yourself.":
            jump label_two

label label_one:
    nar "You sit next to Lucien."
    l "Hey [name], how was History?"
    pl "It was okay. What about you?"
    l "Great! I love History lots. And I was with Arthur."
    pl "Oh, Arthur."
    nar "You remember Lucien briefly mentioning Arthur earlier."
    pl "What's he like?"
    l "He is really big and tall. But don't worry, he's super shy actually."
    pl "I'm sure I'll meet him soon."
    l "You will! And for lunch we're having croissants, which are my favourite."
    pl "Great."
    l "Let me ask you a random question before class starts."
    pl "Sure."
    l "If you could live in any year in the past, what would it be?"

    $ lucien_answer = renpy.input("What year in the past would you live in?")
    $ lucien_answer = lucien_answer.strip()

    pl "[lucien_answer]."
    l "Oh, that's crazy! A lot of Vichy was built around that time."
    # TODO: ADD SPRITE — Ms Dubois
    # TODO: REMOVE — Mr Pernette sprite
    ta "Welcome everyone to English."
    nar "Ms Dubois writes something on the board."
    nar "{i}The Invisible Man{/i}"
    ta "Today we are discussing {i}The Invisible Man{/i} — a character who is, by the end of the novel, completely invisible to the other characters in the book."
    l "That's kind of sad."
    ta "It is."
    ta "Today I'm giving you your books. Please read to chapter three before the bell goes."
    nar "She hands everybody a book."
    nar "You start reading."
    nar "Ring ring ring — the bell rings."
    nar "Everybody storms out the door, eager to get to lunch."

    jump morning_tea

label label_two:
    nar "You sit by yourself."
    nar "Lucien looks back at you."
    l "Why aren't you sitting next to me?"
    menu:
        "What do you tell him?"

        "Make up a nice lie.":
            nar "You walk over and whisper in his ear."
            pl "Well, the girl sitting next to me looks nice. Thought I'd get to know her, you know."
            l "Ohhh [name], I fully understand! Charlotte is a very pretty girl!"
            nar "You walk back to your seat, and Lucien watches you sit next to Charlotte, grinning."
            nar "He winks at you and turns back to focus."
            # TODO: ADD SPRITE — Ms Dubois
            # TODO: REMOVE — Mr Pernette sprite
            ta "Welcome everyone to English."
            nar "Ms Dubois writes something on the board."
            nar "{i}The Invisible Man{/i}"
            ta "Today we are discussing {i}The Invisible Man{/i} — a character who is, by the end of the novel, completely invisible to the other characters in the book."
            pl "That's kind of sad."
            ta "It is."
            ta "Today I'm giving you your books. Please read to chapter three before the bell goes."
            nar "She hands everybody a book."
            nar "You start reading."
            nar "Ring ring ring — the bell rings."
            nar "Everybody storms out the door, eager to get to lunch."
            nar "You catch up with Lucien to walk with him to lunch."
            jump morning_tea

        "Tell him you don't feel like sitting next to him.":
            $ lucien -= 1
            pl "Listen, Lucien. I don't feel like sitting next to you."
            l "Oh. Okay."
            nar "You walk back to your seat. Lucien looks like he's about to cry."
            nar "The class continues on as usual, and you zone out looking out the window."
            nar "The clouds drift slowly."
            nar "Before you know it, it is time for lunch."
            nar "You catch up with Lucien before he walks out the door."
            pl "I'm sorry."
            l "Why would you ditch me like that. What did I even do?"
            pl "I just wanted to meet new people, you know. I'm sorry."
            pl "Can we please forget about this?"
            l "Okay."
            l "And I'm fine with you sitting away from me next time."
            l "We don't have to sit next to each other 24/7 to still be friends."
            l "It was just... unexpected."
            jump morning_tea

label morning_tea:
    # TODO: ADD BACKGROUND — school quad
    # TODO: REMOVE — all classroom sprites
    nar "You and Lucien walk to the outdoor playground."
    l "This is the Quad. Everyone plays soccer, handball, and basketball here."
    pl "Do you like any of those sports?"
    l "Nah, I'm not a very sporty person. I like going on runs though."
    pl "Cool."
    menu:
        "Will you ask Lucien to go on a run sometime?"

        "Ask him to go on a run.":
            $ run = True
            pl "We should go on a run sometime."
            l "That's a great idea! I can take you around the town."
            pl "Yeah."
            jump morning_tea_1

        "Don't ask.":
            $ run = False
            jump morning_tea_1

label morning_tea_1:
    nar "Lucien waves at a group of three boys sitting at a bench."
    nar "You walk over to the group."
    # TODO: ADD SPRITES — Arthur, Jaques, Paul
    l "Hey guys, this is [name]. They're the exchange student my family is hosting for a year."
    a "Hello!"
    j "Hello!"
    p "Hello."
    pl "Hey everyone."
    l "Guys, I was telling [name] about this really cool spot I found that we can go to after school."
    nar "Everyone looks at Lucien with interest — but Paul just stares at the ground."
    l "So, who can come?"
    a "Sure."
    l "What about you, Jaques?"
    j "Hmmm..."
    j "Why not. I'll come."
    l "Oh well! That's everyone. Who's excite—"
    p "What about me?"
    l "Sorry, Paul. Can you come?"
    p "Yeah, sure. If you want me to."
    l "Fine."
    j "Fine."
    a "Fine."
    l "Everyone, meet out the front of school. We'll head off straight away."
    nar "The boys continue giggling and talking."
    nar "Eventually, the bell rings for class and everyone packs up."
    # TODO: ADD BACKGROUND — end of school / afternoon
    # TODO: REMOVE — Arthur, Jaques, Paul sprites
    nar "The day and classes pass, and before you know it, it's the end of school."
    nar "You go meet Lucien and his friends outside the front of the school."
    nar "They're all waiting there."
    pl "What's up, guys."
    l "Hey, [name]!"
    l "Ready to leave?"
    pl "Yeah."
    nar "You and the boys take the walk through the beautiful streets of Vichy"
    # TODO: NEXT SCENE — Streets of Vichy 
    nar "You enjoy looking at the [lucien_answer]s arcitecture."
    pl "So how long have all of you known eachother?"
    l "Since we were like, 6. We all grew up on the same street"
    a "Yeah."
    j "Lucien cried on the first day of school, and Arthur had to calm him down."
    l "That is not true"
    a "It is a little."
    nar "Paul smiles a little bit."
    l "Okay moving on."
    pl "What do you guys usally do after school?"
    j "We all go home and study."
    l "And I always want to hang out, but nobody ever wants to."
    a "We all are too busy hang out after school"
    l "After today, you will want to hang out, every day."
    nar "You notice that Paul isn't listening"
    menu:
        "Do you ask Paul if he is okay?"
        
        "Ask him if he is ok.":
            $ paul += 1
            pl "Paul, you okay?"
            p "Yeah, I'm just a bit tired."
            pl "Cool"
            jump vichy_springs_1


        "Ignore it":
            "Nobody seems to notice anyway, so its fine"
            jump vichy_springs_1

label vichy_springs_1:
    nar "You arrive a bushy deadend."
    a "Whats this lucien?"
    j "Yeah where are we"
    l "Okay, I didn't tell anyone but we are going to have to work out way through the bush."
    ajp "Lucien!"
    l "It fine, its only like 200 meters"
    ajp "Okay."
    nar "Everyone looks a bit grumpy."
    l "Okay lets go!"
    nar "you and the group trunch through the thick bush"
    nar "Lucien is at the front of the group, holding back the bushes for everyone"
    nar "He accedently lets go of one and it hits Paul in the face."
    p "Agh!"
    p "What was that for?"
    l "I'm sorry. Mistake"
    p "Ok."
    nar "You and the group continue walking."
    nar "Suddenly you hear the group gasp"
    nar "You look up, and see the sight of the old, abandoned Vichy Springs."
    nar "The water is a beautiful shade of aqua, steaming with warmth"
    nar "There are hints of the history this place had before"
    nar "Stone figures are carved out, and rusted gold rails sit."
    nar "Everything looks so new and old, at the same time."
    nar "Untouched from the people for so long."
    j "Its so beautiful!"
    p "Yeah"
    a "We can't tell anyone about this."
    l "Why?"
    a "Then everyone will want to go."
    l "Oh. Who cares? Lets swim!"
    nar "The boys are hesatative"
    a "We didn't bring swimmers."
    l "We don't need swimmers! We can just go in our clothes"
    a "You really didn't think this through."
    l "What did you think we were going to do. Sit down and rest?"
    j "YES! Exacly"
    l "Buh"
    l "What do you think, [name]?"
    menu:
        "Should you come back tommorow with swimmers?"

        "Go home, come back tommorow for a swim.":
            $ lucien -= 1
            pl "I think we should come back tommorow with our swimmers and towels."
            l "Okay. Can we at least rest here for a while"
            ajp "Sure"
            nar "You and the group find a place to rest."
            nar "You all look at the water glisten."
            pl "Why are the pumps still on? Somebodys got to be paying for them"
            a "That is odd."
            l "The town probably preserves it for historical purposes"
            a "Then why would they not tell anybody about it?"
            l "Probably so dumb kids don't ruin it."
            p "Makes sense."
            nar "Nobody talks after that, and everybody continues to soak in the glimmering sunlight."
            


        "Go for a swim in you school clothes":
                pl "I think we should go for a swim. Whats there to loose?"
                jump vichy_springs_swim_1

label vichy_springs_swim_1
    ajp "Ok. Lets do this."
    nar "You "
    $ lucien += 1

    

    
    



    
    

   
