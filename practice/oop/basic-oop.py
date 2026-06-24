class Animal:
    def __init__(self, name: str, age: int, typee: str):
        self._name = name
        self._age = age
        self._type = typee
        
    def speak(self, statement: str) -> None:
        print(statement)

    def print_details(self) -> None:
        print(f"Name: {self._name}\nAge: {self._age}\nType: {self._type}")
        
def main():
    animal = Animal("Inu", 7, "Dog")
    animal.print_details()

if __name__ == "__main__":
    main()
