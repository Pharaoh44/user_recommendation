restaurants = {
    "Mexican": ["Rosa's", "Generosa's", "Red Carpet Bar & Restaurant"],
    "Japanese": ["Misaki Sushi", "Pearl", "Beluga Bar"],
    "Jamaican": ["Fish N Tings", "Jamaican Grill", "Yardie Kithen"],
    "Italian": ["Portofino", "Little Venice", "La Trattoria"],
    "Portugese": ["Devil's Ilse", "The Cottage Cafe", "Port O Call"]


}

def reccomend():
    for key in restaurants.values():
        print(key)
        

print(reccomend())