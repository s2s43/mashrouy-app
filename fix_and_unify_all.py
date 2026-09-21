import os

# 1. التأكد من وجود المجلدات
os.makedirs('modules', exist_ok=True)
os.makedirs('agents', exist_ok=True)

# 2. ملف التطبيق الرئيسي الموحد app.py
app_code = '''import streamlit as st

st.set_page_config(
    page_title="منظومة مشروعي ERP",
    page_icon="🤖",
    layout="wide"
)

# القائمة الجانبية الموحدة والثابتة
st.sidebar.title("🎮 منظومة مشروعي ERP")
st.sidebar.caption("مركز التحكم بالوكلاء والخدمات")

menu = st.sidebar.radio(
    "اختر القسم المطلوب:",
    [
        "🚦 مركز التعميدات والموافقات",
        "🎮 قسم ألعاب الفيديو (GameAgent)",
        "✍️ التسويق و SEO (BloggerAgent)",
        "📈 الأسهم والكريبتو (CryptoAgent)",
        "💻 البرمجة والخدمات (DevAgent)",
        "📲 التنبيهات والتلغرام (TelegramAgent)"
    ]
)

st.sidebar.divider()
st.sidebar.success("🟢 جميع الوكلاء نشطون")

# 1. مركز التعميدات
if menu == "🚦 مركز التعميدات والموافقات":
    st.title("🚦 مركز التعميدات والموافقات التنفيذية")
    st.caption("صمام الأمان: لا يتم إرسال أو نشر أي أمر إلا بعد موافقتك الصريحة.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("القرارات المعلقة", "3")
    col2.metric("القرارات المعمدة", "12")
    col3.metric("مستوى السيطرة", "100% بشرية")
    
    st.divider()
    st.subheader("📋 الطلبات بانتظار الاعتماد")
    
    with st.expander("📌 [APPR-101] وكيل التدوين (BloggerAgent) - نشر مقال SEO", expanded=True):
        st.write("**العنوان:** دليل شامل: استخدام الذكاء الاصطناعي في تحسين أداء الألعاب")
        st.write("**المحتوى:** مقال صاغه الذكاء الاصطناعي بـ 1200 كلمة جاهز للنشر على Blogger.")
        st.caption("التاريخ: 2026-09-21")
        c1, c2 = st.columns([2, 2])
        with c1:
            if st.button("🟢 اعتمد ونفّذ الآن", key="app1"):
                st.success("تم التعميد بالنشر!")
        with c2:
            if st.button("🔴 رفض القرار", key="rej1"):
                st.error("تم الرفض.")

    with st.expander("📌 [APPR-102] وكيل ألعاب الفيديو (GameAgent) - تعديل eCPM", expanded=True):
        st.write("**القرار:** رفع الحد الأدنى لـ eCPM floor إلى .50 في شبكات AdMob/Unity")
        c1, c2 = st.columns([2, 2])
        with c1:
            if st.button("🟢 اعتمد ونفّذ الآن", key="app2"):
                st.success("تم تحديث أسعار الإعلانات!")
        with c2:
            if st.button("🔴 رفض القرار", key="rej2"):
                st.error("تم الرفض.")

# 2. قسم ألعاب الفيديو
elif menu == "🎮 قسم ألعاب الفيديو (GameAgent)":
    st.title("🎮 قسم إدارة ألعاب الفيديو والمونتايز")
    st.info("🤖 **الوكيل المسؤول:** GameAgent")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("إجمالي الظهور الإعلاني", "245,800")
    m2.metric("متوسط eCPM الحالي", ".20")
    m3.metric("العائد اليومي المتوقع", ".90")
    
    st.subheader("الألعاب النشطة والشلال الإعلاني (Waterfall)")
    st.write("- **Game #1 (Subway Runner AI):** Unity Ads 🟢 - eCPM Floor: .00")
    st.write("- **Game #2 (Crypto Puzzle):** AdMob 🟢 - eCPM Floor: .50")

# 3. قسم التسويق و SEO
elif menu == "✍️ التسويق و SEO (BloggerAgent)":
    st.title("✍️ قسم التسويق، الـ SEO، والمدونات")
    st.info("🤖 **الوكيل المسؤول:** BloggerAgent")
    st.write("يقوم الوكيل بصياغة المقالات، تحليل الكلمات المفتاحية، وإرسالها لمركز التعميدات قبل النشر.")

# 4. قسم الأسهم والكريبتو
elif menu == "📈 الأسهم والكريبتو (CryptoAgent)":
    st.title("📈 قسم التداول والتحليل المالي")
    st.info("🤖 **الوكيل المسؤول:** CryptoAgent")
    st.write("فحص المؤشرات الفنية (RSI, MACD) وإعداد توصيات المحفظة.")

# 5. قسم البرمجة والخدمات
elif menu == "💻 البرمجة والخدمات (DevAgent)":
    st.title("💻 قسم التطوير المباشر والبرمجة")
    st.info("🤖 **الوكيل المسؤول:** DevAgent")
    st.write("مراجعة جودة الكود، فحص الأخطاء، وإدارة التحديثات تلقائياً.")

# 6. قسم التنبيهات والتلغرام
elif menu == "📲 التنبيهات والتلغرام (TelegramAgent)":
    st.title("📲 قسم التنبيهات وإشعار المدير")
    st.info("🤖 **الوكيل المسؤول:** TelegramAgent")
    st.write("ربط التنبيهات الفورية وبوت التلغرام لإرسال الملخصات اليومية.")
'''

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("✅ تم توحيد كود جميع الأقسام بنجاح داخل app.py بملف واحد مالي الشاشة!")
