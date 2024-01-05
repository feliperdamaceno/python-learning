from dataclasses import dataclass
from string import ascii_lowercase


@dataclass
class Encoder:
    message: str = ""

    def __handle_enconding(self, message: str, shift: int, decode: bool = False):
        shift = -shift if decode else shift

        encoded_message = ""
        for character in message:
            if not character.isalpha():
                encoded_message += character
                continue

            encoded_shift = ascii_lowercase.find(character) + shift
            encoded_position = encoded_shift % len(ascii_lowercase)
            encoded_message += ascii_lowercase[encoded_position]

        self.message = encoded_message

    def encode(self, message: str, shift: int):
        self.__handle_enconding(message, shift)

    def decode(self, message: str, shift: int):
        self.__handle_enconding(message, shift, decode=True)
