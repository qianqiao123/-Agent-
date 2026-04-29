from app.llm import call_llm
from app.tools.python_executor import execute_python

def run_viz_agent(task, df):
    prompt = f"""
生成 matplotlib 代码完成:
{task}

保存为 output.png
"""
    code = call_llm(prompt)
    return execute_python(code, df)
