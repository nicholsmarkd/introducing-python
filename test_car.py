import car


def test_brake():
    assert car.brake() == 'brake'


def test_go():
    assert car.go().upper() == 'GO'
