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
define d = Character("Day")


image bg home = "#F2D4A7"
image bg street = "#A8BFA8"
image bg school = "#C4B89A"
image bg forest = "#6B8F5E"
image bg springs = "#5FBFB0"

transform far_left:
    xalign 0.0
    yalign 1.0
    zoom 2.0

transform left_mid:
    xalign 0.25
    yalign 1.0
    zoom 2.0

transform center_mid:
    xalign 0.50
    yalign 1.0
    zoom 2.0

transform right_mid:
    xalign 0.75
    yalign 1.0
    zoom 2.0

transform far_right:
    xalign 0.9
    yalign 1.0
    zoom 2.0


transform normal_size:
    ease 0.15 zoom 2.0

transform talking_size:
    ease 0.15 zoom 2.16

init python:
    _last_speaker_tag = None

    def make_speaker_zoom(tag):
        def callback(event, **kwargs):
            global _last_speaker_tag

            if event != "show_done":
                return

            if _last_speaker_tag and _last_speaker_tag != tag and renpy.showing(_last_speaker_tag):
                renpy.show(_last_speaker_tag, at_list=[normal_size])

            if renpy.showing(tag):
                renpy.show(tag, at_list=[talking_size])

            _last_speaker_tag = tag

        return callback

define mu = Character("Josette", callback=make_speaker_zoom("josette"))
define l = Character("Lucien", callback=make_speaker_zoom("lucien"))
define a = Character("Arthur", callback=make_speaker_zoom("arthur"))
define j = Character("Jaques", callback=make_speaker_zoom("jaques"))
define p = Character("Paul", callback=make_speaker_zoom("paul"))
define v = Character("Verrain", callback=make_speaker_zoom("verrain"))
define b = Character("Budak", callback=make_speaker_zoom("budak"))
define t = Character("Mr Pernette", callback=make_speaker_zoom("mrpernette"))
define ta = Character("Ms Dubois", callback=make_speaker_zoom("msdubois"))
define h = Character("Harriet", callback=make_speaker_zoom("harriet"))

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
default comp = False
default fight = False

label start:
    play music "music.mp3"
    scene bg home
    nar "You wake up. Lips dry, confused about where you are."
    nar "You suddenly remember — you're in your new exchange family's house."
    nar "You get out of bed and get ready to walk downstairs."
    nar "You walk down the stairs, and catch a glimpse of your exchange family's mum."
    show josette at center_mid
    mu "How did you sleep, darling!"
    pl "Okay... I woke up a couple of times."
    mu "Lucien is still in his room, but he should be coming down soon."
    pl "Great."
    mu "Also, I'm making pancakes to celebrate your first day of school in France."
    nar "You don't like pancakes, but you don't show it."
    pl "Delicious."
    nar "You sit down at the table. It's awkward — you only met your family last night."
    nar "After what feels like 30 minutes of silence, Lucien finally walks down the stairs."
    show lucien at left_mid
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
    scene bg street
    show lucien at left_mid
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
    scene bg school
    hide lucien
    nar "Eventually, you arrive at school. You and Lucien have been split up because you're in separate classes, so you are all alone."
    nar "The teacher walks into the class."
    show mrpernette at center_mid
    t "Hello class, sorry I'm late."
    t "We have a new exchange student today. Their name is [name]. They will be in this History class until the end of the year."
    t "Please give them a warm welcome."
    nar "The class stays silent. It's really awkward."
    nar "The class continues, and the teacher talks about WWI tactics. Before you know it, the bell rings."
    nar "In the next class, you are with Lucien."
    hide mrpernette
    show lucien at left_mid

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
    hide lucien
    show msdubois at center_mid
    ta "Welcome everyone to English."
    nar "Ms Dubois writes something on the board."
    nar "{i}The Invisible Man{/i}"
    ta "Today we are discussing {i}The Invisible Man{/i} — a character who is, by the end of the novel, completely invisible to the other characters in the book."
    show lucien at left_mid
    l "That's kind of sad."
    ta "It is."
    ta "Today I'm giving you your books. Please read to chapter three before the bell goes."
    nar "She hands everybody a book."
    nar "You start reading."
    nar "Ring ring ring — the bell rings."
    nar "Everybody storms out the door, eager to get to lunch."
    hide msdubois
    hide lucien
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
            hide lucien
            show msdubois at center_mid
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
            hide msdubois
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
            hide lucien
            show msdubois at center_mid
            pl "I'm sorry."
            l "Why would you ditch me like that. What did I even do?"
            pl "I just wanted to meet new people, you know. I'm sorry."
            pl "Can we please forget about this?"
            l "Okay."
            l "And I'm fine with you sitting away from me next time."
            l "We don't have to sit next to each other 24/7 to still be friends."
            l "It was just... unexpected."
            hide msdubois
            jump morning_tea

label morning_tea:
    scene bg school
    show lucien at left_mid
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
    show arthur at far_left
    show jaques at far_right
    show paul at right_mid
    show lucien at left_mid
    l "Hey guys, this is [name]. They're the exchange student my family is hosting for a year."
    ajp "Hello!"
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
    hide arthur
    hide jaques
    hide paul
    hide lucien
    nar "The day and classes pass, and before you know it, it's the end of school."
    nar "You go meet Lucien and his friends outside the front of the school."
    show lucien at far_left
    show arthur at left_mid
    show paul at center_mid
    show jaques at right_mid
    nar "They're all waiting there."
    pl "What's up, guys."
    l "Hey, [name]!"
    l "Ready to leave?"
    pl "Yeah."
    scene bg street
    show lucien at far_left
    show arthur at left_mid
    show paul at center_mid
    show jaques at right_mid
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
    scene bg forest
    show lucien at far_left
    show arthur at left_mid
    show paul at center_mid
    show jaques at right_mid
    nar "You arrive at a bushy dead end."
    a "What's this, Lucien?"
    j "Yeah, where are we?"
    l "Okay, I didn't tell anyone, but we are going to have to work our way through the bush."
    ajp "Lucien!"
    l "It's fine, it's only like 200 metres."
    ajp "Okay."
    nar "Everyone looks a bit grumpy."
    l "Okay, let's go!"
    nar "You and the group trudge through the thick bush."
    nar "Lucien is at the front, holding back branches for everyone."
    nar "He accidentally lets go of one and it hits Paul in the face."
    p "Agh!"
    p "What was that for?"
    l "I'm sorry. Mistake."
    p "Okay."
    nar "You and the group continue walking."
    nar "Suddenly, you hear the group gasp."
    $ achievement.grant("found_vichy_springs")
    scene bg springs
    hide arthur
    hide jaques
    hide paul
    hide lucien
    nar "You look up and see the old, abandoned Vichy Springs."
    nar "The water is a beautiful shade of aqua, steaming with warmth."
    nar "There are hints of the history this place once had."
    nar "Stone figures are carved out, and rusted gold rails sit at the edges."
    nar "Everything looks so new and old at the same time."
    nar "Untouched by people for so long."
    show lucien at far_left
    show jaques at left_mid
    show paul at center_mid
    show arthur at far_right
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
            j "Don't worry Paul, we will go in tomorrow."
            nar "You notice that the boys treat Paul like a younger brother."
            l "Time to go."
            a "Aghh ok."
            nar "You and the boys get up and begin to walk home."
            hide arthur
            hide jaques
            hide paul
            hide lucien
            jump walk_home_from_swim

        "Go for a swim in your school clothes.":
            $ lucien += 1
            pl "I think we should just go for it. What's there to lose?"
            jump vichy_springs_swim_1

label vichy_springs_swim_1:
    ajp "Okay. Let's do this."
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
    scene bg springs
    hide arthur
    hide jaques
    hide paul
    hide lucien
    nar "The water is perfect. Warm, clear, still."
    nar "For a while, nobody says anything. You all just float."
    show lucien at far_left
    show paul at left_mid
    show jaques at right_mid
    show arthur at far_right
    l "I told you."
    a "Yeah. You told us."
    nar "Even Jaques doesn't have a comeback for that."
    nar "The sun starts to dip behind the trees."
    l "We should probably head back."
    nar "Nobody moves straight away."
    nar "Nobody wants to be the first to leave."
    nar "Eventually you all get out and walk back home."
    a "That was incredible."
    j "Yeah, thanks Lucien."
    l "You're welcome. Can we go again tomorrow?"
    ajp "Yes!"
    hide arthur
    hide jaques
    hide paul
    hide lucien
    jump walk_home_from_swim

label walk_home_from_swim:
    scene bg street
    show lucien at left_mid
    show arthur at far_left
    show paul at center_mid
    show jaques at right_mid
    nar "You and the boys walk home."
    nar "Eventually, everyone reaches a point where they have to split up."
    l "Come on [name], its time to go."
    pl "Bye everyone."
    ajp "Bye [name]! See you tomorrow."
    hide arthur
    hide jaques
    hide paul
    nar "You and Lucien walk away."
    l "Well that's my friend group."
    pl "They're a nice bunch of people. But I have a question—"
    menu:
        "Ask Lucien why everyone treats Paul like that"

        "Ask him.":
            $ lucien -= 1
            pl "Why does everyone ignore Paul?"
            l "We don't ignore him! That's just how we always treat him."
            l "And he is fine with it."
            pl "Oh. Okay."
            jump walk_home_after_lucien_question

        "Ignore it.":
            pl "Nevermind."
            l "Oh. Ok."
            jump walk_home_after_lucien_question

label walk_home_after_lucien_question:
    scene bg home
    show lucien at center_mid
    nar "You arrive at Lucien's home."
    nar "You go to knock on the door, but Lucien just unlocks it with his key."
    l "Home, Sweet Home."
    l "I dibs first shower!"
    pl "But aren't you supposed to give your exchange student first priority?"
    l "Nah."
    hide lucien
    nar "Lucien runs away, and leaves you dripping in your wet clothes."
    nar "You don't want to make Lucien's mum angry, so you run up to your room to find a towel."
    nar "You open a cupboard, and it's filled with towels. Lucky."
    nar "When you pull out a towel, a diary falls out. On the front it reads {i}Lucien's Diary{/i}."
    menu:
        "Will you read the diary?"

        "Read it.":
            nar "You open the diary to a random page."
            nar "It reads:"
            nar "{i}October 7{/i}"
            nar "{i}Today was the first day of the school holidays. I spent the whole day reading.{/i}"
            pl "Hmm."
            nar "{i}It was a really good day until I went to sleep.{/i}"
            nar "{i}I got woken up by a loud sound. I quickly realised that{/i}"
            nar "{i}Dad came home late last night. Mum shouted at him. I think they are getting a divorce.{/i}"
            pl "Woah. Lucien has a lot more going on."
            show lucien at center_mid
            nar "You hear Lucien coming up the stairs. You pack up the towels and slide his diary back where it was."
            nar "He walks in on you doing it."
            l "What are you doing in that cupboard?"
            pl "Just getting a towel."
            l "Oh."
            l "Ok."
            jump night_time

        "Respect his privacy.":
            $ karma += 100
            nar "You grab a towel and put the diary where it belonged."
            show lucien at center_mid
            nar "You hear Lucien walking up the stairs."
            l "Hey [name]."
            pl "Hi."
            jump night_time

label night_time:
    scene bg home
    show lucien at center_mid
    l "Your turn for the shower. It's down the stairs and to the left of the kitchen."
    pl "Ok."
    hide lucien
    nar "You have a shower and get changed. You come out of the bathroom and see Lucien in the living room."
    show lucien at center_mid
    pl "Where's your mum and dad?"
    l "Mum works at the local cafe, she should be back in 15 minutes, and dad works late."
    pl "What's his job?"
    l "I umm— don't really know."
    l "He is very vague about it."
    pl "You should ask him tonight."
    l "Maybe not."
    pl "Oh."
    pl "Can we do something?"
    l "Like what?"
    pl "A board game or something like that."
    l "Sure."
    hide lucien
    nar "You and Lucien walk upstairs and look under his bed."
    show lucien at center_mid
    l "I have Cluedo, Monopoly, or Jenga."
    menu:
        "Which game do you choose?"

        "Cluedo":
            pl "I choose Cluedo."
            l "Great choice, my favourite."
            hide lucien
            nar "Lucien grabs the game and you head downstairs."
            nar "He sets up the game and puts it out onto the table."
            show lucien at center_mid
            l "Oh shucks."
            pl "What?"
            l "We need three people to play."
            pl "Dang it."
            l "We could ask my sister—"
            l "But she wouldn't want to play."
            pl "No, let's try."
            l "Ok, she's not going to say yes if I ask, but if you ask she will."
            l "Her room is next to mine. Good luck."
            hide lucien
            nar "Lucien follows you upstairs and hides behind a corner. He makes a thumbs up towards you."
            nar "You knock on the door."
            show harriet at center_mid
            nar "A teen girl opens the door."
            h "Hello?"
            pl "Hey, my name is [name], I'm the exchange student you're hosting."
            h "Oh. What do you want?"
            pl "I was wondering if you would like to play Cluedo with us since we don't have enough players?"
            h "Umm."
            h "Sure. This better be quick though."
            hide harriet
            nar "You and Lucien's sister walk downstairs."
            show lucien at left_mid
            show harriet at right_mid
            nar "Lucien is waiting downstairs."
            nar "You all sit down."
            l "Who wants to be dealer?"
            nar "Nobody answers."
            l "Sure, I will."
            nar "Lucien deals everyone some cards and a sheet."
            nar "You play the game collecting evidence."
            l "I have the murderer! I know who did it."
            nar "It's not his turn yet, so you have a chance to guess the murderer before him."
            nar "You worry — you are pretty close, but can't quite pin the nail on the head."
            menu:
                "Do you take a chance and guess?"

                "Take a chance.":
                    l "I guess Mr. Lonchan in the Basement, with the Cheese wheel."
                    nar "You open the answer pouch and look inside."
                    l "I got it correct!"
                    h "Oh no. I gotta go back to my room now."
                    l "Please don't go — one more round?"
                    nar "She is about to answer when you hear a knocking at the door."
                    nar "Harriet looks up at Lucien."
                    h "Saved by mum."
                    hide harriet
                    nar "She runs up to her room."
                    nar "You and Lucien go to the door to let her in."
                    hide lucien
                    show josette at center_mid
                    mu "Hey boys! How was school?"
                    show lucien at left_mid
                    l "Good."
                    mu "Good to hear!"
                    mu "I'm going to make dinner."
                    l "Ok."
                    hide josette
                    nar "You and Lucien walk back to the game and pack it up."
                    pl "That was fun."
                    l "Yeah."
                    l "Want to watch TV?"
                    pl "Sure. Whatever you want."
                    nar "You and Lucien sit down on the couch and he turns on the TV."
                    nar "He puts on a nature documentary and you wait until dinner time."
                    jump after_game

                "Let Lucien win.":
                    $ game = True
                    $ lucien -= 1
                    nar "You roll the dice, and pick a clue card up."
                    nar "It reads:"
                    nar "{i}Verrain opens up when you reveal your deepest secret{/i}"
                    pl "Hmm. That's odd."
                    l "What is it?"
                    pl "The card just says something I've never seen before."
                    l "What does it say?"
                    pl "Verra-, Verrain opens up when you reveal..."
                    pl "Your deepest secret?"
                    l "That's really weird."
                    l "Was it you, Harriet?"
                    h "Nope."
                    l "Hmm. Must just be part of the game."
                    pl "That means you have to answer it."
                    l "What? No."
                    pl "Come on, it's the rules."
                    h "Yeah, Lucien."
                    nar "Harriet says this in a mocking voice."
                    l "Fine."
                    l "I genuinely think I'm a bad friend sometimes. But I don't know why."
                    nar "Nobody answers."
                    l "Forget I said anything."
                    h "That's your secret? That's it?"
                    l "What did you want to hear, Harriet?"
                    nar "He laughs it off. But he doesn't look at you when he says it."
                    nar "A knock sounds at the door."
                    l "Can you get it, Harriet. Please."
                    h "Fine."
                    hide harriet
                    nar "Lucien looks like he is about to cry as he packs up the game."
                    hide lucien
                    nar "He runs up to his room."
                    pl "Lucien, wait—"
                    nar "He ignores you."
                    show josette at center_mid
                    mu "All ok, [name]?"
                    nar "Lucien's mum notices you sitting alone."
                    pl "Yeah. What's for dinner?"
                    mu "Onion soup and soufflés."
                    pl "Delicious."
                    hide josette
                    nar "You go and lie down on the couch and wait for dinner time."
                    jump after_game

        "Monopoly":
            show lucien at center_mid
            l "This is going to take forever."
            pl "What, you don't like Monopoly?"
            l "It's not that I don't like it, it just takes too long."
            pl "Oh okay. Well it's my favourite so we are playing it."
            hide lucien
            nar "You and Lucien walk downstairs and set up the game."
            show lucien at center_mid
            l "I bags the dog."
            pl "Oh. Good choice."
            pl "Do you have any pets?"
            l "I used to have a dog. Gaston."
            pl "Awwww."
            l "He died a few years ago."
            l "Anyways, let's play."
            nar "You begin to play. But what is your strategy?"
            menu:
                "What's your strategy?"

                "Buy all the houses.":
                    nar "You lock in and spend all your money on different collections."
                    nar "Lucien grabs the dice and rolls them."
                    nar "He moves his player onto one of your properties."
                    pl "Better pay up."
                    l "This is the real reason I hate Monopoly. I always lose!"
                    $ lucien += 1
                    nar "You and Lucien laugh while you play."
                    nar "In the end, you have most of the properties and sets."
                    l "I guess you win."
                    pl "Yeah."
                    nar "You hear a knock on the door."
                    l "Mum's home."
                    hide lucien
                    show josette at center_mid
                    mu "Hey boys! How was school?"
                    show lucien at left_mid
                    l "Good."
                    mu "Good to hear!"
                    mu "I'm going to make dinner."
                    l "Ok."
                    hide josette
                    nar "You and Lucien walk back to the game and pack it up."
                    pl "That was fun."
                    l "Yeah."
                    l "Want to watch TV?"
                    pl "Sure. Whatever you want."
                    nar "You and Lucien sit down on the couch and he turns on the TV."
                    nar "He puts on a nature documentary and you wait until dinner time."
                    jump after_game

                "Save your money.":
                    l "Haha! Why are you not buying any properties?"
                    pl "I read a book that it was the best strategy."
                    l "Well it obviously isn't! I'm beating you."
                    nar "Lucien looks happy and smiling."
                    nar "You and Lucien play for hours until the game finishes."
                    l "I won!"
                    pl "Says the guy who didn't like Monopoly."
                    l "I guess times change. Besides, I haven't played it in a while."
                    nar "You hear a knock on the door."
                    l "Mum's home."
                    hide lucien
                    show josette at center_mid
                    mu "Hey boys! How was school?"
                    show lucien at left_mid
                    l "Good."
                    mu "Good to hear!"
                    mu "I'm going to make dinner."
                    l "Ok."
                    hide josette
                    nar "You and Lucien walk back to the game and pack it up."
                    pl "That was fun."
                    l "Yeah."
                    l "Want to watch TV?"
                    pl "Sure. Whatever you want."
                    nar "You and Lucien sit down on the couch and he turns on the TV."
                    nar "He puts on a nature documentary and you wait until dinner time."
                    jump after_game

        "Jenga":
            pl "Jenga."
            l "Nice and quick."
            pl "Yeah. I used to play this with my—"
            nar "A sad memory flies into your head."
            pl "Nevermind."
            nar "Lucien looks confused but brushes it off."
            hide lucien
            nar "You and Lucien walk downstairs and set up the game."
            show lucien at center_mid
            l "Do you want to go first?"
            pl "Sure."
            nar "You pull out a brick near the bottom and place it on the top."
            l "Lucky."
            nar "You and him continue to take bricks off until the tower looks like old ruins."
            l "How is it still standing up!?"
            nar "Lucien is laughing and having a really good time."
            pl "I don't know, but it's your turn."
            l "Damn it."
            l "I was trying to distract you."
            pl "I know."
            nar "Lucien grabs a brick, and almost in slow motion, you can see the whole tower shake."
            nar "He pulls just a bit too hard, and the whole tower collapses."
            l "Nooooo!"
            pl "Haha."
            l "Why!"
            l "That one was obviously going to fall!"
            pl "You could have never known."
            nar "Lucien begins to pack up the bricks into the box."
            pl "Don't want to play again?"
            l "No, I just thought you'd had enough."
            pl "Oh, yeah ok."
            nar "This is an awkward situation, but before anyone can say anything, you hear a knock on the door."
            l "Mum's finally home."
            hide lucien
            show josette at center_mid
            nar "Both of you run to the door."
            l "Hey mum!"
            mu "Hey darling, how was your day?"
            show lucien at left_mid
            l "It was good."
            mu "What about you, [name]?"
            pl "Great! I love Vichy so much."
            nar "You quickly realise that this is the first time you have felt truly happy in a long time."
            mu "Good to hear. Why is there water on the floor?"
            nar "Lucien goes to speak but you quickly interrupt him."
            pl "I had a shower, and coming out I got some water on the floor, sorry."
            mu "Oh, it's fine honey."
            hide josette
            nar "Josette walks away."
            l "So, wanna keep playing?"
            pl "Sure."
            nar "You and Lucien walk back to the game and continue playing, until it is time for dinner."
            nar "You win most of the games, but this round, the tower is looking really depleted."
            l "Your turn."
            pl "Noooo!"
            nar "You take a brick. The tower falls down instantly as soon as you release the pressure."
            $ achievement.grant("clumsy")
            jump after_game

label after_game:
    scene bg home
    show lucien at left_mid
    show josette at center_mid
    show harriet at right_mid
    mu "Dinner time!"
    nar "You and Lucien run to the dinner table, hungry from the big day you have just had."
    nar "Josette puts a dish of steaming soup on the table, and a plate of little ramekins filled with soufflé."
    nar "Lucien whispers in your ear."
    l "Mum works at the cafe so she's an amazing chef."
    nar "Josette serves everybody with a serving of each dish."
    mu "Be careful, it's hot."
    nar "When she's done serving, everybody starts eating."
    nar "You finish your food."
    pl "That was the best food I've ever had in my life, Josette!"
    mu "Made with love!"
    nar "You and Lucien laugh"
    mu "So [name], how was your family back at home?"
    pl "They are ok. But i'm happy to be with you guys."
    mu "Awww."
    mu "Why just ok?"
    l "I..I don't know."
    mu "Oh. Okay."
    mu "Are you guys ready to go to bed?"
    l "Yes"
    pl "Yeah."
    hide josette
    hide lucien
    scene bg home
    nar "You get ready to go to bed, clean your teeth. You are really tired."
    nar "You check your watch 10:00PM. Wow, time flies really fast in Vichy."
    nar "You sit in your room and look out the window, reflecting on the day you have had."
    nar "You enjoyed vichy springs, but something about the energy it gave off seemed familiar."
    nar "You watch the street, no cars or people passing by, toatally empty."
    nar "So different to you own home, which was full of bustling people."
    pl "I think I prefer it here."
    nar "BANG"
    nar "You turn back looking at the window, trying to spot what happened."
    nar "Suddenly, you spot a glimpse of someone walking down the street in a satin gown. Their presence is eerie."
    nar "They are just walking in the middle of the road, face hidden by the gown."
    nar "All of a sudden they look up at you in the eyes."
    pl "Wha.."
    nar "You dodge down below the window out of fear"
    nar "After a minuite, you look back up to see if they are still there"
    nar "they are gone, like they where never there."
    pl "I must need to go to sleep."
    nar "Even though your heart is pumping from fear,"
    nar "You jump into your bed, and drift to sleep."
    d "{i}Day 2{i}"
    nar "Knock..Knock...Knock"
    if run == True and lucien >= 1:
        show lucien at center_mid
        l "Wake up [name]! We are going on a run!"
        pl "Ughhh Ok."
        nar "You quickly get changed into some clothes"
        pl "Why didn't you tell me?"
        l "I forgot, anyway you will thank me later."
        pl "You are too tired to respond"
        nar "You and lucien walk downstairs"
        nar "He quickly begins running."
        pl "No warm up?"
        l "Your a real fun sponge."
        pl "Nevermind."
        nar "You and him begin to run"
        nar "You notice that after running for a while in the streets of vichy, your paces and steps syncronise"
        pl "Where are we going?"
        l "For a run"
        nar "He says this in a mocking tone"
        pl "Obviously. Where are you taking me?"
        l "Not to sound like a therapist or anything, but the journey matters more than the result."
        pl "Wise.."
        nar "You notice how good lucien is at running. You are going at quite a fast, and his breath barley breathes."
        menu:
            "Do you compliment Lucien?"

            "Compliment Him":
                $ lucien += 1
                $ comp = True
                pl "Your really good at running."
                l "Thanks."
                pl "Do you do any competitions, like cross country?"
                l "Whats cross country?"
                pl "Like a running competition."
                l "Oh no. Nobody nearby runs anything like that, besides i'm not even good enough."
                pl "Yes you are! Your bearley-"
                nar "You struggle a bit to talk and run"
                pl "-struggling, and we are going at quite a good pace"
                pl "You need to find a competition, and win!"
                l "Maybe that could be my goal."
                pl "Yeah. Maybe I could do it too...and come last"
                nar "Lucien bursts out laughing"
                pl "Hey!"
                l "Sorry, Sorry you wouldn't come last"
                pl "Good."
                jump after_run_q

            "Keep running quietly":
                jump after_run_q

    else:
        hide lucien
        jump after_night_1

label after_run_q:
    scene bg street
    show lucien at center_mid
    nar "You and lucien continue running, through the streets of vichy"
    nar "Eventually, they open to a beautiful coastline, showered by pink sunrise"
    pl "Vichy is on the Coast!?"
    l "Yeah, you didn't know?"
    pl "I came by car, and we never drove past it."
    l "How did you not know though?"
    pl "I just told you."
    nar "You continue running, and you eventually loop back home"
    jump after_run

label after_night_1:
    scene bg home
    show lucien at center_mid
    nar "Someone opens the door and slams into your room"
    l "[name], Get Up, You are late for school!"
    if run == True:
        pl "I must have fallen back asleep."
        nar "You quickly get changed into your school clothes, and take a peice of toast with fresh jam on it out the door."
        nar "You and lucien quickly run to school."
        l "Another run, hey!"
        nar "You and lucien laugh"
        jump d1
    else:
        nar "You quickly get changed into your school clothes, and take a peice of toast with fresh jam on it out the door."
        nar "You and lucien quickly run to school."
        jump d1

label d1:
    scene bg street
    show lucien at left_mid
    nar "You keep on running, until you spot Paul walking to school"
    show paul at center_mid
    pl "Lets walk with him."
    l "No. Otherwise we will be late."
    pl "We could at least ask him to run with us"
    l "Don't tell him I told you this, but he isn't the fittest."
    menu:
        "Do you laugh along with him?"

        "Laugh along with the joke":
            $ karma -= 100
            pl "Haha. Then lets at least say hello"
            l "Fine"
            nar "You and lucien run past Paul, and wave at him as you pass."
            pl "Hey paul! Want to run with us?"
            p "Sure!"
            nar "His face lights up."
            nar "Lucien looks at you sternly and whispers to you"
            l "Why did you actually invite him?"
            menu:
                "Do you finally tell him to stop being mean?"

                "Tell him to stop being a bully":
                    $ karma += 100
                    $ paul += 1
                    pl "Stop."
                    pl "I'm over it. Your so mean to Paul, and he didn't even do anything. And I don't know if you mean it, but it happens constantly!"
                    nar "Paul heard that."
                    nar "He looks at you. He is embarresed, but slightly shocked."
                    nar "You look back up at Lucien. He is silent. He could be angry."
                    l "Stop What?"
                    pl "Being a bully."
                    l "I'm not. But ok."
                    pl "Good."
                    nar "You, paul and Lucien go on a run"
                    nar "You all arrive at the same time."
                    jump after_run_to_school

                "Watch silently as paul keeps taking hits":
                    $ paul -= 1
                    l "You can come paul, but I don't think you would be able to keep up."
                    p "I'll come."
                    nar "Lucien sighs, annoyed."
                    nar "You, Paul and lucien start to run again."
                    l "Oh my god, we are so late for school it started 20 minutes ago."
                    l "We are going to have to run faster."
                    nar "So you do run faster. You pick up the pace."
                    pl "Wha-"
                    nar "Paul is running really fast. Like really fast. He is a way better runner than lucien."
                    pl "What were you talking about Lucien? Paul is a great runner?"
                    l "My bad"
                    nar "You, paul and Lucien run to school and arrive just on time."
                    jump after_run_to_school

        
        
        "Tell him it is mean":
            $ karma += 100
            $ paul += 1
            $ lucien -= 1
            nar "You and lucien run past Paul, and wave at him as you pass."
            pl "Hey paul! Want to run with us?"
            p "Sure!"
            nar "His face lights up."
            nar "Lucien looks at you sternly and whispers to you"
            l "Why did you actually invite him?"
            pl "What he gonna make a differnce?"
            l "I don't know...Hes just..Annoying."
            pl "How can he be annoying, if hes shy?"
            pl "I think YOU are being annoying. Nobody cares what paul thinks."
            pl "I want YOU to say sorry to paul, for all this trouble you have put him through, and I don't even know how long it has been going on for."
            l "Your not my dad."
            menu:
                "Do you say a really mean roast?"

                "Say it.":
                    $ lucien -= 2
                    $ fight = False
                    pl "Well maybe you need a new one because I havn't even seen him once."
                    nar "Luciens eyes water up."
                    nar "He looks behind him."
                    l "How dare you!"
                    pl "I'm sorry, I didn't mean it!"
                    l "No! I'm leaving."
                    nar "Lucien runs away from you and Paul"
                    nar "You regret your choice."
                    nar "You feel really bad."
                    pl "Are you okay paul?"
                    p "Yeah, i'm fine. Thank you for saying something. Nobody has ever really noticed."
                    p "But I don't think he means it."
                    pl "How?"
                    p "I kind of got the hint a lot of things are going on at home for him."
                    pl "Oh. Yeah"
                    pl "Do you think he will forgive me?"
                    p "Yeah. The thing about Lucien is he dosne't care if you do something wrong. He will just move on and forget. Give or take till the end of the day."
                    nar "You have never seen Paul be this open and talk this much."
                    pl "Well lets head off. Can we walk. I'm tired."
                    p "Yeah"
                    p "I don't mind being late."
                    nar "You and Paul walk to school, and arrive late"
                    jump after_run_to_school

                "Agree with him.":
                    p "I'm sorry. I'm just really tired."
                    nar "Lucien sighs, annoyed."
                    nar "You, Paul and lucien start to run again."
                    l "Oh my god, we are so late for school it started 20 minutes ago."
                    l "We are going to have to run faster."
                    nar "So you do run faster. You pick up the pace."
                    pl "Wha-"
                    nar "Paul is running really fast. Like really fast. He is a way better runner than lucien."
                    pl "What were you talking about Lucien? Paul is a great runner?"
                    l "My bad"
                    nar "You, paul and Lucien run to school and arrive just on time."
                    jump after_run_to_school

label after_run:
    scene bg home
    show lucien at center_mid
    nar "You open the door"
    l "Shhh!"
    pl "What?"
    l "Shhh! Be quite"
    pl "Why?"
    l "I maybe...didn't tell mum about our..run. So maybe we just, don't tell her. Besides, my whole family are late risers."
    pl "Okay. Why didn't you just tell her?"
    l "Because then she would have said no."
    nar "You and lucien sneak into your rooms"
    nar "Tired because of how early it is, you hop back into bed to rest your eyes....but slowly you drift to sleep."
    hide lucien
    jump after_night_1

label after_run_to_school:
    nar "You arrive at school and continue the day as usual."
    nar "Geography and Math pass quickly, and the bell rings for recess."
    nar "You meet the group sitting at their usual spot."
    if lucien <= -5:
        nar "You notice lucien isn't sitting here"
        pl "Wheres lucien?"
        j "I don't know. Havn't seen him all morning."
        menu:
            "Do you go look for Lucien and apologise?"

            "Look for him":
                $ lucien += 1
                pl "I'm gonna go look for him. Anyone wanna come?"
                if paul >= 2 and jaques >= 2 and arthur >= 2:
                    p "I'll come!"
                    j "I come along too"
                    a "Sure."
                    $ achievement.grant("popular")
                elif paul >= 2 and jaques >= 2:
                    p "I'll come!"
                    j "I come along too"
                elif paul >= 2 and arthur >= 2:
                    p "I'll come!"
                    a "Sure."
                elif jaques >= 2 and arthur >= 2:
                    j "Sure"
                    a "Don't forget me."
                elif paul >= 2:
                    p "I'll come!"
                elif jaques >= 2:
                    j "I'll come!"
                elif arthur >= 2:
                    a "I can come with you."
                else:
                    nar "nobody responds"
                    pl "I guess its just me"

            "Let him be by himself":
                pl "Oh okay. Are we still going to the springs after school."
                j "We all brought a swimmers."
                p "Yeah."
                pl "Even without lucien"
                a "Lucien can come if he wants to. And he will want to come."
                pl "Ok."
                nar "The bell rings for class"
                pl "Wow, that went fast."
                a "On wednesdays, school is shorter, so class is shorter."
                pl "Why?"
                a "To help the-"
                j "To help the teachers plan for their lessons"
                a "Hey!"
                a "I was going to say that."
                j "I know. I just did it to annoy you."
                nar "The group laughs"
                pl "Paul, are you a good swimmer?"
                p "No. I can't go any fast. I like running though."
                if run == True:
                    pl "Cool! Me and lucien when on a run this morning."
                    pl "You should come sometime."
                    p "Really! That sounds great."
                else:
                    pl "Thats cool! I think Lucien is also a runner."
                    nar "Paul sighs."

    else:
        pl "Hey guys!"
        j "Hey [name]!"
        if fight == True:
            nar "Lucien looks up at you. He looks sad."
            menu:
                "Do you apologise?"

                "Apologise":
                    pl "Lucien, I'm really sorry about this morning."
                    l "Thankyou for apologising." 
                    l "I'm sorry for being such a bad freind to paul. I will say sorry to him."
                    l "And I know that i'm mean sometimes.."
                    l "But honestly I don't mean it." 
                    nar "Your happy that all the drama has been resolved."
                    pl "So lets head to class."
                    l "Yeah"
                    l "Oh! I almost forgot. Did you pack your swimmers?"
                    pl "No! I forgot."
                    l "Don't worry, I did it for you."
                    pl "Thanks."
                    nar "The bell rings for class."
                    pl "See everyone after school!"
                    jump going_to_vichy_springs_2
                    

                "Be stubborn":
                    $ achievement.grant("antisocial") 
                    nar "You and the group eat lunch in silence."
                    nar "Arthur remembers something and talks"
                    a "Guys, I just remembered I got tickets to the rugby match!"
                    j "Cool! Whos playing?"
                    a "France v Australia"
                    j "Where even is Australia?"
                    a "How do you not know that?!"
                    j "I don't pay attention in Geography.."
                    a "But geography is like the best subject."
                    j "Nooo Its so boring, espacially with Mr Casidy"
                    a "I have never had him. Is he bad?"
                    j "He SO bad! He forgets stuff all the time, always shows up 20 minutes late to class."
                    nar "The group laugh."
                    nar "The bell rings."
                    a "Time to go. See you after school outside again."
                    pl "So we are still going to the springs?"
                    j "Yeah."
                    a "Lucien your rather quite today. Are you okay?"
                    l "Yes. I'm FINE."
                    j "Calm down cranky."
                    l "Go to class."
                    nar "Athur, jaques and Paul walk away, shocked at Luciens antisocial behavior."
                    l "So your not going to say sorry?"
                    nar "You finally realise that if you don't apologise, Lucien is going to continue to be angry."
                    pl "Lucien, I'm really sorry about this morning."
                    l "Thankyou. I'm sorry for being such a bad freind to paul. I will say sorry to him." 
                    nar "Your happy that all the drama has been resolved."
                    pl "So lets head to class."
                    l "Yeah"
                    l "Oh! I almost forgot. Did you pack your swimmers?"
                    pl "No! I forgot."
                    l "Don't worry, I did it for you."
                    pl "Thanks."
                    jump going_to_vichy_springs_2

        else:
            pl "Ready for the springs this afternoon?"
            nar "Everyone replies, exited for the second outing to the springs"
            l "Does everbody have their swimmers?"
            nar "You didn't pack them."
            ajp "Yeah."
            pl "Noo!"
            l "Don't worry, I did it for you"
            l "Great. Meet same place as usual after class."
            ajp "Good."
            jump going_to_vichy_springs_2
                
label going_to_vichy_springs_2:


    return