class Text:

    def __init__(self, text):
        self.__text = text

    def len(self):
        return len(self.__text)

    def count_letter(self):
        count = 0
        for i in self.__text:
            if i.isalpha():
                count += 1
        return count

    def count_space(self):
        count = 0
        for i in self.__text:
            if i == " ":
                count += 1
        return count

    def len_no_space(self):
        count = 0
        for i in self.__text:
            if i != " ":
                count += 1
        return count

    def massive_word(self):
        self.__massive = self.__text.split()
        return self.__massive

    def massive_sentece(self):
        self.__massive = self.__text.split(".")
        return self.__massive