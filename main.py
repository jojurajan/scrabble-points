from scrabble import Scrabble

word = ''
while word != 'exit':
	word = raw_input('Enter word : ')
	print Scrabble().getValue(word)