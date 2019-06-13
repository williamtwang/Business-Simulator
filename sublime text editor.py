#outline for pricing simulator:

#elements: price, cash, location(higher rent but more customers), tips, inventory, 
#ads/sponsorship ads, popularity(more customers), maintenance, revenue, profit, show info

#random evets where your supplier goes down and u have to lose or pay money
#continuously moving

#input("Where do you want your business located? \n downtown (rent: $1000 /month) \n suburbs (rent: $650 /month) \n middle of nowhere (rent: $250 /month)"
import keyboard
import pygame as pg
import random 
#global starting variables


#based o location, price, qualtiy, popularity
#ratio: price and quality, if bad quality less populairty
#after every 5 seconds, print the data about the day: how many units sold, 
#popularity, inventory,  


#location has 3 multiplyers, downtown is 7, suburbs is 1.3, nowhere is 1
#price and quality ratio (10,5,1): 
# if self.supplier == 10:
#     if self.location == " middle of nowhere (rent: $8 /day)":
#         if self.unitPrice/self.supplier > 10:
#    selif self.location

# random integer (baseed on location) greatest to lease


    

#popularity if more than 5 customers, add .1 to the number as a multiplyer
#for every customer if tey are happuy



class Game():
    '''
        This makes a game
    '''

    def __init__(self):
        self.mult = 0
        self.clock = pg.time.Clock()
        self.cost = 0
        self.day = 0
        self.cash = 100
        self.popularity = 1
        self.revenue = 0
        self.unitPrice = 0
        self.numUnits = 0
        self.location = 0
        self.locationCustomers = [[0,3], [2,5], [4,7]]
        self.numCustomers = 0
        self.totalRevenue = 0
        self.prev = 0 
        self.rent = [5,10,15]


    def customers(self):
        if self.unitPrice/self.cost <= 1:
            self.mult = 2.5
            self.popularity += 2
        elif self.unitPrice/self.cost <= 1.5:
            self.mult = 1.8
            self.popularity += .6
        elif self.unitPrice/self.cost <= 2:
            self.mult = 1.4
            self.popularity += .3
        elif self.unitPrice/self.cost <= 2.5:
            self.mult = 1.2
            self.popularity += .2
        elif self.unitPrice/self.cost <= 3:
            self.mult = 1.1
            self.popularity += .1
        elif self.unitPrice/self.cost <= 3.5:
            self.mult = 1
            self.popularity -= .3
        elif self.unitPrice/self.cost <= 4:
            self.mult = 1
            self.popularity -= .6
        elif self.unitPrice/self.cost <= 5:
            self.mult = .9
            self.popularity -= 1
        elif self.unitPrice/self.cost > 5:
            self.mult = .7
            self.popularity -= 2

    def dailyCustomers(self):
        if self.popularity <= 0:
            self.popularity = 1
        self.numCustomers = round(random.randrange((self.locationCustomers[self.location])[0], (self.locationCustomers[self.location])[1])*self.mult*self.popularity)

    def dailyRevenue(self):
        
        if self.numUnits >= self.numCustomers and not (self.numUnits == 0):
            self.revenue = self.numCustomers*self.unitPrice
            self.numUnits -= self.numCustomers
        elif self.prev < self.numCustomers:
            self.popularity -= 1
            self.revenue = self.numUnits*self.unitPrice

            #self.numUnits = 0

        self.cash += self.revenue
        self.totalRevenue += self.revenue
        self.cash -= self.rent[0]

    #def checkIn():
        #while not keyboard.is_pressed('CTRL'):
            #if keyboard.is_pressed('shift'):
                #while keyboard.is_pressed('shift'):
                    #noValue = 1
                #print('William is Gay')


    def startTimer(self):
    #check if keyboard is just pressed once
        while True:
            key = 0
            while (key == 0):
               # try:
                if keyboard.is_pressed('CTRL'):
                    while keyboard.is_pressed('CTRL'):
                        noValue = 1
                    key = 1
                    #checkIn()
                    self.day +=1            
                elif keyboard.is_pressed('SHIFT'):
                    while keyboard.is_pressed('SHIFT'):
                        noValue = 1
                    key = 1
                    self.start()
                    #checkIn()
                
                
                # print(key)
                
                    #changeSettings()
            
                    #self.settings()
            self.prev = self.numUnits
            self.showData()

        
        
                
            

            


    def checkInput(self, input, values):
        for value in values:
            if input == value:
                return True
        return False

    def askSupplier(self):
        supplier = 0
        while supplier != "premium" and supplier != "normal" and supplier != "cheap":
        #while checkInput(supplier, ["premium", "normal", "cheap"]):
            supplier = input("Choose a supplier:\npremium ($10)\nnormal ($5)\ncheap ($1)\nanswer: ")
            print(supplier)
        if supplier == "premium":
            self.cost = 10
        elif supplier == 'normal':
            self.cost = 5
        else:
            self.cost = 1

        #based on quality, increases popularity uses ratio
    def asknumUnits(self):
        self.numUnits = -1
        while self.numUnits == -1 or self.numUnits * self.cost > self.cash:
            self.numUnits = int(input("How many units would you like to purchase?\nanswer:"))
            
            if self.numUnits * self.cost > self.cash:
                print("You do not have enough cash!")
                continue

            else:

                break
        self.cash -= self.numUnits*self.cost
        print("You have $" + str(self.cash) + " left")

        
    def showData(self):
        self.customers()
        self.dailyCustomers()
        self.dailyRevenue()
        print ("Day " + str(self.day) + ":")
        print ("Customers: " + str(self.numCustomers))
        print ("Units left: " + str(self.numUnits))
        print ("Daily revenue: " + str(self.revenue))
        print ("Total revenue: " + str(self.totalRevenue))
        print ("Cash: " + self.cash)
        if self.prev < self.numCustomers:
            print("You ran out of inventory and left " + str(self.numCustomers-self.prev) + " customers unhappy; popularity is decreased")
            print("Press SHIFT to update inventory")
            self.numUnits = 0
        
        #print ("Profit: " + str(self.revenue-self.numUnits*self.cost))

    #def changeSettings(self):
       # print("it worked bruh")
    





    #def settings(self):
        
        


    def askUnitPrice(self):
        self.unitPrice = int(input("What would you like your sale price to be?\nanswer:"))
        print("units: " + str(self.numUnits))
        print("price: $" + str(self.unitPrice))

    def start(self):
        self.askSupplier()
        self.asknumUnits()
        self.askUnitPrice()
        print("Press 'CTRL' to progress one day")
        self.startTimer()

    def main(self):
        print("The business simulator:\nstarting cash: 100")
        print ("Your current location is middle of nowhere (rent: $8 /day)")
        print("Press Shift to start")
        while True:  # making a loop
            try:
        # used try so that if user pressed other than the given key error will not be shown
                #if keyPressed("S"):
                if keyboard.is_pressed('shift'):
                    self.start()
                    break
                else:
                    pass
            except:
                break


if __name__ == "__main__":
    g = Game()
    g.main()



