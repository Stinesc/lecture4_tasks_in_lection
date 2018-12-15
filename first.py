class Text:

    def __init__(self, text):
        self.text = text.lower()

    def find_most_popular(self):
        word_dict = dict()
        words_list = self.text.replace('.', '').replace(',', '').split()
        for word in words_list:
            word_dict[word] = word_dict.get(word, 0) + 1
        most_popular_word_count = max(word_dict.values())
        for word in word_dict.keys():
            if word_dict.get(word) is not None:
                return most_popular_word_count, word


if __name__ == "__main__":

    text = Text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the \
             industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and \
             scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into\
             electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release \
             of Letraset ' sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus ' \
            'PageMaker including versions of Lorem Ipsum.")

    print(text.find_most_popular())