word = input("Enter Word: ") 
def CountLetters(_word):
  letters = 0
  for l in _word:
      if l != " ":
          letters += 1
  return letters

print(CountLetters(word), 'is the number of letters')
