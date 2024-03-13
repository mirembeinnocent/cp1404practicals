from guitar import Guitar


def test_guitar():

    # Create sample guitars
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000)

    # Test get_age() method
    assert gibson.get_age(2022) == 100
    assert another_guitar.get_age(2022) == 9

    # Test is_vintage() method
    assert gibson.is_vintage(2022) == True
    assert another_guitar.is_vintage(2022) == False

    print("All tests passed!")


test_guitar()


