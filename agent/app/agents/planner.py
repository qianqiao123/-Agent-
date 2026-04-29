import json
from app.llm import call_llm

def plan_tasks(query):
    prompt = f"""
拆解数据分析任务，返回JSON数组：
用户需求: {query}

格式：
[
  {{"task":"xxx","agent":"data"}},
  {{"task":"xxx","agent":"analysis"}},
  {{"task":"xxx","agent":"viz"}},
  {{"task":"xxx","agent":"report"}}
]
"""
    result = call_llm(prompt)

    try:
        return json.loads(result)
    except:
        return [
            {"task": "清洗数据", "agent": "data"},
            {"task": "分析数据", "agent": "analysis"},
            {"task": "可视化", "agent": "viz"},
            {"task": "生成报告", "agent": "report"},
        ]
