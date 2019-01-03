import _thread
import dill

class Const:
    def __init__(self, objList, shame="Shame on you for try to change my object"):

        self.objList = objList
        self.shame = shame

        self.dump = dill.dumps(objList)

        _thread.start_new_thread(self.run , ())

    def run(self):
        while True:
            if dill.dumps(self.objList) != self.dump:
                print(self.shame)
                load = dill.loads(self.dump)
                for index, obj in enumerate(self.objList):                       
                        self.objList[index] = load[index]
