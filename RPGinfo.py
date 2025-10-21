class RPGInfo():
    author = "Georgia Cadman" # class varible

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self): # instance menthod
        print("Welcome to Grommet Cup")
        print("Cold sweat runs down your back, you can hear your own pants. As your eyes open you awake in a room that isn't quite yours but your all to familiar with the sights. " \
        "It's been months since you left the comfort of the worn bed sheets atop you, months since you had changed from the clothes one your- wait- hold on, where is my jacket you think to your self. " \
        "Your eyes dart around the room, not here, strange, youve never left to explore the unfamiliar home you sleep in, who couldve taken it...")
        print("Nows not the time to ponder the what ifs, you need that jacket, its the last thing your last reminder of them. You rise from the warm sheets with on goal in mind, find it.")
    

    @staticmethod
    def info():
        print('made by using the OPP RPG Game Creator - Georgia Cadman')

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"Created by {cls.author}")