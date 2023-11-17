#!/bin/python3
# Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price

# Creating menus
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("brunch", brunch_items, "11am", "4pm")

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00
}
early_bird = Menu("early_bird", early_bird_items, "3pm", "6pm")

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00, 'espresso': 3.00
}
dinner = Menu("dinner", dinner_items, "5pm", "11pm")

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", kids_items, "11am", "9pm")

# Test string representation and calculate_bill
print(brunch)
print(f"Total bill: ${brunch.calculate_bill(['pancakes', 'home fries', 'coffee']):.2f}")

print(early_bird)
print(f"Total bill: ${early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']):.2f}")

# Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __str__(self):
        return f"Franchise located at {self.address}"

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Creating franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# Test Franchise methods
print(flagship_store)
print("Available menus at 12 noon:", [menu.name for menu in flagship_store.available_menus("12pm")])
print("Available menus at 5pm:", [menu.name for menu in flagship_store.available_menus("5pm")])

# Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Creating business
arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place = Franchise("189 Fitzgerald Avenue", [Menu("Take a' Arepa", arepas_menu, "10am", "8pm")])

take_a_arepa = Business("Take a' Arepa", [arepas_place, flagship_store, new_installment])

