from app.llm import call_llm

def generate_report(context):
    prompt = f"""
根据分析结果生成报告:

{context}

要求:
- 结论明确
- 有建议
"""
    return call_llm(prompt)
