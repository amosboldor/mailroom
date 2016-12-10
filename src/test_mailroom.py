"""Testing mailroom mudule."""
import pytest
import sys
import mailroom


NUMS = [
    ['200', 200],
    ['0', 0],
    ['11.11', 11.11],
]


NAMES = [
    ['billy', 'billy'],
    ['Wanda Sykes', 'Wanda Sykes']
]


DICT = {
    'rick': {'history': [100, 6, 40, 22], 'total': 21,
             'avg_donation': 200, 'num_donations': 2},
    'slim': {'history': [11], 'total': 213,
             'avg_donation': 200, 'num_donations': 32},
    'bob flannery': {'history': [1], 'total': 54,
                     'avg_donation': 2000, 'num_donations': 32},
    'jack': {'history': [33000], 'total': 3,
             'avg_donation': 1, 'num_donations': 32}
}

REPORT = [
    ['Donor', 'Total', 'Donations', 'Avg.', 'Donation', 'Num.', 'Donations'],
    ['Slim', '213', '200', '32'],
    ['Jack', '3', '1', '32'],
    ['Rick', '21', '200', '2'],
    ['Bob', 'Flannery', '54', '2000', '32']
]


def test_format_email():
    """Test out output of thank email."""
    from mailroom import format_email
    email = format_email('bob flannery', DICT)
    assert email == """\n
        Dear Bob Flannery,

            We thank you for your generous donation of $1.00.
            We hope that you have a fantastic life,
            and we look forward to seeing you at the charity gala.

        Sincelery,
            Barbie Corp.
    """


def test_sort_donors():
    """Testing if sort function sort by ammount."""
    from mailroom import sort_donors
    dict_sorted = ['slim', 'bob flannery', 'rick', 'jack']
    assert dict_sorted == sort_donors(data=DICT)


@pytest.mark.parametrize('name, res', NAMES)
def test_verify_name(name, res):
    from mailroom import verify_name
    assert verify_name(name) is res


@pytest.mark.parametrize('inp, output', NUMS)
def test_verify_num(inp, output):
    """Test verify_num catches non-number input."""
    from mailroom import verify_num
    assert output == verify_num(inp)


def test_invalid_verify_num():
    """Verify verify_num raises exception if input is not a number."""
    from mailroom import verify_num
    with pytest.raises(Exception):
        verify_num('NOTAnumber12e')


def test_print_report():
    """Test the print_report output."""
    from mailroom import print_report
    report = print_report(DICT).split()
    for m in REPORT:
        for n in m:
            assert n in report


def test_set_stats():
    """Test set_stats."""
    from mailroom import set_stats
    assert set_stats(DICT['rick']) == {
        'history': [100, 6, 40, 22],
        'total': 168,
        'avg_donation': 42,
        'num_donations': 4}






