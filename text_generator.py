import random

class Markov(object):

    def __init__(self, order):
        self.graph = {}
        self.text = None
        self.order = order
        self.group_size = self.order + 1
        
        return

    def train(self, filename):
        self.text = open(filename).read().split()
        self.text = self.text + self.text[ : self.order]
        

        for i in range(0, len(self.text) - self.group_size):
            
            key = tuple(self.text[i : i + self.order])
            value = self.text[i + self.order]

            if key in self.graph:
                self.graph[key].append(value)
            else:
                self.graph[key] = [value]
       
        return

    def generate(self,length):
        index = random.randint(0, len(self.text) - self.order)
        result = self.text[index : index + self.order]

        for i in range(length):
            state = tuple(result[len(result) - self.order : ])
            next_word = random.choice(self.graph[state])
            result.append(next_word)
       

        sentence=[]

        for word in result:
        	each_word=list(word)
        	letter = each_word[len(word)-1]
        	if letter == ',' or letter == '.' or letter == '?' or letter == '!':
        		result.insert(result.index(word)+1,"\n")
        	



        return " ".join(result[self.order : ])

    def word(self,pos):
        firstword = ["From","When","Look","Those","Then","Is","For","As","When","O"]
        lastword = [" thee."," cold."," be."," sweet."," commits."]
        if pos == 1: 
            return firstword[random.randint(0,len(firstword)-1)]
        else:
            return lastword[random.randint(0,len(lastword)-1)]






        


		
	

	
