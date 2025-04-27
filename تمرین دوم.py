Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... # انتخاب یک عدد تصادفی بین 1 تا 100
... secret_number = random.randint(1, 100)
... 
... # شمارش تعداد تلاش‌ها
... attempts = 0
... 
... # شروع حلقه حدس زدن
... while True:
...     guess = int(input("یک عدد بین 1 تا 100 حدس بزنید: "))
...     attempts += 1  # افزایش تعداد تلاش‌ها
...     
...     if guess < secret_number:
...         print("برو بالاتر!")
...     elif guess > secret_number:
...         print("بیا پایین‌تر!")
...     else:
...         print(f"آفرین! در {attempts} تلاش درست حدس زدی!")
