#!/usr/bin/env python3
add = __import__('calculator_1').add
sub = __import__('calculator_1').sub
mul = __import__('calculator_1').mul
div = __import__('calculator_1').div
a = 10
b = 5
print(f'{a} + {b} = ', add(a,b))
print(f'{a} - {b} = ', sub(a,b))
print(f'{a} * {b} = ', mul(a,b))
print(f'{a} / {b} = ', div(a,b))