class Passenger:
    def __init__(self, FirstName, LastName, PassportNumber, PhoneNumber, SeatNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PassportNumber = PassportNumber
        self.PhoneNumber = PhoneNumber
        self.SeatNumber = SeatNumber

    def setFirstName(self, FirstName):
        self.FirstName = FirstName

    def getFirstName(self):
        return self.FirstName

    def setLastName(self, LastName):
        self.LastName = LastName

    def getLastName(self):
        return self.LastName

    def setPassportNumber(self, PassportNumber):
        self.PassportNumber = PassportNumber

    def getPassportNumber(self):
        return self.PassportNumber

    def setPhoneNumber(self, PhoneNumber):
        self.PhoneNumber = PhoneNumber

    def getPhoneNumber(self):
        return self.PhoneNumber

    def setSeatNumber(self, SeatNumber):
        self.SeatNumber = SeatNumber

    def getSeatNumber(self):
        return self.SeatNumber

    def display_passenger(self):
        print(
            f"First name: {self.FirstName}, Last name: {self.LastName}, Passport number: {self.PassportNumber}, Phone number: {self.PhoneNumber}, Seat number: {self.SeatNumber}")


class BoardingTicket:
    def __init__(self, passengerName, flightData, gateNumber, arrivalTime, seatNumber, destinationPlace):
        self.passengerName = passengerName
        self.flightData = flightData
        self.gateNumber = gateNumber
        self.arrivalTime = arrivalTime
        self.seatNumber = seatNumber
        self.destinationPlace = destinationPlace

    def setPassengerName(self, passengerName):
        self.passengerName = passengerName

    def getPassengerName(self):
        return self.passengerName

    def setFlightData(self, flightData):
        self.flightData = flightData

    def getFlightData(self):
        return self.flightData

    def setGateNumber(self, gateNumber):
        self.gateNumber = gateNumber

    def getGateNumber(self):
        return self.gateNumber

    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime

    def getArrivalTime(self):
        return self.arrivalTime

    def setDestinationPlace(self, destinationPlace):
        self.destinationPlace = destinationPlace

    def getDestinationPlace(self):
        return self.destinationPlace

    def display_BoardingTicket(self):
        print(
            f"Passenger name: {self.passengerName}, Flight data: {self.flightData}, Gate number: {self.gateNumber}, Arrival time: {self.arrivalTime}, Where we will land: {self.destinationPlace}")


class Reservation:
    def __init__(self, EmiratesID, ReservationID, passenger, FlightCode, Status):
        self.EmiratesID = EmiratesID
        self.ReservationID = ReservationID
        self.Passenger = passenger
        self.FlightCode = FlightCode
        self.Status = Status

    def setEmiratesID(self, EmiratesID):
        self.EmiratesID = EmiratesID

    def getEmiratesID(self):
        return self.EmiratesID

    def setReservationID(self, ReservationID):
        self.ReservationID = ReservationID

    def getReservationID(self):
        return self.ReservationID

    def setPassenger(self, passenger):
        self.Passenger = passenger

    def getPassenger(self):
        return self.Passenger

    def setFlightCode(self, FlightCode):
        self.FlightCode = FlightCode

    def getFlightCode(self):
        return self.FlightCode

    def setStatus(self, Status):
        self.Status = Status

    def getStatus(self):
        return self.Status

    def display_Reservation(self):
        print(
            f"Emirates ID: {self.EmiratesID}, Reservation ID: {self.ReservationID}, Passenger: {self.Passenger}, Flight code: {self.FlightCode}, Status: {self.Status}")


class FlightInfo:
    def __init__(self, boardingTill, terminal, arrivalCity, arrivalCountry, timeSpan):
        self.boardingTill = boardingTill
        self.terminal = terminal
        self.arrivalCity = arrivalCity
        self.arrivalCountry = arrivalCountry
        self.timeSpan = timeSpan

    def setBoardingTill(self, boardingTill):
        self.boardingTill = boardingTill

    def getBoardingTill(self):
        return self.boardingTill

    def setTerminal(self, terminal):
        self.terminal = terminal

    def getTerminal(self):
        return self.terminal

    def setArrivalCity(self, arrivalCity):
        self.arrivalCity = arrivalCity

    def getArrivalCity(self):
        return self.arrivalCity

    def setArrivalCountry(self, arrivalCountry):
        self.arrivalCountry = arrivalCountry

    def getArrivalCountry(self):
        return self.arrivalCountry

    def setTimespan(self, timeSpan):
        self.timeSpan = timeSpan

    def getTimespan(self):
        return self.timeSpan

    def display_FlightInfo(self):
        print(
            f"Boarding till: {self.boardingTill}, Terminal: {self.terminal}, Arrival city: {self.arrivalCity}, Arrival country: {self.arrivalCountry}, Time span: {self.timeSpan}")


class BoardingSystem:
    def __init__(self, boardingPass, boardingAnnouncement, boardingGroupSize, boardingEmployees, boardingTime):
        self.boardingPass = boardingPass
        self.boardingAnnouncement = boardingAnnouncement
        self.boardingGroupSize = boardingGroupSize
        self.boardingEmployees = boardingEmployees
        self.boardingTime = boardingTime

    def setBoardingPass(self, boardingPass):
        self.boardingPass = boardingPass

    def getBoardingPass(self):
        return self.boardingPass

    def setBoardingAnnouncement(self, boardingAnnouncement):
        self.boardingAnnouncement = boardingAnnouncement

    def getBoardingAnnouncement(self):
        return self.boardingAnnouncement

    def setBoardingGroupSize(self, boardingGroupSize):
        self.boardingGroupSize = boardingGroupSize

    def getBoardingGroupSize(self):
        return self.boardingGroupSize

    def setBoardingEmployees(self, boardingEmployees):
        self.boardingEmployees = boardingEmployees

    def getBoardingEmployees(self):
        return self.boardingEmployees

    def setBoardingTime(self, boardingTime):
        self.boardingTime = boardingTime

    def getBoardingTime(self):
        return self.boardingTime

    def display_BoardingSystem(self):
        print(
            f"Boarding pass: {self.boardingPass}, Boarding announcement: {self.boardingAnnouncement}, Boarding group size: {self.boardingGroupSize}, Boarding employees: {self.boardingEmployees}, Boarding time: {self.boardingTime}")


# Create Passenger object
passenger = Passenger("James ", "Smith", "A987B", "0501122334", "09A")

# Create BoardingTicket object
boarding_ticket = BoardingTicket("James Smith", " 5A6BCD78", "Gate 03", "13:30 AM", "09A", "New York JFK")

# Create Reservation object
reservation = Reservation("984-2004-198873", "251", "James Smith", "627", "Authorized")

# Create FlightInfo object
flight_info = FlightInfo("11:20 AM", "Terminal 2", "New York JFK", "USA", "2 hours and 10 minutes")

# Create BoardingSystem object
boarding_system = BoardingSystem("629", "Boarding starts at 11:20 AM", "100 passengers", "Boarding staff", "11:20 AM")

print("\nPassenger Details:\n")
passenger.display_passenger()
print("\n")

print("Boarding Ticket Details:\n")
boarding_ticket.display_BoardingTicket()
print("\n")

print("Reservation Details:\n")
reservation.display_Reservation()
print("\n")

print("Flight Information:\n")
flight_info.display_FlightInfo()
print("\n")

print("Boarding System Information:\n")
boarding_system.display_BoardingSystem()