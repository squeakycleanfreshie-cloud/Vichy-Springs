init python:
    achievement.register("found_vichy_springs", display_name="Spa Day", description="Discovered Vichy Springs")
    achievement.register("enter_le_repli", display_name="Welcome to Le Repli!", description="Stumble upon a hidden world")
    achievement.register("lost_paul", display_name="Paul? Where are you?!", description="Lose Paul.")
    achievement.register("pacifist", display_name="Pacifist", description="How did you not kill anyone?")
    achievement.register("lucien_friend", display_name="Friendship, Over!", description="Lose the friendship with Lucien.")
    achievement.register("bully", display_name="Bully", description="Become a bully")
    achievement.register("popular", display_name="Popular", description="Become best freinds with everyone")
    achievement.register("saint", display_name="Saint", description="Be a really good person")
    achievement.register("clumsy", display_name="Clumsy", description="Knock over the tower in Jenga")
    achievement.register("popular", display_name="Popular", description="Have all the freinds help you look for Lucien")
    achievement.register("antisocial", display_name="Antisocial", description="I never liked you anyway!")

    my_achievement_ids = [
        "found_vichy_springs",
        "enter_le_repli",
        "lost_paul",
        "pacifist",
        "lucien_friend",
        "bully",
        "popular",
        "saint",
        "clumsy",
        "popular",
        "antisocial",
    ]

    my_achievement_names = {
        "found_vichy_springs": "Spa Day",
        "enter_le_repli": "Welcome to Le Repli!",
        "lost_paul": "Paul? Where are you?!",
        "pacifist": "Pacifist",
        "lucien_friend": "Friendship, Over!",
        "bully": "Bully",
        "popular": "Popular",
        "saint": "Saint",
        "clumsy": "Clumsy",
        "popular": "Popular",
        "antisocial": "Antisocial",
    }

    my_achievement_descriptions = {
        "found_vichy_springs": "Discovered Vichy Springs",
        "enter_le_repli": "Stumble upon a hidden world",
        "lost_paul": "Lose Paul.",
        "pacifist": "How did you not kill anyone?",
        "lucien_friend": "Lose the friendship with Lucien.",
        "bully": "Become a bully",
        "popular": "Become best freinds with everyone",
        "saint": "Be a really good person",
        "clumsy": "Knock over the tower in Jenga",
        "popular": "Have all the freinds help you look for Lucien",
        "antisocial": "I never liked you anyway! (loose the freindship with lucien)",
    }

screen achievements_screen():
    tag menu

    frame:
        background "#f5e6c8"
        xfill True
        yfill True
        padding (40, 40)

        viewport:
            scrollbars "vertical"
            mousewheel True
            vbox:
                spacing 15
                text "Achievements" size 80 color "#3a2e28"

                for id in my_achievement_ids:
                    $ unlocked = achievement.has(id)
                    hbox:
                        spacing 20
                        text (my_achievement_names[id] if unlocked else "???") size 60 color ("#3a2e28" if unlocked else "#999999")
                        text (my_achievement_descriptions[id] if unlocked else "Locked") size 40 color ("#5a4a3a" if unlocked else "#aaaaaa")

        textbutton "Return":
            action Return()
            xalign 0.5
            yalign 1.0