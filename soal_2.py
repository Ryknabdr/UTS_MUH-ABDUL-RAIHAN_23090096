def kabisat(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False
tahun =int(input("masukan tahun broo: "))

if kabisat(tahun):
    print(tahun, "wah ini tahun kabisat broo")
else:
    print(tahun, "waduh ini bukan tahun kabisat broo")