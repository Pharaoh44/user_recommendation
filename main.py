from restaurants import types, restaurant_data

def autocomplete(text):
    matches = [category for category in types if category.startswith(text)]
    return matches

def retrieve_data(selected_category):
    matching_restaurants = [restaurant for restaurant in restaurant_data if restaurant[0] == selected_category]
    return matching_restaurants

while True:
    user_input = input("Enter the beginning of a category (e.g. 'f' for french, 'a' for american): ".lower())

    autocomplete_results = autocomplete(user_input)

    if not autocomplete_results:
        print("No matching categories found.")
    
    else:
        print("Matching categories: ")
        for category in autocomplete_results:
            print(category)

        selected_category = input("Select a category to retrieve data (or press Enter to exit): ").lower()

        if selected_category == "":
            break

        matching_restuarants = retrieve_data(selected_category)

        if not matching_restuarants:
            print("No restaurants found for the selected category.")

        else:
            print(f"Restaurants in the {selected_category} category:")
            for restaurant in matching_restuarants:
                print(f"Name: {restaurant[1]}")
                print(f"Pricing: {restaurant[2]}/5")
                print(f"Rating: {restaurant[3]}/5")
                print(f"Address: {restaurant[4]}")
