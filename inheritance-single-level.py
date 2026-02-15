class Product:
    name = ""
    price = 0
    brand = "" 
    warranty = 0 


    def display(self):
        print("Parent class name " , self.name, "price", self.price, "brand" ,self.brand)
    def calc_price(self):
        total_price = self.price * self.count 
        print("parent class calcprice method total price: ",total_price)
         



class Electronics(Product):
    type = "Electronics"
    count = 10


    def displayAlldetails(self):
        #to call a parent class method use super keyward
        super().display()
        super().calc_price()
        print("--------------")
        print("name:", self.name , "price:" , self.price , "brand:" , self.brand ,"warranty :", self.warranty , "type:" , self.type , "count:" , self.count)


prod = Electronics()
prod.name = "TV"
prod.price = 30000
prod.branch = "sony"
prod.warranty = 3 
#prod.type = "ELECTRONICS"
prod.displayAlldetails();
