class parkingGarage():
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTickets = {}

    def takeTicket(self, ticketnum):
        print(self.tickets)
        self.tickets.remove(ticketnum)
        self.parkingSpaces.remove(ticketnum)
        self.currentTickets[ticketnum] = ""
        print(self.currentTickets)

    def payForParking(self):
        ticketnum = int(input('please choose your ticket: '))
        if ticketnum == 0:
            ticketnum = int(input('please enter valid ticket'))

        amount = int(input('please enter payment amount: '))
        if amount == 0:
            amount = int(input('please enter a valid amount: '))

        if ticketnum in self.currentTickets.keys():
            self.currentTickets[ticketnum] = "Paid"
            print("Ticket has been paid. You now have 15 minutes to leave.")


myGarage = parkingGarage()


def runGarage():
    while True:
        response = input(
            'what would you like to do? take ticket, pay or leave? ')
        if response.lower() == 'take ticket':
            ticketnum = int(input('choose a ticket number: '))
            myGarage.takeTicket(ticketnum)
        elif response.lower() == 'pay':
            myGarage.payForParking()


runGarage()
