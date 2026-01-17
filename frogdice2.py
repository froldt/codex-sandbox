<<<<<<< HEAD
import random

"""FrogDice is based on the rules from Pass the Pigs
(http://www.passthepigs.com/). Thank you to them for the game idea.

The inspiration comes from Frogdice, Inc - a game company located in Lexington, Kentucky. Every time that I heard their name I thought of a dice game using little frogs. Since such a thing didn't seem to exist, I decided to go ahead and create it."""

# ---- functions ---- #
def roll_the_dice(player, score, points):
	#-- roll dice --#
	frog1 = random.randint(1,6)
	frog2 = random.randint(1,6)
	
	#-- calculate score from the roll --#
	if frog1 == frog2:
		#this calculates the doubles
		print "\n%s, you rolled:" % (player)
		if frog1 == 1 or frog1 == 2:
			#sider - 1 point
			roll_points = 2
			points += 2
			which_frog(frog1)
			which_frog(frog2)
			print "which is worth %i points." % roll_points
			should_I_roll(player, score, points)
		elif frog1 == 3:
			#hopper - 20 points
			roll_points = 20
			points += 20
			which_frog(frog1)
			which_frog(frog2)
			print "which is worth %i points." % roll_points
			should_I_roll(player, score, points)
		elif frog1 == 4:
			#frog legs - 20 points
			roll_points = 20
			points += 20
			which_frog(frog1)
			which_frog(frog2)
			print "which is worth %i points." % roll_points
			should_I_roll(player, score, points)
		elif frog1 == 5:
			#noser - 40 points
			roll_points = 40
			points += 40
			which_frog(frog1)
			which_frog(frog2)
			print "which is worth %i points." % roll_points
			should_I_roll(player, score, points)
		else:
			#road kill - back to 0
			which_frog(7)
			print "so you're roadkill...\nBack to zero!"
			points = 404
			set_score(player, score, points)
	elif (frog1 == 1 and frog2 == 2):
		#this determines if you lost your points and your turn
		which_frog(frog1)
		which_frog(frog2)
		print "\nFrog out! You just lost your turn and any new points."
		points = 0
		set_score(player, score, 0)
	elif (frog1 == 2 and frog2 == 1):
		#this determines if you lost your points and your turn
		which_frog(frog1)
		which_frog(frog2)
		print "\nFrog out! You just lost your turn and any new points."
		points = 0
		set_score(player, score, 0)
	else:
		#adds together the points from the combo throws
		roll_points = calculate_score(frog1) + calculate_score(frog2)
		points += roll_points
	
	#return results to the screen - including possible points
	print "\n%s, you rolled:" % (player)
	which_frog(frog1)
	which_frog(frog2)
	if roll_points == 1:
		print "which is worth 1 point."
		should_I_roll(player, score, points)
	elif roll_points > 1:
		print "which is worth %i points." % roll_points
		should_I_roll(player, score, points)
	else:
		print "you don't get any new points this turn... Next!"
		print "Your score stays at %i." % score

def calculate_score(score):
	#determines the score of a single frog
	if score == 1:
		return 1
	elif score == 2:
		return 1
	elif score == 3:
		return 5
	elif score == 4:
		return 5
	elif score == 5:
		return 10
	else:
		return 1

def should_I_roll(player, score, points):
	new_score = score + points
	find_winner(player, score, points)
	prompt = "What do you want to do?\n  1) roll again and try for more points\n  2) keep score of %i and pass turn\n: " % (new_score)
	dice_roll = raw_input(prompt)
	if "q" in dice_roll:
		print "Have a great day!"
		exit()
	elif "s" in dice_roll:
		show_scores(player, score, points)
		should_I_roll(player, score, points)
	elif "c" in dice_roll:
		print"""
Commands:
  about - information about the game
  help - this help screen (BOOM! You already found it, you incredibly smart, attractive person, you!)
  quit - exits the game
  scores - displays current scores for all of the users
----------------------
"""
		should_I_roll(player, score, points)
	elif "a" in dice_roll:
		#about
		print """
This is FrogDice.
(It's a dice game... with frogs!)
Written by Matthew French-Holt.
Insipired by the name of game company FrogDice
	(www.frogdice.com)
Every time Matthew heard their name, he thought
of a modified version of the "Pass the Pigs" game.
Currently at v1.0
3 September 2012

----------------------
"""
		should_I_roll(player, score, points)
	elif "h" in dice_roll:
		print """This be the help, argh.
		
The game is simple (though more challenging without visuals).
- roll your two frogs
- calculate the score
- decide if you want to keep that score or try again

The possible combinations are:
Sider - frog on it's side
  1 point, or 2 points for double
Hopper - frog on its feet
  5 points, 20 points for double
Frog Legs - frog on its back
  5 points, 20 points for double
Noser - frog on its nose and front feet
  10 points, 40 points for double
Road Kill - frogs touching
  back to 0 points!
Frog Out - one frog on each side
  lose points and turn

Type in "command" to see the different options.
----------------------
"""
		should_I_roll(player, score, points)
	elif int(dice_roll) == 1:
		#game on!
		roll_the_dice(player, score, points)
	elif int(dice_roll) == 2:
		set_score(player, score, points)
	else:
		#catch-all
		print "\nI don't understand that command"
		should_I_roll(player, score, points)


def set_score(player, score, points):
	# this determines what the score is
	global the_players
	current_player = which_player(player)
	if points == 0:
		the_players[current_player].points = 0
		next_player(player)
	elif points == 404:
		the_players[current_player].points = 0
		the_players[current_player].score = 0
		next_player(player)
	else:
		the_players[current_player].score = score + points
		the_players[current_player].points = 0
		next_player(player)


def next_player(player):
	#this tracks whose turn it is
	global the_players
	how_many = len(the_players)
	current_player = which_player(player)
	if current_player == how_many - 1:
		#roll back to beginning of Player 1
		next_player = 0
	else:	
		next_player = current_player + 1
	
	print "\n\n--------------\n%s, your current score is %i." % (the_players[next_player].name, the_players[next_player].score)
	roll_the_dice(the_players[next_player].name, the_players[next_player].score, the_players[next_player].points)


def which_player(player):
	i = 0
	while i < how_many_players:
		if the_players[i].name == player:
			return i
		else:
			i += 1


def find_winner(player, score, points):
	new_score = score + points
	if new_score >= 250:
		print "We have a winner!\nCongratulations, %s!" % player
		exit()
	else:
		return "not yet!"


def which_frog(current_frog):
	frog1_pic = """	     __    ___
	  __(_ \\__/_  \\
	 /    \\   \\__  \\
	(          __   )
	 \\__ _/ __/_   /
	    (__/  \\___/"""
	frog2_pic = """	   ___    __
	  /  _\\__/ _)__
	 /    /   /    \\
	(               )
	 \\   _\\__ \\_ __/
	  \\___/  \\__)"""
	frog3_pic = """	 _((O)
	(_    \\_______
	  \\           \\
	   \\ \\ \\   /   )
	    -/ /--(  _/
	   ((_/ ((__/"""
	frog4_pic = """	  _/   )) / ))
	 /    )--/ /-
	(    /   \ \ \   
	 \________    \_
	          \    _)
	           (0))"""
	frog5_pic = """	       _____
	      / / _ )
	     /  L_ | 
	  ((O)   /U
	 /    _\\ \\
	(____/ (_/"""
	frog6_pic = """	 ____    )))  __
	(_  _\__(((__/ _)__
	  /  /   )))  /    \\
	 (      (((         )
	 _\ _\___)))_ \_ __/
	(____/  (((  \__)"""
	
	if current_frog == 1:
		print frog1_pic
	elif current_frog == 2:
		print frog2_pic
	elif current_frog == 3:
		print frog3_pic
	elif current_frog == 4:
		print frog4_pic
	elif current_frog == 5:
		print frog5_pic
	elif current_frog == 6:
		random_frog = random.randint (1,2)
		if random_frog == 1:
			print frog1_pic
		else:
			print frog2_pic
	else:
		print frog6_pic


def show_scores(player, score, points):
	global the_players
	print "\n----------------------\n"
	i = 0
	while i < len(the_players):
		name = the_players[i].name
		score = the_players[i].score
		print "%s has %i points." % (name, score)
		i +=1
	print "\n----------------------\n"
	should_I_roll(player, score, points)
	
# ---- end of functions ---- #


# ---- class ---- #
class Player:
	'The empty outline for each player'
	
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.points = 0

# ---- end of class ---- #


# -- print rules -- #
print """Welcome to FrogDice!
\nIt's a pretty simple dice game with only a couple of rules:
\t1) roll your frogs (ie: dice)
\t2) choose to keep your score and pass your turn
\t      -or-
\t   roll again and try for more points
\t   (BTW - games go to 250 points.)
"""

#here live the players
global the_players # this is used in set_score, next_player, and show_scores
the_players = []

# -- initiate player(s) -- #
while True:
	try:
		how_many_players = int(raw_input("How many players are there? : "))
		break
	except ValueError:
		print("Oops! That was no valid number. Try again...")

count = 0
while count < how_many_players:
	current_player = count + 1
	prompt = "Player %i name: " % current_player
	current_player_name = raw_input(prompt)
	the_players.append(Player(current_player_name))
	count += 1


# --start the game -- #
roll_the_dice(the_players[0].name, the_players[0].score, the_players[0].points)
=======
#!/usr/bin/env python3
"""Roll a set of dice and report the results.

This utility is intentionally small and focused, serving as a simple example
script for this repo.
"""

from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class RollResult:
    rolls: list[int]

    @property
    def total(self) -> int:
        return sum(self.rolls)


def roll_dice(count: int, sides: int) -> RollResult:
    rolls = [random.randint(1, sides) for _ in range(count)]
    return RollResult(rolls=rolls)


def format_result(result: RollResult) -> str:
    roll_text = " ".join(str(roll) for roll in result.rolls)
    return f"Rolls: {roll_text} (total {result.total})"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Roll a set of dice and print the results.",
    )
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=2,
        help="Number of dice to roll (default: 2).",
    )
    parser.add_argument(
        "sides",
        nargs="?",
        type=int,
        default=6,
        help="Number of sides on each die (default: 6).",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.count < 1:
        raise SystemExit("count must be at least 1")
    if args.sides < 2:
        raise SystemExit("sides must be at least 2")
    result = roll_dice(args.count, args.sides)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
>>>>>>> f991f2faf026633ff6677237b7ff213d0c7485b1
