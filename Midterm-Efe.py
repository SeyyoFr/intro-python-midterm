import random

class Game:
    def __init__(self):
        self.rooms = ["Green", "Yellow", "Red", "Blue", "White"]
        self.current_room = "Green" 
        self.exit_room = "White"

        

        self.room_directions = {
            "Yellow": {"north": "Blue", "south": "Red"},
            "Blue": {"south": "Yellow", "west": "White"},
            "Red": {"north": "Yellow", "west": "Green"},
            "Green": {"east": "Red", "south": "White"},
            "White": {"east": "Blue", "north": "Green"}
        }
        
        self.gold_box_room = ""
        self.silver_box_room = ""
        self.key_box = ""
        self.dragon_room = ""

        self.gold_box_open = False
        self.silver_box_open = False
        self.box_opened = False

        self.has_key = False
        self.exit_unlocked = False
        self.game_over = False

        self.dragon_question_asked = False
        self.dragon_answer_wrong = False

        self.setup_game()

    def setup_game(self):        
        self.gold_box_room = random.choice(self.rooms)
        self.silver_box_room = random.choice(self.rooms)

        while self.silver_box_room == self.gold_box_room:
            self.silver_box_room = random.choice(self.rooms)

        self.key_box = random.choice(["gold", "silver"])
        self.dragon_room = random.choice(self.rooms)

       
    def move(self,direction):
        if direction in self.room_directions[self.current_room]:
            self.current_room = self.room_directions[self.current_room][direction]
        else:
            print("You cannot go that way dude!!")    

    def describe_room(self):
        text = "You are in the " + self.current_room + " room."

        directions = self.room_directions[self.current_room]
        door_list = []

        for direction in directions:
            door_list.append(direction.capitalize())

        for i in range(len(door_list)):
            if i == 0:
                text += " There is a door " + door_list[i]    
            else:
                text += " and a door " + door_list[i]
        
        if self.current_room == self.gold_box_room:
            text += ". There is a gold box here."
        if self.current_room == self.silver_box_room:
            text += ". There is a silver box here." 
        if self.current_room == self.dragon_room:
            text += " There is a dragon here."
        if self.current_room == self.exit_room:
            text += ". There is an EXIT here." 
            if self.exit_unlocked:
                text += " EXIT is unlocked."
            else:
                text += " EXIT is locked."
        print(text)

    def open_box(self):
        if self.current_room == self.gold_box_room:
            if self.box_opened:
                print("You have already opened a box.")
                return
            print("Gold box is open")
            self.gold_box_open = True
            self.box_opened = True
           
            if self.key_box !="gold":
                print("Wrong box. You lose the game.")
                self.game_over = True
                
        elif self.current_room == self.silver_box_room:
            if self.box_opened:
                print("A box was already opened")
                return
            print("Silver box is open")
            self.silver_box_open = True
            self.box_opened = True

            if self.key_box != "silver":
                print("Wrong box. You lose.")
                self.game_over = True
        else:
            print("There is no box here")

    def get_key(self):
        if self.gold_box_open and self.current_room == self.gold_box_room and self.key_box == "gold":
            self.has_key = True
            print("You have the EXIT key now")
        elif self.silver_box_open and self.current_room == self.silver_box_room and self.key_box == "silver":
            self.has_key = True
            print("You have the EXIT key now")
        else:
            print("There is no key here")

    def unlock_exit(self):
        if self.current_room != self.exit_room:
            print("There is no EXIT here")
        elif self.has_key:
            self.exit_unlocked = True
            print("The EXIT is unlocked now")
        else:
            print("You don't have the key, EXIT still locked")

    def exit_game(self):
        if self.current_room != self.exit_room:
            print("There is no EXIT here")
        elif self.exit_unlocked:
            print("Congratulations! You made it!")
            self.game_over = True
        else:
            print("EXIT is locked")


    def process_command(self, command):
        if command == "go north":
            self.move("north")
        elif command == "go south":
            self.move("south")
        elif command == "go east":
            self.move("east")
        elif command == "go west":
            self.move("west")
        elif command == "open box":
            self.open_box()
        elif command == "get key":
            self.get_key()
        elif command == "unlock exit":
            self.unlock_exit()
        elif command == "exit":
            self.exit_game()
        elif command == "where is the key":
            self.where_is_key()
        elif command == "ask me":
            self.ask_dragon()
        elif command == "gprok":
            self.answer_dragon("gprok")
        else:
            print("Invalid command")

    def where_is_key(self):
        if self.current_room != self.dragon_room:
            print("There is no dragon here")
        elif self.dragon_answer_wrong:
            print("Dragon will not answer anymore")
        else:
            print("Dragon says you need to answer a question to tell you where the key is.")

    def ask_dragon(self):
        if self.current_room != self.dragon_room:
            print("There is no dragon here")
        elif self.dragon_answer_wrong:
            print("Dragon will not answer anymore")
        else:
            print('Dragon asks "Who is the best proffesor in this university?"')
            self.dragon_question_asked = True

    def answer_dragon(self, answer):
        if self.current_room != self.dragon_room:
            print("There is no dragon here")
        elif self.dragon_answer_wrong:
            print("Dragon will not answer anymore")
        elif self.dragon_question_asked == False:
            print("Ask the dragon first")
        else:
            if answer == "gprok":   
                print("Dragon says correct, the key is in the " + self.key_box + " box.")
            else:
                print("Dragon says wrong answer")
                self.dragon_answer_wrong = True
game = Game()



while game.game_over == False:
    game.describe_room()
    command = input("USER: ").strip().lower()
    game.process_command(command)

