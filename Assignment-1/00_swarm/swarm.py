class Agent:
    def __init__(self, name):
        self.name = name

    def do_task(self, task):
        print(f"{self.name} is doing: {task}")

# List of agents with different tasks
agents = [
    ("Agent A", "analyze data"),
    ("Agent B", "collect user feedback"),
    ("Agent C", "generate report")
]

# Assign each agent their task
for name, task in agents:
    agent = Agent(name)
    agent.do_task(task)
