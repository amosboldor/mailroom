"""Module to assist with donations."""


DONORS = {}


def send_thanks(donor_name):
    """Send formatted email to donor."""
    email = 'Thank you {} for your generous donation!'.format(donor_name)
    return(email)


def sort_donors(data=DONORS):
    """Return sorted donor data."""
    return sorted(data, key=lambda donor: data[donor]['total'], reverse=True)
