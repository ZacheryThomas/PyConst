import _thread
import time
class Const:
    def __init__(self, objList=None):
        if objList is not None:
            self.objList = objList
            pass
        else:
            self.objList = []

        _thread.start_new_thread(self.run , ())

    def run(self):
        # do the thing
        while True:
            time.sleep(1)
            print("running...") #TODO: remove
            pass
        
        
        
