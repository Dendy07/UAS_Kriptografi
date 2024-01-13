def encrypt(plaintext, key):
    # Inisialisasi hasil enkripsi dengan nilai nol
    ciphertext = ""

    # Melakukan operasi XOR antara setiap karakter plainteks dan kunci
    for i in range(len(plaintext)):
        # Mengonversi karakter ke dalam bentuk ASCII dan melakukan operasi XOR
        result = ord(plaintext[i]) ^ ord(key[i % len(key)])  # Menggunakan modulo untuk mengulang kunci jika lebih pendek dari plainteks

        # Mengonversi hasil XOR kembali ke dalam bentuk karakter dan menambahkannya ke ciphertext
        ciphertext += chr(result)

    return ciphertext

def decrypt(ciphertext, key):
    # Dekripsi pada OTP adalah sama dengan enkripsi
    return encrypt(ciphertext, key)

# Contoh penggunaan
if __name__ == "__main__":
    # Meminta input dari pengguna
    plaintext = input("Masukkan Plainteks: ").upper()
    key = input("Masukkan Kunci: ").upper()

    # Enkripsi
    encrypted_text = encrypt(plaintext, key)
    print("Hasil Enkripsi:", encrypted_text)

    # Dekripsi
    decrypted_text = decrypt(encrypted_text, key)
    print("Hasil Dekripsi:", decrypted_text)
