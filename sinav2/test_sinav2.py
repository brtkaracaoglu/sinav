from PyQt5 import QtWidgets
# ui/mainWindow modülünden Ui_MainWindow sınıfı içe aktarılır.
from ui.mainWindow import Ui_MainWindow
# sinav2 modülünden Sinav2 sınıfı içe aktarılır.
from sinav2 import Sinav2
# pytest kütüphanesinden fixture fonksiyonu içe aktarılır.
import pytest

# app_window adında bir fixture fonksiyonu tanımlanır.
@pytest.fixture
def app_window():
    # QApplication sınıfından bir nesne oluşturulur.
    app = QtWidgets.QApplication([])
    # Sinav2 sınıfından bir nesne oluşturulur.
    window = Sinav2()
    # Fixture nesnesi yield edilir ve nesne kullanıldıktan sonra kapatılır ve uygulama sonlandırılır.
    yield window
    window.close()
    app.exit()


# test_successful_script adında bir test fonksiyonu tanımlanır.
# Bu fonksiyon app_window fixture'ını kullanarak başarılı bir senaryoyu test eder.
def test_successful_script(app_window):
    app_window.ui.lineEdit.setText("2")
    app_window.ui.lineEdit_2.setText("3")
    app_window.ui.pushButton.click()
    assert app_window.ui.label.text() == "Sonuc: 5"

# test_unsuccessful_script_text adında bir test fonksiyonu tanımlanır.
# Bu fonksiyon app_window fixture'ını kullanarak başarısız bir senaryoyu test eder.
# İlk girdi kutusuna sayı yerine metin yazıldığında hata mesajı verilmesi beklenir.
def test_unsuccessful_script_text(app_window):
    app_window.ui.lineEdit.setText("asd")
    app_window.ui.lineEdit_2.setText("3")
    app_window.ui.pushButton.click()
    assert app_window.ui.label.text() == "Hata! Metin yerine tam sayı giriniz..."

def test_unsuccessful_script_negative(app_window):
    app_window.ui.lineEdit.setText("2")
    app_window.ui.lineEdit_2.setText("-3")
    app_window.ui.pushButton.click()
    assert app_window.ui.label.text() == "Hata! Negatif sayı yerine tam sayı giriniz..."

def test_unsuccessful_script_zero_onehundred_range(app_window):
    app_window.ui.lineEdit.setText("2")
    app_window.ui.lineEdit_2.setText("103")
    app_window.ui.pushButton.click()
    assert app_window.ui.label.text() == "Hata! 0 - 100 aralığında tam sayı giriniz..."

if __name__ == '__main__':
    pytest.main()

