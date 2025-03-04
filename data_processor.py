# data_processor.py
import pandas as pd
import json

class DataProcessor:
    """
    数据处理器类，用于处理微信导出的CSV文件，清洗数据并生成训练数据。
    """

    def process_csv(self, file_path: str) -> dict:
        """
        处理CSV文件，过滤非文本消息并配对对话。

        参数:
            file_path (str): CSV文件的路径。

        返回:
            dict: 包含处理状态和配对数据的字典。
        """
        # 读取CSV文件并过滤非文本消息
        df = pd.read_csv(file_path)
        df = df[df['message_type'] == 'text']

        # 配对对话
        paired_data = []
        prev_user, prev_message = None, None
        for _, row in df.iterrows():
            if row['sender'] == '用户A' and prev_user == '用户B':
                paired_data.append({'input': prev_message, 'response': row['message']})
            prev_user, prev_message = row['sender'], row['message']

        # 将配对数据保存为JSON文件
        with open('training_data.json', 'w') as f:
            json.dump(paired_data, f)

        return {'status': 'success', 'data': paired_data}