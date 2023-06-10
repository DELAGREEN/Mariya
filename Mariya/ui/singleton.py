'''
Синглтон в реализации Гвидо Ванросума
управляет инстансами обьектов
тем самым не дает вызывать больше ОДНОГО экземпляра класса 
'''
###WARNING###
###Втупую скопировано###

class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it
            
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it
        
    def init(self, *args, **kwds):
        pass