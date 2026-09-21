import streamlit as st
import os

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="منظومة إدارة الأعمال والتداول ERP",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تهيئة قاعدة البيانات المركزية
try:
    from database import ERPDatabase
    ERPDatabase.initialize()
except Exception as e:
    st.error(f"🚨 خطأ في تحميل قاعدة البيانات database.py: {e}")

# 3. القائمة الجانبية للتنقل بين الوحدات والأقسام
st.sidebar.title("🏛️ منظومة ERP المركزية")
st.sidebar.caption("نظام إدارة الأعمال والوكلاء الذكي")
st.sidebar.divider()

menu_choice = st.sidebar.radio(
    "اختر اللوحة أو القسم المطلوب:",
    [
        "📈 قسم الأسهم والتداول (Stock Terminal)",
        "🚦 مركز التعميدات والموافقات التنفيذية",
        "🎮 قسم استوديو الألعاب (Unity Ads)",
        "💻 قسم التطبيقات وVS Code (GitHub)",
        "📝 قسم المدونات وSEO (AdSense)",
        "📢 قسم السوشيال ميديا والحملات",
        "💰 قسم المحاسبة والميزانية العامة",
        "🤖 قسم إدارة الوكلاء والتلغرام",
        "📋 قسم إدارة المهام وجدول العمل",
        "🧪 شاشة فحص سلامة الملفات"
    ]
)

st.sidebar.divider()
st.sidebar.info("💡 حالة النظام: **نشط وجاهز 🟢**")

# 4. توجيه التنقل بناءً على اختيار المستخدم
if menu_choice == "📈 قسم الأسهم والتداول (Stock Terminal)":
    try:
        from modules.trading_module import render_trading_module
        render_trading_module()
    except Exception as e:
        st.error(f"🚨 حدث خطأ أثناء تحميل لوحة التداول: {e}")

elif menu_choice == "🚦 مركز التعميدات والموافقات التنفيذية":
    try:
        from modules.approvals import render_approvals_hub
        render_approvals_hub()
    except Exception as e:
        st.error(f"🚨 حدث خطأ أثناء تحميل مركز التعميدات approvals.py: {e}")

elif menu_choice == "🧪 شاشة فحص سلامة الملفات":
    st.title("🧪 شاشة فحص وسلامة تركيب الملفات")
    st.write("تقوم هذه الشاشة بالتحقق التلقائي من مسارات الملفات وعدم تداخلها:")
    
    files_to_check = {
        "الملف الرئيسي (app.py)": "app.py",
        "قاعدة البيانات (database.py)": "database.py",
        "وحدة التداول (modules/trading_module.py)": "modules/trading_module.py",
        "مركز التعميدات (modules/approvals.py)": "modules/approvals.py"
    }
    
    for label, path in files_to_check.items():
        if os.path.exists(path):
            st.success(f"✅ {label}: متوفر في المسار الصحيح!")
        else:
            st.error(f"❌ {label}: مفقود! المسار المتوقع: `{path}`")

else:
    # شاشة مؤقتة تنبيهية للأقسام الأخرى
    st.title(f"🛠️ {menu_choice}")
    st.info("هذا القسم تحت الإنشاء والتطوير حالياً. سيتم ربط ملفه الخاص في التحديثات القادمة.")
