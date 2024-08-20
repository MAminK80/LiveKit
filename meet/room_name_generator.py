import string
import random


class RoomNameGenerator:
    def generate_name(self):
        def generate_random_string(length):
            letters = string.ascii_letters
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        return f'{generate_random_string(3)}--{generate_random_string(3)}--{generate_random_string(3)}'
