# This article cover [PEP 572 -- Assignment Expressions](https://www.python.org/dev/peps/pep-0572/#abstract) and [Когда и зачем использовать оператор :=](https://medium.com/nuances-of-programming/%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D0%B8-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D0%B2-python-d2e70bf85a40)

## Preamble

More recently, Python 3.8 introduced the colon assignment operator `:=`, similar to the assignment operator `=`. **Using this operator allows you to speed up and shorten your code**.

This notation has its origins in mathematics. When writing equations, you can write something like:

 a = 5, a + b = 7. 

 Then, using a simple algebraic operation, it is easy to calculate that b = 2. In this context, the equal sign means identity. The variables a and b are constant numbers, and although their meaning is unknown when the task is initialized, they exist and do not change.

On the other hand, in mathematics, there is another notation for the relation **'x is defined as y'**. The notation `x := y` does **not mean that x and y are equal to each other**. *Here x is defined to be any value of y*. **The equation is one-sided rather than symmetrical**, which is somewhat difficult to understand. This notation only applies to long lists of variable definitions in highly specialized scientific articles.

## Abstract

This is a proposal for creating a way to assign to variables within an expression using the notation

> `NAME := expr`

> Naming is an important part of programming that allows you to use a "descriptive" name instead of a longer expression and also makes it easier to reuse values. **Currently, this can only be done as an instruction, which makes this operation unavailable when generating lists, as well as in other expressions**.

## The importance of real code

During the development of this PEP many people (supporters and critics both) have had a tendency to focus on toy examples on the one hand, and on overly complex examples on the other.

The danger of toy examples is twofold: they are often too abstract to make anyone go "ooh, that's compelling", and they are easily refuted with "I would never write it that way anyway".

The danger of overly complex examples is that they provide a convenient strawman for critics of the proposal to shoot down ("that's obfuscated").

Yet there is some use for both extremely simple and extremely complex examples: they are helpful to clarify the intended semantics. Therefore, there will be some of each below.

## Toy cases

### **case 1**

Consider the following code, with a function `f` defined as `f = lambda x: x + 2`, which simply adds 2 to whatever you enter:

```python3
data = [1,2,3,4]
f_data = [y for x in data if (y := f(x)) is not 4]
```

We get `[3, 5, 6]`, since these function results are not equal to 4. This is a much more efficient implementation than its alternative, which runs the input twice through the function:

```python3
f_data = [f(x) for x in data if f(x) is not 4]
```

### **case 2**

```python3
# Handle a matched regex
if (match := pattern.search(data)) is not None:
    # Do something with match

```

### **extra**

```python3
f = lambda x : (m := x+1) + (m**2)
```

`f(3)` returns `20` because `(m: = x + 1)` evaluates to `4` and `(m ** 2)` evaluates to `16`. Their sum is `20`, which is a fairly clean but somewhat tricky method.

## complex cases

### **case 1**

Example from Python standard library. sity.py

env_base is only used on these lines, putting its assignment on the if moves it as the "header" of the block.

*before:*
```python3
env_base = os.environ.get("PYTHONUSERBASE", None)
if env_base:
    return env_base
```

*improved:*
```python3
if env_base := os.environ.get("PYTHONUSERBASE", None):
    return env_base
```

### **case 2**

Example from Python standard library. sysconfig.py

Calling fp.readline() in the while condition and calling .match() on the if lines make the code more compact without making it harder to understand.

*before:*
```python3
while True:
    line = fp.readline()
    if not line:
        break
    m = define_rx.match(line)
    if m:
        n, v = m.group(1, 2)
        try:
            v = int(v)
        except ValueError:
            pass
        vars[n] = v
    else:
        m = undef_rx.match(line)
        if m:
            vars[m.group(1)] = 0
```

*improved:*
```python3
while line := fp.readline():
    if m := define_rx.match(line):
        n, v = m.group(1, 2)
        try:
            v = int(v)
        except ValueError:
            pass
        vars[n] = v
    elif m := undef_rx.match(line):
        vars[m.group(1)] = 0
```

### **extra**

Simplifying list comprehensions

A list comprehension can map and filter efficiently by capturing the condition:

```python3
results = [(x, y, x/y) for x in input_data if (y := f(x)) > 0]
```

Similarly, a subexpression can be reused within the main expression, by giving it a name on first use:

```python3
stuff = [[y := f(x), x/y] for x in range(5)]
```
Note that in both cases the variable y is bound in the containing scope (i.e. at the same level as results or stuff).

## Style guide recommendations

As expression assignments can sometimes be used equivalently to statement assignments, the question of which should be preferred will arise. For the benefit of style guides such as PEP 8, two recommendations are suggested.

1. If either assignment statements or assignment expressions can be used, prefer statements; they are a clear declaration of intent.

2. If using assignment expressions would lead to ambiguity about execution order, restructure it to use statements instead.