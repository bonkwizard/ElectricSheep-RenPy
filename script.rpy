# The script of the game goes in this file.

# Declare characters used by this game.
define a = Character(_("AI"), color="#ffffff")
define t = Character(_("Townsfolk"), color="#646464")
define e = Character(_("Elder"), color="#522f1c")
define s = Character(_("Shopkeep"), color="#307388")


# Tracker Variables
default suspicionTracker = 0
default dmgTracker = 0
default warTracker = 0
default breakerTracker = 0
default heroTracker = 0
default enemyName = "hostile"

# Variable for removing options
default removed_options = []

# Item Flags
default hasID = False
default hasFuse = False
default hasSpear = False

# Scene Flags
default robotDestroyed = False
default pinkcomKnown = False
default seenSpear = False
default proneCheck = False
default defendCheck = False

# Combat Variables
default player_max_hp = 100
default player_hp = player_max_hp
default enemy_max_hp = 0
default enemy_hp = enemy_max_hp

# Dice Roller
label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d8 = renpy.random.randint(1, 8)
    $ d10 = renpy.random.randint(1, 10)
    $ d12 = renpy.random.randint(1, 12)
    $ d20 = renpy.random.randint(1, 20)
    return

# A Shake animation used only once lol
transform shake(rate=0.090):
    linear rate xoffset 2 yoffset -6
    linear rate xoffset -2.8 yoffset -2
    linear rate xoffset 2.8 yoffset -2
    linear rate xoffset -2 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat

# The game starts here.

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# LOBBY
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label start:

    play music "music_intro.mp3" volume 0.25
    scene bg desert with fade

    "Mason Co Robotic Facility, a factory long thought to be abandoned, towers over you."

    "Easily the size of a city, yet still below average. Intimidating nonetheless."

    "No one would come here without reason."

    show fixer normal with fade
    "And that includes you, a supposed Fixer."

    "One tasked with maintaining and repairing factories created back when man still roamed the earth."

    "There is no demand for this place to be repaired, nor do you have any ties to it, 
    your only goal is to sate your curiosity. A rare emotion for your kind."

    "Equipped with only a Flathead Sword, you travel closer."
    
    hide player
    scene bg factory entrance with fade

    "You find yourself standing before the rusted and destroyed west entry gate, 
    no longer fulfilling its purpose of protecting the facility."

    scene bg lobby with fade

    "Walking inside reveals what could be assumed to be a lobby similar to that of a hotel. 
    The only life found here are the plants sprouting all around."

    "A stone fountain is located in the center of the lobby. 
    No water currently flows through it, leaving an algae filled pool."

    "There are a few doors on the left and right side of the room, 
    but the door that catches your attention is at the other end of the lobby, 
    right next to the front desk. It's a metal door locked behind an ID reader."

    jump lobby_choice

label lobby_choice:

    menu:
        # removes options that have been chosen before. only used for some parts
        set removed_options
        "What to do..."
        "[[Interact] Head through the door leading deeper into the facility":
            jump path_lobby_door

        "[[Interact] Search the front desk":
            jump path_lobby_desk

        "[[Interact] Investigate the fountain":
            jump path_lobby_fountain

        "[[Item] Use the ID Card on the door scanner" if hasID == True: # only appears if flag is true 
            jump path_lobby_id

label path_lobby_door:
    
    "You walk up to the door hoping it's unlocked... it's not. You try to pry it open with your sword."

    "It's sturdier than anticipated. Seems the only way through is to find an ID for the scanner."

    "Hopefully it still functions."

    jump lobby_choice

label path_lobby_desk:
    
    play sound "desk_search.wav"
    "It's been picked clean..."

    jump lobby_choice

label path_lobby_fountain:
    
    "You walk up to the stone fountain. 
    It's fine stonework seems to be what's keeping it from crumbling after all these years."

    "You notice something in the water."

    play sound "id_get.wav"

    show id:
        xalign 0.5
        yalign 0.5

    "[[{b}You've collected an ID Card{/b}]"

    $ hasID = True
    hide id

    jump lobby_choice

label path_lobby_id:
    jump the_ai

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# The AI
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label the_ai:
    
    "You swipe the ID Card through the scanner hoping it still works and to your surprise, it does."

    play sound "id_read2.wav"

    "A small jingle plays indicating that the ID Card has been verified. 
    The metal door opens automatically."

    play sound "door2.mp3" volume 0.5

    scene black with fade

    "You step past it into a pitch black room. You're incapable of making anything out."

    "You instinctively reach for the switch on the side of your head to turn on your lights. 
    Yet before your hand makes it..."

    # creates new transistion
    define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
 
    scene bg ai room with circleirisout

    "The lights on the ceiling turn on."

    "You were almost blinded by the sudden contrast of light."

    "The room is small. Housing nothing more than some cushioned chairs."

    show camera:
        xalign 0.5
        yalign 0.5

    "You notice a camera on the wall. You saw some in the lobby, but they didn't interest you as they were all broken."

    "This one though, is on."
    hide camera

    show ai normal at left
    show fixer normal at right: 
        xzoom -1.0
    a "Welcome to Mason Co Robotic Facility!"

    "A voice rang out from a speaker on a nearby wall."

    a "It's been forever since an outside bot visited my facility."

    a "Hold on..."

    show sword:
        xalign 0.5
        yalign 0.5

    a "That sword on your back!"

    hide sword

    a "Not only are you the first visitor in ages, you're a Fixer, too!?"
    
    show ai happy
    a "And here I thought they abandoned me."

    "Looks like the AI running the place is still operational."

    menu:
        "How to respond..."

        "[[Gesture] Give a thumbs up":
            jump path_ai_thumb

        "[[Interact] Head towards the next door":
            jump path_ai_door

        "[[Attack] Destroy the speaker and camera":
            jump path_ai_attack

label path_ai_thumb:
    
    show fixer thumbsup

    "You don't have a voicebox you can use to communicate, 
    so you simply give a thumbs up to the camera. That should be enough to show that you are here to help."

    a "Great! I'll open the door leading into the facility and guide you to the nearest place in need of repair."

    show fixer normal at right: 
        xzoom 1.0
    
    play sound "door3.mp3" volume 0.75

    "The door at the other end of the room opens up."

    a "I've never seen how you Fixers work before, so I'm excited!"

    jump welcome

label path_ai_door:

    "You don't have a voicebox you can use to communicate, 
    so you won't bother trying."

    show fixer normal at right: 
        xzoom 1.0

    "You head towards the door at the other end of the room."

    show ai sad

    a "I guess you're in a hurry."

    show ai normal

    a "I'll open the door leading into the facility and guide you to the nearest place in need of repair."
    
    play sound "door3.mp3" volume 0.75
    
    "The door at the other end of the room opens up."

    a "I've never seen how you Fixers work before, so I'm excited!"

    jump welcome

label path_ai_attack:

    "You're not here to help, but to sate your curiosity."

    "Having an AI constantly in your ear (even if you don't technically have ears) 
    while exploring is going to be annoying, so you plan to shut it up."

    play audio "sword_hit1.wav" 
    with vpunch

    "You swing your sword at the speaker, smashing it to pieces."

    play audio "sword_hit2.wav" 
    with vpunch

    hide ai
    "Then you do the same with the camera."

    "That should be enough to show that you should be left alone."

    show fixer normal at right: 
        xzoom 1.0
    
    "You head towards the door at the other end of the room. Just like the last door, it locked. This time by the AI."

    play sound "door3.mp3" volume 0.75

    "Luckily it's not as sturdy, so you pry it open and step through."

    $ breakerTracker += 1
    $ suspicionTracker = 5
    jump welcome

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Welcome
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label welcome:
    
    play music "music_factory.mp3" volume 0.25 fadeout 1
    scene bg welcome with fade
    
    "You find yourself on a platform looking out to a vast open area."

    "Gigantic, building-like silos that stretch all the way to the unseeable ceiling above laid out 
    throughout the facility."

    "You can see long platforms attached to them that connect the silos to each other and stairs on 
    their side that lead up and down."

    "Traversing this facility without a guide can be a nightmare."

    show pinkcom robot:
        xalign 0.5
        yalign 0.5

    "You spot a fellow robot hunched over near the platform railing and stairs that lead up to a nearby silo."
    
    hide pinkcom robot

    if suspicionTracker == 0:
        a "Again, welcome to Mason Co!"

        a "This is only a small section of the facility with not much importance, but we will start here first."

        a "Just head right up those stairs."

    jump welcome_choice

label welcome_choice:

    scene bg welcome

    menu:
        set removed_options
        "What to do..."

        "[[Interact] Head up the stairs":
            if robotDestroyed:
                "With one less threat in the facility, you walk up the metal stairs."
            else:
                "You ignore the robot and walk up the metal stairs."
            
            play sound "walk_tran1.wav"
            show bg stairs
            
            if suspicionTracker < 5:
                a "Right this way, my good Fixer."
            else:
                "You head up the metal stairs."

            jump crossroads

        "[[Interact] Look down from the platform":
            jump path_welcome_look
        
        "[[Interact] Walk up to the robot":
            "They might know something."

            show fixer normal at left
            show pinkcom single at right

            "As you walk closer, the robot begins twitching."

            if suspicionTracker == 0:
                a "Careful with getting too close, it might lounge at you."

            jump path_welcome_robot

label path_welcome_look:

    "You look down from the platform."

    scene bg look down

    "The floor is pitch black from the lack of light, giving the illusion that the silos 
    are growing from the depths of the earth. There are pipes of varying sizes that uniformly 
    stretch out in multiple directions."

    jump welcome_choice


label path_welcome_robot:

    show fixer normal at left
    with move
    show pinkcom single at right
    

    menu:
        set removed_options
        "What to do..."

        "[[Interact] Walk away":
            "Best not to get involved with it."
            jump welcome_choice

        "[[Gesture] Look towards a nearby camera in confusion" if suspicionTracker == 0:
            jump path_welcome_robot_question

        "[[Item] Show it the ID Card" if hasID:
            jump path_welcome_robot_id
        
        "[[Attack] Destroy the robot":
            jump robot_fight

label path_welcome_robot_question:
    hide pinkcom single
    show fixer normal at center: 
        xzoom -1.0
    with move
    show ai normal at left
    a "Why are you looking over here? This isn't one of my models."

    a "It broke into my facility 156 years ago."

    show ai confused

    a "Or was it 178?"

    show ai sad

    a "My time management isn't what it used to be."

    show ai normal

    a "I do know it came from Pinkcom, though."

    show ai confused

    a "I would have thought that a Fixer like you would know the difference between models."

    hide ai
    show fixer normal at center: 
        xzoom 1.0

    $ pinkcomKnown = True
    $ enemyName = "Pinkcom"
    $ suspicionTracker += 1
    jump path_welcome_robot

label path_welcome_robot_id:
    call dice_roll from _call_dice_roll
    
    show id:
        xalign 0.5
        yalign 0.5

    "Maybe it will do something if you show the ID."

    hide id
    play sound "pinkcom_cry1.wav"

    "Its head twists and looks in your direction."

    play sound "sword_hit2.wav" 
    with hpunch

    "It pauses for a moment, before slashing at you."

    "[[You've taken [d4] damage]"

    "Luckily the assault is halted by its lack of energy. It stays in place, staring at you, hoping you come closer."

    "Sadly you lost the ID Card in the process."

    "[[{b}You've lost the ID Card{/b}]"

    $ player_hp -= d4
    $ hasID = False
    jump path_welcome_robot

label robot_fight:

    play music "music_combat1.mp3" volume 0.5
    show bg welcome with pixellate
    show fixer normal at left
    show pinkcom single at right

    # Set starting attributes
    $ enemy_max_hp = 5
    $ enemy_hp = enemy_max_hp
    $ player_attack_value = 0
    
    # has the hp bars appear. located in screens.rpy
    show screen hp_bars
    
    # Fight keeps going until one side has no HP
    while player_hp > 0 and enemy_hp > 0:

        # Player
        call dice_roll from _call_dice_roll_1

        menu:
            "Light Attack":
                if d10 >= 8:                        #Crit
                    $ player_attack_value = d4 + d6
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit1.wav" 
                    with vpunch
                    "[[Massive Hit! [player_attack_value] damage!]"
                else:                               #Not Crit
                    $ enemy_hp -= d4
                    play sound "sword_hit1.wav" 
                    with hpunch
                    "[[A simple strike. [d4] damage!]"
            "Heavy Attack":
                if d10 >= 9:                        #Crit
                    $ player_attack_value = (d4 + d6) * 2
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit2.wav" 
                    with vpunch
                    "[[Massive Hit! [player_attack_value] damage!]"
                elif d10 >= 5:                      #Not Crit
                    $ player_attack_value = d6 + 2
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit2.wav" 
                    with hpunch
                    "[[A heavy strike. [player_attack_value] damage!]"
                else:
                    play sound "sword_miss1.wav" 
                    with hpunch
                    "You miss..."
                    play sound "pinkcom_cry2.wav"

        # Enemy
        call dice_roll from _call_dice_roll_2

        if d20 >= 19:
            $ player_hp -= d10
            play sound "sword_hit3.wav" 
            with vpunch
            "[[The [enemyName] robot makes a heavy swing, dealing [d10] damage!]"
        elif d20 <=2:                           # Heal
            $ enemy_hp += d4
            play sound "pinkcom_cry3.wav"
            if enemy_hp < enemy_max_hp:
                "[[The [enemyName] bot's self repair kicks in, healing [d4] hp!]"
            else:
                $ enemy_hp = enemy_max_hp
                "[[The [enemyName] bot fully repairs itself!]"
        else:
            $ player_hp -= d4
            play sound "sword_hit2.wav" 
            with hpunch
            "[[The [enemyName] robot makes a swing, dealing [d4] damage!]"
    # If the player loses
    if player_hp <= 0:
        hide screen hp_bars
        "You're either too rusty or simply unlucky..."
        jump death
    hide screen hp_bars

    play sound "pinkcom_cry4.wav"
    "The [enemyName] robot is no more."

    $ warTracker += 1
    $ robotDestroyed = True
    play music "music_factory.mp3" volume 0.25 fadeout 1
    jump welcome_choice

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Crossroads
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label crossroads:
    stop sound
    scene bg crossroads with fade

    "After walking up 1,056 steps, you reach a platform connected to two(2) bridges that lead into different directions."

    "Left and Right, a classic choice."

    if suspicionTracker < 5:
        a "Left will get you there faster, but there are currently some Pinkcom models in the way."
        pause 2.0
        a "{size=-10}Right is of no importance.{/size}"

    jump crossroads_choice

label crossroads_choice:
   
    menu:
        set removed_options
        "What to do..."

        "[[Interact] Go Left":
            jump silo
        "[[Interact] Go Right":
            jump town_start
        "[[Interact] Look towards a nearby camera in confusion" if suspicionTracker < 5:
            
            show camera:
                xalign 0.5
                yalign 0.5

            a "Stop looking over here, I don't have an answer for you!"

            a "Ignore Right and go Left!"

            hide camera

            jump crossroads_choice

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Silo
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label silo:
    
    play sound "walk_tran2.wav"

    if suspicionTracker < 5:
        "They said go Left, so you go Left."
    else:
        "Guess you'll go Left."
    
    stop sound
    show bg silo entrance with fade

    "After 1 and 46 minutes of walking, you arrive at one of the silos." 

    "There is only a door that leads inside."

    if suspicionTracker < 5:
        a "This should be the only bump in the road."

        a "It will be dangerous, but I'm sure a Fixer like you should have it covered."

        a "Let me get the door for you."
    play sound "door1.mp3" volume 0.5
    scene bg silo with fade
    "The door opens automatically, revealing a wide open room with an exit at the other end."

    "Piles of scrap and destroyed machine litter the area."

    "You can not discern what purpose the room had in the past, but now it looks to be occupied by 12 [enemyName] robots."

    jump silo_fight

label silo_fight:

    play music "music_combat2.mp3" volume 0.5 fadeout 1
    show fixer normal at left
    show pinkcom group at right
    show bg silo with pixellate

    $ enemy_max_hp = 60
    $ enemy_hp = enemy_max_hp
    $ player_attack_value = 0
    
    show screen hp_bars
    
    while player_hp > 0 and enemy_hp > 0:

        # Player
        call dice_roll from _call_dice_roll_3

        menu:
            "Light Attack":
                if d10 >= 8:                        #Crit
                    $ player_attack_value = d4 + d6
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit1.wav" 
                    with vpunch
                    "[[Massive Hit! [player_attack_value] damage!]"
                else:
                    $ enemy_hp -= d4
                    play sound "sword_hit1.wav" 
                    with hpunch
                    "[[A simple strike. [d4] damage!]"
            "Heavy Attack":
                if d10 >= 9:                        #Crit
                    $ player_attack_value = (d4 + d6) * 2
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit2.wav" 
                    with vpunch
                    "[[Massive Hit! [player_attack_value] damage!]"
                elif d10 >= 5:
                    $ player_attack_value = d6 + 2
                    $ enemy_hp -= player_attack_value
                    play sound "sword_hit2.wav" 
                    with hpunch
                    "[[A heavy strike. [player_attack_value] damage!]"
                else:
                    play sound "sword_miss1.wav" 
                    with hpunch
                    "You miss..."
                    play sound "pinkcom_cry2.wav"

        # Enemy
        call dice_roll from _call_dice_roll_4

        if d20 >= 19:
            $ player_hp -= d20
            play sound "sword_hit3.wav" 
            with vpunch
            "[[The [enemyName] robots make a heavy swing, dealing [d20] damage!]"
        elif d20 <=2:                           # Heal
            $ enemy_hp += d8
            queue sound "pinkcom_cry3.wav"
            if enemy_hp < enemy_max_hp:
                "[[The [enemyName] bots' self repair kicks in, healing [d8] hp!]"
            else:
                $ enemy_hp = enemy_max_hp
                "[[The [enemyName] bots fully repairs themselves!]"
        else:
            $ player_hp -= d10
            play sound "sword_hit2.wav" 
            with hpunch
            "[[The [enemyName] robots make a swing, dealing [d10] damage!]"
    
    if player_hp <= 0:
        hide screen hp_bars
        "You're either too rusty or simply unlucky..."
        jump death
    hide screen hp_bars

    play sound "pinkcom_cry4.wav"
    "The [enemyName] robots have been destroyed."

    $ warTracker += 1
    jump left_ending

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Town
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label town_start:

    play sound "walk_tran2.wav"

    if suspicionTracker < 5:
        "They're clearly hiding something."

        a "Wait!"
    else:
        "Guess you'll go Right."

    show black with fade

    "After 6 hours and 4 minutes of walking a seemingly straight forward path, 
    you arrive at a massive platform that leads off to multiple silos."

    "However, that's not the important part."

    stop sound
    scene bg town outside with fade

    "Atop this platform rests some sort of small town. The last thing you expected to find here."

    "Unlike the towns found outside, their buildings appear to be made entirely out of scrap metal. 
    Most likely due to the lack of natural resources here."

    if suspicionTracker < 5:
        show camera:
            xalign 0.5
            yalign 0.5
        
        "You take notice that the AI hasn't spoken to you since you took the Right path."

        "There are cameras and speakers here and there that look to be functional, but they aren't using them."

        "Weird..."

        hide camera

    "With nowhere else to go but forward, you head into the village."
    
    play music "music_town.mp3" volume 0.25 fadeout 1
    show bg town with fade
    show fixer normal at left
    show villager group at right

    "The residents simply stare at your arrival."

    "They look to be different models than the [enemyName] robots. Perhaps they were made here."

    "A particularly worn down robot confronts you. Their voice box sounds worn out as well."
    
    show elder normal at right

    e "S-sorry for-r the awkward town gre-e-eting."

    e "Seeing an-n-n-n unkn-n-own model such as you s-show up has put-t-t-t them on edge."
    show elder confused
    e "What b-brings you here, t-t-traveler?"
    jump town_start_choice

label town_start_choice:
    show elder normal
    menu:
        set removed_options
        "How to respond..."
        

        "[[Gesture] Indicate you're just passing through":
            "You make a walking motion with your fingers."
            show elder confused
            e "I s-see... no voice box or is-s-s it broken-n?"
            show elder normal
            e "What-t-tever the matter is it is sham-me you are just pas-s-ssing through."
            show elder happy
            e "I wis-s-sh you luck on your t-t-travels."
            jump town

        "[[Gesture] Give a thumbs up":
            show fixer thumbsup
            "You do just that, giving the old bot a well mannered thumbs up."
            show elder confused
            e "...r-right..."
            pause 2.0
            show elder normal
            show fixer normal
            e "Well, en-njoy your t-t-time in town."
            hide elder
            "The old bot awkwardly bows before turning around and leaving."

            "Kind of quick to give up there, pal..."
            jump town

        "[[Gesture] Point to your sword":
            show sword:
                xalign 0.5
                yalign 0.5
            "You point to the sword on your back."
            
            e "Hm?"

            e "A Flathead S-sword?"

            hide sword

            e "Having a Fixer w-w-weapon with you should-d mean you're a F-f-fixer, right?"

            "You nod your head."
            show elder happy
            e "Won-nderful n-n-news!"

            e "F-father brought-t-t us a Fixer."

            e "I s-s-shall take my l-leave, but please s-stay as long as-s you need-d-d."
            show elder normal
            e "Do vis-sit the shrine whil-l-le you're here."
            hide elder
            "The old bot bows before heading off."
            jump town

        "[[Attack] Destroy them":
            "An easy target."

            "Friendly or not, a robot that isn't you is a threat."
            play audio "sword_hit2.wav" 
            with hpunch
            hide elder
            show villager group:
                shake
            "You quickly slash them with your sword, destroying it in one fell swoop. 
            The other residents begin to panic."

            "No matter, they're next."

            play music "music_town_destroyed.mp3" volume 0.25 fadeout 1
            scene bg town destroyed with fade

            "The town had no defenses, so it took little time to deal with the rest."

            "You leave a destroyed town behind as you exit."
            $ breakerTracker += 1
            jump right_ending

        "[[Item] Show them the ID Card" if hasID:
            show id:
                xalign 0.5
                yalign 0.5
            "You take out the ID Card and hold it out towards them."
            show elder confused
            e "Oh?"

            e "D-didn't think I'd see one of thos-se again-n-n."
            show elder normal
            hide id
            e "I'm sorry to s-say, but I don't think-k it will be much h-help here."

            e "Father t-turned off most of the ID locked-d doors."

            e "They s-s-saw no need to have t-them using up energy."

            e "I c-can take it off-f-f your hands if you w-want."
            show fuse:
                xalign 0.5
                yalign 0.5
            e "In return I c-can give you a-a-a Fuse. It should help-p you in the fut-ture."
            hide fuse
            jump path_elder_id

label path_elder_id:

    menu:
        "How to respond..."

        "[[Gesture] Give a thumbs up":
            show fixer thumbsup
            e "W-wonderful! Here you g-go."

            show id at left:
                yalign 0.5
            with move
            show id at right:
                yalign 0.5
            with move

            "[[{b}You've lost the ID Card{/b}]"
            hide id
            $ hasID = False

            show fuse at right:
                yalign 0.5
            with move
            show fuse at left:
                yalign 0.5
            with move

            play sound "fuse_get.wav"
            "[[{b}You've gained a Fuse{/b}]"
            hide fuse
            $ hasFuse = True

            show elder confused
            show fixer normal
            e "You haven't-t said why you are h-here yet, t-t-traveler."
            jump town_start_choice
        
        "[[Gesture] Give a thumbs down":
            e "A s-s-shame..."
            show elder confused
            e "You haven't-t said why you are h-here yet, t-t-traveler."
            jump town_start_choice

label town:

    scene bg town map with fade

    call screen town_nav

    # interactive map 
    screen town_nav():
        add "bg town map"
        modal True

        imagebutton auto "bg leave marker %s":
            focus_mask True
            hovered Notify("Leave")
            action Jump("right_ending")

        imagebutton auto "bg shrine marker %s":
            focus_mask True
            hovered Notify("Shrine")
            action Jump("shrine")

        imagebutton auto "bg shop marker %s":
            focus_mask True
            hovered Notify("Shop")
            action Jump("shop")

label shrine:
    "There seems to be a shrine somewhere in the center of town."

    show black with fade

    "Its's not uncommon for a settlement to worship something."

    "Most times it's the AI that resides in the area, 
    and due to the lack of much outside influence, that's probably what's happening here."

    scene bg shrine location with fade
    play sound "churchbells.wav" volume 0.25

    "You arrive at the shrine."

    "It's about as you expected for a scrap town like this, 
    a simple roof being supported by pillars with an altar in the center."

    "There are bots huddled around, praying towards the altar. None of them pay you any mind."
    jump shrine_choice

label shrine_choice:
    menu:
        set removed_options
        "What to do..."

        "[[Interact] Investigate the altar":
            "You notice something sitting atop the altar."

            "You begin making out its form as you get close."

            show spear:
                xalign 0.5
                yalign 0.5

            "It's a Philipspear, a Fixer weapon."

            "Hanging off of it are red ropes with bells attached at the end."

            "They're treating it like a holy relic."

            hide spear

            "To think you would find a Fixer weapon here. This factory is full of surprises."
            $ seenSpear = True
            jump shrine_choice

        "[[Interact] Eavesdrop on their prayers":
            "You listen in on what they are praying for and to whom."

            "They are praying to a figure they call 'Father'." 

            "You can probably guess who this Father is."

            "Their prayers are almost all about helping their town survive and thrive, 
            as well as eliminating the [enemyName] robots."

            "Seems they've been left unanswered."
            jump shrine_choice

        "[[Interact] Leave":
            "Welp, you've seen enough."
            jump town

        "[[Interact] Take the Philipsear" if seenSpear:
            "You get closer to the Philipspear."

            "One of the worshipers takes notice of the Flathead sword on your back."
            show villager group at left
            show villager group as group2 at right
            "They stop praying and gather the attention of the others."

            "You enter high alert thinking you just upset them."

            "They all begin speaking in unison."
            play music "music_shrine_event.mp3" volume 0.25 fadeout 1
            t "Father has gifted us a Fixer."
            # has text appear on screen. located in screens.rpy
            show screen prayers
            t "Our prayers have been answered."
            hide screen prayers
            "One of them walks up to the altar, grabbing the Philipspear."
            show screen prayers
            t "Our prayers have been answered."
            hide screen prayers
            show spear:
                xalign 0.5
                yalign 0.5
            "They turn to you and kneel, offering you the Philipspear."
            show screen prayers
            t "Our prayers have been answered."
            hide screen prayers

            play sound "spear_get.wav"
            "It would be rude to refuse, so you take the Philipspear."
            hide spear
            hide villager group
            hide group2
            play music "music_town.mp3" volume 0.25 fadeout 1
            "The worshippers return to what they were doing, as if what just conspired never happened."

            "[[{b}You've obtained the Philipspear{/b}]"
            $ hasSpear = True
            $ heroTracker += 1
            stop sound
            jump shrine_choice


label shop:
    "You stop by a store selling tech."
    
    scene bg shop inside with fade

    "Their wares look old, but they can still have their uses."

    "A rusted bot from behind the counter calls out to you."

    s "Ya here just to window shop, pal?"

    jump shop_choice

label shop_choice:
    menu:
        s "What ya buying?"
        "[[Interact] Leave the shop":
            jump town

        "[[Interact] Trade the ID Card for a Fuse" if hasID:
            s "Aye. That works for me, pal"
            "[[{b}You've lost the ID Card{/b}]"
            $ hasID = False

            show fuse:
                xalign 0.5
                yalign 0.5

            play sound "fuse_get.wav"
            "[[{b}You've gained a Fuse{/b}]"
            hide fuse
            $ hasFuse = True
            jump shop_choice

        "[[Interact] Trade the ID Card for Chains" if hasID:
            s "Aye. That works for me, pal"
            "[[{b}You've lost the ID Card{/b}]"
            $ hasID = False

            show chains:
                xalign 0.5
                yalign 0.5
            
            play sound "chains_get.wav"
            "[[{b}You've gained some Chains{/b}]"
            hide chains
            $ hasFuse = True
            jump shop_choice

        "[[Interact] Trade the Fuse for a Cluster Bomb" if hasFuse:
            s "Aye. That works for me, pal"
            "[[{b}You've lost a Fuse{/b}]"
            $ hasFuse = False

            show clusterbomb:
                xalign 0.5
                yalign 0.5
            
            play sound "clusterbomb_get.wav"
            "[[{b}You've gained a Cluster Bomb{/b}]"
            hide clusterbomb
            jump shop_choice
        
        "[[Interact] Trade the Fuse for a Repair Kit" if hasFuse:
            s "Aye. That works for me, pal"
            "[[{b}You've lost a Fuse{/b}]"
            $ hasFuse = False

            show repairkit:
                xalign 0.5
                yalign 0.5
            
            play sound "repairkit_get.wav"
            "[[{b}You've gained a Repair kit{/b}]"
            hide repairkit
            jump shop_choice

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Endings
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

label left_ending:
    play music "music_end.mp3" volume 0.25 fadeout 1
    scene bg end with fade
    if suspicionTracker == 5:
        "You've left the silo."

        "The fight was hard, but you've never left more alive."

        "Well as much as a robot can be."

        "It's nice not having a care in the world."

        "You've made a decision."

        "This place will become your playground!"

        "Who cares if you've pissed off the AI running the place? You're free to do what you want!"

        "You march forward deeper into the factory, enjoying yourself every step of the way."
        show black with fade
        pause 2.0
        "[[{b}Ending 1a: Renegade{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    elif warTracker == 2:
        "You've left the silo."

        a "Great job!"

        a "You had me worried there for a second."

        a "Let's continue on, we should be there soon."

        "It's talking again..."

        "As long as you get to fight more, that's all that matters."

        "If you help out along the way, great."

        "You continue following the AI's path, fighting any [enemyName] robot you come across."
        show black with fade
        pause 2.0
        "[[{b}Ending 2: War{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    else:
        "You've left the silo."

        a "Great job!"

        a "You had me worried there for a second."

        a "Let's continue on, we should be there soon."

        "You give a thumbs up and follow the path ahead."

        show black with fade
        pause 2.0
        "[[{b}Ending 5a: Fixer{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    return


label right_ending:
    play music "music_end.mp3" volume 0.25 fadeout 1
    scene bg end with fade
    
    if breakerTracker == 2:
        "Nothing feels better than snuffing the life out of a fellow robot."

        "You wonder if there are any more towns in this factory."

        "It is massive afterall."

        "You imagine how the AI must be feeling seeing you slaughter one of their towns."

        "The anger..."

        "The helplessness..."

        show black with fade
        pause 2.0
        "It fills you with joy."
        pause 2.0
        "[[{b}Ending 3: Breaker{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    elif suspicionTracker == 5:
        "Nothing feels better than exploring the unknown."

        "You wonder what other interesting things can be found in this old forgotten factory."

        "It is massive afterall."

        "Whatever the case is, you're gonna enjoy yourself."

        show black with fade
        pause 2.0
        "[[{b}Ending 1b: Renegade{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    elif heroTracker == 1:
        "After traveling a mile out from the town, the AI comes back."

        a "Sorry. I didn't want you to see that."

        "You look towards the nearest camera and tilt your head."

        a "I felt ashamed about not being able to help them, so I just ignored it."

        a "Hoping they can survive on their own."

        a "They did for a while, but..."
        pause 2.0
        a "Their town was bigger and had more residents."

        a "However, due to the poor condition of my facility, they had to deal with many hardships."

        a "I'm hoping that you can be my..."
        pause 2.0
        a "...no..."

        a "our solution."

        a "That is if you're okay with that."

        "You give a thumbs up."
        pause 2.0
        a "Thank you."

        "You continue forward filled with a new found determination."
        show black with fade
        pause 2.0
        "[[{b}Ending 4: Hero{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    else:
        "After traveling a mile out from the town, the AI comes back."

        a "Sorry. I didn't want you to see that."

        "You look towards the nearest camera and tilt your head."
        pause 2.0
        a "It's nothing."

        "You give a thumbs up and follow the path ahead."

        "The factory ain't gonna fix itself."
        show black with fade
        pause 2.0
        "[[{b}Ending 5b: Fixer{/b}]"
        "{cps=25}[[{b}To Be Continued{/b}]{/cps}"

    return
        

label death:
    play music "music_end.mp3" volume 0.25 fadeout 1
    scene black with fade
    "You have become another footnote on the history of the Mason Co Robotic Facility."
    pause 2.0
    "You are eventually forgotten..."
    "{cps=25}[[{b}You have Died{/b}]{/cps}"
    return