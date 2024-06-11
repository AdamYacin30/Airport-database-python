# Airport program prepared by Adam Yassine

# create a class for Airport
class Airport:

    def __init__(self, code, city, country):
        # function used to initialize instance variables for code, city, and country
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        # function used to return how the program should be printed out
        return f'{self._code}({self._city}, {self._country})'


    def getCode(self):
        # Function used to get the unique Airport code
        return self._code


    def getCity(self):
        # Function used to get the Airport city
        return self._city


    def getCountry(self):
        # Function used to get the Airport country
        return self._country


    def setCity(self, city):
        # Function used to update/set the instance variable of city
        self._city = city

    def setCountry(self, country):
        # Function used to update/set the instance variable of country
        self._country = country


