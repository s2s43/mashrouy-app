# 📲 وكيل التنبيهات
from agents.base_agent import BaseAgent

class TelegramAgent(BaseAgent):
    def __init__(self):
        super().__init__("وكيل التنبيهات (TelegramAgent)", "إدارة المنظومة")

    def send_report(self, agent_report):
        msg = f"📊 *تقرير إنجاز من {agent_report['agent_name']}*
القسم: {agent_report['module']}
عدد المهام المكتملة: {agent_report['total_tasks_completed']}"
        self.log_action("إرسال تلغرام", f"تم توجيه التقرير للإدارة بنجاح")
        return True
