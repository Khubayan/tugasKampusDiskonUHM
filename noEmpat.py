print("Masukkan Harga")
cpu = int(input("CPU: "))
ram = int(input("RAM: "))
motherB = int(input("Motherboard: "))

total_harga = cpu + ram + motherB

if total_harga > 1500000:
  diskon = float(total_harga * 0.10)
  total_bayar = total_harga - diskon
  print("Harga Total: " + str(total_bayar) + " (diskon)")
else:
  print("Harga Total: " + str(total_harga) + " (tidak mendapatkan diskon)")