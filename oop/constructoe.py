class Cricket:
    def __init__(self, board, country, captain):
        self.board = board
        self.country = country
        self.captain = captain
        print('i am inside constructor')
    
    def teamInfo(self):
        print("country of team is {}".format(self.country))
        print("board of team is {}".format(self.board))
        print("captain of team is {}".format(self.captain))

obj = Cricket("Bcci","India","Virat")
#obj = Cricket()
obj.board = 'bcci'
obj.teamInfo()