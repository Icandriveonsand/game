class Item():
    def __init__(self):
        self.name = None
        self.description = None
        self.visible = False
    
    def set_name(self, name_to_set):
        self.name = name_to_set

    def set_description(self, description_to_set):
        self.description = description_to_set

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def get_details(self):
        print(f"""{self.name}
{"-"*len(self.name)}
{self.description if self.description else ' '}
""")
        
if __name__ == "__main__":
    shears = Item()
    shears.set_name("Garden Shears")
    shears.set_description("Red handled gardening shears, the metal slightly rusted by years of use")
    shears.get_details()

    wilburs_shirt = Item()
    wilburs_shirt.set_name("Wilbur's Shirt")
    wilburs_shirt.set_description("A yellow tinted baggy shirt, stained with mysterious sauces, it smells of a dying carcass")
    wilburs_shirt.get_details()

    bread = Item()
    bread.set_name("Loaf of Bread")
    bread.set_description("A loaf of good ol white bread")
    bread.get_details()

    wilburs_key = Item()
    wilburs_key.set_name("Wilbur's Room Key")
    wilburs_key.set_description(" A small yellow key, slightly bent, in messy sharpie reads Wilburs Room, upon closer look you can see its covering an engraving reading R1")
    wilburs_key.get_details()

    cheese = Item()
    cheese.set_name("Cheese")
    cheese.set_description("Think that small cheese snack pack that comes with crackers.. except someone ate all the crackers..")
    cheese.get_details()

    pennelopes_jacket = Item()
    pennelopes_jacket.set_name("Pennelopes Jacket")
    pennelopes_jacket.set_description("")