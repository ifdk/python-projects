# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation7
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    highest_elevation_so_far = 0
    if city1.population >= min_population and city1.elevation > highest_elevation_so_far:
        return_city = city1
    print(highest_elevation_so_far)
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    print(city2.population >= min_population)
    print(city2.elevation > highest_elevation_so_far)
    if city2.population >= min_population and city2.elevation > highest_elevation_so_far:
        highest_elevation_so_far = city2.elevation
        return_city = city2
    print(highest_elevation_so_far)
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    print(city3.population >= min_population)
    print(city3.elevation > highest_elevation_so_far)
    if city3.population >= min_population and city3.elevation > highest_elevation_so_far:
        highest_elevation_so_far = city3.elevation
        return_city = city3
    print(highest_elevation_so_far)
    # Format the return string
    if return_city.name:
        return return_city.name + ", " + return_city.country
    else:
        return ""


# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    highest_elevation_so_far = 0
    if city1.population >= min_population and city1.elevation > highest_elevation_so_far:
        return_city = city1

    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?

    if city2.population >= min_population and city2.elevation > highest_elevation_so_far:
        highest_elevation_so_far = city2.elevation
        return_city = city2

    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?

    if city3.population >= min_population and city3.elevation > highest_elevation_so_far:
        highest_elevation_so_far = city3.elevation
        return_city = city3

    # Format the return string
    if return_city.name:
        return return_city.name + ", " + return_city.country
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""

# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""
