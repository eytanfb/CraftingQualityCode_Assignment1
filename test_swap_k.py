import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_empty_list(self):
        """Testing with empty list. The function should still return empty list for any k"""
        L = list()
        k = 0
        L_expected = list()
        
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
        k = 1
        
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
        k = 2
        
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
    def test_single_element_list(self):
        """Testing with single element. The list should return the same"""
        L = [1.0]
        k = 0
        L_expected = [1.0]
        
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
        k = 1
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
    def test_two_elements_swap(self):
        """Test two elements with k = 1, should reverse the list"""
        L = [1, 2]
        k = 1
        L_expected = [2, 1]
        
        a1.swap_k(L, k)
        self.assertEquals(L_expected, L)
        
    def test_two_elements_not_swapping(self):
        """Test two elements where k is bigger than len(L)"""
        self.fail()

if __name__ == '__main__':
    unittest.main(exit=False)
