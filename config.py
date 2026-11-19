import os
from dotenv import load_dotenv
load_dotenv()

# 项目根目录
project_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')


#定义配置文件
class Config:
    def __init__(self):
        # 大模型配置
        self.api_key = os.getenv("LLM_API_KEY")
        self.base_url = os.getenv("LLM_BASE_URL")
        self.model_name = os.getenv("LLM_MODEL_NAME", "qwen-plus")

        # 数据库配置
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.database = 'travel_rag'

        # 日志配置
        self.log_file = os.path.join(project_root, 'SmartVoyage', 'logs/app.log')


if __name__ == '__main__':
    print(Config().log_file)
