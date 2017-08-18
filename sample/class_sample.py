#sample using GET
class Toto:

    def __init__(self,iparam,sparam,lparam):
        self.GET = {'my_int':iparam,
                    'my_string':sparam,
                    'my_list':lparam}
    
    def SET(self,key,value):
        self.GET[key]=value

    def __repr__(self):
        return self.GET.__repr__()

    def extract(self,l):
        return [self.GET[x] for x in l]

#sample using __dict__
class Tata:

    def __init__(self,iparam,sparam,lparam):
        self.index = iparam
        self.word = sparam
        self.indexes = lparam

    def __repr__(self):
        return str(self.__dict__)

class Test:
    def fun1(self):
        return 'toto'
    def fun2(self):
        return 'tata'

    

if __name__ == '__main__':
    toto = Toto(8,'toto',[1,2,3,6,89])
    print(toto)
    toto.GET['my_list']
    i,s = toto.extract(['my_int','my_string'])
    print(str(i))
    print(s)

    tata = Tata(56,'tata',[45,54,21,56])
    print(tata)
