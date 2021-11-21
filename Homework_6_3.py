class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income ={"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return "{0} {1}".format(self.name, self.surname)
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

employ = Position ("Ivan", "Ivanov", "analyst", 100000, 50000)
print(employ.name)
print(employ.surname)
print(employ._income)
print(employ.get_full_name())
print(employ.get_total_income())