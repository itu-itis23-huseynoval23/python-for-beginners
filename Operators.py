# ARITHMETIC OPERATORS

1 + 1  # 2
2 - 1  # 1
2 * 2  # 4
4 / 2  # 2
4 % 3  # 1
4 ** 2  # 16
4 // 2  # 2

age = 8
age += 8  # age = age + 8
print(age)

# COMPRASION OPERATORS

a = 1
b = 2

a == b # False
a != b # True
a > b # False
a <= b # True

# BOOLEAN OPERATORS

condition1 = True
condition2 = False

not condition1 #False 
condition1 and condition2 #False
condition1 or condition2 #True

print( 0 or 1 )## 1
print( False or 'hey')## 'hey'
print( 'hi' or 'hey')## 'hi'
print([] or False)## 'False'
print(False or [])## '[]'
# Eger birincide 0, bos coxluq, false kimi ifadeler varsa
# ikinci secimi secir, yoxdursa birinci secimde qalir.

#and ise tersini edir eger birinci secim sehvdirse onu secir
# duzdure ikincini secir.
print( 1 and 0)## 0

# BITWISE OPERATORS

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

#TERNARY OPERATORS

def is_adult(age):
    if age > 18:
        return True
    else:
        return False
# IS same to the :
def is_adult2(age):
    return True if age > 18 else False

