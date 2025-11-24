#Q.2.WAP to input any alphabet and check whether it is vowel or consonant.
alphabet=input("Enter Alphabet:")
alphabet=alphabet.upper()
if alphabet in ["A","E","I","O","U"]:
  print(alphabet,"is Vowel!")
else:
  print(alphabet,"is Consonant!")


