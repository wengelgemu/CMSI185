'''
desserts.py
Name: Wengel Gemu
Collaborators:
Date: September 12th, 2019
Desscription: This program prints out recipes for desserts.
'''




def border():
    print('------------*******<><><><><>oooooo<><><><>******-------------')

def title():
    print('Tiramisu (Wolfgang Puck)')

# recipie instructions for ladyfingers
def ladyfingers():
    print('Ladyfingers: ')
    print('* 6 eggs, separated')
    print('* Melted butter, for brushing pan')
    print()

# recipie instructions for mascarpone crea,
def mascarpone_cream(): 
    print('Mascarpone Cream: ')
    print('* 6 egg yolks')
    print('* 1 cup sugar')
    print('* 1/3 cup Marsala')
    print('* 1/4 cup brandy')
    print('* 2 pounds mascarpone cheese')
    print()

# recipie instructions for espresso syrup
def espresso_syrup(): 
    print('Espresso Syrup: ')
    print('* 1 cup espresso, hot')
    print('* 3 tablespoons brown sugar')
    print('* 1 tablespoon sugar')
    print('* 1 teaspoon lemon juice')
    print('* 1 teaspoon vanilla extract')
    print('* 1/2 cup grated bittersweet chocolate')


# recipie instructions for parafait cream
def parfait_cream(): 
    print('Parfait Cream:')
    print('* 2 cups melted vanilla ice cream')
    print('* 4 tablespoons orange flavored liqueur')
    print('* 1 cup raspberries')

def combined_title():
    print('Ladyfinger Parfait')

# function calling tiramisu components
def tiramisu():
    border()
    title()
    border()
    ladyfingers()
    mascarpone_cream()
    espresso_syrup()
    border()

# function displaying ladyfinger parfait recipie
def combined_recipies():
    border()
    combined_title()
    border()
    ladyfingers()
    parfait_cream()
    border()

tiramisu()
combined_recipies()
