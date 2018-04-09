import modrest

tims = modrest.Restaurant('tim\'s', 'italian')

tims.describe_restaurant()
tims.increment_number_served(39)
tims.describe_restaurant()