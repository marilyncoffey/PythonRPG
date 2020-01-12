class Weapon(object):

    def __init__(self, name, accuracy, damage, price):
        self.name = name
        self.toHit = accuracy
        self.damage = damage
        self.price = price

    def __str__(self):
        result = ""
        result += "The weapon is: " + self.name + "\n"
        result += "The accuracy is: " + str(self.toHit) + "\n"
        result += "The damage is: " + str(self.damage) + "\n"
        result += "The price is: " + str(self.price) + "\n"
        return result

    def get_name(self):
        return self.name
    def get_toHit(self):
        return self.toHit
    def get_damage(self):
        return self.damage
    def get_price(self):
        return self.price

class Armor(object):

    def __init__(self, name, armor, cost):
        self.name = name
        self.ac = armor
        self.cost = cost

    def __str__(self):
        result = ""
        result += "The armor is called: " + self.name + "\n"
        result += "The armor rating is: " + str(self.ac) + "\n"
        result += "The armor costs: " + str(self.cost) + "\n"
        return result
        
    def get_name(self):
        return self.name
    def get_ac(self):
        return self.ac
    def get_cost(self):
        return self.cost

class Consumable(object):

    def __init__(self, name, heal, price):
        self.name = name
        self.heal = heal
        self.price = price

    def __str__(self):
        result = self.name
        return result
        
    def get_name(self):
        return self.name
    def get_heal(self):
        return self.heal
    def get_price(self):
        return self.price

    def use():
        playerHP += self.heal
