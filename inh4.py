class A:
    def get(self):
        print("this is get class A . ")

class B:
    def put(self):
        print("this is put class B..")
    
    def get(self):
        print("this is a  get 2nd")
        
class C(A,B):
    def display(self):
        print("this is display class C...")
        print("y:", self.y)

        objb=B()
        objb.get()


objc=C()
objc.y=500
objc.get()
objc.display()


# his is get class A .
# this is display class C...
# y: 500
# this is a  get 2nd

