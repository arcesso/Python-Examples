#! python3

import random
import logging

# set logging
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Program start.')

def guessAndToss():
	global games
	logging.debug('init guessAndToss')
	guess = ''
	logging.debug('Guess is: ' + guess)
	
	# record toss.  0 is tails, 1 is heads
	toss = random.randint(0, 1) 
	logging.debug('Toss is ' + str(toss))
	
	# acquire input from user
	while guess not in ('heads', 'tails'):
		print('Guess the coin toss! Enter heads or tails:')
		guess = input()
		logging.debug('Guess is: ' + guess)

	# convert to numeral
	if guess == 'tails':
		guess = 0
		logging.debug('Guess recorded as tails.  Guess = ' + str(guess))
	else:
		guess = 1
		logging.debug('Guess recorded as heads.  Guess = ' + str(guess))

	# compare results
	if toss == guess:
		print('You got it!')
		return
	elif games != 1:
		print('Nope! Guess again!')
		games += 1
		logging.debug('Games played: ' + str(games))
		logging.debug('Recurse')
		return guessAndToss()  # recurse making sure to exit loop before starting it again.
	else:
		print('You suck!')
		return

games = 0
guessAndToss()

logging.debug('Program End.')