### the object which can be handled by 'with' must have __enter__() and __exit__() methods

class Sample:
    def __enter__(self):
        print("enter")
        return 0
    
    def __exit__(self, exc_type, exc_val, exc_tb): ### must have these arguments
        ### exc_type is error type; exc_val is error value; exc_tb is the location where the error happened
        print("exit")


with Sample() as sample:
    print("sample", sample)