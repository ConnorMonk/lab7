



#unit testing for storedb.py

import sqlite3
import unittest
import storedb
import os


class testSqliteDb(unittest.TestCase):

    def setUp(self):
        self.__db = storedb.create("test.db")
        self.__db = storedb.fill("test.db")

    def tearDown(self):
        os.remove("test.db")

    def testAddProduct(self):
        
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        
        storedb.addProduct("test.db", "badname", 4.20, 5, "bad description")
        
        self.assertTrue(len(storedb.addProduct.productName) > 0, "name cannot be empty")
        self.assertIsInstance(productName, str, "name must be a string")
        self.assertTrue(len(description) > 0, "description cannot be empty")
        self.assertIsInstance(description, str, "description must be a string")
        
        self.assertTrue(price > 0, "price must be greater than 0")
        self.assertIsInstance(price, float, "price must be a float")
        
        c.execute("SELECT rowid from Category;")
        validRowIds = c.fetchall()
        self.assertTrue(categoryID in validRowIds, "invalid categoy ID")
        

if __name__ == '__main__':
    unittest.main()