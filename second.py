class Text:

    def __init__(self, text):
        self.text = text

    def find_bias_str(self, bias=1):
        result_string = ''
        words_list = self.text.replace('.', '').replace(',', '').split()
        for word in words_list:
            bias_str = ''
            for char in word:
                bias_str += chr(ord(char) + bias)
            result_string = f'{result_string} {bias_str}'
        return result_string

if __name__ == "__main__":

    text = Text("zzz")

    print(text.find_bias_str())