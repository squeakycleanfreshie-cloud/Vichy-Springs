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
define h = Character("Harriet")

default paul = 0
default lucien = 0
default arthur = 0
default jaques = 0
default name = "Player"
default icecream = "vanilla"
default run = False
default swim = False
default karma = 0
default game = False

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
    ajp "Hello!"
    # NOTE: Paul's hello should be flatter/quieter than Arthur and Jaques — consider a separate line for him
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
    # TODO: ADD BACKGROUND — school exterior, afternoon
    # TODO: REMOVE — Arthur, Jaques, Paul sprites
    nar "The day and classes pass, and before you know it, it's the end of school."
    nar "You go meet Lucien and his friends outside the front of the school."
    nar "They're all waiting there."
    pl "What's up, guys."
    l "Hey, [name]!"
    l "Ready to leave?"
    pl "Yeah."
    # TODO: ADD BACKGROUND — streets of Vichy
    # TODO: ADD SPRITES — all four boys walking
    nar "You and the boys take the walk through the beautiful streets of Vichy."
    nar "You enjoy looking at the architecture."
    pl "So how long have all of you known each other?"
    l "Since we were like, six. We all grew up on the same street."
    a "Yeah."
    j "Lucien cried on the first day of school, and Arthur had to calm him down."
    l "That is not true."
    a "It is a little."
    nar "Paul smiles at that — just a little."
    l "Okay, moving on."
    pl "What do you guys usually do after school?"
    j "Nothing really."
    p "We usually just hang around the quad or go to Lucien's."
    l "Which is why the springs will be so fun. Something actually different."
    nar "Paul goes quiet and looks away."
    menu:
        "Do you say anything to Paul?"

        "Ask if he's okay.":
            $ paul += 1
            pl "You alright, Paul?"
            p "Yeah. Fine."
            nar "He doesn't look fine. But he gives you a small nod — like he appreciated being asked."
            jump vichy_springs_approach

        "Leave it.":
            nar "Nobody else seemed to notice anyway."
            jump vichy_springs_approach

label vichy_springs_approach:
    # TODO: ADD BACKGROUND — bushy dead end / forest edge
    nar "You arrive at a bushy dead end."
    a "What's this, Lucien?"
    j "Yeah, where are we?"
    l "Okay, I didn't tell anyone, but we are going to have to work our way through the bush."
    ajp "Lucien!"
    l "It's fine, it's only like 200 metres."
    ajp "Okay."
    nar "Everyone looks a bit grumpy."
    l "Okay, let's go!"
    # TODO: ADD BACKGROUND — dense bush / pushing through trees
    nar "You and the group trudge through the thick bush."
    nar "Lucien is at the front, holding back branches for everyone."
    nar "He accidentally lets go of one and it hits Paul in the face."
    p "Agh!"
    p "What was that for?"
    l "I'm sorry. Mistake."
    p "Okay."
    nar "You and the group continue walking."
    nar "Suddenly, you hear the group gasp."
    # TODO: ADD BACKGROUND — Vichy Springs reveal (wide shot, aqua water, steam, stone figures, rusted gold rails)
    nar "You look up and see the old, abandoned Vichy Springs."
    nar "The water is a beautiful shade of aqua, steaming with warmth."
    nar "There are hints of the history this place once had."
    nar "Stone figures are carved out, and rusted gold rails sit at the edges."
    nar "Everything looks so new and old at the same time."
    nar "Untouched by people for so long."
    j "It's so beautiful."
    p "Yeah."
    a "We can't tell anyone about this."
    l "Why?"
    a "Then everyone will want to come."
    l "Oh. Who cares? Let's swim!"
    nar "The boys hesitate."
    a "We didn't bring swimmers."
    l "We don't need swimmers. We can just go in our clothes."
    a "You really didn't think this through."
    l "What did you think we were going to do — sit down and rest?"
    j "Yes! Exactly."
    l "Buh—"
    l "What do you think, [name]?"
    menu:
        "What do you do?"

        "Go home, come back tomorrow with swimmers.":
            $ lucien -= 1
            $ swim = False
            pl "I think we should come back tomorrow with our swimmers and towels."
            l "Okay. Can we at least rest here for a while?"
            ajp "Sure."
            nar "You and the group find a place to sit."
            nar "You all look at the water glisten."
            pl "Why are the pumps still on? Somebody's got to be paying for them."
            a "That is odd."
            l "The town probably preserves it for historical purposes."
            a "Then why would they not tell anyone about it?"
            l "Probably so dumb kids don't ruin it."
            p "Makes sense."
            nar "Nobody talks after that. Everyone soaks in the glimmering afternoon light."
            nar "Paul dips his hands in the water."
            p "Its really warm."
            j "Don't worry Paul, We will go in tommorow."
            nar "You notice that the boys treat Paul like a younger brother."
            l "Time to Go."
            a "Aghh OK."
            nar "You and the boys get up and begin to walk home"
            jump walk_home_from_swim
            # TODO: NEXT SCENE — walk home / next day return

        "Go for a swim in your school clothes.":
            $ lucien += 1
            pl "I think we should just go for it. What's there to lose?"
            jump vichy_springs_swim_1

label vichy_springs_swim_1:
    ajp "Okay. Let's do this."
    # TODO: ADD BACKGROUND — boys at water's edge, about to jump in
    nar "One by one, everyone kicks off their shoes."
    nar "Lucien is the first one in — no hesitation."
    l "Come on!"
    nar "Arthur follows, slowly. The water reaches his waist before anyone else is even in."
    nar "Jaques cannonballs in, drenching everyone."
    ajp "Jaques!"
    j "Worth it."
    nar "You look over at Paul. He's still standing at the edge, looking at the water."
    menu:
        "Do you say anything to Paul?"

        "Wave him in.":
            $ paul += 1
            pl "Come on, Paul."
            nar "He looks at you for a second. Then steps in."
            p "It's warm."
            pl "Yeah."
            nar "He doesn't say anything else. But he stays close to you."
            jump vichy_springs_swim_2

        "Jump in yourself.":
            nar "You jump in. Paul watches from the edge a moment longer, then steps in quietly on his own."
            jump vichy_springs_swim_2

label vichy_springs_swim_2:
    # TODO: ADD BACKGROUND — in the water, golden afternoon light, steam rising
    nar "The water is perfect. Warm, clear, still."
    nar "For a while, nobody says anything. You all just float."
    l "I told you."
    a "Yeah. You told us."
    nar "Even Jaques doesn't have a comeback for that."
    nar "The sun starts to dip behind the trees."
    l "We should probably head back."
    nar "Nobody moves straight away."
    nar "Nobody wants to be the first to leave."
    nar "Eventually you all get out and walk back home."
    a "That was incredible"
    j "Yeah, thanks lucien"
    l "Your welcome. Can we go again tommorow?"
    ajp "Yes!"
    jump walk_home_from_swim

label walk_home_from_swim:
    nar "You and the boys walk home."
    nar "Eventually, everyone reaches a point where they have to split up."
    l "Come on [name], its time to go."
    pl "Bye everyone."
    ajp "Bye [name]! See you tommorow"
    nar "You and Lucien walk away."
    l "Well thats my freind group."
    pl "There a nice bunch of people. But I have a question-"
    menu:
        "Ask Lucien why everyone treats Paul like that"

        "Ask Him":
            $ lucien -= 1
            pl "Why does everyone ignore Paul."
            l "We don't ignore him! Thats just how we always treat him."
            l "And he is fine with it."
            pl "Oh. Okay."
            jump walk_home_after_lucien_question

        "Ignore it":
            pl "Nevermind."
            l "Oh. Ok."
            jump walk_home_after_lucien_question

label walk_home_after_lucien_question:
    nar "You arrive at Luciens home."
    nar "You go to knock on the door, but Lucien just unlocks it with his key."
    l "Home, Sweet Home."
    l "I dibs first shower!"
    pl "Buh"
    pl "Arent you supposed to give your exchange student the first priority?"
    l "Nah."
    nar "Lucien runs away, and leaves you dripping in your wet clothes"
    nar "You don't Luciens mum angry when you come home, so you run up to your room to find a towel."
    nar "You open up a cupboards, and its filled with towels. Lucky."
    nar "When you pull out a towel, a diary falls out. On the front it reads {i}Luciens Diary{i}"
    menu:
        "Will you read the diary?"

        "Read it":
            nar "You open the dairy to a random page."
            nar "It reads:"
            nar "{i}October 7{i}"
            nar "{i}Today was the first day of the school holidays. I spent the whole day reading.{i}"
            pl "Hmm"
            nar "{i}It was a really good day until I went to sleep{i}"
            nar "{i}I got woken up by a loud sound. I quickly realised that{i}"
            nar "{i}Dad came home late last night. Mum shouted at him. I think they are getting a divorce.{i}"
            pl "Woah. Lucien has a lot more going on."
            nar "You hear lucien coming up the stairs. You pack up the towels and slide his diary back where it was."
            nar "He walks in on you doing it"
            l "What are you doing in that cupboard?"
            pl "Just getting a towel."
            l "Oh"
            l "Ok"
            l "Your turn for the shower. Its down the stairs and to the left of the kitchen"
            pl "Ok"
            jump night_time
        "Respect his privacy":
            $ karma += 100
            nar "You grab a towel and put the diary where it belonged."
            nar "You hear lucien walking up the stairs."
            l "Hey [name]"
            pl "Hi"
            jump night_time
        
label night_time
    l "Your turn for the shower. Its down the stairs and to the left of the kitchen"
    pl "Ok"
    nar "You have a shower and get changed. You are coming out of the bathroom and see Lucien in the living room."
    pl "Wheres your mum and dad?"
    l "Mum works at the local cafe, she should be back in 15 minutes, and dad works late."
    pl "Whats his job?"
    l "I umm- don't really know"
    l "He is very vauge about it."
    pl "You should ask him tongight"
    l "Maybe not."
    pl "Oh."
    pl "Can we do something?"
    l "Like what?"
    pl "A board game or something like that."
    l "Sure."
    nar "You and Lucien walk upstairs and look under his bed."
    l "I have cluedu, munopolee, or junga."
    menu:
        "Which game do you choose?"

        "Cluedu":
            pl "I choose Cluedu"
            l "Great Choice, my favourite."
            nar "Lucien grabs the game and you head downstairs."
            nar "He sets up the game and puts it out onto the table."
            l "Oh shucks,"
            pl "What?"
            l "We need three people to play."
            pl "Dang it."
            l "We could ask my sister-"
            l "But she wouldn't want to play."
            pl "No, lets try."
            l "Ok, shes not going to say yes if I ask, but if you ask she will."
            l "Her room is next to mine. Good Luck"
            nar "Lucien follows you upstairs and hides behind corner. He makes a thumbs up towards you."
            nar "You knock on the door."
            nar "A teen girl opens the door."
            h "Hello?"
            pl "Hey, my name is [name], I'm the exchange student your hosting."
            h "oh. what do you want?"
            pl "I was wondering if you would like to play Cluedu with us since we don't have enough players?"
            h "Umm."
            h "Sure. This better be quick though."
            nar "You and Luciens sister walk downstairs"
            nar "Lucien is waiting downstairs."
            nar "You all sit down."
            l "Who wants to be dealer?"
            nar "Nobody answers"
            l "Sure, I will."
            nar "Lucien deals everyone some card and a sheet."
            nar "You play the game collecting evidence."
            l "I have the murderer! I know who did it."
            nar "Its not his turn yet, so you have a chance to guess the murderer before him."
            nar "You worry, you are pretty close, but can't quite pin the nail on the head."
            menu:
                "Do you take a chance and guess?"

                "Take a chance":
                    l "I guess Mr.Lonchan in the Basement, with the Cheese wheel."
                    nar "You open the answer pouch and look inside."
                    l "I got it correct!"
                    h "Oh no. I gotta go back to my room now."
                    l "Please don't go- One more round?"
                    nar "She is about to answer when you hear a knocking on the door."
                    nar "Harriet looks up at lucien"
                    h "Saved by mum"
                    nar "She runs up to her room."
                    nar "You and lucien go to the door to let her in."
                    mu "Hey boys! How was school."
                    l "Good."
                    mu "Good to hear!"
                    mu "I'm going to make dinner."
                    l "ok"
                    nar "You and Lucien walk back to the game and pack it up."
                    jump after_game

                "Let lucien win":
                    $ game = True
                    nar "You roll the dice, and pick a clue card up"
                    nar "It reads:"
                    nar "{i}Verrain opens up when you reveal your deepest secret{i}"
                    pl "Hmm Thats odd."
                    l "What is it?"
                    pl "The card just says something ive never seen before."
                    l "What does it say?"
                    pl "Verra-, Verrain opens up when you reveal..."
                    pl "Your deepest secret?"
                    l "Thats really weird."
                    l "Was it you, Harriet?"
                    h "Nope."
                    l "Hmm. Must just be apart of the game."
                    pl "That means that you have to answer it."
                    l "What! No."
                    pl "Come on, its the rules."
                    h "Yeah Lucien"
                    nar "Harriet says this in a mocking voice"
                    l "Fine."
                    l "I genuinely think I'm a bad friend sometimes. But I don't know why."
                    nar "Nobody Answers."
                    l "Forget I said anything."
                    h "Thats your secret. Thats it?"
                    l "What did you want to hear Harriet?"
                    nar "He laughs it off."
                    nar "A knock sounds at the door."
                    l "Can you get it Harriet. Please."
                    h "Fine."
                    nar "Lucien looks like he is about to cry as he packs up the game."
                    nar "He runs up to his room."
                    pl "Lucien Wait -"
                    nar "He ignores you."
                    mu "All ok [name]"
                    nar "Luciens mum notices you sitting alone."
                    pl "Yeah. Whats for dinner?"
                    mu "Onion Soup and Soufles."
                    pl "Delicous."



        "Munopolee":

        "Junga":


label after_game:
