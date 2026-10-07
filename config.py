# Configuration file for Email Checker Pro

PROVIDERS = {
    "gmail": {
        "imap_server": "imap.gmail.com",
        "imap_port": 993,
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 465,
        "display_name": "Gmail"
    },
    "outlook": {
        "imap_server": "outlook.office365.com",
        "imap_port": 993,
        "smtp_server": "smtp.office365.com",
        "smtp_port": 587,
        "display_name": "Outlook"
    },
    "yahoo": {
        "imap_server": "imap.mail.yahoo.com",
        "imap_port": 993,
        "smtp_server": "smtp.mail.yahoo.com",
        "smtp_port": 465,
        "display_name": "Yahoo"
    },
    "yandex": {
        "imap_server": "imap.yandex.com",
        "imap_port": 993,
        "smtp_server": "smtp.yandex.com",
        "smtp_port": 465,
        "display_name": "Yandex"
    },
    "mailru": {
        "imap_server": "imap.mail.ru",
        "imap_port": 993,
        "smtp_server": "smtp.mail.ru",
        "smtp_port": 465,
        "display_name": "Mail.ru"
    },
    "proton": {
        "imap_server": "imap.proton.me",
        "imap_port": 993,
        "smtp_server": "smtp.proton.me",
        "smtp_port": 587,
        "display_name": "ProtonMail"
    }
}

TRANSLATIONS = {
    "ar": {
        "title": "مدقق البريد الإلكتروني",
        "email": "البريد الإلكتروني",
        "password": "كلمة المرور",
        "provider": "مزود البريد",
        "language": "اللغة",
        "check": "فحص",
        "clear": "مسح",
        "export": "تصدير",
        "warning": "تحذير",
        "enter_email_password": "يرجى إدخال البريد وكلمة المرور",
        "checking": "جاري الفحص...",
        "valid": "✓ صحيح",
        "invalid": "✗ خاطئ",
        "status": "الحالة",
        "inbox_count": "عدد الرسائل",
        "result": "النتيجة",
        "error": "خطأ",
        "timeout": "انتهت مهلة الانتظار",
        "unsupported": "مزود غير مدعوم",
        "success": "نجح التحقق",
        "failed": "فشل التحقق",
        "imap_login": "تسجيل دخول IMAP",
        "smtp_login": "تسجيل دخول SMTP",
        "notes": "ملاحظات: استخدم كلمات مرور التطبيقات للحسابات المحمية بـ 2FA"
    },
    "en": {
        "title": "Email Checker Pro",
        "email": "Email Address",
        "password": "Password",
        "provider": "Email Provider",
        "language": "Language",
        "check": "Check",
        "clear": "Clear",
        "export": "Export",
        "warning": "Warning",
        "enter_email_password": "Please enter email and password",
        "checking": "Checking...",
        "valid": "✓ Valid",
        "invalid": "✗ Invalid",
        "status": "Status",
        "inbox_count": "Messages Count",
        "result": "Result",
        "error": "Error",
        "timeout": "Connection timeout",
        "unsupported": "Provider not supported",
        "success": "Login successful",
        "failed": "Login failed",
        "imap_login": "IMAP Login",
        "smtp_login": "SMTP Login",
        "notes": "Note: Use app passwords for 2FA protected accounts"
    }
}
