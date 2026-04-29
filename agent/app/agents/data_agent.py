from app.llm import call_llm
from app.tools.python_executor import execute_python

def run_data_agent(task, df):
    prompt = f"""
写pandas代码完成任务:
{task}

输入变量: df
输出变量: result
"""
    code = call_llm(prompt)
    return execute_python(code, df)
