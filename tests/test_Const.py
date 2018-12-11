import unittest, time
from pyconst.Const import Const

class TestConst(unittest.TestCase):
    def test_constructor_params(self):
        c = Const([])
        #TODO check that the objList thing works


    def test_object(self):
        list1 = [1,'two',3]
        list2 = [1,'two',3]

        c = Const([list1])

        list1[0] = 2
        time.sleep(.1)
        self.assertEqual(list1,list2)

        list1[1] = 'twoo'
        time.sleep(.1)
        self.assertEqual(list1,list2)

        list1 = [1,2,3]
        time.sleep(.1)
        self.assertEqual(list1,list2)


    def test_object_methods(self):
        class TestClass:
            def func(self):
                a = 3+5
                print(a)

        obj = Const([])
        obj_copy = Const([])

        c = Const([obj])

        def func(self):
            a = 3
            print(a)

        obj.run = func

        time.sleep(.1)
        self.assertEqual((obj.run.__code__.co_code),(obj_copy.run.__code__.co_code)) #This won't catch anything with same structure but different value. Probably fine

    def test_complex_object(self):
        c = Const([])
        #TODO
