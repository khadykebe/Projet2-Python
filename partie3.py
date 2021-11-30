"""____________________________________________________________________________

    Classe Pile: voir les definitions ci-dessous
    Dernier arrive premier servi : LIFO
    La classe dispose d'une structure de type list pour ranger les données
    Les consultations, les insertions, les suppressions se font du même cote                                         
    _____________________________________________________________________________
"""
class Pile():

    def __init__(self):
        self.elements = []

    #pour voir la pile entière
    def voirPile(self):
        return self.elements

    #Insere un objet en tete de la pile 
    def push(self, element):
        self.elements.insert(0,element)

    #Retourne True si un noeud est dans la pile
    def contains_noeud(self, noeud):
        return noeud in self.elements
    
    #Retourne true si la pile est vide
    def empty(self):
        return self.elements == []

    #Retourne et supprime l'element en tete de pile
    #Retourne une exception si la pile est vide
    def remove(self):
        return self.elements.pop(0)

    

"""____________________________________________
                                            
    Test des structures de données Pile et File 
    ____________________________________________
"""
print("\n")
print("=========Pile(LIFO:Last In First Out)================")
#instanciation de la pile
pile=Pile()
print("\n")
print("L'etat de la pile initail:", pile.voirPile())
print("\n")
print('la pile est vide?:', pile.empty())
print("\n")
pile.push("Mamadou")
pile.push("Mansour")
pile.push("Dame")
pile.push("Khady")
print("L'etat de la pile aprés ajout:", pile.voirPile())
print("\n")
print('la pile est vide?:', pile.empty())
print("\n")
#L'élément recemment ajouté de la liste sera enlevé
pile.remove() 
print("L'etat de la pile aprés suppression du sommet:", pile.voirPile())
print("\n")
print('la pile est vide?:', pile.empty())
print("\n")




#Implémentation de la classe File par héritage
class File(Pile):
    def __init__(self):
        self.elements = []
    def remove(self):
        return self.elements.pop()

print("========= File (FIFO:First In First Out) par héritage de la classe pile ================")
print("\n")
p=File()
p.push("Mamadou")
p.push("Mansour")
p.push("Dame")
p.push("Khady")
print(p.elements)
p.remove() #Le premier élément de la liste sera enlevé
print(p.elements)