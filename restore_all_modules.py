import os

app_code = '''import streamlit as st
from modules.approvals_module import render_approvals_module
from modules.games_module import render_games_module

st.set_page_config(
    page_title="منظومة مشروعي - إدارة الذكاء الاصطناعي ERP",
    page_icon="🤖",
    layout="wide"
)

# القائمة الجانبية الشاملة لكافة الأقسام والوكلاء
st.sidebar.title("🎮 منظومة مشروعي ERP")
st.sidebar.caption("إدارة الأقسام والوكلاء المستقلين")

menu = st.sidebar.radio(
    "اختر القسم:",
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
st.sidebar.success("🟢 جميع الوكلاء يعملون في الخلفية")

# التوجيه الشامل للأقسام
if menu == "🚦 مركز التعميدات والموافقات":
    render_approvals_module()

elif menu == "🎮 قسم ألعاب الفيديو (GameAgent)":
    render_games_module()

elif menu == "✍️ التسويق و SEO (BloggerAgent)":
    st.title("✍️ قسم التسويق والـ SEO")
    st.info("🤖 **الوكيل المسؤول:** BloggerAgent")
    st.markdown("""
    - **المهام الموكلة:** تحليل الكلمات المفتاحية، كتابة المقالات، وتجهيز المسودات.
    - **الحالة الحية:** يعمل على تجهيز مقال جديد وحفظه في **مركز التعميدات** بانتظار موافقتك.
    """)

elif menu == "📈 الأسهم والكريبتو (CryptoAgent)":
    st.title("📈 قسم تحليل الأسهم والعملات الرقمية")
    st.info("🤖 **الوكيل المسؤول:** CryptoAgent")
    st.markdown("""
    - **المهام الموكلة:** مراقبة أسواق الكريبتو والمؤشرات (RSI / MACD) والتنبه بالفرص.
    - **الحالة الحية:** فحص حركة السوق مستمر.
    """)

elif menu == "💻 البرمجة والخدمات (DevAgent)":
    st.title("💻 قسم التطوير والبرمجة")
    st.info("🤖 **الوكيل المسؤول:** DevAgent")
    st.markdown("""
    - **المهام الموكلة:** فحص الثغرات، تدقيق الأكواد، واختبار الأداء البرمجي.
    - **الحالة الحية:** خامل (جاهز لتلقي المهام البرمجية).
    """)

elif menu == "📲 التنبيهات والتلغرام (TelegramAgent)":
    st.title("📲 قسم الإشعارات والتلغرام")
    st.info("🤖 **الوكيل المسؤول:** TelegramAgent")
    st.markdown("""
    - **المهام الموكلة:** توجيه التقارير الملخصة والتنبيهات العاجلة لجوال المدير.
    - **الحالة الحية:** متصل بالبوت وقيد الانتظار.
    """)
'''

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("✅ تم إعادة كافة الأقسام والوكلاء إلى القائمة الرئيسية بنجاح!")
