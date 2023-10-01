import random

RULES = """RULES:
Each time you get the turn you roll the dice.
If you get 1 it adds to your total score and you finish the turn.
If not you can choose to either roll the dice again or end your turn.
If you choose to roll the dice each time you didn't get 1 \
    the number you got is added to your current score, \
    but if you will get 1 your current score will be set to 1 and you will finish your turn.
After you finish your turn, the score you got will be added to your total score.
The first player to get 50 points wins.
GOOD LUCK!!!
"""
def roll_the_dice() -> int:
    return random.randint(1, 6)

class Score:
    __total_score = None
    __current_score = None

    def __init__(self) -> None:
        self.__total_score = 0
        self.__current_score = 0
    
    def add_to_current(self, score : int) -> None:
        self.__current_score += score

    def set_current(self, value : int):
        self.__current_score = value
    
    def add_to_total(self) -> None:
        self.__total_score += self.__current_score
        self.__current_score = 0
    
    def get_current(self) -> int:
        return self.__current_score
    
    def get_total(self) -> int:
        return self.__total_score

class Entity:
    _score = None
    _name = None

    def __init__(self, name = "bot") -> None:
        self._score = Score()
        self._name = name
    
    def take_turn(self):
        pass

    def get_score(self) -> bool:
        return self._score.get_total()
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name) -> None:
        self._name = name

class Player(Entity):
    def take_turn(self):
        while True:
            score = roll_the_dice()
            print("You rolled", score)

            self._score.add_to_current(score)
            print("Your current score is", self._score.get_current())

            if score == 1:
                self._score.set_current(1)
                break

            if self.__get_player_responce() == False:
                break
        
        print("Your turn has ended")
        self._score.add_to_total()
        print("Now your total score is", self._score.get_total())
        print("-" * 15)
    
    def __get_player_responce(self) -> bool:
        while True:
            responce = input("Roll again? y / n: ")
            if responce == "y":
                return True
            elif responce == "n":
                return False
            else:
                print("Wrong input!")

class Bot(Entity):
    def take_turn(self):
        self._score.add_to_current(roll_the_dice())
        self._score.add_to_total()
        print(self.get_name() + " has " + str(self.get_score()) + " points")
        print("+" * 15)

class Game:
    __player = None
    __bots = None
    __winScore = None

    def __init__(self) -> None:
        self.__player = Player()
        self.__bots = [Bot(name="Bot" + str(i)) for i in range(3)]
        self.__winScore = 50

    def start(self) -> None:
        self.__player.set_name(input("Enter your name: "))
        print("Hello", self.__player.get_name(), "and welcome the PIG game!")
        print(RULES)
        self.__update()

    def __update(self) -> None:
        while True:
            self.__player.take_turn()
            if self.__player.get_score() >= self.__winScore:
                print("Player '" + self.__player.get_name() + "' won")
                return

            for bot in self.__bots:
                bot.take_turn()
                if bot.get_score() >= self.__winScore:
                    print("Bot '" + bot.get_name() + "' won")
                    return
                
def pig():
    game = Game()
    game.start()

pig()