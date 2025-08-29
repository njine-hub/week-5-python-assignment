# Base Class (General Smartphone)
class Smartphone:
    def __init__(self, brand, model, battery_capacity, storage, color):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  # mAh
        self.storage = storage  # GB
        self.color = color
        self.battery_level = 100  # starts fully charged
        self.apps = []  # installed apps

    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} - {self.color}, {self.storage}GB, {self.battery_capacity}mAh"

    # Method to make a call
    def make_call(self, contact):
        if self.battery_level > 5:
            self.battery_level -= 5
            return f"Calling {contact}... Battery now at {self.battery_level}%"
        else:
            return " Battery too low to make a call!"

    # Method to install apps
    def install_app(self, app_name):
        self.apps.append(app_name)
        return f"Installed {app_name}. Total apps: {len(self.apps)}"

    # Method to charge phone
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f" Charging... Battery now at {self.battery_level}%"


# Derived Class (Specific Model - Redmi A3X)
class RedmiA3X(Smartphone):
    def __init__(self, color, storage=128):
        super().__init__("Redmi", "A3X", 5000, storage, color)

    # Polymorphism: overriding make_call
    def make_call(self, contact):
        if self.battery_level > 3:
            self.battery_level -= 3  # more efficient battery
            return f" Redmi A3X calling {contact} with AI Noise Cancellation. Battery at {self.battery_level}%"
        else:
            return " Redmi A3X battery too low!"


# Another Derived Class (iPhone)
class iPhone(Smartphone):
    def __init__(self, model, color, storage=256):
        super().__init__("Apple", model, 4000, storage, color)

    # Polymorphism: overriding install_app
    def install_app(self, app_name):
        if app_name not in self.apps:
            self.apps.append(app_name)
            return f" App {app_name} installed via App Store!"
        return f"App {app_name} is already installed!"


# --- Example Usage ---
redmi = RedmiA3X(color="Blue")
iphone = iPhone(model="14 Pro", color="Black")

print(redmi.phone_info())
print(redmi.make_call("joseph"))
print(redmi.install_app("WhatsApp"))
print(redmi.charge(10))

print("\n--- iPhone ---")
print(iphone.phone_info())
print(iphone.make_call("Best Friend"))
print(iphone.install_app("Safari"))


#question 2
# Base Class (Animal)
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived Classes with different move() behavior
class Dog(Animal):
    def move(self):
        return "🐕 RUNNING!"

class Fish(Animal):
    def move(self):
        return "🐟 SWIMMING !"

class Bird(Animal):
    def move(self):
        return "🐦 FLYING!"

class Snake(Animal):
    def move(self):
        return "🐍 SLITHERING!"


# --- Example Usage ---
animals = [Dog(), Fish(), Bird(), Snake()]

for animal in animals:
    print(animal.move())
