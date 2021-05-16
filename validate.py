class Validate:   
    def range(self, min_num, max_num, error, question):
        user_input = self.int(question, error)
        while user_input > max_num or user_input < min_num:
            print(error)
            user_input = self.int(question, error)
        return user_input

