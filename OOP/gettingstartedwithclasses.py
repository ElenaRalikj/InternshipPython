#item1='Phone'
#item1_price=100
#item1_quantity=5
#item1_price_total=item1_price*item1_quantity

#print(type(item1)) #str
#print(type(item1_price)) #int
#print(type(item1_quantity)) #int
#print(type(item1_price_total)) #int

class Item:
    pay_rate=0.8 #The pay rate after 20% discount
    all=[]
    def __init__(self,name:str,price:float,quantity=0):#putting name here as a parameter allows us to assign the attribute name dinamically
       #by passing quantity=0, it's already taking this parameter as an integer
       #print(f'An instance created: {name}, {price}, {quantity}')

       #Run validations to the received arguments
       assert price >= 0,f"Price {price} is not greater than or equal to zero!"
       assert quantity >= 0,f"Quantity{quantity} is not greater than or equal to zero!"
       #Assign to self object
       self.name=name #this allows us to assign the attributes dinamically
       self.price=price
       self.quantity=quantity

       #Actions to execute
       Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price=self.price*self.pay_rate#we can either access pay_rate from the class level or the instance level so we are accessing it just like this


item1=Item('Phone',100,1)
item2=Item('Laptop',1000,3)
item3=Item('Cable',10,5)
item4=Item('Mouse',50,5)
item5=Item('Keyboard',75,5)

print(Item.all)


# item1=Item('Phone',100,1)#reading from Item level (0.8)
# item1.apply_discount()
# print(item1.price)
#random_str=str('4')
#item1.name='Phone'
#item1.price=100
#item1.quantity=5
#print(item1.calculate_total_price(item1.price,item1.quantity))#item1 is passed as an argument in self from the method

# item2=Item('Laptop',1000,3)
# item2.pay_rate=0.7#gonna take it from instance level
# item2.apply_discount()
# print(item2.price)

#item2.name='Laptop'
#item2.price=1000
#item2.quantity=3
#print(item2.calculate_total_price(item2.price,item2.quantity))#item1 is passed as an argument in self from the method


#print(type(item1)) #item
#print(type(item1.name)) #str
#print(type(item1.price)) #int
#print(type(item1.quantity)) #int

#random_str='aaa'
#print(random_str.upper())

#print(item1.name,item1.price,item1.quantity)
#print(item2.name,item2.price,item2.quantity)

#item2.has_numpad=False
#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#print(Item.pay_rate)
#print(item1.pay_rate)#cant find the pay rate attribute on the instance level so it went on class level and found it there
#print(item2.pay_rate)# -||-

#print(Item.__dict__)#All the attributes for Class level
#print(item1.__dict__)#All the attributes for instance level