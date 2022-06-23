#문자열 슬라이싱
from re import I


a= "Life is too short, You need Python"
b= a[0] + a[1] + a[2] + a[3]
b
a[0:2]
a[5:7]
a[12:17]
a[:]
a[19:-7]

c="20220623Rainy"
year=c[:4]
day=c[4:8]
weather=c[8:]
year
day
weather


d="Pithon"
d[:1]
d[2:]
d[:1] + 'y' + d[2:]

