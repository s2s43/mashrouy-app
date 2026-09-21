import streamlit as st
import pandas as pd
from database import ERPDatabase

def render_games_module():
    ERPDatabase.initialize()

    st.title("🎮 قسم ألعاب الفيديو والإعلانات (Unity and AdMob)")
    st.caption("متابعة إحصائيات الألعاب، أداء إعلانات Unity and AdMob، ومتابعة GameAgent")
    st.divider()

    if 'games_data' not in st.session_state:
        st.session_state['games_data'] = [
            {
                'game_id': 'GAME-001',
                'title': 'Desert Racer 3D',
                'platform': 'Android / Unity',
                'ecpm': 14.50,
                'revenue_usd': 185.30,
                'status': 'نشط 🟢',
                'ad_network': 'Unity Ads + AdMob'
            },
            {
                'game_id': 'GAME-002',
                'title': 'Cyber Runner',
                'platform': 'iOS / Unity',
                'ecpm': 22.10,
                'revenue_usd': 72.56,
                'status': 'نشط 🟢',
                'ad_network': 'AppLovin + Unity Ads'
            }
        ]

    games = st.session_state['games_data']

    st.subheader("📊 مؤشرات العوائد والـ eCPM")
    total_rev = sum(g['revenue_usd'] for g in games)
    avg_ecpm = sum(g['ecpm'] for g in games) / len(games) if games else 0.0

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("إجمالي أرباح الألعاب", f"")
    m2.metric("متوسط eCPM", f"")
    m3.metric("عدد الألعاب النشطة", len(games))
    m4.metric("الشبكات الإعلانية", "Unity / AdMob / AppLovin")

    st.divider()

    st.subheader("⚙️ أزرار التحكم والعمليات")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.button("🔄 تحديث تقارير eCPM الآن", use_container_width=True)
    with c2:
        st.button("⚡ تحسين شلال الإعلانات (Waterfall)", use_container_width=True)
    with c3:
        st.button("📲 إرسال تقرير الأرباح للتلغرام", use_container_width=True)
    with c4:
        st.button("🤖 إنابة GameAgent", use_container_width=True)

    st.divider()

    st.subheader("🤖 بطاقة متابعة وكيل الألعاب (GameAgent)")
    agents = ERPDatabase.get_agents()
    game_agent = agents.get('game_agent', {
        'name': 'وكيل استوديو الألعاب (GameAgent)',
        'module': 'قسم ألعاب الفيديو',
        'status': 'نشط 🟢',
        'schedule_type': 'يومي (Daily)',
        'last_completed': 'تم تحديث وحدات الإعلانات وضبط أسعار eCPM Floor.',
        'next_intention': 'تحليل أداء إعلانات المكافآت (Rewarded Video) وترفيع eCPM.'
    })

    with st.expander(f"📋 تفاصيل عمل الوكيل: {game_agent.get('name')} [{game_agent.get('status')}]", expanded=True):
        ag1, ag2 = st.columns(2)
        with ag1:
            st.markdown(f"**جدولة المهمة:** {game_agent.get('schedule_type')}")
            st.markdown(f"**✅ المهام المنفذة سابقاً:**
{game_agent.get('last_completed')}")
        with ag2:
            st.markdown(f"**🎯 خطة العمل القادمة:**
{game_agent.get('next_intention')}")

    st.divider()

    st.subheader("➕ إضافة لعبة جديدة للقائمة")
    with st.form("add_game_form", clear_on_submit=True):
        f1, f2, f3 = st.columns(3)
        with f1:
            in_title = st.text_input("اسم اللعبة:", placeholder="مثال: Space War 3D")
        with f2:
            in_platform = st.text_input("المنصة / المحرك:", placeholder="مثال: Android / Unity")
        with f3:
            in_ecpm = st.number_input("متوسط eCPM ($):", min_value=0.1, value=12.0, step=0.5)

        if st.form_submit_button("➕ إضافة اللعبة"):
            if in_title:
                new_id = f"GAME-00{len(games) + 1}"
                st.session_state['games_data'].append({
                    'game_id': new_id,
                    'title': in_title,
                    'platform': in_platform if in_platform else 'Unity Engine',
                    'ecpm': in_ecpm,
                    'revenue_usd': 0.0,
                    'status': 'نشط 🟢',
                    'ad_network': 'Unity Ads + AdMob'
                })
                st.success(f"تمت إضافة اللعبة {in_title} بنجاح!")
                st.rerun()
            else:
                st.error("يرجى إدخال اسم اللعبة!")

    st.divider()

    st.subheader("📋 قائمة ألعاب الاستوديو")
    if games:
        for game in games:
            title_header = f"📌 {game['title']} ({game['game_id']}) | المنصة: {game['platform']} | eCPM: \ | العائد: \ [{game['status']}]"
            with st.expander(title_header):
                st.write(f"**الشبكات الإعلانية المربوطة:** {game.get('ad_network', 'Unity Ads')}")
                st.write(f"**العائد الإجمالي المسجل:** ")
    else:
        st.info("لا توجد ألعاب مسجلة حالياً.")
