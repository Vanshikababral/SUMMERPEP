# from typing import Dict, TypedDict
# from langgraph.graph import StateGraph

# from IPython.display import display, Image

# #defined a state
# class AgentState(TypedDict):
#     msg : str

# #passed state as the input to the graph
# def greeting_node(state: AgentState) -> AgentState:
#     state['msg'] = "Hello, World" #passing value to the dict 
#     return state

# graph = StateGraph(AgentState)
# graph.add_node("Hello World", greeting_node)
# graph.set_entry_point("Hello World")
# graph.set_finish_point("Hello World")

# app = graph.compile()

# print(Image(app.get_graph().draw_mermaid_png()))


# # Run graph
# result = app.invoke({"msg": "Hello"})

# print(result)

from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    msg: str


def greeting_node(state: AgentState):
    state["msg"] = "Hello, World!"
    return state


graph = StateGraph(AgentState)

graph.add_node("Hello World", greeting_node)

graph.set_entry_point("Hello World")
graph.set_finish_point("Hello World")

app = graph.compile()

result = app.invoke({"msg": "Hello"})

print(result)