def get_city_country_loc(city, country, population=0):
    """Generate a neatly formatted Location"""
    full_location = f"{city}, {country}"
    if population:
        full_location += f" - Population={population}"
    return full_location.title()