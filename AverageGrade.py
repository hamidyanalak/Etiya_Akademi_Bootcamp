midterm = float(input("Lütfen vize notunuzu giriniz : "))
final = float(input("Lütfen final notunuzu giriniz : "))

if midterm < 0 or midterm > 100 or final < 0 or final > 100:
    print("Lütfen geçerli bir not giriniz. (0-100) ")
elif final < 40 or midterm == final*2:
    print("Dersten kaldınız.")
else:
    avg = midterm * 0.4 + final * 0.6
    avg = round(avg,3)
    if avg >=80:
        print(avg , "AA Dersten geçtiniz!")
    elif avg >=70:
        print(avg , "BB Dersten geçtiniz!")
    elif avg >=60:
        print(avg , "CC Dersten geçtiniz!")
    elif avg >=50:
        print(avg , "DD Dersten geçtiniz!")
    else:
        print(avg , "FF Dersten kaldınız.")
