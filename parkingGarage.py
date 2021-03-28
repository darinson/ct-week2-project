class parkingGarage():
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTickets = {}

    def takeTicket(self):

        if self.tickets == []:
            print("Garage is full.")
            return parkingGarage

        print("Here the available tickets: ", self.tickets)
        ticketnum = int(input('Choose a ticket number: '))
        if ticketnum not in self.tickets:
            print("Ticket not available.")
            print("Here the available tickets: ", self.tickets)
            ticketnum = int(input('Please enter valid ticket number: '))

        self.tickets.remove(ticketnum)
        self.parkingSpaces.remove(ticketnum)
        self.currentTickets[ticketnum] = ""
        print("Current tickets pulled: [{}]".format(
            ','.join([str(key) for key in self.currentTickets.keys()])))

    def payForParking(self):
        ticketnum = int(input('Please choose your ticket: '))
        if ticketnum not in self.currentTickets.keys():
            print("Ticket not found, here are the available tickets: [{}]".format(
                  ','.join([str(key) for key in self.currentTickets.keys()])))
            ticketnum = int(input('Please enter valid ticket: '))

        amount = (input('Please enter payment amount of $20: '))
        # if isinstance(self.amount, str):
        # amount = input('Please enter a number: ')
        if float(amount) < 20:
            amount = float(input('Please enter a valid amount: '))

        if float(amount) > 20:
            print("Thank you for your donation.")

        if ticketnum in self.currentTickets.keys():
            self.currentTickets[ticketnum] = "Paid"
            print("Ticket has been paid. You now have 15 minutes to leave.")

    def leaveGarage(self):
        ticketnum = int(input('Please enter your ticket number: '))
        if ticketnum not in self.currentTickets.keys():
            print("Ticket not found, here are the available tickets: [{}]".format(
                  ','.join([str(key) for key in self.currentTickets.keys()])))
            ticketnum = int(input('Please enter a valid ticket: '))
        if self.currentTickets[ticketnum] != "Paid":
            amount = float(
                input('Ticket has not been paid, please enter a payment of $20:'))
           # if isinstance(self.amount, str):
            #    amount = input('Please enter a number: ')
            if float(amount) < 20:
                amount = float(input('Please enter the valid amount: '))

            if float(amount) > 20:
                print("Thank you for your donation.")
        del self.currentTickets[ticketnum]

        print("Your ticket has been paid.\nThank you, have a nice day")
        self.tickets.append(ticketnum)
        self.tickets = sorted(self.tickets)
        self.parkingSpaces.append(ticketnum)
        self.parkingSpaces = sorted(self.parkingSpaces)


myGarage = parkingGarage()


def runGarage():
    while True:
        response = input(
            'What would you like to do? Take ticket, pay or leave? ')
        if response.lower() == 'take ticket':
            myGarage.takeTicket()
        elif response.lower() == 'pay':
            myGarage.payForParking()
        elif response.lower() == 'leave':
            myGarage.leaveGarage()
           # if myGarage.currentTickets == {}:
            # print("All tickets paid, good bye!")
            # break


runGarage()
