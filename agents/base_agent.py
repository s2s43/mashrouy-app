# 🧠 القاعدة الأساسية للوكيل الذكي
from datetime import datetime

class BaseAgent:
    def __init__(self, name, module_name):
        self.name = name
        self.module_name = module_name
        self.logs = []
        self.tasks = []

    def log_action(self, action, details):
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.logs.append(log_entry)
        print(f"[{self.name}] 📝 {action}: {details}")

    def generate_report(self):
        return {
            "agent_name": self.name,
            "module": self.module_name,
            "total_tasks_completed": len(self.logs),
            "recent_activity": self.logs[-5:] if self.logs else []
        }
