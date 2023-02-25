# CMD app for morse code decryption and encryption

#### Video Demo:  <URL HERE>
#### Description:
This is a command line app to decrypt and encrypt morse code with an added morse code guessing game.

Use `-h` or `--help` in the command line for more info on how to use the app, there will still be a detailed explanation below


### The decoding function
---
Purpose: Decodes a string of morse code
Usage: Make sure to separate each letter with spaces and each word with a "/" refer to the example below

Prefix: `-d` or `--decode`

Args: One or multiple morse code letters

Example use:

    -d ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

Output:

     hello world

### The encrypting function
---
Purpose: Encrypt a string in morse code
Usage: Make sure to separate each word with a space and only use supported characters.

Supported characters: "A":".-",
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
    "Ü":"..--"

Prefix: `-e` or `--encrypt`

Args: One or multiple characters aka a sentence

Example use:

    -e "Hello world"

Output:

    .... . .-.. .-.. --- / .-- --- .-. .-.. -..


### The play command
---
Purpose: Gives u a random english string (determined by the difficulty function see blow) for you to encrypt in morse code in a set amount of attempts

Prefix: `-p` or `--play`

Args: `s` or `start`

Example use:

    -p start

Output:

    You have 3 guess(es)
    Encrypt the following: X


### The difficulty function
---
Purpose: Sets the difficulty of your game(see fucntion above)

Prefix: `-pd` or `--playdifficulty`

Args: `easy`, `medium` or `hard`

- Easy: Only generates letters with 3 guesses
- Medium: Only generates words with 10 guesses
- Hard: Only generates 4 letter sentences with 40 guesses

Example use:

        -p start -pd medium

Output:
        
        You have 10 guess(es)
        Encrypt the following: House
