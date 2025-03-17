from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SEO Tool")
window.setGeometry(100, 100, 400, 300)
label = QLabel("اولین تست نرم‌افزار!", window)
label.move(150, 130)
window.show()
sys.exit(app.exec())
