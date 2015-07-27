from encoding import EncoderI
from magic_square import make_magic_square


class MagicEncoder(EncoderI):


    def set_key(self, key):
        self.square = key

    def encode(self, message):
        return None


if __name__ == "__main__":
    encoder = MagicEncoder()
    n = 5
    key = make_magic_square(n)
    message = 'Hello, world!'
    cipher = encoder.encode(message)
    print(cipher)