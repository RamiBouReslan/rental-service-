class Vehicle:

    def __init__ (self, brand, model, year, dailyRental):
        self.brand = brand
        self.model = model 
        self.year = year
        self.dailyRental= dailyRental

    def displayInfo(self):
        
        print (f"{category}: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.dailyRental}/day.")
        






# def promt ():
#     vehicleDetails = Vehicle(input(f"Enter {category} brand:") , input(f"Enter {category} model: "),
#                             int(input(f"Enter {category} year: ")), float(input(f"Enter {category} daily rental price: $")))
#     return vehicleDetails




# # for the code
# category = input ("Enter the vehicle type: ")

# vehicleDetails = promt()
# vehicleDetails.displayInfo()