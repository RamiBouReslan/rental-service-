class Vehicle:

    def __init__ (self, brand, model, year, dailyRental):
        self.brand = brand
        self.model = model 
        self.year = year
        self.dailyRental= dailyRental

    def displayInfo(self):        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.dailyRental}/day.")
        
class RentalCost(Vehicle):
    # def superMetod(self):
    #     super().__init__(self)
    
    def __init__ (self, brand, model, year, dailyRental, numberOfDays):
        super().__init__ (brand, model, year, dailyRental)
        self.days = numberOfDays
        self.rentalcost = 0
    
    def calculateRent(self):
        self.rentalCost = self.dailyRental*self.days
        return self.rentalCost
    
    def displayInfo(self):
        print (f"Rental cost for {self.brand} {self.model} for {numberOfDays} days: $ {self.rentalCost}")
        







# def promt ():
#     vehicleDetails = Vehicle(input(f"Enter {category} brand :") , input(f"Enter {category} model: "),
#                             int(input(f"Enter {category} year: ")), float(input(f"Enter {category} daily rental price: $")))
#     return vehicleDetails




# # for the code
category = input ("Enter the vehicle type: ")
vehicleDetails = Vehicle(input(f"Enter {category} brand: ") , input(f"Enter {category} model: "), int(input(f"Enter {category} year: ")), float(input(f"Enter {category} daily rental price: $")))
numberOfDays = int(input("Enter the number of days you wish to rent the car for: "))

rental = RentalCost(vehicleDetails.brand, vehicleDetails.model, vehicleDetails.year, vehicleDetails.dailyRental, numberOfDays)

rental.calculateRent()
rental.displayInfo()
# numberOfDays.displayInfo()
# vehicleDetails = promt()
# vehicleDetails.displayInfo()