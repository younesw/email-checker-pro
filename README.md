# Email Checker Pro

## نظرة عامة | Overview

تطبيق سطح مكتب احترافي للتحقق من حسابات البريد الإلكتروني باستخدام IMAP و SMTP.

Professional desktop application for verifying email accounts using IMAP and SMTP protocols.

## المميزات | Features

✅ **دعم تعدد الخدمات** | Multi-provider support
- Gmail
- Outlook
- Yahoo
- Yandex
- Mail.ru
- ProtonMail

✅ **فحص ثنائي** | Dual verification
- IMAP Login Check
- SMTP Login Check

✅ **واجهة سهلة** | Easy to use interface
- Arabic & English support
- Real-time results
- Clear error messages

✅ **معلومات مفصلة** | Detailed information
- Connection status
- Message count
- Protocol-specific errors

## التثبيت والتشغيل | Installation & Usage

### الطريقة الأولى: تشغيل الملف الجاهز (Easiest)

1. حمّل ملف `EmailCheckerPro.exe` من مجلد `dist/`
2. شغّل الملف مباشرة (لا تحتاج لأي تثبيت)

### الطريقة الثانية: التشغيل من الكود (For Development)

**المتطلبات:**
- Python 3.8+
- pip

**الخطوات:**

```bash
# 1. استنسخ المستودع
git clone https://github.com/younesw/email-checker-pro.git
cd email-checker-pro

# 2. ثبّت المتطلبات
pip install -r requirements.txt

# 3. شغّل التطبيق
python main.py
```

### الطريقة الثالثة: بناء exe الخاص بك (Advanced)

```bash
# Windows
build_exe.bat

# Linux/Mac
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## كيفية الاستعمال | How to Use

1. **أدخل بريدك الإلكتروني** في حقل "Email Address"
2. **أدخل كلمة المرور** في حقل "Password"
   - استخدم **App Password** للحسابات المحمية بـ 2FA
3. **اختر مزود البريد** من قائمة "Provider"
4. **اضغط زر "Check"** لبدء الفحص
5. **شاهد النتائج** في منطقة النتائج

## شرح النتائج | Understanding Results

```
Status: VALID   → البيانات صحيحة ✓
Status: INVALID → البيانات خاطئة ✗
Status: ERROR   → حدث خطأ في الاتصال ⚠️
```

## ملاحظات مهمة | Important Notes

⚠️ **استخدم هذا التطبيق على حساباتك الخاصة فقط**

⚠️ **For 2FA Protected Accounts:**
- أنشئ "App Password" من إعدادات حسابك
- استخدم App Password بدلاً من كلمة المرور الأساسية

⚠️ **الخصوصية:**
- هذا التطبيق يعمل بدون اتصال بأي خادم خارجي
- بيانات المرور تُستخدم فقط للاتصال بخوادم البريد الموثوقة
- لا يتم حفظ أي بيانات على جهازك

## التحكم باللغة | Language Control

- اختر من قائمة اللغة:
  - **العربية (AR)** للواجهة العربية
  - **English (EN)** للواجهة الإنجليزية

## أخطاء شائعة | Common Issues

### "IMAP Authentication failed"
- ✓ تأكد من كلمة المرور صحيحة
- ✓ استخدم App Password بدلاً من كلمة المرور العادية
- ✓ تأكد من تفعيل IMAP في إعدادات البريد

### "Connection timeout"
- ✓ تحقق من اتصالك بالإنترنت
- ✓ قد تكون هناك مشكلة في الشبكة
- ✓ جرّب بعد دقائق قليلة

### "Provider not supported"
- ✓ اختر المزود الصحيح من القائمة
- ✓ تأكد من كتابة البريد بشكل صحيح

## المساعدة الإضافية | More Help

- **Gmail 2FA:** https://support.google.com/accounts/answer/185833
- **Outlook 2FA:** https://support.microsoft.com/en-us/account-billing
- **Yahoo 2FA:** https://help.yahoo.com/kb/SLN2268.html

## الترخيص | License

MIT License - Feel free to use and modify

## المساهمة | Contributing

مرحباً بالمساهمات! يمكنك:
- إضافة خدمات بريد جديدة
- تحسين الواجهة
- إصلاح الأخطاء
- إضافة لغات جديدة

## الدعم | Support

إذا واجهت أي مشاكل:
1. تحقق من القسم "أخطاء شائعة"
2. تأكد من صحة البيانات المدخلة
3. جرّب مع حساب آخر
4. تفضل بفتح issue في المستودع

---

**Made with ❤️ by Younes**
