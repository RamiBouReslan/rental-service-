class Vehicle:

    def __init__ (self, brand, model, year, dailyRental):
        self.brand = brand
        self.model = model 
        self.year = year
        self.__dailyRental= dailyRental

    def getDailyRental(self):
        return self.__dailyRental

    def setDailyRental(self, price):
        if price > 0:
            self.__dailyRental = price
        else:
            return ("Daily rental price must be positive")
  

    def displayInfo(self,category):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__dailyRental}/day.")
        
class RentalCost(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, numberOfDays):
        super().__init__ (brand, model, year, dailyRental)
        self.days = numberOfDays
        self.rentalcost = 0
    
    def calculateRent(self):
        self.rentalCost = self.getDailyRental()*self.days
        return self.rentalCost
    
    def displayInfo(self, category):
        print (f"Rental cost for {self.brand} {self.model} for {self.days} days: $ {self.rentalCost}")
        
class SeatCapacity(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, numberOfSeats):
        super().__init__ (brand, model, year, dailyRental)
        self.seats = numberOfSeats

    def displayInfo(self,category):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seats}, Rental Price: ${int(self.getDailyRental())}/day.")

class EngineCapacity(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, enginePower):
        super().__init__ (brand, model, year, dailyRental)
        self.engine = enginePower

    def displayInfo(self,category):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine}cc, Rental Price: ${int(self.getDailyRental())}/day.")


# Funtions to input and manipulate data


def transportation (category):

    vehicleDetails = Vehicle(input(f"Enter {category} brand : ").capitalize() ,
                             input(f"Enter {category} model: ").capitalize() ,
                             int(input(f"Enter {category} year: ")),
                             float(input(f"Enter {category} daily rental price: $")))
    
    return vehicleDetails

def rentalPrice(vehicleDetails,category):
        
    numberOfDays = int(input(f"Enter the number of days you wish to rent the {category} for: "))

    rental = RentalCost(vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        numberOfDays)
    return rental


def ifCar(vehicleDetails,category):
    
    numberOfSeats = int(input(f"Enter the number of seats for the {category}: "))

    newVehicledetails = SeatCapacity (vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        numberOfSeats)

    return newVehicledetails

def ifBike(vehicleDetails,category):
    
    enginePower = int(input(f"Enter the engine power for the {category}in 'cc': "))

    newVehicleDetails = EngineCapacity(vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        enginePower) 

    return newVehicleDetails

def updatedPrice(rental):
 
    updatedRentalPrice = float(input(f"Enter updated daily rental price: $"))
    
    rental.setDailyRental(updatedRentalPrice)
    
    return rental.getDailyRental()



                                            #  The Program Starts Here  #

vehicleList = []

action = input("Do you wish to enter vehicle details? (Yes or No): ").capitalize()


while action == "Yes":
    
    category = input ("Enter the vehicle type (Car or Bike): ").capitalize()
    
    vehicleDetails = transportation(category) 
    
    categories = { 
        "Type" : category
    }
    
    if category == "Car":
            newVehicleDetails = ifCar(vehicleDetails,category) 

    elif category == "Bike":
            newVehicleDetails = ifBike(vehicleDetails,category)
       
    
    rental = rentalPrice(vehicleDetails,category)
    rental.calculateRent()
    categories["Details"] = newVehicleDetails
    categories["Rental"] = rental
        
    vehicleList.append(categories)

    action = input("Do you wish to add new vehicle details? (Yes or No): ").capitalize()

update = input("Do you wish to edit a price? (Yes or No): ").capitalize()

newPrice = {}
updatedList= []
while update == "Yes":
    
    updatedVehicleBrand = input(f"Enter the vehicle brand you wish update: ").capitalize()
    updatedVehicleModel = input(f"Enter the vehicle brand you wish update: ").capitalize()
    for categories in vehicleList:
        
        updatedBrand = categories["Details"]
        
        if updatedVehicleBrand == updatedBrand.brand and updatedVehicleModel == updatedBrand.model:
            newPrice = {
                "Brand" : updatedBrand.brand , 
                "Model" : updatedBrand.model ,
                "Updated Price" : updatedPrice(categories['Rental'])}
            
            updatedList.append(newPrice)

    update = input("Do you wish to edit a price? (Yes or No)").capitalize()
   


print ("<===========================================================================>\n")
for categories in vehicleList:
    
    vehicleData = categories["Details"]
    vehicleData.displayInfo(categories["Type"])

print ("\n" )

for categories in vehicleList:

    rental = categories["Rental"]
    rental.displayInfo(categories["Type"])

print ('\n')

for index in updatedList:
        print(f"The Updated rental price for {index['Brand']} {index['Model']} is ${index['Updated Price']}.")

print ("\n<===========================================================================>")   

   
