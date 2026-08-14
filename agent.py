from crewai import Agent

timeline_parser = Agent(
    role="Timeline Parser",
    goal="Create a chronological timeline from incident logs.",
    backstory="Expert in analyzing system logs."
)

root_cause_agent = Agent(
    role="Root Cause Investigator",
    goal="Find the root cause and impact.",
    backstory="Experienced Site Reliability Engineer."
)

writer_agent = Agent(
    role="Postmortem Writer",
    goal="Write a professional incident postmortem.",
    backstory="Technical documentation specialist."
)