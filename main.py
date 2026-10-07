import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QMessageBox
)
from email_checker import EmailChecker
from config import PROVIDERS, TRANSLATIONS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Checker Pro")
        self.resize(1100, 700)
        self.language = "ar"
        self.checker = EmailChecker()

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()

        # Header row
        header = QHBoxLayout()
        title = QLabel("Email Checker Pro")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.addWidget(title)
        header.addStretch()

        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["العربية", "English"])
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        header.addWidget(self.lang_combo)
        layout.addLayout(header)

        # Form row
        form_row = QHBoxLayout()

        self.email_label = QLabel("البريد الإلكتروني")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("example@gmail.com")

        self.password_label = QLabel("كلمة المرور")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password / App Password")

        self.provider_label = QLabel("مزود البريد")
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(sorted(PROVIDERS.keys()))

        self.check_btn = QPushButton("فحص")
        self.check_btn.clicked.connect(self.run_check)

        self.clear_btn = QPushButton("مسح")
        self.clear_btn.clicked.connect(self.clear_all)

        form_row.addWidget(self.email_label)
        form_row.addWidget(self.email_input)
        form_row.addWidget(self.password_label)
        form_row.addWidget(self.password_input)
        form_row.addWidget(self.provider_label)
        form_row.addWidget(self.provider_combo)
        form_row.addWidget(self.check_btn)
        form_row.addWidget(self.clear_btn)

        layout.addLayout(form_row)

        # Output area
        output_label = QLabel("النتيجة")
        output_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(output_label)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("font-size: 12px; font-family: Consolas; background: #f8f8f8;")
        layout.addWidget(self.output)

        # Notes
        self.notes = QTextEdit()
        self.notes.setReadOnly(True)
        self.notes.setMaximumHeight(120)
        self.notes.setPlainText("ملاحظات: استخدم كلمات مرور التطبيقات للحسابات المحمية بـ 2FA")
        layout.addWidget(self.notes)

        central.setLayout(layout)
        self.change_language(0)

    def change_language(self, index):
        self.language = "ar" if index == 0 else "en"
        trans = TRANSLATIONS[self.language]

        self.setWindowTitle(trans["title"])
        self.email_label.setText(trans["email"])
        self.password_label.setText(trans["password"])
        self.provider_label.setText(trans["provider"])
        self.check_btn.setText(trans["check"])
        self.clear_btn.setText(trans["clear"])
        self.notes.setPlainText(trans["notes"])

    def run_check(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        provider = self.provider_combo.currentText()

        if not email or not password:
            QMessageBox.warning(self, "Warning", "Please enter email and password")
            return

        result = self.checker.check_account(email, password, provider)

        self.output.clear()
        self.output.append(f"Email: {result['email']}\n")
        self.output.append(f"Provider: {result['provider']}\n")
        self.output.append("=" * 50)
        self.output.append(f"IMAP: {result['imap']['status']} - {result['imap']['message']}\n")
        if 'inbox_count' in result['imap']:
            self.output.append(f"Inbox Count: {result['imap']['inbox_count']}\n")
        self.output.append(f"SMTP: {result['smtp']['status']} - {result['smtp']['message']}\n")

    def clear_all(self):
        self.email_input.clear()
        self.password_input.clear()
        self.output.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
