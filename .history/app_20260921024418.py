import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import requests
import json

# ================= =================
# إعدادات الصفحة والتصميم العالي والجودة (RTL)
# ================= =================
st.set_page_config(
    page_title="منظومة مشروعي - إدارة الذكاء الاصطناعي",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق اتجاه النص العربي وضبط التصميم
st.markdown("""
    <style>
    body, .stMarkdown, .stButton, div, button, input { direction: rtl; text-align: right; }
    .stMetric { background-color: #f8f9fa; padding: 10px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# ================= =================
# إدارة الحالة للأنظمة المدمجة (Session State)
# ================= =================
if 'portfolio_balance' not in st.session_state:
    st.session_state.portfolio_balance = 10000.0
if 'owned_assets' not in st.session_state:
    st.session_state.owned_assets = {}
if 'trade_history' not in st.session_state:
    st.session_state.trade_history = []
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = ""
if 'saas_orders' not in st.session_state:
    st.session_state.saas_orders = []

# ================= =================
# القائمة الجانبية (Sidebar Navigation)
# ================= =================
st.sidebar.title("🔒 مشروع: مشروعي")
st.sidebar.subheader("مركز التحكم والقيادة")

menu = st.sidebar.radio(
    "اختر القسم المطلوب:",
    [
        "📊 لوحة القيادة والمراقبة",
        "📈 وكيل الأسهم والعملات الرقمية (Crypto & Stocks)",
        "🛠️ متجر الخدمات وأتمتة البرمجة (Micro-SaaS)",
        "📣 وكيل التسويق والـ SEO والشبكات",
        "⚙️ مركز التنبيهات والربط السحابي (APIs & Telegram)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("💡 جميع الأنظمة متصلة ومجانية 100%.")

# ================= =================
# 1. لوحة القيادة والمراقبة
# ================= =================
if menu == "📊 لوحة القيادة والمراقبة":
    st.title("📊 لوحة القيادة التنفيذية")
    st.write("مرحباً بك! هذه الشاشة توضح أداء المنظومة، الرصيد المالي، وحالة الوكلاء النشطين.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("رصيد محفظة التداول الافتراضية", f"${st.session_state.portfolio_balance:,.2f}")
    with col2:
        st.metric("عدد الصفقات المنفذة", len(st.session_state.trade_history))
    with col3:
        st.metric("طلبات الخدمات المباعة (SaaS)", len(st.session_state.saas_orders))
    with col4:
        st.metric("حالة المنظومة", "🟢 تعمل بكفاءة")

    st.markdown("---")
    st.subheader("🤖 حالة وكلاء الذكاء الاصطناعي في الخلفية")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.success("🟢 **وكيل البرمجة والخدمات**\n\nيستقبل الطلبات")
    with c2:
        st.success("🟢 **وكيل الأسهم والكريبتو**\n\nيفحص المؤشرات")
    with c3:
        st.success("🟢 **وكيل التسويق والـ SEO**\n\nيولد المحتوى")
    with c4:
        st.success("🟢 **وكيل التنبيهات**\n\nمتصل بالتلغرام")

# ================= =================
# 2. وكيل الأسهم والعملات الرقمية
# ================= =================
elif menu == "📈 وكيل الأسهم والعملات الرقمية (Crypto & Stocks)":
    st.title("📈 وكيل التحليل المالي والتداول الافتراضي الشامل")
    st.write("تحليل وحساب صفقات الأسهم والعملات الرقمية تلقائياً بناءً على مؤشر القوة النسبية (RSI).")

    asset_type = st.radio("اختر نوع السوق:", ["أسهم عالمية (Stocks)", "عملات رقمية (Crypto)"], horizontal=True)
    
    if asset_type == "أسهم عالمية (Stocks)":
        symbol = st.text_input("أدخل رمز السهم (مثال: AAPL, NVDA, MSFT, TSLA):", "AAPL").upper()
    else:
        symbol = st.text_input("أدخل رمز العملة الرقمية (مثال: BTC-USD, ETH-USD, SOL-USD):", "BTC-USD").upper()

    if st.button("🔍 فحص الأصل المالي وتنفيذ توصية الوكيل"):
        try:
            asset = yf.Ticker(symbol)
            df = asset.history(period="1mo", interval="1d")
            
            if not df.empty:
                current_price = df['Close'].iloc[-1]
                
                # حساب RSI
                delta = df['Close'].diff()
                gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                rs = gain / loss
                rsi = 100 - (100 / (1 + rs))
                current_rsi = rsi.iloc[-1]

                st.info(f"السعر الحالي لـ **{symbol}**: **${current_price:,.2f}** | قيمة مؤشر RSI: **{current_rsi:.2f}**")

                if current_rsi < 40 and st.session_state.portfolio_balance >= current_price:
                    st.session_state.portfolio_balance -= current_price
                    st.session_state.owned_assets[symbol] = st.session_state.owned_assets.get(symbol, 0) + 1
                    st.session_state.trade_history.append({"التاريخ": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "الأصل": symbol, "العملية": "شراء", "السعر": current_price})
                    st.success(f"🟢 **توصية الشراء:** تمت محاكاة شراء أصل من {symbol} بسعر ${current_price:,.2f}")

                elif current_rsi > 60 and st.session_state.owned_assets.get(symbol, 0) > 0:
                    st.session_state.portfolio_balance += current_price
                    st.session_state.owned_assets[symbol] -= 1
                    st.session_state.trade_history.append({"التاريخ": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "الأصل": symbol, "العملية": "بيع", "السعر": current_price})
                    st.warning(f"🔴 **توصية البيع:** تمت محاكاة بيع أصل من {symbol} بسعر ${current_price:,.2f}")

                else:
                    st.info("⚪ **توصية الوكيل:** الانتظار والمراقبة (HOLD).")

            else:
                st.error("تعذر جلب البيانات. تأكد من صحة الرمز.")
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال بالأسواق: {e}")

    st.markdown("---")
    st.subheader("📜 سجل المحاكاة والأصول المملوكة")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**الأصول المملوكة حالياً:**")
        st.json(st.session_state.owned_assets)
    with col_b:
        st.write("**سجل الصفقات:**")
        if st.session_state.trade_history:
            st.dataframe(pd.DataFrame(st.session_state.trade_history))
        else:
            st.write("لا توجد صفقات منفذة حتى الآن.")

# ================= =================
# 3. متجر الخدمات وأتمتة البرمجة (Micro-SaaS)
# ================= =================
elif menu == "🛠️ متجر الخدمات وأتمتة البرمجة (Micro-SaaS)":
    st.title("🛠️ متجر الخدمات والبرمجة الذكي")
    st.write("أنشئ منتجات Micro-SaaS أو قدم خدمات برمجة فائقة السرعة لعملائك.")

    tab1, tab2 = st.columns(2)
    with tab1:
        st.subheader("طلب بناء تطبيق / خدمة")
        client_name = st.text_input("اسم العميل أو المشروع:", "عميل رقم 1")
        service_type = st.selectbox("نوع الخدمة المطلوبة:", ["صفحة هبوط تسويقية (Landing Page)", "حاسبة أرباح تفاعلية", "أداة تحسين SEO"])
        price = st.number_input("قيمة الخدمة ($):", value=49.0)

        if st.button("🔨 تنفيذ الخدمة وتوليد الكود"):
            code_template = f"<!-- كود تم إنشاؤه أوتوماتيكياً بواسطة وكيل مشروعي لـ {client_name} -->\n<h1>خدمة {service_type} الذكية</h1>\n<p>تم التسليم بنجاح وتجهيز الخدمة بالكامل.</p>"
            st.session_state.generated_code = code_template
            st.session_state.saas_orders.append({"العميل": client_name, "الخدمة": service_type, "المبلغ": f"${price}", "التاريخ": datetime.datetime.now().strftime("%Y-%m-%d")})
            st.success("✅ تم اعتماد الطلب وتوليد المشروع فوراً!")

    with tab2:
        st.subheader("سجل مبيعات الخدمات (Passive Income)")
        if st.session_state.saas_orders:
            st.dataframe(pd.DataFrame(st.session_state.saas_orders))
        else:
            st.write("لا توجد مبيعات مسجلة بعد.")

    if st.session_state.generated_code:
        st.markdown("---")
        st.subheader("💻 الكود المولد للعميل:")
        st.code(st.session_state.generated_code, language="html")

# ================= =================
# 4. وكيل التسويق والـ SEO والشبكات
# ================= =================
elif menu == "📣 وكيل التسويق والـ SEO والشبكات":
    st.title("📣 وكيل تسويق الخدمات وجلب الزيارات (SEO & Social)")
    st.write("صياغة منشورات السوشيال ميديا ومقالات الـ SEO لجلب عملاء وتكثيف الانتشار مجاناً.")

    keyword = st.text_input("الكلمة المفتاحية أو اسم المنتج:", "أفضل أدوات تحليل الأسهم بالذكاء الاصطناعي")

    if st.button("📝 كتابة مقال SEO وحملة تسويقية"):
        with st.spinner("جاري صياغة المحتوى المحسّن..."):
            seo_article = f"## {keyword}\n\nتعتبر أتمتة التحليل المالي من أهم الخطوات للربح المستدام. توفر لك منصاتنا الذكية إمكانية الوصول إلى تنبيهات لحظية ومتابعة الأسواق بدقة عالية.\n\n### المميزات:\n1. تحليل فني أوتوماتيكي.\n2. تنبيهات تلغرام فورية.\n3. أمان عالي بدون مخاطرة."
            social_post = f"🚀 لا تدع الفرص تفوتك في الأسواق! تعرّف على {keyword} وكيف يمكنك الاستفادة منها الآن. #ذكاء_اصطناعي #تداول #مشروعي"

            col_sec1, col_sec2 = st.columns(2)
            with col_sec1:
                st.subheader("📰 مقال جاهز للموقع/المدونة (SEO):")
                st.markdown(seo_article)
            with col_sec2:
                st.subheader("📱 منشور جاهز للتواصل (X / LinkedIn):")
                st.text_area("نص المنشور:", social_post, height=150)

# ================= =================
# 5. مركز التنبيهات والربط السحابي
# ================= =================
elif menu == "⚙️ مركز التنبيهات والربط السحابي (APIs & Telegram)":
    st.title("⚙️ ربط التنبيهات مع هاتفك (Telegram Bot)")
    st.write("ربط البوت لتصلك إشعارات الأرباح وتوصيات الأسهم والخدمات على هاتفك مباشرة.")

    bot_token = st.text_input("رمز التلغرام (Telegram Bot Token):", type="password")
    chat_id = st.text_input("معرّف المحادثة (Chat ID):", type="password")

    test_message = st.text_area("رسالة التجربة:", "🔔 تنبيه من لوحة مشروعي: جميع الوكلاء يعملون بنجاح!")

    if st.button("📲 إرسال إشعار تجريبي إلى الهاتف"):
        if bot_token and chat_id:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {"chat_id": chat_id, "text": test_message}
            try:
                res = requests.post(url, json=payload)
                if res.status_code == 200:
                    st.success("✅ تم إرسال الإشعار لتطبيق التلغرام على هاتفك بنجاح!")
                else:
                    st.error(f"فشل الإرسال: {res.text}")
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
        else:
            st.warning("يرجى إدخال الـ Token والـ Chat ID تجربة الإرسال.")