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
            donor_name = verify_name(get_name()).title()
            amount = verify_num(get_amount())
            DONORS.setdefault(donor_name, {})
            DONORS[donor_name].setdefault("history", []).append(amount)
            set_stats(DONORS[donor_name])
            print(send_thanks(donor_name))
        elif action.lower() in "create report":
            print_report(DONORS)
        elif action in QUIT:
            sys.exit()
        else:
            print('Wrong Input')


def set_stats(donor):
    """Update total donations and avg donation for a donor."""
    donor["total"] = sum(donor["history"])
    donor["num_donations"] = len(donor["history"])
    donor["avg_donation"] = donor["total"] / donor["num_donations"]


def send_thanks(donor_name):
    """Send formatted email to donor."""
    email = """\n
        Dear {},

            We thank you for your generous donation of ${:,.2f}.
            We hope that you have a fantastic life,
            and we look forward to seeing you at the charity gala this christmas.

        Sincelery,
            Barbie Corp.
    """

    return(email.format(donor_name, DONORS[donor_name]["history"][-1]))


def sort_donors(data=DONORS):
    """Return sorted donor data."""
    return sorted(data, key=lambda donor: data[donor]['total'], reverse=True)


def verify_name(name):
    """Return name from user."""
    while True:
        if name.lower() == 'list':
            for donor in DONORS.keys():
                print(donor)
        elif name.lower() in QUIT:
            main()
        else:
            return name


def get_name():
    """Ask user for donor name."""
    return inp("\nDonor's name (or 'list'):  ").title()


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


def print_report(donors):
    """Print out the all the donor data."""
    s = "{:<20}{:<20}{:<20}{:<20}"
    print(s.format('Donor', 'Total Donations', 'Avg Donation', 'Num Donations'))
    for d in donors:
        print(s.format(d.title(),
                       donors[d]['total'],
                       donors[d]['avg_donation'],
                       donors[d]['num_donations']))


if __name__ == '__main__':  # pragma: no cover
    try:
        inp = raw_input
    except NameError:
        pass
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
