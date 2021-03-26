class parkingGarage():
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTickets = {}
    def takeTicket(self,ticketnum):
        print(self.tickets)
        self.tickets.remove(ticketnum)
        self.parkingSpaces.remove(ticketnum)
        print(self.tickets)


myGarage = parkingGarage()

def runGarage():
    while True:
        response = input('what would you like to do? take ticket, park or leave?')
        if response.lower() == 'take ticket':
            ticketnum = int(input('choose a ticket number:'))
            myGarage.takeTicket(ticketnum)

runGarage()
