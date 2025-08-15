class Flower:
    def __init__(self,price,color,smell):
        """Constructor to initialize flower attributes"""
        self.price = price
        self.color = color
        self.smell = smell
        
    def get(self):
        """Method to input flower details"""
        self.price = input("Enter price: ")
        self.color = input("Enter color: ")
        self.smell = input("Enter smell: ")
    
    def display(self):
        """Method to display flower details"""
        print("\nFlower Details:")
        print(f"Price: {self.price}")
        print(f"Color: {self.color}")
        print(f"Smell: {self.smell}")

# Create flower objects
lilly = Flower()
rose = Flower()
hibiscus = Flower()

# Get and display details for each flower
print("Enter details for Lilly:")
lilly.get()

print("\nEnter details for Rose:")
rose.get()

print("\nEnter details for Hibiscus:")
hibiscus.get()

# Display all flowers
print("\nDisplaying all flower details:")
lilly.display()
rose.display()
hibiscus.display()