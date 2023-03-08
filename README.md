# Calculator App

This is a simple calculator app built using Python and the Tkinter GUI toolkit.

## How the App Works

When the app is launched, the `Calculator` class is initialized. This class sets up the calculator's display, defines the appearance of the buttons, and creates the buttons using a for loop.

The `click` method is responsible for handling user input. When a button is clicked, the corresponding method is called. If the button clicked is a number or operator, it is appended to the `expression` attribute. If the button clicked is "C", the `clear` method is called to reset the calculator. If the button clicked is "DEL", the last character in the `expression` attribute is removed. If the button clicked is "=", the `eval` function is used to evaluate the expression and return the result.

The `clear` method sets the `expression` attribute to an empty string and sets the calculator's display to 0.

## Dependencies

- Python 3
- Tkinter

## How to Use

1. Open the calculator app by running the `main.py` file using Python.

2. Use the buttons on the calculator to enter numbers and perform arithmetic operations.

3. To clear the calculator's display, press the "C" button.

4. To delete the last entered character, press the "DEL" button.

5. To calculate the result, press the "=" button. The result will be displayed in the calculator's display.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
<br>
<br>
<br>
<br>
# Aplikasi Kalkulator

Ini adalah aplikasi kalkulator sederhana yang dibangun dengan menggunakan Python dan toolkit GUI Tkinter.

## Cara Kerja Aplikasi

Ketika aplikasi diluncurkan, kelas `Calculator` diinisialisasi. Kelas ini menyiapkan tampilan kalkulator, menentukan tampilan tombol, dan membuat tombol menggunakan perulangan for.

Metode `click` bertanggung jawab untuk menangani masukan pengguna. Ketika tombol ditekan, metode yang sesuai dipanggil. Jika tombol yang ditekan adalah angka atau operator, itu akan ditambahkan ke atribut `expression`. Jika tombol yang ditekan adalah "C", metode `clear` dipanggil untuk mengatur ulang kalkulator. Jika tombol yang ditekan adalah "DEL", karakter terakhir pada atribut `expression` dihapus. Jika tombol yang ditekan adalah "=", fungsi `eval` digunakan untuk mengevaluasi ekspresi dan mengembalikan hasil.

Metode `clear` mengatur atribut `expression` menjadi string kosong dan mengatur tampilan kalkulator menjadi 0.

## Dependensi

- Python 3
- Tkinter

## Cara Penggunaan

1. Buka aplikasi kalkulator dengan menjalankan file `main.py` menggunakan Python.

2. Gunakan tombol di kalkulator untuk memasukkan angka dan melakukan operasi aritmatika.

3. Untuk menghapus tampilan kalkulator, tekan tombol "C".

4. Untuk menghapus karakter terakhir yang dimasukkan, tekan tombol "DEL".

5. Untuk menghitung hasil, tekan tombol "=" Hasil akan ditampilkan di tampilan kalkulator.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.

