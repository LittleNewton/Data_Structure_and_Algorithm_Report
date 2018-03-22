# 5.5.3 Simple Cryptography

class CaesarCipher:
    def __init__(self,shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
            # shift is the step you set for the code
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    def encrypt(self,message):
        return self._transform(message,self._forward)
    def decrypt(self,secret):
        return self._transform(secret,self._backward)
    def _transform(self,original,code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)
if __name__ == '__main__':
    cipher = CaesarCipher(5)
    message = input('Please input:\n')
    forward = cipher.encrypt(message)
    print('forward:',forward)
    backward = cipher.decrypt(message)
    print('backward:',backward)