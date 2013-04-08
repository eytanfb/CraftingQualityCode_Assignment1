import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_0_people_should_return_0_buses(self):
        """Checks lower boundry given by precondition"""
        expected = 0
        actual = a1.num_buses(0)
        self.assertEquals(expected, actual)

    def test_50_people_should_return_1_bus(self):
        """Checks the first meaningful boundry"""
        expected = 1
        actual = a1.num_buses(50)
        self.assertEquals(expected, actual)
        
    def test_75_people_should_return_2_buses(self):
        """Checks a middle number"""
        expected = 2
        actual = a1.num_buses(75)
        self.assertEquals(expected, actual)
        
    def test_1000_people_should_return_20_buses(self):
        """Checks a bigger number as valuable input"""
        expected = 20
        actual = a1.num_buses(1000)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
