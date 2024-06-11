
airportsSet = set()

# iterate through the codes inside the allFlights dictionary

    for i in allFlights.values():
        # if the given destination is the same as the actual destination, print in desired format
        for j in i:
            if origAirport == i.getOrigin():
                return f'Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}'
            elif destAirport == i.getDestination():
                return f'Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}'
            # if not, then append the destination in the list
            elif i.getDestination() not in destinationList:
                destinationList.append(i)

        origFlights = findAllCityFlights(origAirport.getCity())
        destFlights = findAllCitYFlights(destAirport.getCity())

        for i in origFlights:
            if i.getOrigin().getCity() == origAirport.getCity():
                airportsSet.add(i.getDestination().getCode())
        for j in destFlights:
            if i.getDestination().getCity == destAirport.getCity()
                airportsSet.add(i.getDestination().getCode())

    if len(airportsSet) > 0:
        return airportsSet
    else:
        return -1

airportsSet = set()
destinationList = []

# iterate through the codes inside the allFlights dictionary
if allFlights[origAirport.getCode()]:
    for i in allFlights[origAirport.getCode()]:
        # if the given destination is the same as the actual destination, print in desired format
        if i.getDestination() == destAirport:
            return f'Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}'
        # if not, then append the destination in the list
        elif i.getDestination() not in destinationList:
            destinationList.append(i)

    # if the list is not empty then add flights to the list
    if len(destinationList) != 0:
        for j in destinationList:
            # iterate through the list of destinations
            if allFlights[j.getDestination().getCode()]:
                for i in allFlights[origAirport.getCode()]:
                    if i.getDestination() == destAirport:
                        airportsSet.add(i.getOrigin().getCode())
    # if the set is not empty then return the set. otherwise return -1
    if len(airportsSet) != 0:
        return airportsSet
    else:
        return -1