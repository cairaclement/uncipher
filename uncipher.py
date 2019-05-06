#!python3
# ETAION | VKJXQZ
import string
import sys

static_most_frequent = 'ETAION'
static_less_frequent = 'VKJXQZ'

SCORE_LIMIT = 5

alphabet = string.ascii_lowercase * 2

english_letters = string.ascii_lowercase.upper()

def get_letter_count(message):
	""" Count the frequency of each alphabet in the message """

	# letter mapping, each letter count is initially 0 (zeros)
	letter_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, \
	'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, \
	'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

	# iterate throught the supplied message
	for letter in message:
		# the letter has to be in the english alphabet
		if letter.upper() in english_letters:
			# we can proceed
			letter_counter[letter.upper()] += 1

	return letter_counter

def get_frequency_order(message):
	aft_count = get_letter_count(message)

	aft_count_sorted = sorted(list(zip(tuple(aft_count.keys()), tuple(aft_count.values()))), 
		key=lambda x: x[1], 
		reverse=True)
	letter_appearance = ''.join([x[0] for x in aft_count_sorted])

	return letter_appearance

def get_match_score(message):
	message = get_frequency_order(message)
	counter = 0
	message_6 = message[:6]
	last_message_6 = message[-6:]
	# check the first 6 score
	for letter in message_6:
		if letter in static_most_frequent:
			counter += 1 
	for letter in last_message_6:
		if letter in static_less_frequent:
			counter += 1 
	return counter

def exit_():
	""" provide feature of holding on before exiting """
	input('Press <enter> to exit ..')
	exit()

if __name__ == '__main__':

	# check if argument is complete
	if len(sys.argv) != 2:
		# print the helper message
		print()
		print('USAGE: {} < cipher text >')
		print()
		# and call the custom exit function
		exit_()

	# title of the message
	print('BREAKING SUBTITUTION CIPHER USING FREQUENCY ANALYSIS')
	print('-'*30)

	# what we are cracking
	JARGON = sys.argv[1]
	# status
	print('Cracking: {}'.format(JARGON))
	print()

	#posibilities = []
	all_dec = []

	# loop through all alphabet shift
	for shift in range(1, 26):

		dec = ''.join([alphabet[alphabet.index(x) + shift] if x in alphabet else x for x in JARGON])
		dec_match_score =  get_match_score(dec)
		#print('TEXT: {}'.format(dec))
		#print('Match Score: {}'.format(dec_match_score))
		#print('-'*30)

		
		all_dec.append((dec_match_score, dec))
		#if dec_match_score > SCORE_LIMIT:
			#print('Found posibilities correct Text: ')
		#	posibilities.append(dec)

	print('-'*30)
	posibiliity = max(all_dec)		
	# print the posibiliites
	#for posibiliity in posibilities:
	print('Result: {}'.format(posibiliity[1]))

