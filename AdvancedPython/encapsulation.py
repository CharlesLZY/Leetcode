class Sample:
    def __init__(self):
        self.__private = 0
        self.public = 1
        self.__getPrivate()
    
    def __getPrivate(self):
        print(self.__private)
    
    def getPublic(self):
        print(self.public)

    def __test__(self):
        print("OK")


test = Sample()
# test.__getPrivate() ### attribute and method with __ prefix can not be called outside the class
# test.getPublic()
test.__test__()