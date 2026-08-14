from crewai import Task
from agent import timeline_parser, root_cause_agent, writer_agent

def create_tasks(logs):

    timeline_task = Task(
        description=f"Generate a timeline from:\n{logs}",
        expected_output="Chronological timeline",
        agent=timeline_parser
    )

    root_task = Task(
        description=f"Find the root cause from:\n{logs}",
        expected_output="Root cause analysis",
        agent=root_cause_agent
    )

    report_task = Task(
        description="""
Create a professional postmortem using
the timeline and root cause analysis.
""",
        expected_output="Professional postmortem report",
        agent=writer_agent
    )

    return timeline_task, root_task, report_task