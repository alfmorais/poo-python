from datetime import datetime


class Person:
    def __init__(self, name, age, eating=False, speaking=False) -> None:
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_borned_year(self):
        actual_year = int(datetime.now().year)
        return actual_year - self.age

    def start_to_eat(self, food: str):
        if self.eating:
            print(f'The {self.name} are eating...')
            return

        if self.eating:
            print("Can not eating while speaking...")
            return

        print(f'The {self.name} start to eat pizza.')
        self.eating = True

    def stop_to_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return

        print(f'{self.name} stop to eat...')
        self.eating = False

    def speak(self, subject: str):
        if self.eating:
            print(f'{self.name} can not speaking while eating...')
            return

        if self.speaking:
            print(f'{self.name} is speaking...')
            return

        print(f'{self.name} start to speak about {subject}.')
        self.speaking = True

    def stop_to_speak(self):
        if not self.speaking:
            print(f'{self.name} is not speak.')
            return

        print(f'{self.name} stop to speak.')
        self.speaking = False
