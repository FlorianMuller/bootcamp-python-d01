from dataclasses import dataclass


@dataclass
class GotCharacter():
    first_name: str
    is_alive: bool = True


@dataclass
class Lannister(GotCharacter):
    """A class representing a member of the Lannister family"""
    family_name: str = None
    house_words: str = "Hear Me Roar!"

    def __post_init__(self):
        if not self.family_name:
            self.family_name = self.__class__.__name__

    def print_house_words(self):
        print(self.house_words)

    def be_cool(self):
        print("A Lannister always pay his debt")

    def die(self):
        self.is_alive = False


if __name__ == "__main__":    
    cersei = Lannister("Cersei")
    print(cersei.__dict__)

    cersei.print_house_words()

    cersei.die()
    print(cersei.is_alive)

    print(cersei.__doc__)
