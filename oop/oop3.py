class Shop:
    city = 'Nagpur'

    def shopInfo(self):
        print('Shop category ',self.shop_cat)
        print('Shop city ',self.city)
        print('Shop owner ',self.owner)
        print('shop offers',self.offers)

parvati = Shop()
parvati.shop_cat = 'Fertilizers'
parvati.owner = 'Sunil'
parvati.offers = 'No'

parvati.shopInfo()