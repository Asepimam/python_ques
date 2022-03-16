import datetime

def hari(tanggal):
    """
    mencari nama hari dari tanggal yang dikirimkan
    """
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    return hari[tanggal.weekday()]

def promo_weekday(tanggal):
    total_pesanan = int(input("Total pesanan: "))
    """
    dalam kode ini kita menggunakan fungsi hari() yang mengembalikan nama hari
    dari tanggal yang dikirimkan jika hari tidak sesui maka kode_promo tidak bisa digunakan.dan saat total_pesanan lebih dari 50000 maka kode promo 
    tidak akan digunakan lalu akan langsung menampilkan harga normal
    """
    if hari(tanggal) == "Jumat" or hari(tanggal) == "Sabtu" or hari(tanggal) == "Minggu":
        if total_pesanan >=40000 and total_pesanan <=50000:
            kode_promo = "WEEKENDCERIA"
            gunakan = input(str.upper( "Gunakan kode promo " + kode_promo + "? (y/n) "))
            if gunakan == "y":
                diskon = total_pesanan * 4/100
                total_akhir = total_pesanan - diskon
                print("diskon: Rp.{:.0f}".format(diskon))
                print("Total_akhir: Rp.{:.0f}".format(total_akhir))
                # if total_pesanan <=50000:
                #     diskon = total_pesanan * 5/100
                #     total_akhir = total_pesanan - diskon
                #     print("Total: Rp.{:.0f}".format(diskon))
                #     print("total akhir: Rp.{:.0f}".format(total_akhir))
            elif gunakan == "n":
                print("Total: Rp.{:.0f}".format(total_akhir))
            else:
                print("Input yang anda masukkan salah")
        else:
            print("Total: Rp.{:.0f}".format(total_pesanan))
        return "Terimakasih telah berbelanja di toko kami"
    
    else:
        print("Total: Rp.{:.0f}".format(total_pesanan))
        print("terimakasih telah berbelanja di toko kami")
        return "Hari ini tidak ada promo!"
    
# kita bisa hari nya mengugunakan fungsi datetime.datetime()
# print(promo_weekday(datetime.date(2022,3,18)))
# atau mengecek apakah hari ini promo_weekday(dateime.datetime.now())
print(promo_weekday(datetime.datetime.now()))