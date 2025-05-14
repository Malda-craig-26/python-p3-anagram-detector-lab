# your code goes here!
class Anagram:
    def __init__(self, word):
       self.word = word.lower()
       self.sorted_word = sorted(self.word)

    def match(self,word_list) :
        matches = []
        for w in word_list:
            if sorted(w.lower()) == self.sorted_word:
                matches.append(w)
        return matches
    
words = ['listen', 'enlist', 'Google', 'inlets', 'banana']
anagram_detector = Anagram('listen')
print(anagram_detector.match(words))

"""
def prepare(func):

    def preheat(*args,**kwags):
        print("Oven is at 40deg")
        func(*args,**kwags)

    return preheat

class Sufuria:

    def __init__(self):
        self.color = "Silver"
        self.material = "Aluminium"
        print("Initialized")

    @property
    def color(self) :
        return self._color
    
    @color.setter
    def color(self) :
        print("color cannot be changed")

    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, m):
        if m  in ["Silver","Gold","Alluminium"]:
            self._material = m
        else:
            raise ValueError("Material must be either Silver,Gold,Alluminium")



    def __repr__(self):
        return f"I am the object, my color"


    @prepare
    def cook(self,food):
         print(f"{food} is ready")

sufuria1 = Sufuria()
"""



