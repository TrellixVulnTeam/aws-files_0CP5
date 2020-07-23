from snapshot_practice.file import add_two_numbers

def test_add_two_number(snapshot):

    return_value = add_two_numbers(1, 2)

    snapshot.assert_match(return_value, 'gpg_reponse')
