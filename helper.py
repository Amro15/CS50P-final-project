from word_generator import generate_letter, generate_word, generate_sentence
import asyncio

MORSE_CODE_DICT : dict = { 
    "A":".-",
    "N":"-.",
	"B":"-...",
    "O":"---",	 
 	"C":"-.-.",
    "P":".--.",	 
 	"D":"-..",
    "Q":"--.-",	 
 	"E":".",
    "R":".-.",	 
 	"F":"..-.",
    "S":"...",	 
 	"G":"--.",
    "T":"-",	 
 	"H":"....",
    "U":"..-",	 
 	"I":"..",
    "V":"...-",	 
 	"J":".---",
    "W":".--",	 
 	"K":"-.-",
    "X":"-..-",	 
 	"L":".-..",
    "Y":"-.--",	 
 	"M":"--",
    "Z":"--..",
    "1":".----",
    "6":"-....",	 
 	"2":"..---",
    "7":"--...",	 
 	"3":"...--",
    "8":"---..",	 
 	"4":"....-",
    "9":"----.",	 
 	"5":".....",
    "0":"-----",
    " ":"/",
    "?":"..--..",
    ";":"-.-.-.",	 
 	":":"---...",
    "/":"-..-.",	 
 	"-":"-....-",
    "\'":".----.",	 
 	"\"":".-..-.",
    "(":"-.--.",
    ")":"-.--.-",	 
 	"=":"-...-",
    "+":".-.-.",	 
 	"*":"-..-",
    "@":".--.-.",
    "Á":".--.-",
    "Ä":".-.-", 
 	"É":"..-..",
    "Ñ":"--.--", 
 	"Ö":"---.",
    "Ü":"..--" }	
"""Stores morse code represenations of characters with characters being the keys and the morese code being the values"""

DIFFICULTY : list = ["easy", "medium", "hard"]
"""Stores the available difficulties to choose form"""

DIFFICULTIES_DICT : dict = {"easy" : {"func": generate_letter, "number_of_guesses": 3}, "medium": {"func" : generate_word, "number_of_guesses" : 10}, "hard": {"func" : generate_sentence, "number_of_guesses" : 40}}
"""Stores the function used  to generate the guess and the number of guesss for every difficulty"""

async def wait(delay: int ) -> None:
    """Waits the passed amount in seconds"""
    await asyncio.sleep(delay)