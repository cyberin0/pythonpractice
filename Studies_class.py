"""
#
class ThirdTimesA_MF_Charm():
    def __init__(self, docu1, docu2):
        self.d1 =docu1
        self.d2 =docu2
        
    def sux2suckTBH(self):
        print('Here\'s that', self.d1, 'and that other', self.d2, 'for ya!')
print("\n")

DocRequest = ThirdTimesA_MF_Charm('BRRRRNENENBRBNNERNNRENNBRBBRB', 'Silly Spyder')
ThirdTimesA_MF_Charm.sux2suckTBH(DocRequest)


#
class SimpleClass():
    def __init__(self, first, second):
        self.f = first
        self.s = second
    def SimpleObject(self):
        print(self.f, self.s)
print("\n")

UserObject2= SimpleClass('neeeeeeerrrrrrrrrrmmm', 1000)
SimpleClass.SimpleObject(UserObject2)



#
class Class3():
    def __init__(self, arg1, arg2, arg14, arg23):
        self.arg1=arg1
        self.arg2=arg2
        self.arg3=arg14
        self.arg4=arg23
    def Object3(self):
        print('You calculated', self.arg1, 'catastrophes within', self.arg2, 'while', self.arg3, 'were visited by', self.arg4, 'aliens.')
print("\n")
PrintoutObject = Class3('323,429,012', '14 systems ', '1501 systems ', 'Pleadian' )
Class3.Object3(PrintoutObject)


#
class Class4():
    def __init__(self, big, legend):
        self.b=big
        self.l=legend
    def Object4Trial(self):
        print(self.b, self.l)
print("\n")
BeeegReturn=Class4('something', 'doable')
Class4.Object4Trial(BeeegReturn)

print('\n')
"""

#
class ArtisanSandwich():
    def __init__(self, bread, cheese, protein, sandwich):
        self.br=bread
        self.ch=cheese
        self.pro=protein
        self.das=sandwich
    def SanDescription(self):
        print('Great choice! I\'ll get started on that', self.das, 'right away!')
        print('------')
        print('You wanted', self.ch, 'and', self.pro, 'on', self.br + ",", 'is that correct?')
        
VeganSandwich = ArtisanSandwich('whole wheat bread', 'vegan pepperjack', 'tempeh', 'Vegan Sandwich')
GrossAssMeatSandwich = ArtisanSandwich('white', 'chedder', 'turkey & ham', 'LOLWTF')

ArtisanSandwich.SanDescription(VeganSandwich)
print('\n')
VeganSandwich.SanDescription()
GrossAssMeatSandwich.SanDescription()



#Note that there are two ways to printout the class object 'Vegan Sandwich'
#class.object(item)
# OR
#item.object()

"""
print('\n')
#
class Jackets():
    def __init__(self, size, color, season):
        self.si=size
        self.co=color
        self.se=season
    def MyChoice(self):
        print('You chose the', self.co, 'jacket in a size', self.si + ', best for', self.se + '.')


Blackjacket = Jackets('medium', 'black', 'winter')
Blackjacket.MyChoice()
print('\n')
EddieBauer = Jackets('medium', 'grey', 'fall or winter')
EddieBauer.MyChoice()