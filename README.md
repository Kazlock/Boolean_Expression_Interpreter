#Boolean Expression Interpreter

####To run:
`$ python bei.py`

####Evaluate Expression
```
&gt x=true
&gt y=false
&gt x and y
False
```

####Compare Expressions
```
&gt cmpr (x and y) or (x and z) | x and (y or z)
Equivalent
```

####Create Truth Table
```
&gt tt x or y
+------------------------+
|   x   |   y   | x or y |
|------------------------|
| True  | True  |   True |
|------------------------|
| True  | False |   True |
|------------------------|
| False | True  |   True |
|------------------------|
| False | False |  False |
+------------------------+
```

####Exit REPL
&gt q

####Operator precedence is not implemented correctly at moment so clear ambiguities with parenthesis
