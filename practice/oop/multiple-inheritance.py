# === CASE 1: CHAINED INHERITANCE ===

class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_values(self):
        print(f"a: {self.a}\nb: {self.b}")

class Y(X): 
    def __init__(self, a, b, c):
        # We don't need to assign what we listed in the main __init__() for this linear case
        super().__init__(a, b)
        self.c = c

    def print_values(self):
        print(f"a: {self.a}\nb: {self.b}\nc: {self.c}")

class Z(Y):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def print_values(self):
        print(f"a: {self.a}\nb: {self.b}\nc: {self.c}\nd: {self.d}")

# === CASE 2: MULTIPLE INHERITANCE === 

""" 
    How this whole thing works:
    
    ----Zombie----
    |            |
    v            v
  Enemy      GameEntity

  Python does not treat these two classes simultaneously; instead, it forms an MRO chain

  Zombie -> GameEntity -> Enemy -> Object

  Zombie will call super().__init__() with all the arguments it needs

  GameEntity will then call super().__init__() with **kwargs so that it catches all the elements it needs 
  and then throws the rest to Enemy

  Enemy will catch the remianing elements and call its __init__() function

  So now all the relevant __init__() functions are called and Zombie receives what it needed
"""

class GameEntity:
    def __init__(self, hp: int, fp: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self._hp = hp 
        self._fp = fp

    def show_stats(self):
        print("~ENTITY STATS~\n")
        print(f"HP: {self._hp}\nFP: {self._fp}\n")

class Enemy:
    def __init__(self, dp: int, enraged: bool = False) -> None:
        self._dp = dp
        self._enraged = enraged

    def enemy_function(self):
        print("Hello I am an enemy")

class Zombie(GameEntity, Enemy):
    def __init__(self, hp, fp, dp, enraged):
        # Make sure to assign what you listed in the main __init__()
        super().__init__(hp=hp, fp=fp, dp=dp, enraged=enraged)

    def print_stats(self) -> None:
        print(f"HP: {self._hp}\nFP: {self._fp}\nDP: {self._dp}\nEnraged: {'Yes' if self._enraged == True else 'No'}\n")

    def enemy_function(self):
        # This goes down the MRO chain to find a class which has the enemy_function defined (i.e. Enemy in this case)
        super().enemy_function()
        print("Hello I am a zombie!")

def main():
    print("===== CASE 1 =====\n")
    x = X(20, 40)
    y = Y(50, 70, 90)
    z = Z(110, 130, 150, 170)

    arr = [x, y, z]

    for a in arr:
        a.print_values()
        print()

    print("===== CASE 2 =====\n")

    z = Zombie(100, 100, 200, True)
    z.print_stats()
    z.enemy_function()

main()

