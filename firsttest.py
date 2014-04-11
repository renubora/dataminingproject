#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"

import checkfile


if __name__ == '__main__':
   
# Just to test the build works
	print "Build tool seems to work."


#FailingTest
#assert checkfile() == 'cust'

#PassingTest
	assert checkfile.checkheader() == 'customer_ID'
	print "test passed"

# Test unit test now with snap-ci
#assert "customer_ID,shopping_pt,record_type,day,time,state,location,group_size,homeowner,car_age,car_value,risk_factor,age_oldest,age_youngest,married_couple,C_previous,duration_previous,A,B,C,D,E,F,G,cost,total_change,cum_change,old_A,old_B,old_C,old_D,old_E,old_F,old_G,old_C_previous" = OutputFirstHeaderItem()

# will do this later- switch to unit testing for project- figure out
# Pycharm  maybe (though that might be too automated. Pyscripter seems too automated for learning but we'll see)

