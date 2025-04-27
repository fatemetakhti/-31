Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # دریافت عدد از کاربر
... n = int(input("یک عدد صحیح وارد کنید: "))
... 
... # رسم مثلث عددی با حلقه for
... for i in range(1, n + 1):
...     for j in range(1, i + 1):
...         print(j, end=" ")
