from app.llm import call_llm

def run_analysis_agent(task, df):
    prompt = f"""
数据:
{df.head().to_string()}

任务:
{task}

输出分析结论:
"""
    return call_llm(prompt)
