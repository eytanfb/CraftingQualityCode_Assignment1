import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_empty_list(self):
        """Tests stock_price_summary with empty list"""
        expected = (0.0, 0.0)
        actual = a1.stock_price_summary([])
        self.assertEquals(expected, actual)
    
    def test_list_with_one_positive_change(self):
        """Tests stock_price_summary with for one change"""
        positive_change = 1.32
        expected = (positive_change, 0.0)
        actual = a1.stock_price_summary([1.32])
        self.assertEquals(expected, actual)

    def test_list_with_one_negative_vhange(self):
        """Test stock_price_summary with one negative change"""
        negative_change = -1.32
        expected = (0.0, negative_change)
        actual = a1.stock_price_summary([-1.32])
        self.assertEquals(expected, actual)
        
    def test_list_with_multiple_values(self):
        """Test the function with multiple values both positive and negative"""
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        expected = (0.14, -0.17)
        actual = a1.stock_price_summary(price_changes)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
