"""Testing mailroom mudule."""
import pytest

AMOUNT_INPUT = [
    ['200', 200],
    ['0', 0],
    ['11.11', 11.11],
]

DICT = {
    'rick': {'history': [], 'total': 21, 'avg_donation': 200, 'num_donations': 32},
    'slim': {'history': [], 'total': 213, 'avg_donation': 200, 'num_donations': 32},
    'bob': {'history': [1], 'total': 54, 'avg_donation': 200, 'num_donations': 32},
    'jack': {'history': [], 'total': 3, 'avg_donation': 200, 'num_donations': 32}
}

def test_send_thanks():
    """Test out output of thank email."""
    from mailroom import send_thanks
    email = send_thanks('bob', DICT)
    assert email == """\n
        Dear bob,

            We thank you for your generous donation of $1.00.
            We hope that you have a fantastic life,
            and we look forward to seeing you at the charity gala this christmas.

        Sincelery,
            Barbie Corp.
    """


def test_sort_donors():
    """Testing if sort function sort by ammount."""
    from mailroom import sort_donors
    dict_sorted = ['slim', 'bob', 'rick', 'jack']
    assert dict_sorted == sort_donors(data=DICT)


@pytest.mark.parametrize('inp, output', AMOUNT_INPUT)
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
    report = print_report(DICT)
    assert 'Rick' in report and 'Slim' in report and 'Bob' in report and 'Jack' in report
