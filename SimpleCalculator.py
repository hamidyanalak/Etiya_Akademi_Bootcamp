number1 = int(input("Lütfen ilk sayıyı giriniz: "))
number2 = int(input("Lütfen ikinci sayıyı giriniz: "))

print("1. Toplama \n2. Çıkarma \n3. Çarpma \n4. Bölme \n")

choice = int(input("Lütfen yapmak istediğiniz seçimi belirtiniz : "))

match choice:
    case 1:
        print("Sonuç: " , (number1 + number2))
    case 2:
        print("Sonuç: " , (number1 - number2))
    case 3:
        print("Sonuç: " , (number1 * number2))
    case 4:
        print("Sonuç: " , (number1 / number2))
    case _:
        print("Lütfen geçerli bir işlem giriniz.")
