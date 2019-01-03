import unittest, time
from pyconst.Const import Const

class TestConst(unittest.TestCase):
    def test_constructor_params(self):
        c = Const([])
        #TODO check that the objList thing works


    def test_object(self):
        list1 = [1,'two',3]
        list2 = [1,'two',3]

        c = Const(list1)

        list1[0] = 2
        time.sleep(.1)
        self.assertEqual(list1,list2)

        list1[1] = 'twoo'
        time.sleep(.1)
        self.assertEqual(list1,list2)


    def test_complex_object(self):
        obj_list = [Const([])]
        obj_list_copy = [Const([])]

        c = Const(obj_list)

        def run(self):
            obj_list = [Const([])]
            obj_list_copy = [Const([])]

            c = Const(obj_list)

        obj_list[0].run = run
        #TODO investigate why shame sometimes prints multiple times in this test??

        time.sleep(.1)
        self.assertEqual((obj_list[0].run.__code__.co_code),(obj_list_copy[0].run.__code__.co_code)) #This won't catch anything with same structure but different value. Probably fine
