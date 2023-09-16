restaurants = {
    "Mexican": ["Rosa's", "Generosa's", "Red Carpet Bar & Restaurant"],
    "Japanese": ["Misaki Sushi", "Pearl", "Beluga Bar"],
    "Jamaican": ["Fish N Tings", "Jamaican Grill", "Yardie Kithen"],
    "Italian": ["Portofino", "Little Venice", "La Trattoria"],
    "Portugese": ["Devil's Ilse", "The Cottage Cafe", "Port O Call"]


}

def reccomend(theme):
    theme = input("What kind of food from bermuda would you like to try?\nWe have a selction of Mexican, Japanese, Jamaican, Italian and Portugese.\nWhat would you like? ")
    if theme == "Mexican":
        print(f"Mexican restaurants in the area are: {restaurants['Mexican']}")
    elif theme == "Japanese":
        print(f"Japanese restaurants in the area are: {restaurants['Japanese']}")
    elif theme == "Jamaican": 
        print(f"Jamaican restaurants in the area are: {restaurants['Jamaican']}")
    elif theme == "Italian":
        print(f"Italian restaurants in the area are: {restaurants['Italian']}")
    elif theme == "Portugese":  
        print(f"Portugese restaurants in the area are: {restaurants['Portugese']}")
    else:
        print("No such theme exists in the recommendation system.")
        x = input("Try again? Y/N? ")
        if x == "y":
            reccomend(theme)
        else:
            return None
 


print(reccomend(restaurants))