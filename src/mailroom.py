"""Module to assist with donations."""
import sys
import os


DONORS = {}
QUIT = ['quit', 'exit', 'q']


def main():  # pragma: no cover
    """Entry point."""
    try:
        start_banner()
        mailroom()
    except KeyboardInterrupt:
        sys.exit()


def start_banner():  # pragma: no cover
    """Initial screen output."""
    os.system('clear')
    banner = ''
    title = ''
    term_size = os.get_terminal_size()[0]
    for i in range(term_size):
        banner += '='
    for i in range(term_size // 2 - 8):
        title += ' '
    title += "MAILROOM MADNESS"
    print(banner + '\n\n' + title + '\n\n' + banner)
    print("Enter 'q' to quit / go back. Single words work for initial prompt.")


def mailroom():  # pragma: no cover
    """Main function that call other functions."""
    while True:
        action = input("\nSend thank you email or create report:  ")
        if action.lower() in "send thank you email":
            print(send_thanks())
        elif action.lower() in "create report":
            print(create_report())
        elif action in QUIT:
            sys.exit()
        else:
            print('Invalid Input')


def send_thanks():  # pragma: no cover
    """Handle sending thank you email to donor."""
    donor_name = verify_name(get_name()).title()
    amount = verify_num(get_amount())
    DONORS.setdefault(donor_name, {})
    DONORS[donor_name].setdefault("history", []).append(amount)
    set_stats(DONORS[donor_name])
    return(format_email(donor_name))


def set_stats(donor):
    """Update total donations and avg donation for a donor."""
    donor["total"] = sum(donor["history"])
    donor["num_donations"] = len(donor["history"])
    donor["avg_donation"] = donor["total"] / donor["num_donations"]
    return donor


def format_email(donor_name, don=DONORS):
    """Send formatted email to donor."""
    email = """\n
        Dear {},

            We thank you for your generous donation of ${:,.2f}.
            We hope that you have a fantastic life,
            and we look forward to seeing you at the charity gala.

        Sincelery,
            Barbie Corp.
    """

    return(email.format(donor_name.title(), don[donor_name]["history"][-1]))


def sort_donors(data=DONORS):
    """Return sorted donor data."""
    return sorted(data, key=lambda donor: data[donor]['total'], reverse=True)


def verify_name(name):
    """Return name from user."""
    if name.lower() == 'list':
        for donor in DONORS.keys():
            print(donor)
        return verify_name(get_name())
    elif name.lower() in QUIT:
        main()
    else:
        return name


def get_name():
    """Ask user for donor name."""
    return input("\nDonor's name (or 'list'):  ").title()


def get_amount():
    """Take user input."""
    return input("\n    Donation Amount:  ")


def verify_num(user_input):
    """Return amount entered."""
    try:
        user_input = float(user_input)
    except ValueError:
        if user_input.lower() in QUIT:
            main()
        else:
            print('Invalid Input')
            return verify_num(get_amount())
    else:
        return user_input


def create_report(donors=DONORS):
    """Print out the all the donor data."""
    header_s = "\t{:<20}{:<20}{:<20}{:<20}"
    donor_s = "\t{:<20}{:<20,.2f}{:<20,.2f}{:<20}"
    report = '\n'
    report += header_s.format('Donor',
                              'Total Donations',
                              'Avg. Donation',
                              'Num. Donations') + '\n'
    for d in donors:
        report += '\n' + donor_s.format(d.title(),
                                        donors[d]['total'],
                                        donors[d]['avg_donation'],
                                        donors[d]['num_donations'])
    return report


if __name__ == '__main__':  # pragma: no cover
    main()
