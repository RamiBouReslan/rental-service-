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
  

    def displayInfo(self):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__dailyRental}/day.")
        
class RentalCost(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, numberOfDays):
        super().__init__ (brand, model, year, dailyRental)
        self.days = numberOfDays
        self.rentalcost = 0
    
    def calculateRent(self):
        self.rentalCost = self.getDailyRental()*self.days
        return self.rentalCost
    
    def displayInfo(self):
        print (f"Rental cost for {self.brand} {self.model} for {self.days} days: $ {self.rentalCost}")
        
class SeatCapacity(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, numberOfSeats):
        super().__init__ (brand, model, year, dailyRental)
        self.seats = numberOfSeats

    def displayInfo(self):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year},Seats: {self.seats} Rental Price: ${self.getDailyRental()}/day.")

class EngineCapacity(Vehicle):

    def __init__ (self, brand, model, year, dailyRental, enginePower):
        super().__init__ (brand, model, year, dailyRental)
        self.enginge = enginePower

    def displayInfo(self):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year},Engine: {self.enginge}cc, Rental Price: ${self.getDailyRental()}/day.")

def transportation (category):

    vehicleDetails = Vehicle(input(f"Enter {category} brand :") ,
                             input(f"Enter {category} model: ") ,
                             int(input(f"Enter {category} year: ")),
                             float(input(f"Enter {category} daily rental price: $")))
    
    return vehicleDetails

def rentalPrice(vehicleDetails):
        
    numberOfDays = int(input(f"Enter the number of days you wish to rent the {category} for: "))

    rental = RentalCost(vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        numberOfDays)
    return rental


def ifCar(vehicleDetails):
    numberOfSeats = int(input("Enter the number of seats: "))

    newVehicledetails = SeatCapacity (vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        numberOfSeats)

    return newVehicledetails

def ifBike(vehicleDetails):
    enginePower = int(input("Enter the engine power in 'cc': "))

    newVehicledetails = EngineCapacity(vehicleDetails.brand, vehicleDetails.model, 
                        vehicleDetails.year, vehicleDetails.getDailyRental(), 
                        enginePower) 

    return newVehicledetails

def updatedPrice():

    updatedRentalPrice = (float(input(f"Enter updated daily rental price: $")))

    return rental.setDailyRental(updatedRentalPrice)




# # for the code
vehicleList = []

action = input("Do you wish to enter vehicle details? (yes or no): ")


while action == "yes" and action != "no":
    category = input ("Enter the vehicle type (Car or Bike): ").lower()
    categories = { 
        "Type" : category
    }

    if category == "car" and category != "bike":

        vehicleDetails = transportation(category) 
        newVehicledetails = ifCar(vehicleDetails)
        rental = rentalPrice(vehicleDetails)

        categories["Details"] = newVehicledetails
        categories["Rental"] = rental
       

    elif category != "car" and category == "bike":

        vehicleDetails = transportation(category)
        newVehicledetails = ifBike(vehicleDetails)
        rental = rentalPrice(vehicleDetails)

        categories["Details"] = newVehicledetails
        categories["Rental"] = rental
        
    vehicleList.append(categories)

    action = input("Do you wish to add new vehicle details? (yes or no): ")


for i in range(len(vehicleList)):
    categories = vehicleList[i]
    categories["Details"] = newVehicledetails
    newVehicledetails.displayInfo()
    print(vehicleList[i])

# rental.calculateRent()
# rental.displayInfo()

# rental = RentalCost(vehicleDetails.brand, vehicleDetails.model, vehicleDetails.year, vehicleDetails.getDailyRental(), numberOfDays)
# rental.calculateRent()
# rental.displayInfo()
# # numberOfDays.displayInfo()

# vehicleDetails.displayInfo()