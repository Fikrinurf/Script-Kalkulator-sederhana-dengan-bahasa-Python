## membuat kalkulator sederhana dengan bahasa pemograman python
## dengan pengkondisian else if




print("===========================================")
print("Program Kalkulator Sederhana dengan Else If")
print("===========================================")

print("\n")


angkaPertama = float(input("Masukan angka Pertama :"))
operator = input("Masukan operator (+,-,x,/) :")
angkaKedua = float(input("Masukan angka Kedua :"))


if operator == '+': 
    hasil = angkaPertama + angkaKedua
    print(f"hasil dari {angkaPertama} + {angkaKedua} adalah :{hasil}")
elif operator == '-':
    hasil = angkaPertama - angkaKedua
    print(f"hasil dari {angkaPertama} - {angkaKedua} adalah :{hasil}")
elif operator == 'x':
    hasil = angkaPertama * angkaKedua
    print(f"hasil dari {angkaPertama} x {angkaKedua} adalah :{hasil}")
elif operator == '/':
    hasil = angkaPertama / angkaKedua
    print(f"hasil dari {angkaPertama} / {angkaKedua} adalah :{hasil}")
else:
    print("Anda salah memasukan operatorrrrr Kisamaaaaaaaaaaaaaaaaaaaaaaaa!!!!!")
