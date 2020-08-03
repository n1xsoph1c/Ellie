def get_reaction(text):
	if text == "JUST DO IT":
		print("What you want me to do?")
		task = input("Say: ")

		if task == "play music":
			print("What music you want me to play?")
			music = input("Name: ")

		if task == "Die":
			print("Why would I do that?")
			reason = input("why: ")
	
	else:
		print("Hmm okay")