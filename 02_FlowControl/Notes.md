# Flow Control (My Notes)

## Comparision Operators - Standard C 

| `==` | Equality              |
| `!=` | Not Equality          | 
| `<`  | Less Than             |
| `>`  | Greater Than          |
| `<=` | Less than or Equal    |
| `>=` | Greater than or Equal | 

_Returns Booleans - 'True' or 'False'._

## Boolean Operators

| `and` | Logical And |
| `or`  | Logical Or  |
| `not` | Negation    |

## Conditions

Always evaluate down to a Boolean - 'True' or 'False'.

## Blocks

Defined by INDENTATION! 
(_Past personal experience - either use hard spaces or tabs only!_)

* Blocks are defined when indentation increases.
* Blocks contain may contain other blocks.
* Blocks end when indentation decreases to zero or to a containing blocks indentation.

## Control Statements

### If, Elif, Else...
```
if True:
   TrueEvent()
else:
   NotTrueEvent()
NormallyScheduledProgramming()

if a < 0 :
   ALessThanZero()
elif a == 0:
   AEqualsZero()
else
   ANotLessThanAndNotEqualZero()
NormallyScheduledProgramming()
```

### While Loops (Break and Continue)

```
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
```

### For Loops and Ranges (next!)