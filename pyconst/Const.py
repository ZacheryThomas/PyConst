import _thread
import time
import pickle

class Const:
    def __init__(self, objList):
        self.objList = objList

        objListConstCopy = [pickle.loads(pickle.dumps(obj)) for obj in objList]
        self.objListConstCopy = objListConstCopy

        _thread.start_new_thread(self.run , ())


    def run(self):
        # do the thing
        while True:
            time.sleep(10)
            print("running...") #TODO: remove
            print( pickle.dumps(self.objList) == pickle.dumps(self.objListConstCopy) )

            pass
