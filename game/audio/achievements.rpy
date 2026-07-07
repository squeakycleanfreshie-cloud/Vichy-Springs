init python:
    achievement.register("found_vichy_springs", display_name="Found Vichy Springs", description="Discovered the hidden lake.")
    my_achievement_ids = ["found_vichy_springs"]

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
                text "Achievements" size 40 color "#3a2e28"

                $ unlocked = achievement.has("found_vichy_springs")
                hbox:
                    spacing 20
                    text ("Found Vichy Springs" if unlocked else "???") size 24 color ("#3a2e28" if unlocked else "#999999")
                    text ("Discovered the hidden lake." if unlocked else "Locked") size 20 color ("#5a4a3a" if unlocked else "#aaaaaa")

        textbutton "Return":
            action Return()
            xalign 0.5
            yalign 1.0