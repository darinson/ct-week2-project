class parkingGarage():
    def __init__(self):
        self.tickets = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.parkingSpaces = ['1', '2', '3',
                              '4', '5', '6', '7', '8', '9', '10']
        self.currentTickets = {}

    def takeTicket(self):

        if self.tickets == []:
            print("Garage is full.")
            return parkingGarage()

        print("Here are the available tickets: ", self.tickets)
        ticketnum = (input('Choose a ticket number: '))
        while ticketnum not in self.tickets:
            print("\nTicket not available.")
            print("Here are the available tickets: ", self.tickets)
            ticketnum = (input('Please enter valid ticket number: '))

        self.tickets.remove(ticketnum)
        self.parkingSpaces.remove(ticketnum)
        self.currentTickets[ticketnum] = ""
        print("Success")

    def payForParking(self):

        if self.currentTickets == {}:
            print("Garage is empty.")
            return parkingGarage()

        ticketnum = input('Please choose your ticket: ')
        while ticketnum not in self.currentTickets.keys():
            print("Ticket not found, here are the available tickets: [{}]".format(
                  ','.join(str(k) for k in sorted([int(key) for key in self.currentTickets.keys()]))))
            ticketnum = input('Please enter valid ticket: ')

        if self.currentTickets[ticketnum] == "Paid":
            print("Ticket has already been paid.")
            return parkingGarage()

        amount = (input('Please enter payment amount of $20: '))

        while amount.isdigit() == False:
            amount = (input('Please enter a valid payment: '))

        if float(amount) < 20:
            amount = float(input('Please enter an amount of $20: '))

        if float(amount) == 20:
            print("Thank you for your payment.")

        if float(amount) > 20:
            print("Thank you for your donation, Terrell.")

        if ticketnum in self.currentTickets.keys():
            self.currentTickets[ticketnum] = "Paid"
            print("Ticket has been paid. You now have 15 minutes to leave.")

    def leaveGarage(self):

        if self.currentTickets == {}:
            print("Garage is empty.")
            return parkingGarage()

        ticketnum = input('Please enter your ticket number: ')
        while ticketnum not in self.currentTickets.keys():
            print("Ticket not found, here are the available tickets: [{}]".format(
                  ','.join(str(k) for k in sorted([int(key) for key in self.currentTickets.keys()]))))
            ticketnum = input('Please enter a valid ticket: ')

        while self.currentTickets[ticketnum] != "Paid":
            amount = input(
                'Ticket has not been paid, please enter a payment of $20:')
            while amount.isdigit() == False:
                amount = (input('Please enter a valid payment: '))

            if float(amount) < 20:
                amount = float(input('Please enter an amount of $20: '))
                self.currentTickets[ticketnum] = "Paid"

            if float(amount) == 20:
                print("Thank you for your payment.")
                self.currentTickets[ticketnum] = "Paid"

            if float(amount) > 20:
                print("Thank you for your donation, Terrell.")
                self.currentTickets[ticketnum] = "Paid"

        del self.currentTickets[ticketnum]

        print("Your ticket has been paid. Thank you, have a nice day!")
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


runGarage()
