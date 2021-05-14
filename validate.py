class Validate:
    def string(self, question, text):
        user_input = input(question)
        while user_input.isnumeric() or not user_input:
            print(text)
            user_input = input(question)
        return user_input
    def int(self, question, text):
        user_input = input(question)
        while not user_input.isnumeric():
            print(text)
            user_input = input(question)
        return int(user_input)
    def range(self, min_num, max_num, error, question):
        user_input = self.int(question, error)
        while user_input > max_num or user_input < min_num:
            print(error)
            user_input = self.int(question, error)
        return user_input

