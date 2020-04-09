class Solution(object):
    def uniqueMorseRepresentations(self, words):
        global result
        global divide
        self.words = words
        #self.j = j
        x=0
        i=0
        result = []
        final_result = ''
        
        Alphabet = {"a" : ".-",
                "b": "-...",
                "c":"-.-.",
                "d":"-..",
                "e":".",
                "f":"..-.",
                "g":"--.",
                "h":"....",
                "i":"..",
                "j":".---",
                "k":"-.-",
                "l":".-..",
                "m":"--",
                "n":"-.",
                "o":"---",
                "p":".--.",
                "q":"--.-",
                "r":".-.",
                "s":"...",
                "t":"-",
                "u":"..-",
                "v":"...-",
                "w":".--",
                "x":"-..-",
                "y":"-.--",
                "z":"--.."
               }
    
        divide = list(words)
        
        length_of_divide = len(divide)

        while i< length_of_divide:
            length = Alphabet[divide[x]]
            i += 1
            x += 1
            result.append(length)
        final_result = ''.join(result)
        return final_result

word1 = ''
word = str(input())
j = 0
reg = ''
count = 0
for i in word:
  if (i != '[' and i != ']' and i != '"' and i != ' '):
    word1 += i

word2 = list(word1.split(','))

myobj = Solution()  
for i in word2:
  print(i)
  reg += myobj.uniqueMorseRepresentations(i) + "1"
  #print(reg)
  j += 1
reg1 = reg.split("1")

for i in range(len(reg1)-1):
  if(reg[i] == reg[i+1]):
    count += 1
   
print(count-1)
    
    
       
        
