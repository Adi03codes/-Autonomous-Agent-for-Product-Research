# agent.py
from langchain.agents import initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

def run_agent():
    tools = load_tools(["serpapi", "llm-math"])
    llm = ChatOpenAI(temperature=0)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
    result = agent.run("Research top 3 laptops under $1000 and compare specs.")
    print(result)

if __name__ == '__main__':
    run_agent()