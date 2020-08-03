''' 
Word Analizer
=====================

Analize Words
------------------------------
Analizes words from sentence. It Tokenize them and also get 
the :meth:`word meaning`

Example:
-----------------------
	>>>> How old are you?
	['event', 'age', 'self']

	>>>> What is your name?
	['event', 'self', 'name']

	>>>> I am back
	['user', 'back']

How to use:
-------------------
>>>> from WordMeaning import get_meaning`
>>>> text = ["hello", "there"]`
>>>> print(get_meaning(text))`
'''