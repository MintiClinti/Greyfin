import csv
from geopy import distance
from geopy.geocoders import Nominatim
order = []
# info of current user
e_hobbies = ['singing', 'league']
e_city = 'folsom'
e_state = 'ca'


def distancing(city1, state1, city2, state2):
    geolocator = Nominatim(user_agent="app")

    location1 = f"{city1}, {state1}"
    location2 = f"{city2}, {state2}"

    location_info1 = geolocator.geocode(location1)
    location_info2 = geolocator.geocode(location2)

    lat1 = location_info1.latitude
    lon1 = location_info1.longitude
    lat2 = location_info2.latitude
    lon2 = location_info2.longitude

    kms = distance.distance((lat1, lon1), (lat2, lon2))
    if kms < 49:
        return 1.0
    else:
        return 0.5


def match(list1, list2):
    common = set(list1).intersection(set(list2))
    common_num = len(common)

    total = set(list1).union(set(list2))
    total_num = len(total)

    n = common_num / total_num
    return n


def matcher(file, city, state):
    with open(file) as users:
        next(users)
        read = csv.reader(users)

        for user in read:
            if user[-1] == 'elderly':
                continue
            c_hobbies = user[2].split(", ")
            c_city = user[3]
            c_state = user[4]

            range_score = distancing(city, state, c_city, c_state)
            match_score = match(e_hobbies, c_hobbies)
            gross_score = range_score + match_score

            updated = user
            updated.append(gross_score)
            order.append(updated)

    return sorted(order, key=lambda x: x[-1])
