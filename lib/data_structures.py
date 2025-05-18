spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Returns a list of strings with the names of each spicy food.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
        
    Returns:
        list: List of food names
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries where the heat level of the food is greater than 5.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
        
    Returns:
        list: List of spicy food dictionaries with heat level > 5
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Outputs each spicy food in a formatted string.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
    """
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the spicy food whose cuisine matches the given cuisine.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
        cuisine (str): The cuisine to search for
        
    Returns:
        dict: The spicy food dictionary with matching cuisine
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found

def print_spiciest_foods(spicy_foods):
    """
    Outputs only the spicy foods with heat level > 5 in a formatted string.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
    """
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """
    Returns the average heat level of all spicy foods.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
        
    Returns:
        int: The average heat level (rounded to nearest integer)
    """
    if not spicy_foods:
        return 0
    
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return round(total_heat / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    """
    Returns the original list with a new spicy food added.
    
    Args:
        spicy_foods (list): List of dictionaries representing spicy foods
        spicy_food (dict): New spicy food to add
        
    Returns:
        list: Updated list of spicy foods
    """
    # Create a new list to avoid modifying the original
    updated_foods = spicy_foods.copy()
    updated_foods.append(spicy_food)
    return updated_foods
