from misc import files, log

class Tokenizer:
	def __init__(self, sentence):
		self.Sentence = sentence.strip().lower()
		self.Temp_Tokens = self.Sentence.split()
		self.Tokens = list()
		self.Dict = files().open_file("words", "DICT")
		self.Dictionary = [words.strip() for words in open(self.Dict)]

	def Tokenize(self):
		''' Tokenizes a sentence into words '''
		# self.Tokens = self.Sentence.split()
		# return Tokens
		for words in self.Temp_Tokens:
			if "?" in words:
				j = words.replace("?", "")
			else:
				j = words

			self.Tokens.append(j)

	def Save_Words(self):
		newChanges = False
		if not len(self.Dictionary) == 0:
			for token in self.Tokens:
				# for word in self.Dictionary:
				if not token in self.Dictionary:
					self.Dictionary.append(token)	
					self.Dictionary.sort()
					print(log().info("New word ==> \33[34m{token}\33[0m", "Save_Words", "Tokenizer"))
					newChanges = True

			if newChanges:
				try:
					with open(self.Dict, "w") as file:
						for words in self.Dictionary:
							file.writelines(words + "\n")
					print(log().message("Dictionary Updated!", "save_words", "Tokenizer"))
					newChanges = False
				except Exception as e:
					print(log().error(e, "save words", "tokenizer"))
					newChanges = False
		else:
			print(log.warning("No data in dictonary..... Adding words from Sentence", "save_words", "tokenizer"))
			try:
				with open(self.Dict, "w") as file:
					for words in self.Tokens:
						file.writelines(words + "\n")
			except Exception as e:
				print(log.error("Error adding Tokens to Dictionary due to" + e, "save words", "tokenizer"))
