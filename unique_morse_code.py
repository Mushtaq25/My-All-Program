def uniqueMorseRepresentations(words):
  global result
  global divide
  x=0
  i=0
  result = []
  final_result = []
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
  print(len(divide))
  length_of_divide = len(divide)

  while i< length_of_divide:
    length = Alphabet[divide[x]]
    i += 1
    x +=1
    result.append(length)
  return ''.join(result)
    
words = str(input("ENter your word :-"))
print(uniqueMorseRepresentations(words))


