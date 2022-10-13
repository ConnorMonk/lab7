



#unit testing for storedb.py

import unittest
import storedb.py


class CharCounterTestCase(unittest.TestCase):

    def setUp(self):
        self.__db = create("testdb")

    def tearDown(self):
        del self.__db

    def test_init(self):
        text = "tesing123"
        
        # create an object that we will use in this testing
        p = CharacterCounter(text)
        
        # use the testing framework assertions to check results
        self.assertEqual(p.text, text, "'text' does not match input")
        
        # need to test that an exception is raised when given a bad parameter!
        # any other tests?


    def addProduct(dbName, productName, price, categoryID, description):
        