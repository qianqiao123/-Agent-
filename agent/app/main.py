import pandas as pd

from app.agents.planner import plan_tasks
from app.agents.data_agent import run_data_agent
from app.agents.analysis_agent import run_analysis_agent
from app.agents.viz_agent import run_viz_agent
from app.agents.report_agent import generate_report


def run_pipeline(query, file_path):
    df = pd.read_csv(file_path)

    tasks = plan_tasks(query)
    context = []

    for t in tasks:
        agent = t["agent"]
        task = t["task"]

        if agent == "data":
            df = run_data_agent(task, df)

        elif agent == "analysis":
            result = run_analysis_agent(task, df)
            context.append(result)

        elif agent == "viz":
            run_viz_agent(task, df)

        elif agent == "report":
            return generate_report(context)

    return "DONE"
