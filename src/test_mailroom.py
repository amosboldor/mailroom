"""Testing mailroom mudule."""


def test_send_thanks():
    """Test out output of thank email."""
    from mailroom import send_thanks
    email = send_thanks('bob')
    assert email == 'Thanks bob for your generous donation!'


def test_sort_donors():
    """Testing if sort function sort by ammount."""
    from mailroom import sort_donors
    dict = {
        'rick': {'history': [], 'total_donations': 21, 'avg_donation': 200},
        'slim': {'history': [], 'total_donations': 213, 'avg_donation': 200},
        'bob': {'history': [], 'total_donations': 54, 'avg_donation': 200},
        'jack': {'history': [], 'total_donations': 3, 'avg_donation': 200}
    }
    dict_sorted = {
        'slim': {'history': [], 'total_donations': 213, 'avg_donation': 200},
        'bob': {'history': [], 'total_donations': 54, 'avg_donation': 200},
        'rick': {'history': [], 'total_donations': 21, 'avg_donation': 200},
        'jack': {'history': [], 'total_donations': 3, 'avg_donation': 200}
    }
    assert dict_sorted == sort_donors(test=dict)
