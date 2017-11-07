# coding: utf-8
from AbstractRule import AbstractRule

class ConstanteRule(AbstractRule):
    def __init__(self, object):
        super().__init__()
        self._object = object
    
    def check(self,key):
      return True
    
    def valuation(self):
        if(isinstance(self, self.subclass[0])):
            return 0
        else:
            return 1

    def unrank(self, n, r):
        c = self.count(n)
        if r >= c:
            raise ValueError("Le rang r (%d) doit etre strictement inférieur au nombre d'objets de taille %d (%d)"%(r,n,c))

        return self._object

    def rank(self, obj):
        return 0

class EpsilonRule(ConstanteRule):
    def __init__(self, object):
        super().__init__(object)
    
    def __repr__(self):
        return "EpsilonRule("+str(self._object)+")"
    
    def __str__(self):
        return "EpsilonRule("+str(self._object)+")"

    def count(self, n):
        if n==0:
            return 1
        else:
            return 0
    
    def list(self, n):
        if n == 0:
            return [self._object]
        else:
            return []


class SingletonRule(ConstanteRule):
        def __init__(self, object):
            super().__init__(object)

        def __repr__(self):
            return "SingletonRule("+str(self._object)+")"

        def __str__(self):
            return "SingletonRule("+str(self._object)+")"

        def count(self, n):
            if n==1:
                return 1
            else:
                return 0

        def list(self,n):
            if n == 1:
                return [self._object]
            else:
                return []


ConstanteRule.subclass = [EpsilonRule, SingletonRule]

class Epsilon():
    def __init__(self,object):
        self._object = object
    
    def __repr__(self):
        return "Epsilon("+str(self._object)+")"
    
    def __str__(self):
        return "Epsilon("+str(self._object)+")"

    def conv(self,gram, key = None):
        # On vérifie que cette règle n'est pas déjà dans la grammaire
        for k in gram.keys():
            if isinstance(gram[k],EpsilonRule):
                if gram[k]._object == self._object:
                    return k
        if key is None:
            key = "Eps-"+str(len(gram))
        gram[key] = EpsilonRule(self._object)
        return key

class Singleton():
    def __init__(self,object):
        self._object = object

    def __repr__(self):
        return "Singleton("+str(self._object)+")"

    def __str__(self):
        return "Singleton("+str(self._object)+")"

    def conv(self,gram, key = None): 
        # On vérifie que cette règle n'est pas déjà dans la grammaire     
        for k in gram.keys():
            if isinstance(gram[k],SingletonRule):
                if gram[k]._object == self._object:
                    return k
  
        if key is None:
            key = "Sing-"+str(len(gram))
        gram[key] = SingletonRule(self._object)
        return key


if __name__ == '__test_classic__' or __name__ == '__main__':
    print("Cas de tests ConstanteRule:")
    a = object()
    b =  object()
    rule = ConstanteRule(a)
    assert (rule._grammar == {})
    assert (rule._object == a)

    rule1 = EpsilonRule(a)
    rule2 = SingletonRule(b)
    b1 = isinstance(rule1, EpsilonRule) and issubclass(type(rule1), ConstanteRule)
    b2 = isinstance(rule2, SingletonRule) and issubclass(type(rule2), ConstanteRule)
    assert (b1 and rule1.valuation() == 0)
    assert (b2 and rule2.valuation() == 1)

    print("Pass")