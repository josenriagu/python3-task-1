import unittest
# importing additional methods, alternatively, from client3 import * will import all methods and main
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], ( quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    
    """ ------------ Add more unit tests ------------ """
    def test_getRatio_calculateRatio(self):
        price_a = 110.31
        price_b = 112.035
        # expected outputs for test cases
        equal = 0.9846030258401393
        notEqual = 0.9846
        almostEqual = 0.984603025840
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getRatio(price_a, price_b), equal)
        # eureka! it worked, let's do more!!
        self.assertNotEqual(getRatio(price_a, price_b), notEqual)
        self.assertAlmostEqual(getRatio(price_a, price_b), almostEqual)

    def test_getRatio_calculateRatioPriceAEqualToZero(self):
        price_a = 0
        price_b = 112.035
        equal = 0
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getRatio(price_a, price_b), equal)

    def test_getRatio_calculateRatioPriceBEqualToZero(self):
        price_a = 110.31
        price_b = 0
        equal = None
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getRatio(price_a, price_b), equal)
        # the assertion above is similar to assertIsNone which expects a return value of None
        self.assertIsNone(getRatio(price_a, price_b))


if __name__ == '__main__':
    unittest.main()
