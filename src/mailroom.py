"""Module to assist with donations."""
import sys


DONORS = {}
QUIT = ['quit', 'exit', 'q']
inp = input


def main():
    """Main function that call other functions."""
    while True:
        action = inp("\nSend thank you email or create report:  ")
        if action.lower() in "send thank you":
            donor_name = verify_name(get_name())
            amount = verify_num(get_amount())
            DONORS.setdefault(donor_name, []).append(amount)
            set_stats(DONORS[donor_name])
            send_thanks(donor_name)
        elif action.lower() in "create report":
            print(format(sort_donors()))
        elif action in QUIT:
            sys.exit()
        else:
            print('Wrong Input')


def set_stats(donor_name):
    """Update total donations and avg donation for a donor."""
    donor = DONORS[donor_name]
    donor["total"] = sum(DONORS[donor_name]["history"])
    donor["num_donations"] = len(donor["history"])
    donor["avg_donation"] = donor["total"] / donor["num_donations"]


def calc_avg(donor_name):
    """Return total donations for a donor."""
    return reduce(lambda x, y: x + y)


def send_thanks(donor_name):
    """Send formatted email to donor."""
    email = 'Thank you {} for your generous donation!'.format(donor_name)
    return(email)


def sort_donors(data=DONORS):
    """Return sorted donor data."""
    return sorted(data, key=lambda donor: data[donor]['total'], reverse=True)


def verify_name(name):
    """Return name from user."""
    while True:
        input = inp("\nDonor's name (or 'list'):  ")
        if input.lower() == 'list':
            for donor in DONORS.keys():
                print(donor)
        elif input.lower() in QUIT:
            main()
        else:
            return input


def get_name():
    """Ask user for donor name."""
    return inp("\nDonor's name (or 'list'):  ")


def get_amount():
    """Take user input."""
    return inp("\n    Donation Amount:  ")


def verify_num(input):
    """Return amount entered."""
    try:
        input = float(input)
    except ValueError:
        if input.lower() in QUIT:
            main()
        else:
            print('Wrong Input')
            return verify_num(get_amount())
    else:
        return input


if __name__ == '__main__':  # pragma: no cover
    try:
        inp = raw_input
    except NameError:
        pass
    main()
