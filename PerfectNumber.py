# 1 + 2 + 3 = 6 mükemmel sayı örneği

number = int(input("Lütfen bir sayı giriniz : "))
sum = 0

for i in range(1,number):
    if number%i == 0:
        sum += i  # sum = sum + i

if number == sum:
    print(number , "sayısı mükemmel bir sayıdır.")
else:
    print(number, "sayısı mükemmel bir sayı değildir.")
