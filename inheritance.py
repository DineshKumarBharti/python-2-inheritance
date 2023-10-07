class A:
    def get(self):
        self.x=100
        print("this is get class A . ")
        print("get -",self.x)
class B(A):
    def put(self):
        print("this is put class B")
        print("put - ",self.x)
objb=B()
objb.get()
objb.put()