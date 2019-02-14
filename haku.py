import re
import pprint

def regex_search(string, pattern):
	# Luodaan frekvenssi dictionary
	osumat = re.findall(pattern, string)
	frequency = {}
	for osuma in osumat:
		frequency[osuma] = frequency.setdefault(osuma, 0) + 1

	# frequency = {
	# 	'big':12,
	# 	'great':23,
	# 	' big':4,
	# 	..... jne
	# }

	lines = string.splitlines()
	# lines = re.split(r'(?<=\.) ', string)

	return frequency, lines	

def search_cli(string):
	pattern = input('Syötä RegEx kaava: \n')
	if not pattern:
		quit()

	frequency, lines = regex_search(string, pattern)
	hits = 0
	re_pattern = re.compile(pattern)
	for line in lines:
		if re_pattern.search(line):
			for hit in re_pattern.findall(line):
				if type(hit) == tuple:
					for group in hit:
						hits += 1
						line = line.replace(group, '\033[95m' + group + '\033[0m')
				else:
					hits += 1
					line = line.replace(hit, '\033[95m' + hit + '\033[0m')
			print("{}:  {}".format(hits, line))
	pp.pprint(sorted(frequency.items(), key=lambda t: t[1]))
	print("Summa: {}".format(sum(frequency.values())))
	print("Highlightatut matchit: {}".format(hits))
	print("Lauseitten kokonaismäärä: {}".format(len(lines)))
	print("Haettiin kaavalla '{}'".format(pattern))


if __name__ == "__main__":
	import readline
	import sys
	import os
	import atexit

	pp = pprint.PrettyPrinter(indent=4)

	# Tallennetaan haku-pattern historia.
	historyPath = os.path.expanduser('~/.haku_history')

	if os.path.exists(historyPath):
		readline.read_history_file(historyPath)

	def save_history():
		readline.write_history_file(historyPath)

	atexit.register(save_history)


	if len(sys.argv) != 2:
		print("Anna luettavan tiedoston nimi tai polku kansioon jonka sisältä olevista tiedostoista haluat etsiä esim: python3 haku.py dictionary.txt")
		quit()
	elif os.path.isfile(sys.argv[1]):
		# Jos annettu parametri on tiedosto:
		with open(sys.argv[1]) as f:
			search_cli(f.read())
	elif os.path.isdir(sys.argv[1]):
		# Jos annettu parametri on kansio, luetaan kaikki tiedostot ja yhdistetään ne yhdeksi merkkijonoksi
		# ennen haku funktioon syöttämistä
		texts = []
		for root, dirs, files in os.walk(sys.argv[1]):
			for file in files:
				with open(os.path.join(root, file)) as f:
					texts.append(f.read())
		search_cli(r'\n'.join(texts))
	else:
		print("Polkua '{}' ei löytynyt. Siirrä luettava tiedosto kotikansioon.".format(sys.argv[1]))
		quit()


