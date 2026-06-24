import random
import time

class GameEntity:
    def __init__(self):
        self._hp = 0
        self._fp = 0
        self._is_hostile = False
        self._type = None

    def display_details(self):
        pass

class Skeleton(GameEntity):
    def __init__(self):
        super().__init__()
        self._hp = 100
        self._fp = 0
        self._is_hostile = True
        self._type = "Skeleton"

        self._quiver_size = 50
        self._quiver = [random.randint(2, 50) for _ in range(self._quiver_size)]

    def shoot_arrow(self, e: GameEntity) -> int:

        if isinstance(e, Skeleton):
            return -1

        old_hp = e._hp

        quiver_idx = random.randint(0, len(self._quiver) - 1)
        arrow = self._quiver.pop(quiver_idx)

        e._hp -= arrow

        print(
            f"[SKELETON SHOT]\n"
            f"Old HP: {old_hp}\nNew HP: {e._hp}\n"
        )
        return 0


class Player(GameEntity):
    def __init__(self):
        super().__init__()
        self._hp = 150
        self._fp = 50
        self._is_hostile = False
        self._type = "Player"
        self._inventory = []
        self._max_hp = 150

    def heal(self, amount: int):
        if (self._hp + amount > self._max_hp):
            self.hp = self._max_hp
        else:
            self._hp += amount
        print(f"[PLAYER HEALED]")
        print(f"Player healed by {amount}. HP is now {self._hp}\n")

def main():
    skeleton1 = Skeleton()
    player = Player()

    while (True):
        turn = random.randint(1, 2)

        if turn == 1:
            skeleton1.shoot_arrow(player)
        else:
            player.heal(50)

        if player._hp <= 0 or len(skeleton1._quiver) <= 0:
            break

        time.sleep(1)
    
if __name__ == "__main__":
    main()
