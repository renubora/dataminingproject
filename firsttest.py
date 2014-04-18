#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"


import unittest
import checkfile




class TestHeader(unittest.TestCase):
    def test_checkheader(self):

        #print checkfile.checkheader()
        #Failing test
        #self.assertEqual(checkfile.checkheader(),'Dcustomer_ID')

        self.assertEqual(checkfile.checkheader(),'customer_ID')






if __name__ == '__main__':
    unittest.main()





