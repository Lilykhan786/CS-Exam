# Python 
<!-- Que - what is python? who created python? -->
Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. <br />
It was created by **Guido van Rossum** during 1985- 1990, and was released in 1991.

<!-- Que - list some usese of python. -->

### It is used for:
1. AI and machine learning 
2. Data analytics and visualisation
3. Programming applications 
4. Web development 
5. Game development 
6. SEO

<!-- Que - Can we use multi-line comments in python? if yes, then how?  -->

### Note - 
1. Comments starts with a #, and Python will ignore them:
2. Unlike other programming languages Python doesn't support **multi-line comment**.  <br />
But you can use `"""` for multi-line comments.
> *(Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it)*
3. 
___

<!-- Que - What are Tokens? List some Tokens. -->

### Tokens
The smallest individual unit in a program is known as a *token* or a *lexical Unit*

<!-- Que- Define KeyWords with examples -->
- KeyWords (if, for, each, print, class, etc)
<!-- Que- Define Literals with examples -->
- Literals (`x=2`) 
<!-- Que- Define Identifiers with examples -->
- Identifiers (`name`)   
<!-- Que- Define Operators with examples -->
- Operators (`+`, `-` ,`/` ,`*` ,`=` ,`==`)
<!-- Que- Define Punctuators with examples -->
- Punctuators (`;`, `,`, `{}`, `()`, `:`)

+ - `"sleep"` -> single line  string literal.
+ - `"sleep`
`well"` use `\` to use multi line string or `"""`

___

<!-- Que -  What are data types? List some data types with examples -->

### Built-in Data Types

- Text Type:	`str`
- Numeric Types:	`int`, `float`, `complex`
- Sequence Types:	`list`, `tuple`, `range`
- Mapping Type:	`dict`
- Set Types:	`set`, `frozenset`
- Boolean Type:	`bool`
- Binary Types:	`bytes`, `bytearray`, `memoryview`
___

### Types of Operator
Python language supports the following types of operators.

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators
___

### Loops

1. **`while loop`** - Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

2. **`for loop`** -
Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

3. **`nested loops`** -
You can use one or more loop inside any another while, for or do..while loop.

___

### Built-in data types in Python used to store collections of data.
List, Tuple, Set and Dictionary, all with different qualities and usage.

1. **List**
- Lists are used to store multiple items in a single variable.
- Lists are created using square brackets. `[]`

 2. **Tuple**
- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets. `()`

3. **Set**
- Sets are used to store multiple items in a single variable.
- A set is a collection which is both unordered and unindexed.
- Sets are written with curly brackets. `{}`

4. **Dictionary**
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

> **List** and **tuple** is an ordered collection of items. **Dictionary** is unordered collection. List and dictionary objects are mutable i.e. it is possible to add new item or delete and item from it. Tuple is an immutable object.

___

### Mutable and Immutable
The `mutable` objects ***can*** be changed to any value or state without adding a new object. <br >
Whereas, the `immutable` objects ***can not*** be changed to its value or state once it is created. In the case of immutable objects, whenever we change the state of the object, a new object will be created. 
- Immutable are of in-built types
- Custom classes are generally mutable

| Immutable | Mutable |
|  ------   |  ------ | 
|  int      |  list   |
|  float    |  dict | 
|  bool     |  set    |
|  string   |  |
|  unicode  |  |
|  tuple    |  |

