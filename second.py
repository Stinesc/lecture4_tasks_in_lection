LEN_OF_EN_ALPH = 26
class Text:

    def __init__(self, text):
        self.text = text

    def find_bias_str(self, bias=1):
        result_string = ''
        words_list = self.text.replace('.', '').replace(',', '').split()
        for word in words_list:
            bias_str = ''
            for char in word:
                new_char = chr(ord(char) + bias)
                bias_str += new_char if 'z' >= new_char else chr(ord(new_char) - LEN_OF_EN_ALPH)
            result_string = f'{result_string} {bias_str}'
        return result_string

if __name__ == "__main__":

    text = Text("zzz")

    print(text.find_bias_str(3))