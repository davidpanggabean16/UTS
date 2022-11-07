print("----------------- Program Kasir Sederhana  -----------------")
pembeli = input("Nim: ")
print ("Nim Pembeli :", pembeli) 
pembeli = input("Nama: ")
print ("Nama Pembeli :", pembeli)


def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1.  Capucino - Rp 5000")
   print("2. Teh - Rp 3500")
  
   
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas,"  Capucino = Rp", totalmnm)
       mnm=(" Capucino")

   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Teh = Rp", totalmnm)
       mnm=("Teh")
    
   
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
totalsemua=totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)

print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")