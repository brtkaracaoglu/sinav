from ui.mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

class Sinav2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # UI sınıfının örneklenmesi
        self.ui = Ui_MainWindow()
        # UI sınıfının QMainWindow nesnesine bağlanması
        self.ui.setupUi(self)
        # PushButton tıklama sinyali ve ilgili fonksiyonun bağlanması
        self.ui.pushButton.clicked.connect(self.calculate_result)
        self.ui.pushButton.setText("Topla")
        self.ui.label.setText("Sonuc :")

    def calculate_result(self):
        try:
            # İlk LineEdit'ten girilen sayının alınması
            number1 = int(self.ui.lineEdit.text())
            # İkinci LineEdit'ten girilen sayının alınması
            number2 = int(self.ui.lineEdit_2.text())
            # Negatif sayı girildiğinde hata mesajı verilmesi
            if number1 < 0 or number2 < 0:
                raise ValueError("Hata! Negatif sayı yerine tam sayı giriniz...")
            elif number1 < 0 or number1 > 100 or number2 < 0 or number2 > 100:
                raise ValueError("Hata! 0 - 100 aralığında tam sayı giriniz...")
            # Sayıların toplamının hesaplanması
            result = number1 + number2
            # Sonucun Label'a yazdırılması ve str tipine dönüştürülmesi
            self.ui.label.setText("Sonuc: " + str(result))
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                self.ui.label.setText("Hata! Metin yerine tam sayı giriniz...")
            else:
                self.ui.label.setText(str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) # uygulaması başlatılıyor
    window = Sinav2() # Sinav2 sınıfından bir pencere oluşturuluyor
    window.show()  # Pencere gösteriliyor
    sys.exit(app.exec_()) # Uygulama sonlandırılıyor


