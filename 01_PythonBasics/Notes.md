# Python Basics (_My Notes_)

## Comments (Explained where?)

* Single Line - '#' will comment until end of line
* Multi-Line  - ''' will start a comment block, which needs the same to terminate. Note that this is part of Python's Doc String... 

## Math Operators

| Operator | Operation         | Examples | Results | Precedence |
|----------|-------------------|----------|---------|------------|
| **       | Exponentation     | 2 ** 3   |  8      | 1          |
| %        | Modulus/Remainder | 22 % 8   |  6      | 2 (L to R) |
| //       | Integer Division  | 22 // 8  |  2      | 2          |
| /        | Division          | 22 / 8   |  2.75   | 2          |
| *        | Multiplication    | 3 * 5    | 15      | 2          |
| -        | Subtraction       | 5 - 2    |  3      | 3 (L to R) |
| +        | Addition          | 2 + 2    |  4      | 3          |

## Data Types

* Python distinguishes between integers and floats!
* Python strings are distinct from ints/floats - no mixing!
* Python Booleans are True or False - case matters!

### More on Booleans (_from Chapter 2_)

* False - 0, 0.0, and "" ('', i.e. empty string) all evaluate to False.

### Strings

"Math" operations are overloaded for strings, but typed. (So, somethings may fail...)

Concatenation: 'Alice' + 'Bob' -> 'AliceBob'
Replication:   'Alice' * 2     -> 'AliceAlice'

## Variables

Valid variable names follow these rules:

* One word without any spaces
* Valid charcter set: [a-zA-Z0-9_] (i.e. letters, numbers and underscore)



