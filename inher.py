class A:
    def get(self):
        self.x=100
        print("this is get class A . ")
        print("y:",self.x)
class B(A):
    def put(self):
        print("this is put class B..")
        print("x: ",self.x)
        print("y: ",self.y)
class C(B):
    def display(self):
        print("this is display class C...")
        print("y:", self.y)
objc=C()
objc.y=500
objc.get()
objc.put()