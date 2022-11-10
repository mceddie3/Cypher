import os
def trans(counter):
  line = ""
  greet = input ("What would you like to translate? ")
  if(greet=='e'):
    os.system('clear')
  while len(greet) > (counter):
    if greet[int(counter)].lower() == " ":
      line +=" "
    elif greet[int(counter)].lower() == "a":
      line +="n"
    elif greet[int(counter)].lower() == "b":
      line +="o"
    elif greet[int(counter)].lower() == "c":
      line +="p"
    elif greet[int(counter)].lower() == "d":
      line +="q"
    elif greet[int(counter)].lower() == "e":
      line +="r"
    elif greet[int(counter)].lower() == "f":
      line +="s"
    elif greet[int(counter)].lower() == "g":
      line +="t"
    elif greet[int(counter)].lower() == "h":
      line +="u"
    elif greet[int(counter)].lower() == "i":
      line += "v"
    elif greet[int(counter)].lower() == "j":
      line +="w"
    elif greet[int(counter)].lower() == "k":
      line +="x"
    elif greet[int(counter)].lower() == "l":
      line +="y"
    elif greet[int(counter)].lower() == "m":
      line +="z"
    elif greet[int(counter)].lower() == "n":
      line +="a"
    elif greet[int(counter)].lower() == "o":
      line +="b"
    elif greet[int(counter)].lower() == "p":
      line +="c"
    elif greet[int(counter)].lower() == "q":
      line +="d"
    elif greet[int(counter)].lower() == "r":
      line +="e"
    elif greet[int(counter)].lower() == "s":
      line +="f"
    elif greet[int(counter)].lower() == "t":
      line +="g"
    elif greet[int(counter)].lower() == "u":
      line +="h"
    elif greet[int(counter)].lower() == "v":
      line +="i"
    elif greet[int(counter)].lower() == "w":
      line +="j"
    elif greet[int(counter)].lower() == "x":
      line +="k"
    elif greet[int(counter)].lower() == "y":
      line +="l"
    elif greet[int(counter)].lower() =="z":
      line +="m"
    counter = counter + 1
  print(line)
  trans(0)

def Max(counter):
  line = ""
  num = int(input ("What displacement (0-13)? "))
  greet = input ("What would you like to translate? ")
  counter = 0
  while len(greet) > (counter):
    both = ord(greet[counter]) + num
    if both > 122:
      line += chr(int(97) + num)
    else:
      line += chr(both)
    counter = counter + 1
  print(line)
  Max(0)

def lindseyscipher():
  line = ""
  greet = input ("What would you like to translate? ")
  counter = 0
  while len(greet) > (counter):
    line += chr(((ord(greet[counter]) + 13) % 97) + 97)
    print(ord(greet[counter]))
    counter += 1
  print(line)
  lindseyscipher()
    
def main(counter):
    x=input('Password: ')
    if(x== 'password' or x=='11036574.JM'):
      print("Translor:")
      print()
      x=input ("What cypher would you like to use? ")
      if x==("c"):
        trans(counter)
      if x==("m"):
        Max(counter)
      if x==("l"):
        lindseyscipher()
        
    else:
      print('WRONG MOTHA F*CKA')
      counter=counter+1
    if((x!='11036574.JM')and(counter<3)):
      main(counter)
    else:
      return
if __name__ == "__main__":
      main(0)
