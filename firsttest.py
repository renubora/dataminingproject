#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"


import unittest
import checkfile
import datashuffles



class TestHeader(unittest.TestCase):
    def test_checkheader(self):

        #print checkfile.checkheader()
        #Failing test
        #self.assertEqual(checkfile.checkheader(),'Dcustomer_ID')

        self.assertEqual(checkfile.checkheader(),'customer_ID')

class TestShoppingCounts(unittest.TestCase):
    def test_put_csv_in_shoplist(self):
        testlist = datashuffles.put_csv_in_shoplist()

        #Failing test
        #self.assertEqual(len(testlist), 99)

        self.assertEqual(len(testlist), 100)

    def test_remove_header(self):
        headlesslist = datashuffles.remove_header()

        #Failing test
        #self.assertEqual(len(testlist), 100)

        self.assertEqual(len(headlesslist), 99)



if __name__ == '__main__':
    unittest.main()

