import unittest, time
from Const import Const

class TestDetectionEvent(unittest.TestCase):
    def test_constructor_params(self):
        c = Const()
        #TODO check that the objList thing works

    def test_add_obj(self):
        c = Const()
        int1 = 3
        c.add_obj(int1)
        #TODO

    def test_basic_values(self):
        c = Const()
        int1 = 3
        int2 = 3
        c.add_obj(int1)
        int1 = 4
        time.sleep(.1)
        self.assertEqual(int1,int2)

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

        obj = TestClass()
        obj_copy = TestClass()

        c = Const([obj])

        def func(self):
            a = 3
            print(a)

        obj.func = func

        time.sleep(.1)
        self.assertEqual((obj.func.__code__.co_code),(obj_copy.func.__code__.co_code)) #This won't catch anything with same structure but different value. Probably fine

    def test_complex_object(self):
        c = Const()
        #TODO
