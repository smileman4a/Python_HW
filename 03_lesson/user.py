class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.l_name = last_name

    def print_first_name(self):
        print(f"Имя: {self.name}")

    def print_last_name(self):
        print(f"Фамилия: {self.l_name}")

    def print_full_name(self):
        print(f"Имя и фамилия: {self.name} {self.l_name}")
