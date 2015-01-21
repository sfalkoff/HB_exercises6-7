# SCORES.TXT: restaurant_name:rating

# program will open/read scores.txt
restaurants = open('scores.txt')

# creates dictionary
all_restaurants = {}

for line in restaurants: 
    restaurant_data = line.rstrip()
    restaurant_data = restaurant_data.split(":")
    all_restaurants[restaurant_data[0]] = restaurant_data[1]

# sorts alphabetically before printing
for restaurant_name, rating in sorted(all_restaurants.items()):
    print "Restaurant %s is rated at %s." % (restaurant_name, rating)