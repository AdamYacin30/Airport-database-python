# Flight program prepared by Adam Yassine

# import the Airport.py program
from Airport import *

# create a class for Flight
class Flight:
    def __init__(self, flightNo, origin, destination):
        # function used to initialize instance variables for flightNo, origin, destination

        # use isinstance to see if the origin and destination and Airport are objects and Raise a Type error if they are not
        if not isinstance(origin, Airport):
            raise TypeError("the origin and destination must be airport objects")
        elif not isinstance(destination, Airport):
            raise TypeError("the origin and destination must be airport objects")
        else:
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
            # create an empty string object for later use to determine if the flight is domestic or international
            self.loc = ''

    def __repr__(self):
        # function used to determine if the flight domestic or international

        if Flight.isDomesticFlight(self) == True:
            self.loc = 'domestic'
        elif Flight.isDomesticFlight(self) == False:
            self.loc = 'international'

        return f'Flight: {self._flightNo} from {self.getOrigin().getCity()} to {self.getDestination().getCity()} {{{self.loc}}}'

    def __eq__(self, other):
        # function used to check if origin and destination are the same
        if isinstance(other, Flight) and self._origin == other.getOrigin() and self._destination == other.getDestination():
            return True
        else:
            return False

    def getFlightNumber(self):
        # function used to get the flight Number
        return self._flightNo

    def getOrigin(self):
        # function used to get the Origin
        return self._origin

    def getDestination(self):
        # function used to get the destination
        return self._destination

    def isDomesticFlight(self):
        # function used to see if the flight is domestic
        # if the orign and destination are not the same then they are not domestic and therefore it would be international
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    def setOrigin(self, origin):
        # function used to set the origin variable
        self._origin = origin

    def setDestination(self, destination):
        # function used to set the destination variable
        self._destination = destination


