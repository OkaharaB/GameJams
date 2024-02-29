# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define z = Character("Zerk")

define y = Character("You")

# The game starts here.


label start:

    play music "carol.mp3"

    z "Well, we meet again..."

    z "Brother." 

    y "It's been a long time. But your reign of tyranny ends today!"

    z "So that's it, then? No love for your long lost sibling?"

    y "Hard to feel affection in these circumstances. I can't even see you in this dungeon!"

    z "Of course not. This is the darkest dungeon. So obviously, it is black."

    y "Seems lazy... but OK."

    play sound "knifesharpener1.flac"

    y "Draw your weapon!"

    z "If I must... Prepare yourself, brother."

    $ win = 0 

    $ lose = 0 
    

label menmen:
    $ number = renpy.random.randint(1, 3)
menu: 

    "What will you do?"

    "Melee":
        jump rock_1

    "Magic":
        jump paper_1

    "Sword":
        jump scissors_1

label rock_1:
    if number == 1:
        play sound "rock_breaking.flac"
        with hpunch
        z "Ugh."

        y "Hmph."

        jump menmen

    elif number == 2:
        play sound "spell1_0.wav"
        z "Heh. You always were a simpleton."
        z "Imagine, bringing fists to a magic fight."
        $ lose += 1
        jump endcheck
    elif number == 3:
        play sound "whoosh1.wav"
        z "Ugh. You've gotten stronger..."
        $ win += 1
        jump endcheck


label paper_1:
    if number == 1:
        play sound "coin.flac"
        z "My weapons? Turned to coin!?"
        $ win += 1
        jump endcheck
    elif number == 2:
        play sound "explosion.ogg"
        y "How's that!"
        z "Seems our spells are equally matched!"
        y "I've been practicing."
        jump menmen
    elif number == 3:
        play sound "knifesharpener2.flac"
        z "HA!"
        z "My sword can cut through your magic."
        $ lose += 1
        jump endcheck

label scissors_1:
    if number == 1:
        play sound "whoosh1.wav"
        with vpunch
        z "Ha! Take that!"
        $ lose += 1
        jump endcheck
    elif number == 2:
        play sound "rock_breaking.flac"
        z "NO! How!?"
        $ win += 1
        jump endcheck
    elif number == 3:
        play sound "knifesharpener1.flac"
        z "Our blades are equally matched!"
        jump menmen
    

label endcheck:

    if win == 3:
        jump winner
    elif lose == 3:
        jump loser
    else:
        jump wincheck

label wincheck:
    if win == 0:
        jump losecheck0
    elif win == 1:
        jump losecheck1
    elif win == 2:
        jump losecheck2

label losecheck0:
    if lose == 1:
        jump w0l1
    elif lose == 2:
        jump w0l2
    else:
        jump error

label losecheck1:
    if lose == 0:
        jump w1l0
    elif lose == 1:
        jump w1l1
    elif lose == 2:
        jump w1l2
    else:
        jump error

label losecheck2:
    if lose ==0:
        jump w2l0
    elif lose == 1:
        jump w2l1
    elif lose == 2:
        jump w2l2
    else:
        jump error

label w0l1:
    z "HA! You've been bested! Give up!"

    y "I'll never surrender to you! Not after all you've done!"
    
    z "All I'VE done!? All I've ever done is serve the family! All I've ever wanted is peace!"

    y "Don't you dare turn this around on me! Hiya!"

    jump menmen

label w0l2:
    z "...Haa. Brother. I expected more from you."

    y "You haven't won yet!"

    z "Heh. Haven't I? Your odds are dwindling."

    y "Everyone loves an underdog."

    z "Well, then it's time to put this dog out of his misery!"

    jump menmen

label w1l0:
    z "Urk. Lucky shot!"

    y "Yes. And by luck you shall be defeated!"

    z "Why must you always torment me like this!?"

    z "I've done you no harm!"

    y "No harm!? You run from me! You ignore my missives!"

    z "I have duties!"

    y "And now my duty is to defeat you."

    jump menmen

label w1l1:
    y "The scores are even now."

    z "I've barely gotten started!"

    y "Well, then prepare yourself!"

    jump menmen

label w1l2:
    z "Is this what you wanted!? All this carnage!?"

    y "Ugh..."

    z "You could have left me! You could have just continued your life!"

    y "Leave you? On Christmas eve, brother!?"

    z "'Tis just another day to me now..."

    y "Then, maybe you can remember it now as the day you were bested by me!"

    z "You wish!"

    jump menmen

label w2l0:

    z "WHY!?"

    y "Like I said, by luck you shall be defeated."

    z "None of this is fair... I just wanted my peace!"

    y "Your peace comes from tyranny. From ignorance!"

    z "LEAVE ME."

    y "NEVER!" 

    jump menmen

label w2l1:

    z "I don't understand... Why can't you leave me to my dungeon?"

    y "Because, brother. I need you. I need your counsel."

    y "Your companionship."

    z "You would deny me peace, for your needs?"

    y "Such a sad way of seeing things..."

    jump menmen


label w2l2:
    z "Haa... Haa..."

    y "Haa... Haa..."

    z "This is it, you know..."

    y "Yes..."

    z "After this, one of us will be defeated. There's no going back."

    y "It didn't have to be this way... If you'd only listened to reason!"

    z "Reason!? How can you see yourself as the reasonable one? After everything you did!?"

    y "What I did!? Brother, I only wanted us to spend time together."

    z "So you barged into my sanctuary!? You disturbed my holy silence?"

    y "I brought you joy! Festivities!"

    z "YOU BROUGHT ME NOTHING."

    y "... How can you say that?"

    y "Were this dungeon not so dark, you could see. I have brought you a gift."

    z "How.. I..."

    y "Even you deserve a Merry Christmas."

    z "No... That's..."

    z "That's just a trick!"

    y "No-"

    z "TO ARMS!"

    jump menmen


label loser:
    y "Brother... Why?"

    show bg_gameover

    play music "gameover.mp3"

    "GAME OVER" 

    return
    
label winner:
    z "THIS IS IMPOSSIBLE!"

    y "NIGH, BROTHER! YOU HAVE BEEN BESTED!"

    z "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHH-"

    stop music fadeout 1.0



    scene bg_chris

    "Mother" "What are you yelling about!?"

    scene bg_chrismae
    with dissolve

    play music "eve.mp3"

    with hpunch 
    
    "Boys" "Moooooooooooooooooom!"

    scene bg_christmas

    "Boys" "We were just playing!"

    centered "{font=fonts/Christmas.otf}{size=+75}Merry Christmas!{/size}{/font}{p=5.0}{nw}"

    centered "{font=fonts/Christmas.otf}{size=+75}Game by Moritani{/size}{/font}{p=5.0}{nw}"

    centered "{font=fonts/Christmas.otf}{size=+75}For Wosber{/size}{/font}{p=5.0}{nw}"

    return

label error:
    z "Something went wrong here..."

return
