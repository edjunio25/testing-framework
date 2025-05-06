from TestCase import TestCase
from ExampleTests import MyTest

test = MyTest('test_a')
test.run()

test = MyTest('test_b')
test.run()

test = MyTest('test_c')
test.run()

#execute with: python RunSection2.py
#set_up
#test_a
#tear_down
#set_up
#test_b
#tear_down
#set_up
#test_c
#tear_down