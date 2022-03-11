class Dogs:
    def myDog(self):
        print('Dog name is {}'.format(self.name))
        print('Dog fur present  {}'.format(self.furs))
        print('Dog gender is {}'.format(self.gender))

    
    @staticmethod
    def greetDog():
        print('good dog')

rancho = Dogs()
rancho.name = 'rancho'
rancho.breed = 'lab'
rancho.furs = 'yes'
rancho.legs = 4
rancho.gender = 'male'
rancho.food = 'drools'
rancho.myDog() # Dogs.myDog(rancho)
rancho.greetDog()
# by using self we can access the methods of attibutes and class 