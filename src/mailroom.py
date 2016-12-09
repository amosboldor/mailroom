"""Module to assist with donations."""


DONORS = {}


def main():
    """Main function that call other functions."""
    while True:
        action = raw_input("Send a thank you or Create a report")
        if action.lower() == "send a thank you":
            donor_name = get_name()
            DONORS.setdefault(donor_name, []).append(get_amount())
            send_thanks(donor_name)
        elif action.lower() == "create a report":
            print(sorted_donors())
        elif action.quit == "quit":
            exit()
        else:
            print('Wrong Input')


def send_thanks(donor_name):
    """Send formatted email to donor."""
    email = 'Thank you {} for your generous donation!'.format(donor_name)
    return(email)


def sort_donors(data=DONORS):
    """Return sorted donor data."""
    return sorted(data, key=lambda donor: data[donor]['total'], reverse=True)


def get_name():
    """Return name from user."""
    while True:
        input = raw_input("Donor's name (or 'list'): ")
        if input.lower() == 'list':
            for donor in DONORS.keys():
                print(donor)
        elif input.lower() == 'quit':
            main()
        else:
            return input


def get_amount():
    """Return amount entered."""
    while True:
        input = raw_input("Donation Amount: ")
        if type(input) is int:
            return input
        elif input.lower() == 'quit':
            main()
        else:
            print('Wrong Input')


def print_report(donors):
    """Print out the all the donor data."""
    s = "{:<20}{:<20}{:<20}{:<20}"
    print(s.format('Donor', 'Total', 'Avg', 'Num'))
    for d in donors:
        print(s.format(d.title(),
                       donors[d]['total'],
                       donors[d]['avg_donation'],
                       donors[d]['number_of_donations']))
