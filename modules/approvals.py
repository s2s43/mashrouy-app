import streamlit as st
import pandas as pd
from datetime import datetime

def render_approvals_hub():
    st.markdown("## 🚦 مركز التعميدات والموافقات التنفيذية")
    st.markdown("---")

    # تهيئة الحالة الافتراضية للطلبات إذا لم تكن موجودة
    if 'approvals_list' not in st.session_state:
        st.session_state.approvals_list = [
            {"id": 1, "title": "تطوير واجهة التداول الآلي", "department": "التقنية والتطوير", "amount": 15000, "priority": "عالية", "status": "معلق", "date": "2026-09-20"},
            {"id": 2, "title": "شراء تراخيص نظام بلوجر الإعلاني", "department": "التسويق", "amount": 4200, "priority": "متوسطة", "status": "معتمد", "date": "2026-09-18"},
            {"id": 3, "title": "ميزانية الحملة الترويجية للألعاب", "department": "الألعاب", "amount": 8500, "priority": "عالية", "status": "مرفوض", "date": "2026-09-15"}
        ]

    # إحصائيات سريعة للطلبات
    total_reqs = len(st.session_state.approvals_list)
    pending_reqs = len([r for r in st.session_state.approvals_list if r['status'] == 'معلق'])
    approved_reqs = len([r for r in st.session_state.approvals_list if r['status'] == 'معتمد'])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("إجمالي الطلبات", total_reqs)
    with col2:
        st.metric("الطلبات المعلقة ⏳", pending_reqs)
    with col3:
        st.metric("الطلبات المعتمدة ✅", approved_reqs)

    st.markdown("### 📥 الطلبات الواردة التي تتطلب اتخاذ قرار")

    # عرض الطلبات في جدول تفاعلي مع خيارات اتخاذ القرار
    for idx, req in enumerate(st.session_state.approvals_list):
        with st.expander(f"طلب #{req['id']} - {req['title']} ({req['department']}) - الحالة: {req['status']}"):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write(**القسم:**, req['department'])
                st.write(**التاريخ:**, req['date'])
            with c2:
                st.write(**المبلغ المقدر:**, f"{req['amount']} ر.س")
                st.write(**الأولوية:**, req['priority'])
            with c3:
                st.write("**الإجراء التنفيذي:**")
                current_status = req['status']
                
                # أزرار التغيير المباشر للحالة
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("✅ اعتماد", key=f"app_{idx}"):
                        st.session_state.approvals_list[idx]['status'] = 'معتمد'
                        st.rerun()
                with col_b:
                    if st.button("❌ رفض", key=f"rej_{idx}"):
                        st.session_state.approvals_list[idx]['status'] = 'مرفوض'
                        st.rerun()

    st.markdown("---")
    st.markdown("### ➕ إضافة طلب تعميد جديد")
    
    with st.form("new_approval_form"):
        new_title = st.text_input("عنوان الطلب أو المشروع")
        c_dept, c_amt = st.columns(2)
        with c_dept:
            new_dept = st.selectbox("القسم المعني", ["التقنية والتطوير", "التسويق", "الألعاب", "المالية", "الإدارة العليا"])
        with c_amt:
            new_amount = st.number_input("المبلغ المطلوب (ر.س)", min_value=0.0, step=500.0)
        
        new_priority = st.select_slider("درجة الأولوية", options=["منخفضة", "متوسطة", "عالية", "حرجة جداً"])
        
        submitted = st.form_submit_button("إرسال للتعميد والموافقة")
        if submitted and new_title:
            new_id = len(st.session_state.approvals_list) + 1
            st.session_state.approvals_list.append({
                "id": new_id,
                "title": new_title,
                "department": new_dept,
                "amount": new_amount,
                "priority": new_priority,
                "status": "معلق",
                "date": datetime.now().strftime("%Y-%m-%d")
            })
            st.success("تم إضافة طلب التعميد بنجاح وإرساله للمتابعة!")
            st.rerun()

# استدعاء الدالة إذا تم تشغيل الموديول مباشرة
if __name__ == "__main__":
    render_approvals_hub()
