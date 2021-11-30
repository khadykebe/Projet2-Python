class Noeud:

    def __init__(self,name) -> None:
        self.name = name
        self.attribut = {}
        self.listNomVoisin = []

    def setAttribut(self,key,values):
        self.attribut = {key:values}

    def getAttribut(self,key):
        return key
        
    def getName(self):
        return self.name
        
    def egal(self,noeud):
        if self.name == noeud.name:
            print("les deux nodes sont egeaux")
        else:
            print("les deux nodes ne sont pas egeaux")
        
    def getCoutMin(self):
        pass

    def getCout(self,noeud):
        return noeud.cout
    

