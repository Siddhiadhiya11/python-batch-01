class Dogs:
    def myDog(self):
        print('Dog name is {}'.format(self.name))
        print('Dog fur present  {}'.format(self.furs))
        print('Dog gender is {}'.format(self.gender))

rancho = Dogs()
rancho.name = 'rancho'
rancho.breed = 'lab'
rancho.furs = 'yes'
rancho.legs = 4
rancho.gender = 'male'
rancho.food = 'drools'
rancho.myDog() #Dogs.myDog(rancho)

# by using self we can access the methods of attibutes and class 