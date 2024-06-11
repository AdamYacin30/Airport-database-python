# python program for creating Airport and Flight objects prepared by Adam Yassine

# import both the Flight and Airport Programs
from Flight import *
from Airport import *

# create an empty list and dictionary to store all the airports and flights
allAirports = []
allFlights = {}

def loadData(airportFile, flightFile):
    # function used read in all the needed data from the Airport and Flight file

    # create a try function to test for any errors relating to incorrect text files being inputted
    try:
        # open the Airport file as read
        with open(airportFile, 'r') as sheet1:
            for row in sheet1:
                row = row.strip('\n').split(',')
                # .strip() used to remove any whitespaces in the file
                airportCode = row[0].strip()
                airportList = Airport(airportCode, row[2].strip(), row[1].strip())
                allAirports.append(airportList)
            sheet1.close()
    except:
        return False

    try:
        # open the Flight file as read
        with open(flightFile, 'r') as sheet2:
            for row in sheet2:
                row = row.strip('\n').split(',')
                temp = Flight(row[0].strip(), getAirportByCode(row[1].strip()), getAirportByCode(row[2].strip()))
                codeOrigin = temp.getOrigin().getCode()
                if not codeOrigin in allFlights:
                    allFlights.update({codeOrigin: [temp]})
                else:
                    allFlights[codeOrigin].append(temp)
            sheet2.close()
            return True
    except:
        return False


def getAirportByCode(code):
    # function used to get the Airport using its code
    for i in allAirports:
        # if the code is equal to the code inside the dictionary return i. If not then return -1
        if code == i.getCode():
            return i
    return -1


def findAllCityFlights(city):
    # function used to find all the Flights when given the city
    listFlights = []

    for i in allFlights.values():
        for j in i:
            # if the origin or destination is the same as the user input for a city then add the value to the list
            if j.getOrigin().getCity() == city:
                listFlights.append(j)
            if j.getDestination().getCity() == city:
                listFlights.append(j)
    return listFlights


def findAllCountryFlights(country):
    # function to find all the flights when given the country
    listFlights= []
    # nested for loop to iterate through all the allFlights values and for each i
    for i in allFlights.values():
        for j in i:
            # if the origin or destination is the same as the user input for a country then add the value to the list
            if j.getOrigin().getCountry() == country:
                listFlights.append(j)
            if j.getDestination().getCountry() == country:
                listFlights.append(j)
    return listFlights


def findFlightBetween(origAirport, destAirport):
    # function used to find direct flight between origin airport and destination airport

    # create an empty set to store all the possible airport codes and all the destinations
    airportsSet = set()
    for i in allFlights.values():
        # if the given destination is the same as the actual destination, print in desired format
        #for j in i:
        if origAirport == i.getOrigin():
            return f'Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}'
        elif destAirport == i.getDestination():
            return f'Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}'


        origFlights = findAllCityFlights(origAirport.getCity())
        destFlights = findAllCityFlights(destAirport.getCity())

        for i in origFlights:
            if i.getOrigin().getCity() == origAirport.getCity():
                airportsSet.add(i.getDestination().getCode())
        for j in destFlights:
            if i.getDestination().getCity == destAirport.getCity():
                airportsSet.add(i.getDestination().getCode())

    if len(airportsSet) > 0:
        return airportsSet
    else:
        return -1


def findReturnFlight(firstFlight):
    # function used to find the flights that are returning

    # get the code for the returning flight
    returnFlights = allFlights[firstFlight.getDestination().getCode()]
    # iterate to see if a returning flight exists
    if returnFlights:
        for i in returnFlights:
            if i.getDestination() == firstFlight.getOrigin():
                return i
    return -1