travel_log = [
    {
    "country": "France",
    "visits": 2,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, city):
    travel_log.append({"country": country,
                       "visits": visits,
                       "cities": city})

        



add_new_country("Russia",2,["Moscow", "Saint peterson"])
print(travel_log)