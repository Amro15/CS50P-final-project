import pytest
from project import decode_char, decode, encrypt_char, encrypt, play_morse_code_game

def test_decode_char_with_integer():
    assert decode_char(1) == "**1**"

def test_decode_char_with_string():
    assert decode_char("hello world") == "**hello world**" 

def test_decode_char_with_space():
    assert decode_char(" ") == "** **"

def test_decode_char_with_one_morse_code_letter():
    assert decode_char(".----") == "1"
    assert decode_char(".-") == "A"

def test_decode_char_with_multiple_morse_code_letters():
    assert decode_char(".- .---") == "**.- .---**"

def test_decode_with_letter_space_slash_space_letter():
    assert decode(".- / .-") == ("A A", True)

def test_decode_with_letter_slash_space_letter():
    assert decode(".-/ .-") == ("A A", True)

def test_decode_with_letter_space_slash_letter():
    assert decode(".- /.-") == ("A A", True)

def test_decode_with_letter_slash_letter():
    assert decode(".-/.-") == ("A A", True)

def test_decode_with_spaces_letter_slash_letter_spaces():
    assert decode("   .-/.-     ") == ("A A", True)

def test_decode_with_partial_decode():
    assert decode(".-/foo") == ("A **foo**", False)

def test_decode_with_failed_decode():
    assert decode("foo") == ("**foo**", False)

def test_encrypt_char_with_integer():
    assert encrypt_char(1) == ".----"

def test_encrypt_char_with_character():
    assert encrypt_char("A") == ".-"

def test_encrypt_char_with_string():
    with pytest.raises(ValueError):
        encrypt_char("A B")

def test_encrypt_char_with_space():
    assert encrypt_char(" ") == "** **"
    
def test_encrypt_with_no_spaces():
    assert encrypt("helloworld") == (".... . .-.. .-.. --- .-- --- .-. .-.. -..", True)

def test_encrypt_with_spaces():
    assert encrypt("hello world") == ('.... . .-.. .-.. ---  / .-- --- .-. .-.. -..', True)

def test_encrypt_with_partial_fail():
    assert encrypt("hello.") == ('.... . .-.. .-.. --- **.**', False)

def test_encrypt_with_full_fail():
    assert encrypt(".") == ("**.**", False)

def test_play_morse_code_game_random_difficulty():
    with pytest.raises(ValueError):
        play_morse_code_game("normal")
