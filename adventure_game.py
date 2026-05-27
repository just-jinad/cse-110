"""
Author: Tope Jinad

Purpose: Build an adventure game where the user makes choices that lead to different outcomes.
A horror survival story set in Blackwood Forest. 
"""
# I had two friends play before submitting, and neither of them made it out alive on their first attempt.
# I also added some extra levels of choice to make it more engaging and less linear.

print("TITLE: Whispers of Blackwood Forest")
print("................................... \n")

print("""Rain crashes through the twisted branches of Blackwood Forest as thunder tears across the sky.
Your car died nearly an hour ago.
No signal.
No road signs.
No sound except the wind... and something moving between the trees.
You remember the old stories people in the nearby town used to tell:
"If Blackwood calls your name, never answer."
At first, you laughed at those stories.
Now, standing alone in the middle of the forest with darkness swallowing everything around you, they no longer seem funny.
Your flashlight fell during the crash.
Your backpack is soaked.
And somewhere behind you...
CRACK.
A branch snaps.
Your hands shake as you search your pockets and discover two usable items:
A single box of matches.
A weak flashlight with dying batteries.
Far ahead, hidden between the trees, you spot what looks like an abandoned ranger station.
You must choose.""")

print("")
print("A MATCH and a FLASHLIGHT. Which one do you want to pick up?")
print("")

userInput = input("Type 'MATCH' or 'FLASHLIGHT': ").upper()

if userInput == "MATCH":
    print("""
You pick up the match and strike it.
The forest is illuminated for an instant — you see a large grizzly bear.
But something is wrong with it.
Its fur is torn open in places as if something clawed through it from the inside.
One glowing eye stares directly at you.
Then the match dies.
Darkness returns.
""")

  
    choice2 = input("Do you want to RUN, or HIDE behind a tree? Type 'RUN' or 'HIDE': ").upper()

    if choice2 == "RUN":
        print("""
You sprint blindly through the forest, branches tearing your skin as the creature crashes behind you.
You finally see lights ahead — salvation.
A cabin.
You slam the door behind you and barricade it with furniture.
Breathing heavily, you look around.
The cabin walls are covered with newspaper clippings about missing hikers.
Then you notice something horrifying:
The clippings are dated from the last 50 years.
And they all have one thing in common: they all disappeared in Blackwood Forest.
Then a voice whispers from the corner of the room: 'You brought it here.'
A shadow shifts near the window. The front door rattles.
You have seconds to decide.
""")

        choice3 = input("Do you BARRICADE the door further, ESCAPE through the back window, or SEARCH the cabin for a weapon? Type 'BARRICADE', 'ESCAPE', or 'SEARCH': ").upper()

        if choice3 == "BARRICADE":
            print("""
You shove every piece of furniture against the door.
The rattling stops.
Silence.
Then the ceiling above you creaks.
It was never at the door.
It was already inside.
Game over.
""")
        elif choice3 == "ESCAPE":
            print("""
You throw open the back window and drop into the mud.
The forest is dark but you run toward a faint orange glow in the distance.
A highway.
Headlights.
You flag down a truck and collapse into the passenger seat, soaking wet and shaking.
The driver doesn't ask questions.
Neither do you.
You survived Blackwood Forest.
YOU WIN.
""")
        elif choice3 == "SEARCH":
            print("""
You tear open the cabin drawers and find a flare gun with one round loaded.
The front door bursts open.
You raise the gun and fire.
The flare lights up the entire clearing.
Whatever was at the door screams and retreats into the tree line.
The signal flare is also visible from the road.
Twenty minutes later, you hear sirens.
YOU WIN.
""")
        else:
            print("Invalid input. You freeze in panic. The door gives way. Game over.")

    elif choice2 == "HIDE":
        print("""
You dive behind a fallen tree and hold your breath.
The creature stomps past you.
But it isn't chasing by scent.
It's listening.
You cover your mouth as the growling slowly fades away.
Minutes pass.
Then you notice something buried beneath the mud near your hand.
A silver sheriff badge.
You pick it up and see the name engraved on it: 'Sheriff Thompson.'
The last known victim of Blackwood Forest.
A faint lantern light appears deeper in the woods.
Someone is still out there.
Watching.
""")

   
        choice3 = input("Do you APPROACH the light or STAY hidden? Type 'APPROACH' or 'STAY': ").upper()

        if choice3 == "APPROACH":
            print("""
You move carefully toward the lantern.
As you get closer you see a figure — an old woman in a rain coat, holding the lantern steady.
She looks at the badge in your hand and nods slowly.
'He dropped that the night he saved me,' she says.
'Come. I know the way out.'
She leads you through a hidden path you never would have found alone.
By dawn you are standing on a real road, watching the sun rise over the treeline.
YOU WIN.
""")
        elif choice3 == "STAY":
            print("""
You decide the light is a trap and press yourself deeper into the mud.
The lantern slowly moves away.
Then it stops.
Then it goes out entirely.
The growling returns — closer this time.
Much closer.
It found you while you were watching the light.
Game over.
""")
        else:
            print("Invalid input. Your hesitation gives away your position. Game over.")

    else:
        print("Invalid input. Please type 'RUN' or 'HIDE'.")

elif userInput == "FLASHLIGHT":
    print("""
The weak beam flickers but cuts through the darkness enough to reveal an old trail.
The path looks recently used.
Fresh footprints.
Human.
You begin walking carefully.
After several minutes, you hear whispering coming from the trees beside you.
Not one voice.
Many.
The flashlight flickers again.
The whispers stop.
Then a child's voice softly says:
'Help me…'
""")

    
    choice2 = input("Do you FOLLOW the voice or LOOK around first? Type 'FOLLOW' or 'LOOK': ").upper()

    if choice2 == "FOLLOW":
        print("""
You step off the trail toward the child's voice.
The whispers grow louder, layering on top of each other.
Then your flashlight dies completely.
In the sudden darkness you feel a small cold hand take yours.
It pulls you gently forward.
You stumble into a clearing.
In the center stands the ranger station you saw earlier.
The hand releases yours.
The child is gone.
But the station door is unlocked and a radio sits on the desk — still powered.
""")


        choice3 = input("Do you CALL for help on the radio, or WAIT and listen first? Type 'CALL' or 'WAIT': ").upper()

        if choice3 == "CALL":
            print("""
You grab the radio and press the button.
Static. Then a voice.
A real one.
A rescue team picks up your signal within the hour.
They find you exactly where you described.
You never tell them about the child's hand.
Some things are better left in Blackwood.
YOU WIN.
""")
        elif choice3 == "WAIT":
            print("""
You sit in silence and listen.
The radio crackles on its own.
A voice begins reading names.
Dozens of them.
Then it reads yours.
The station door swings shut by itself.
The lock clicks.
Game over.
""")
        else:
            print("Invalid input. You fumble with the radio until the batteries die. Game over.")

    elif choice2 == "LOOK":
        print("""
You sweep the flashlight through the trees.
Two glowing eyes stare back.
Too high off the ground to be an animal on all fours.
Too still to be human.
The eyes blink slowly.
Then a second pair appears beside the first.
Then a third.
Your flashlight flickers.
""")

        # ── LEVEL 3 ──
        choice3 = input("Do you RUN back to the trail, or STAND your ground and SHOUT? Type 'RUN' or 'SHOUT': ").upper()

        if choice3 == "RUN":
            print("""
You spin and sprint back to the trail.
The eyes don't follow.
Whatever they were, they stay in the trees.
You run until you hit a chain-link fence.
On the other side: a road, a gas station, fluorescent lights.
You climb over without looking back.
YOU WIN.
""")
        elif choice3 == "SHOUT":
            print("""
You scream at the top of your lungs.
The eyes vanish instantly.
Silence.
Then your flashlight gives out for good.
In the absolute darkness you hear them moving.
Not away from you.
Around you.
Game over.
""")
        else:
            print("Invalid input. You stand paralyzed until the flashlight dies. Game over.")

    else:
        print("Invalid input. Please type 'FOLLOW' or 'LOOK'.")

else:
    print("Invalid input. Please type 'MATCH' or 'FLASHLIGHT'.")