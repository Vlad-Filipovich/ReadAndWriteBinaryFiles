import shelve

with shelve.open('shelve_test') as cars:
    cars['ope'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])

    for key, value in cars.items():
        print(f'{key} from {value}')
