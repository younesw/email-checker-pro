import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QMessageBox,
    QScrollArea, QGroupBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QColor
from email_checker import EmailChecker
from config import PROVIDERS, TRANSLATIONS

class CheckerThread(QThread):
    finished = pyqtSignal(dict)
    
    def __init__(self, email, password, provider):
        super().__init__()
        self.email = email
        self.password = password
        self.provider = provider
        self.checker = EmailChecker()
    
    def run(self):
        result = self.checker.check_account(self.email, self.password, self.provider)
        self.finished.emit(result)

class EmailCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language = "ar"
        self.translations = TRANSLATIONS
        self.checker = EmailChecker()
        self.checker_thread = None
        
        self.init_ui()
        self.set_language("ar")
    
    def init_ui(self):
        self.setWindowTitle("Email Checker Pro")
        self.setGeometry(100, 100, 1100, 750)
        self.setStyleSheet(self.get_stylesheet())
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Header
        header = QHBoxLayout()
        title = QLabel("Email Checker Pro")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        header.addWidget(title)
        header.addStretch()
        
        # Language selector
        lang_label = QLabel("Language")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["العربية (AR)", "English (EN)"])
        self.lang_combo.currentIndexChanged.connect(self.on_language_changed)
        header.addWidget(lang_label)
        header.addWidget(self.lang_combo)
        
        main_layout.addLayout(header)
        
        # Input form
        form_layout = QHBoxLayout()
        
        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("your_email@gmail.com")
        self.email_input.setMinimumWidth(200)
        
        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Your password or app password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumWidth(180)
        
        self.provider_label = QLabel("Provider")
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(sorted(PROVIDERS.keys()))
        
        self.check_btn = QPushButton("Check")
        self.check_btn.clicked.connect(self.run_check)
        self.check_btn.setMinimumWidth(120)
        self.check_btn.setMinimumHeight(35)
        
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_form)
        self.clear_btn.setMinimumWidth(100)
        self.clear_btn.setMinimumHeight(35)
        
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.provider_label)
        form_layout.addWidget(self.provider_combo)
        form_layout.addWidget(self.check_btn)
        form_layout.addWidget(self.clear_btn)
        form_layout.addStretch()
        
        main_layout.addLayout(form_layout)
        
        # Output area
        output_label = QLabel("Results")
        output_label.setFont(QFont("Arial", 12, QFont.Bold))
        main_layout.addWidget(output_label)
        
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setMinimumHeight(400)
        self.output.setFont(QFont("Courier", 10))
        main_layout.addWidget(self.output)
        
        # Notes
        notes_label = QLabel("Notes")
        notes_label.setFont(QFont("Arial", 10, QFont.Bold))
        main_layout.addWidget(notes_label)
        
        self.notes = QTextEdit()
        self.notes.setReadOnly(True)
        self.notes.setMinimumHeight(80)
        main_layout.addWidget(self.notes)
    
    def get_stylesheet(self):
        return """
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLineEdit, QComboBox, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                background-color: white;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """
    
    def run_check(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        provider = self.provider_combo.currentText()
        
        if not email or not password:
            QMessageBox.warning(self, "Warning", "Please enter email and password")
            return
        
        self.check_btn.setEnabled(False)
        self.check_btn.setText("Checking...")
        self.output.clear()
        self.output.setText("Processing...\n")
        
        self.checker_thread = CheckerThread(email, password, provider)
        self.checker_thread.finished.connect(self.on_check_finished)
        self.checker_thread.start()
    
    def on_check_finished(self, result):
        self.check_btn.setEnabled(True)
        self.check_btn.setText(self.trans("check"))
        
        output_text = f"""
╔════════════════════════════════════════════════════════════╗
║                    CHECK RESULT                            ║
╚════════════════════════════════════════════════════════════╝

Email: {result['email']}
Provider: {result['provider']}

--- IMAP CHECK ---
Status: {result['imap']['status'].upper()}
Method: {result['imap']['method']}
Message: {result['imap']['message']}
"""
        
        if 'inbox_count' in result['imap']:
            output_text += f"Inbox Messages: {result['imap']['inbox_count']}\n"
        
        output_text += f"""
--- SMTP CHECK ---
Status: {result['smtp']['status'].upper()}
Method: {result['smtp']['method']}
Message: {result['smtp']['message']}

╔════════════════════════════════════════════════════════════╗
"""
        
        self.output.setText(output_text)
    
    def clear_form(self):
        self.email_input.clear()
        self.password_input.clear()
        self.output.clear()
    
    def on_language_changed(self, index):
        lang = "ar" if index == 0 else "en"
        self.set_language(lang)
    
    def set_language(self, lang):
        self.language = lang
        trans = self.translations[lang]
        
        self.setWindowTitle(trans["title"])
        self.email_label.setText(trans["email"])
        self.password_label.setText(trans["password"])
        self.provider_label.setText(trans["provider"])
        self.check_btn.setText(trans["check"])
        self.clear_btn.setText(trans["clear"])
        self.notes.setText(trans["notes"])
    
    def trans(self, key):
        return self.translations[self.language].get(key, key)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailCheckerApp()
    window.show()
    sys.exit(app.exec_())
