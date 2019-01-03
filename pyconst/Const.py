import _thread
import time
import pickle

class Const:
    def __init__(self, objList, shame="Shame on you for try to change my object"):
        print('----')
        print('classobj:', id(objList))
        print('----')
        self.objList = objList
        self.shame = shame

        objListConstCopy = [pickle.loads(pickle.dumps(obj)) for obj in objList]
        self.objListConstCopy = objListConstCopy

        _thread.start_new_thread(self.run , ())


    def run(self):
        # do the thing
        while True:
            # time.sleep(10)
            #print(self.objList)
            #print(self.shame) #TODO: only print when the objects differ
            #print( pickle.dumps(self.objList) == pickle.dumps(self.objListConstCopy) )

            for index, enum in enumerate(self.objList):
                # print(self.objList[index], self.objListConstCopy[index])
                if pickle.dumps(self.objList[index]) != pickle.dumps(self.objListConstCopy[index]):
                    # print('----')
                    print(self.objList[index],self.objListConstCopy[index])
                    #print('----')
                    self.objList[index] = pickle.loads(pickle.dumps(self.objListConstCopy[index]))
                    print(self.objList[index],self.objListConstCopy[index])

            pass
