import qrcode

def generate_qr_code(info):
    # buat QR OBJECT nya
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    
    qr.add_data(info)
    qr.make(fit=True)
    
    # Buat gambar QR nya
    img = qr.make_image(fill_color="black", back_color="white")
    
    # PATHYA
    F_gambar = input("Masukan Format gambar :   ")
    img.save(f"D:/kodingan/QR-generet/{F_gambar}")

# Example data for personal information

nama = input("masuka Nama:  ")
nis = input("Masukan Nis :  ")
nisn = input("Masukan Nisn :  ")
gmail = input("masukan Gmail:   ")
phone = input("masukan Phone:   ")

personal_info = str(f"Name : {nama}\nNIS :  {nis}\nNISN :   {nisn}\nCompany:   SMKS FADILAH\nJob :    ASISTEN LAB\nPhone : {phone}\nGmail :   {gmail}\nAddres :   JL. PENDIDIKAN 2 KOTA TANGERANG SELATAN 15227	INDONESIA")

# Hasil
generate_qr_code(personal_info)
print("QR Berhasil Dibuat")
