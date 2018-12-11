import _thread
import time
import pickle

class Const:
    def __init__(self, objList, shame="Shame on you for try to change my object"):
        self.objList = objList
        self.shame = shame

        objListConstCopy = [pickle.loads(pickle.dumps(obj)) for obj in objList]
        self.objListConstCopy = objListConstCopy

        _thread.start_new_thread(self.run , ())


    def run(self):
        # do the thing
        while True:
            time.sleep(10)
            print(shame) #TODO: only print when the objects differ
            print( pickle.dumps(self.objList) == pickle.dumps(self.objListConstCopy) )

            pass
