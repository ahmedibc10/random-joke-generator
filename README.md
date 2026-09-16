# Random Joke Generator 😂

تطبيق ويب تفاعلي لتوليد النكات العشوائية من عدة مصادر خارجية موثوقة.

## ✨ المميزات

- 🎭 **نكتة واحدة عشوائية** - احصل على نكتة عشوائية من أي مصدر
- 📚 **عدة نكات** - احصل على عدة نكات دفعة واحدة
- 🏷️ **نكات من فئات** - اختر فئة محددة من النكات
- 🎲 **وضع المفاجأة** - اترك الحظ يختار لك!
- 🌍 **مصادر متعددة** - ثلاث واجهات برمجية مختلفة
- ⚡ **سرعة عالية** - تحميل فوري للنكات

## 📋 المصادر

### 1. Official Joke API
- **الرابط**: https://official-joke-api.appspot.com
- **الوصف**: مكتبة ضخمة من النكات الإنجليزية
- **المميزات**: نكات متنوعة وعالية الجودة

### 2. JokeAPI
- **الرابط**: https://v2.jokeapi.dev
- **الوصف**: واجهة برمجية متقدمة مع نكات مصنفة
- **الفئات**: Programming, Misc, Knock-Knock, General, Spooky, Dark

### 3. icanhazdadjoke
- **الرابط**: https://icanhazdadjoke.com
- **الوصف**: متخصصة في Dad Jokes الكلاسيكية
- **المميزات**: نكات فريدة وطريفة

## 🚀 البدء السريع

### 1. استنساخ المستودع
```bash
git clone https://github.com/ahmedibc10/random-joke-generator.git
cd random-joke-generator
```

### 2. إنشاء بيئة افتراضية
```bash
python -m venv venv
source venv/bin/activate  # على Windows: venv\Scripts\activate
```

### 3. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 4. تشغيل التطبيق
```bash
streamlit run app.py
```

ثم افتح المتصفح على `http://localhost:8501`

## 📖 الاستخدام

### الحصول على نكتة عشوائية
1. اختر "نكتة واحدة" من الشريط الجانبي
2. اضغط على "احصل على نكتة عشوائية"
3. اقرأ النكتة واستمتع! 😂

### الحصول على عدة نكات
1. اختر "عدة نكات" من الشريط الجانبي
2. حدد عدد النكات (1-10)
3. اضغط على الزر للحصول عليها

### الحصول على نكتة من فئة محددة
1. اختر "نكتة من فئة" من الشريط الجانبي
2. اختر الفئة المطلوبة
3. اضغط على الزر

### وضع المفاجأة
1. اختر "مفاجأة" من الشريط الجانبي
2. اضغط على "اضغط للحصول على مفاجأة!"
3. استمتع بالنكتة المفاجأة مع التأثيرات البصرية! 🎉

## 🛠️ البنية المعمارية

```
random-joke-generator/
├── app.py                    # التطبيق الرئيسي (Streamlit)
├── joke_generator.py         # فئة مولد النكات
├── requirements.txt          # المتطلبات
├── README.md                 # التوثيق
└── .gitignore               # ملف التجاهل
```

## 📊 فئات النكات المدعومة

| الفئة | الوصف |
|-------|-------|
| **Programming** | نكات البرمجة والمطورين |
| **Misc** | نكات متنوعة عامة |
| **Knock-Knock** | نكات الطرق الكلاسيكية |
| **General** | نكات عامة |
| **Spooky** | نكات مخيفة طريفة |
| **Dark** | نكات سوداء (فكاهة داكنة) |

## 💻 المتطلبات

```
Python >= 3.8
requests >= 2.31.0
streamlit >= 1.28.0
python-dotenv >= 1.0.0
```

## 🔧 الإعدادات

يمكن تخصيص التطبيق من خلال:
- تعديل timeout في `joke_generator.py`
- إضافة واجهات برمجية جديدة
- تخصيص الألوان والأيقونات

## 🐛 حل المشاكل

### مشكلة: "لا توجد اتصال بالإنترنت"
- تأكد من توفر الإنترنت
- تحقق من أن الواجهات البرمجية تعمل

### مشكلة: "الطلب استغرق وقتاً طويلاً"
- قد تكون الواجهة البرمجية بطيئة
- جرب مصدراً آخر
- تحقق من سرعة إنترنتك

### مشكلة: "رسالة خطأ عند التشغيل"
- تأكد من تثبيت جميع المتطلبات
- استخدم `pip install -r requirements.txt`

## 🤝 المساهمة

نرحب بمساهماتك! يرجى:

1. Fork المستودع
2. أنشئ فرع جديد (`git checkout -b feature/amazing-feature`)
3. أضف تعديلاتك (`git add .`)
4. اكتب رسالة commit واضحة
5. ادفع التعديلات (`git push origin feature/amazing-feature`)
6. افتح Pull Request

## 📝 الترخيص

his project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👨‍💻 المطور

**Ahmad Ibrahim** (ahmedibc10)
- GitHub: [@ahmedibc10](https://github.com/ahmedibc10)
- البريد الإلكتروني: ahmedibc10@example.com

## 🙏 شكر خاص

- فريق **Official Joke API** على الواجهة البرمجية الرائعة
- فريق **JokeAPI** على الخدمة المتقدمة
- مجتمع **icanhazdadjoke** على النكات الكلاسيكية
- فريق **Streamlit** على الأداة المذهلة

## 📞 التواصل والدعم

- 🐛 [أبلغ عن مشكلة](https://github.com/ahmedibc10/random-joke-generator/issues)
- 💬 [اطلب ميزة جديدة](https://github.com/ahmedibc10/random-joke-generator/issues)
- 📧 أرسل بريداً إلكترونياً

---

**Made with ❤️ by Ahmad Ibrahim**

**الآن، اذهب واحصل على بعض النكات! 😂**