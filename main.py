# Define the parent class Vehicle
class Vehicle:
    # Initialize the attributes of Vehicle
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Define the methods of Vehicle
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model

# Define the child class Car that inherits from Vehicle
class Car(Vehicle):
    # Initialize the attributes of Car
    def __init__(self, make, model, door):
        # Call the parent class constructor
        super().__init__(make, model)
        self.door = door
    
    # Define the methods of Car
    def set_door(self, door):
        self.door = door
    
    def get_door(self):
        return self.door

# Define the child class Pickup that inherits from Vehicle
class Pickup(Vehicle):
    # Initialize the attributes of Pickup
    def __init__(self, make, model, bed):
        # Call the parent class constructor
        super().__init__(make, model)
        self.bed = bed
    
    # Define the methods of Pickup
    def set_bed(self, bed):
        self.bed = bed
    
    def get_bed(self):
        return self.bed

# Create a list to store the vehicles in the garage
garage = []

# Create a loop to prompt the user to add vehicles
while True:
    # Display a menu of options
    print("Welcome to the virtual garage!")
    print("1. Add a car")
    print("2. Add a pickup truck")
    print("3. View the garage")
    print("4. Exit")
    
    # Get the user's choice
    choice = input("Please enter your choice: ")
    
    # Validate the user's choice
    if choice == "1":
        # Get the car's attributes from the user
        make = input("Please enter the car's make: ")
        model = input("Please enter the car's model: ")
        door = input("Please enter the number of doors: ")
        
        # Create a car object with the user's input
        car = Car(make, model, door)
        
        # Add the car object to the garage list
        garage.append(car)
        
        # Display a confirmation message
        print(f"You have added a {car.get_make()} {car.get_model()} with {car.get_door()} doors to the garage.")
    
    elif choice == "2":
        # Get the pickup's attributes from the user
        make = input("Please enter the pickup's make: ")
        model = input("Please enter the pickup's model: ")
        bed = input("Please enter the bed length: ")
        
        # Create a pickup object with the user's input
        pickup = Pickup(make, model, bed)
        
        # Add the pickup object to the garage list
        garage.append(pickup)
        
        # Display a confirmation message
        print(f"You have added a {pickup.get_make()} {pickup.get_model()} with a {pickup.get_bed()} bed to the garage.")
    
    elif choice == "3":
        # Check if the garage is empty
        if len(garage) == 0:
            # Display a message that there are no vehicles in the garage
            print("There are no vehicles in the garage.")
        
        else:
            # Display a header for the garage
            print("The garage contains:")
            
            # Loop through each vehicle in the garage list
            for vehicle in garage:
                # Check if the vehicle is a car or a pickup
                if isinstance(vehicle, Car):
                    # Display the car's attributes
                    print(f"A {vehicle.get_make()} {vehicle.get_model()} with {vehicle.get_door()} doors.")
                
                elif isinstance(vehicle, Pickup):
                    # Display the pickup's attributes
                    print(f"A {vehicle.get_make()} {vehicle.get_model()} with a {vehicle.get_bed()} bed.")
    
    elif choice == "4":
        # Break out of the loop and exit the program
        break
    
    else:
        # Display an error message for invalid input
        print("Invalid choice. Please try again.")
