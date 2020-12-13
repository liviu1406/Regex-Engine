def tallest_people(**name):
    for names, dict_values in sorted(name.items()):
        if dict_values == max(name.values()):
            print(f'{names} : {str(dict_values)}')


# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
