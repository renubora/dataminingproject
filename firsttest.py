#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"


import unittest
import checkfile
import datashuffles
import random_forest



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

    def test_count_points_per_customer(self):
        estimates = datashuffles.count_points_per_customer()
        #check one customer
        six_estimates = [1, 1, 1, 1, 1, 1]
        one_estimate = [1]

        #Failing test
        #one_estimate = [1]
        #self.assertEqual(estimates['10000014'], one_estimate)

        self.assertEqual(estimates['10000014'], six_estimates)

    def test_customer_total_points(self):
        totalpoints = datashuffles.total_customer_points()



        #Failing tests
        #self.assertEqual(totalpoints['10000014'], 3)


        self.assertEqual(totalpoints['10000014'], 6)


    def test_another_customer(self):
        totalpoints = datashuffles.total_customer_points()

        #Failing tests
        #self.assertEqual(totalpoints['10000000'], 3)

        self.assertEqual(totalpoints['10000000'], 9)

### test data issues for figuring out random forest classifer
    def test_list_of_dictionary_should_have_three_items(self):
        testlist = random_forest.make_list_of_dictionaries()
        #Failing tests
        #self.assertEqual(len(testlist), 4)

        self.assertEqual(len(testlist), 3)

    def test_make_sure_dictionary_data_works(self):
        testlist = random_forest.make_list_of_dictionaries()

        #Failing tests
        #self.assertEqual(testlist[1]['age_oldest'],'99')

        self.assertEqual(testlist[1]['age_oldest'],'28')





if __name__ == '__main__':
    unittest.main()

