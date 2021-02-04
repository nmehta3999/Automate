#!/usr/bin/python3
while True:
   print('Who are you?')
   name = input()
   if name != 'Neil':
      print("Sorry, only Neil is allowed")
      continue
   print ('Whats up? Type codeword')
   codeword = input()
   if codeword == 'codeword':
      break
   else :
      print ('Next time your asked for the codeword - type "codeword"!')
print('You\'re in - Party On...');