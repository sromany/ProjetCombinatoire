# coding: utf-8
from rules.AbstractRule import AbstractRule

class ConstanteRule(AbstractRule):
    def __init__(self, object):
        super().__init__()
        self._object = object
    # Ici Epsilon Rules n'est pas connu...
    # Possiblement ça peut exploser
    def valuation(self):
        if(isinstance(self, self.subclass[0])):
            return 0
        else:
            return 1

class EpsilonRule(ConstanteRule):
    def __init__(self, object):
        super().__init__(object)
    
    def count(n):
        if n==0:
            return 1
        else:
            return 0


class SingletonRule(ConstanteRule):
        def __init__(self, object):
            super().__init__(object)

        def count(n):
            if n==1:
                return 1
            else:
                return 0

ConstanteRule.subclass =[EpsilonRule,SingletonRule]


if __name__ == '__test_classic__' or __name__ == '__main__':
    print("Cas de tests ConstanteRule:")

    print("Pass")
