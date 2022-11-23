import shelve

with shelve.open('shelve_test') as cars:
    # cars['opel'] = 'Germany'
    # cars['ford'] = 'USA'
    # cars['mazda'] = 'Japan'
    # cars['renault'] = 'France'

    # del cars['ope']

    # print(cars['ford'])
    # print(cars['renault'])
    #
    # cars['kia'] = 'South Korea'
    #
    # for key in cars:
    #     print(key + ': ' + cars[key])

    # while True:
    #     key = input('Please enter a car name: ').lower()
    #     if key == 'quit':
    #         break
    #     country = cars.get(key, "We don't have a " + key)
    #     print(country)

    # while True:
    #     key = input('Please enter a car name: ').lower()
    #     if key == 'quit':
    #         break
    #     if key in cars:
    #         country = cars[key]
    #         print(country)
    #     else:
    #         print("We don't have a " + key)

    # ordered_keys_list = sorted(list(cars.keys()))
    #
    # for key in ordered_keys_list:
    #     print(key + ' ' + cars[key])

    for value in cars.values():
        print(value)
    print(list(cars.values()))

    for key in cars.keys():
        print(key)
    print(list(cars.keys()))

    for item in cars.items():
        print(item)
    print(list(cars.items()))
