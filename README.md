#Boolean Expression Interpreter

####To run:
`$ python bei.py`

####Evaluate Expression
```
> x=true
> y=false
> x and y
False
```

####Compare Expressions
```
> cmpr (x and y) or (x and z) | x and (y or z)
Equivalent
```

####Create Truth Table
```
> tt x or y
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
'> q'

####Operator precedence is not implemented correctly at moment so clear ambiguities with parenthesis
