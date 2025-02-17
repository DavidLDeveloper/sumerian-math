# Sumerian Mathmatics

Utility for handling base 60 numbers and calculations with optional cuneiform output.

## Why?

Becuase clay tablets from ancient Sumerian and Bablyonian sources contain suprisingly advanced mathmatics including tables of squares and square roots, as well as Pathagorian triplets and more. This will help me tinker with and understand their methodolgy better, and it's an interesting learning experience in Python.

## Usage

Base60(n): takes an INT or Base60() number and creates a new Base60 object.
For example: Base60(7212) === Base60('20C')

Normal mathmatical operators can be used to mutate the Base60 values. For exampple: Base60(3606) \* 2 === '20C' # i.e. 7212

Base60('20C').b10 will return base 10 integer.

Base60('20C').cuneiform() will return cuneiform representation where "|" === 1 and "<" === 10, with columns to represent 1s and 60s and so on... places.
Example:

```
7212 is: 2 3600s, 0 60s, and 12 1s.
or: 7200 + 0 + 12
or, in cuneiform: || - <||

Similarily, 73 would be: | <|||, or 60 + 13.
```
