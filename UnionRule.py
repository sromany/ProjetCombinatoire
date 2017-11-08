# coding: utf-8
from functools import lru_cache
from random import randint

from ConstructorRule import ConstructorRule


class UnionRule(ConstructorRule):
   
        # On ne peut pas faire rank sur AutantAB avec notre grammaire actuelle
        # On a donc décidé de mettre ces fonctions en options
        # Si elles ne sont pas fourni, alors on ne peut pas faire de rank sur la grammaire correspondant    
    def __init__(self, fst, snd, isFst = None, size = None):
        super().__init__((fst, snd))
        # Renvoie vrai si l'objet appartient au membre de gauche de l'union, faux sinon        
        self.isFst = isFst
        # Renvoie la taille de l'objet
        self.size = size       
    
    def __repr__(self):
        return "UnionRule("+str(self._parameters[0])+", "+ str(self._parameters[1]) +")"
    
    def __str__(self):
        return "UnionRule("+str(self._parameters[0])+", "+ str(self._parameters[1]) +")"

    def _calc_valuation(self):
        valGauche = self._grammar[self._parameters[0]].valuation()
        valDroite = self._grammar[self._parameters[1]].valuation()
        return min(valGauche, valDroite)

    @lru_cache(maxsize=32)
    def count(self,i):
        countG = self._grammar[self._parameters[0]].count(i)
        countD = self._grammar[self._parameters[1]].count(i)
        return countG + countD

    @lru_cache(maxsize=32)
    def list(self,i):
        listG = self._grammar[self._parameters[0]].list(i)
        listD = self._grammar[self._parameters[1]].list(i)
        return listG + listD

    @lru_cache(maxsize=32)
    def unrank(self, n, r):
        c = self.count(n)
        if r >= c or r < 0:
            raise ValueError("Le rang r (%d) doit etre strictement inférieur au nombre d'objets de taille %d (%d) et supérieur ou égale à zero"%(r,n,c))

        countG = self._grammar[self._parameters[0]].count(n)
        if r < countG:
            return self._grammar[self._parameters[0]].unrank(n, r)
        else:
            return self._grammar[self._parameters[1]].unrank(n, r - countG)
    
    def rank(self, obj):
        # On ne peut pas faire rank sur AutantAB avec notre grammaire actuelle
        # On a donc décidé de mettre ces fonctions en options
        # Si elles ne sont pas fourni, alors on ne peut pas faire de rank sur la grammaire correspondant
        if self.isFst is None or self.size is None :
            raise Exception("Rank n'est pas autorisé sur cette grammaire")

        # Si l'objet appartient au membre de gauche (Exemple Node pour la règle "Tree":UnionRule("Node","Leaf") alors on retourne le rank de l'objet dans le membre gauche
        if self.isFst(obj):
            return self._grammar[self._parameters[0]].rank(obj)
        # Sinon, le rang de l'oject à droite, est son rang a droite plus le nombre d'objet avant lui (à gauche donc)
        else: 
            return self._grammar[self._parameters[0]].count(self.size(obj)) + self._grammar[self._parameters[1]].rank(obj)  

    def random(self, n):
        if self.count(n) == 0:
            raise Exception("Erreur sur random(%d,%s)" %(n,self))
        return self.unrank(n, randint(0,self.count(n)-1))

class Union():
    def __init__(self,fst,snd,isFst = None,size = None):
        self.union = (fst,snd,isFst,size)
    
    def __repr__(self):
        return "Union("+str(self.union[0])+", "+ str(self.union[1]) +")"
    
    def __str__(self):
        return "Union("+str(self.union[0])+", "+ str(self.union[1]) +")"

    def conv(self,gram, key = None):
        fst,snd,isFst,size = self.union
        
        k1 = fst.conv(gram)
        k2 = snd.conv(gram)
        # On vérifie que cette règle n'est pas déjà dans la grammaire
        for k in gram.keys():
            if isinstance(gram[k],UnionRule):
                if gram[k]._parameters[0] == k1 and gram[k]._parameters[1] == k2:
                    return k
        if key is None:
            key = "Union-"+str(len(gram))
        gram[key] = UnionRule(k1,k2,isFst,size)
        return key


if __name__ == '__test_classic__' or __name__ == '__main__':
    print("Cas de tests UnionRule:")
    cle = (0, 1)
    a,b = cle

    print(cle)
    print(a, sep="/")




    print("Pass")
