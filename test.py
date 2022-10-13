



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
        
        storedb.addProduct("test.db", "badname", 4.20, 3, "bad description")
        
        c.execute("SELECT * FROM Product ORDER BY rowid DESC LIMIT 1;")
        
        addedproduct = c.fetchall()
        print(addedproduct)
        self.assertTrue(len(addedproduct[0][1]) > 0, "name cannot be empty")
        self.assertIsInstance(addedproduct[0][1], str, "name must be a string")
        self.assertTrue(len(addedproduct[0][4]) > 0, "description cannot be empty")
        self.assertIsInstance(addedproduct[0][4], str, "description must be a string")
        
        self.assertTrue(addedproduct[0][2] > 0, "price must be greater than 0")
        self.assertIsInstance(addedproduct[0][2], float, "price must be a float")
        
        c.execute("SELECT rowid from Category;")
        validRowIds = c.fetchall()
        valididlist = []
        for elem in validRowIds:
            valididlist.append(elem[0])
        print(valididlist)
        
        self.assertTrue(addedproduct[0][3] in valididlist, "invalid categoy ID")
        

if __name__ == '__main__':
    unittest.main()