"""
name = "PYthON"

convert lower case character to uppercase character into lowercase
"""

s1 ="PYthON"
s2=""

for c in s1:
    if c.isupper():
        s2+=c.lower()
    else:
        s2+=c.upper()
        print(s1)
        print(s2)
