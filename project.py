import argparse
from helper import MORSE_CODE_DICT, DIFFICULTY, DIFFICULTIES_DICT, wait

def main():
   parser = argparse.ArgumentParser(
       prog="Morse code translator",
       description="Decrypts and ecnrypts strings in morse code with an added morse code guessing game")
   parser.add_argument("-d", "--decode", help="Decodes a string of morse code into english, make sure letters are seperated by spaces and words by the '/' symbol")
   parser.add_argument("-e", "--encrypt", help="Encrypts a string in morse code, make sure words are seperated by spaces")
   parser.add_argument("-p", "--play", help="Stars a morse code game where you have to encrypt a string in morse code in a set amount of time, (Default difficulty is easy and score to win is 3 check -pd, --playdifficulty for more info))", choices=["start", "s"])
   parser.add_argument("-pd", "--playdifficulty", help=f"Sets the difficulty of play, Easy(Generates characters only, number of guesses {DIFFICULTIES_DICT['easy']['number_of_guesses']}), Medium(Generates words only, number of guesses {DIFFICULTIES_DICT['medium']['number_of_guesses']}), Hard(Generates sentences only, number of guesses {DIFFICULTIES_DICT['hard']['number_of_guesses']})", choices=DIFFICULTY, type=str)
   args = parser.parse_args()
   if args.decode:
      decoded_str , fully_decoded = decode(args.decode)
      cannot_fully_decode_error_msg = "Characters that are in between ** ** could not be decoded please check ur spelling and try again"
      if fully_decoded:
          print(decoded_str)
      else:
          print(f"{decoded_str}\n{cannot_fully_decode_error_msg}")
   if args.encrypt:
      encrypted_str, fully_encrypted = encrypt(args.encrypt)
      cannot_fully_encrypt_error_msg = "Characters that are in between ** ** could not be encrypted, make sure you are using characters that appear in the morse dictionary"
      if fully_encrypted:
          print(encrypted_str)
      else:
          print(f"{encrypted_str}\n{cannot_fully_encrypt_error_msg}")
   if args.play:
      difficulty = args.playdifficulty 
      result = play_morse_code_game(difficulty= difficulty if difficulty else "easy")
      if result:
          print("You win!")
      else:
          print("You lose :(")

fully_translated = True
"""Determines if the string has been fully translated"""
def decode_char(char: str) -> str:
   """Decodes a morse code character"""
   try:
      decoded_char = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(str(char))]
   except ValueError:
      fully_translated = False
      return f"**{char}**"
   else:
      global fully_translated
      fully_translated = True
      return decoded_char


def decode(s: str) -> tuple[str, bool]:
    """Decodes a string of morse code returns a tuple of the decoded string and if the string was fully decoded or not"""
    decoded_sentence = ""
    s : str = str(s).strip().split(" ")
    for char in s:
        # / is the seperator between words
        if "/" in char :
            # if there is only / in the sentence just add a space
            if char == "/":
                decoded_sentence = decoded_sentence + " "
                continue
            else:
                    # if char ends with / add the space after decoding and resume the loop
                    if str(char).endswith("/"):
                        char = str(char).replace("/","")
                        decoded_sentence = decoded_sentence + decode_char(char) + " "
                    # if it starts with / add the space before decoding and finish the loop
                    elif str(char).startswith("/"):
                        char = str(char).replace("/","")
                        decoded_sentence = decoded_sentence + " " + decode_char(char)
                    # otherwise it means that the word starts and ends with a / thus we need to add a space before and after the word and resume the loop
                    elif str(char).startswith("/") and str(char).endswith("/"):
                        char = str(char).replace("/", "")
                        decoded_sentence = " " + decoded_sentence + decode_char(char) + " "
                    # that means there is a / in between two words but in 1 list element which we will need to sperate and decode with a space
                    else:
                        char1, char2 = str(char).split("/")
                        decoded_sentence = decoded_sentence + decode_char(char1) + " " + decode_char(char2)
        else:
            # normal chars with no /
            decoded_sentence = decoded_sentence + decode_char(char)

    return decoded_sentence.strip(), fully_translated
        

fully_encrypted = True
"""Determins if the string has been fully encrypted"""
def encrypt_char(char:str) -> str:
   """Encrypts a character to morse code"""
   if len(str(char)) != 1:
       raise ValueError("Cannot encrypt more than one character")
   if char == " ":
      global fully_encrypted
      fully_encrypted = False
      return f"**{char}**"
   try:
      encrypted_char = MORSE_CODE_DICT[str(char).upper()]
   except KeyError:
      fully_encrypted = False
      return f"**{char}**"
   else:
      fully_encrypted = True
      return encrypted_char


def encrypt(s: str ) -> tuple[str, bool]:
   """Encrypts a string of morse code returns a tuple of the decoded string and if the string was fully encrypted or not"""
   encrypted_sentence = ""
   s = str(s).strip().split(" ")
   for index, word in enumerate(s):
      # only add / between words after encrypting the first word
      if index != 0:
         encrypted_sentence = encrypted_sentence + " / "
      encrypted_word = ""
      # encrypt each word
      for char in word:
         encrypted_word = encrypted_word + encrypt_char(char) + " "
      # concatenate each word the sentence
      encrypted_sentence = encrypted_sentence + encrypted_word
   return encrypted_sentence.strip(), fully_encrypted


def play_morse_code_game(difficulty: str) -> bool:
   """Starts a morse code guessing game"""
   num_of_guesses : int = 0
   try:
      max_num_of_guesses : int = DIFFICULTIES_DICT[difficulty]["number_of_guesses"]
   except KeyError:
       raise ValueError(f"Please choose one of these options as your difficulty {DIFFICULTY}")
   generated_guess = DIFFICULTIES_DICT[difficulty]["func"]()
   while num_of_guesses != max_num_of_guesses :
      print(f"You have {max_num_of_guesses - num_of_guesses} guess(es)")
      user_answer = input(f"Encrypt the following: {generated_guess}\n")
      if user_answer != generated_guess:
         print("Incorrect!\n")
         num_of_guesses = num_of_guesses + 1
      else:
         return True
   return False

if __name__ == "__main__":
   main()

