from langgraph.graph import StateGraph
from typing import TypedDict, List, Dict
import time

# Define a simple state
class ConversationState(TypedDict):
    messages: List[Dict]
    current_step: str
    thought_process: List[str]

# Define simple nodes that clearly show what's happening
def greet(state: ConversationState) -> ConversationState:
    """First node: Greet the user"""
    print("\n🟢 ENTERING NODE: greet")
    print("🔄 Processing state...")
    time.sleep(1)  # Slow down to see the flow
    
    state["thought_process"].append("I should greet the user first")
    state["current_step"] = "greeting"
    
    print("✅ Node complete! Updated state:")
    print(f"  - Current step: {state['current_step']}")
    print(f"  - Thought: {state['thought_process'][-1]}")
    return state

def ask_question(state: ConversationState) -> ConversationState:
    """Second node: Ask a question"""
    print("\n🟢 ENTERING NODE: ask_question")
    print("🔄 Processing state...")
    time.sleep(1)  # Slow down to see the flow
    
    state["thought_process"].append("Now I should ask what they need help with")
    state["current_step"] = "questioning"
    
    print("✅ Node complete! Updated state:")
    print(f"  - Current step: {state['current_step']}")
    print(f"  - Thought: {state['thought_process'][-1]}")
    return state

def provide_help(state: ConversationState) -> ConversationState:
    """Third node: Provide help"""
    print("\n🟢 ENTERING NODE: provide_help")
    print("🔄 Processing state...")
    time.sleep(1)  # Slow down to see the flow
    
    state["thought_process"].append("I'll provide some helpful information")
    state["current_step"] = "helping"
    
    print("✅ Node complete! Updated state:")
    print(f"  - Current step: {state['current_step']}")
    print(f"  - Thought: {state['thought_process'][-1]}")
    return state

def summarize(state: ConversationState) -> ConversationState:
    """Final node: Summarize the conversation"""
    print("\n🟢 ENTERING NODE: summarize")
    print("🔄 Processing state...")
    time.sleep(1)  # Slow down to see the flow
    
    state["thought_process"].append("I'll summarize what we discussed")
    state["current_step"] = "summarizing"
    
    print("✅ Node complete! Updated state:")
    print(f"  - Current step: {state['current_step']}")
    print(f"  - Thought: {state['thought_process'][-1]}")
    return state

def run_demo():
    """Run the LanGraph demo with visual feedback"""
    print("\n===== SIMPLE LANGGRAPH DEMO =====")
    print("This demo shows how a graph processes state through nodes and edges")
    
    # Create the graph
    print("\n📊 Creating graph...")
    workflow = StateGraph(ConversationState)
    
    # Add nodes
    print("📍 Adding nodes: greet, ask_question, provide_help, summarize")
    workflow.add_node("greet", greet)
    workflow.add_node("ask_question", ask_question)
    workflow.add_node("provide_help", provide_help)
    workflow.add_node("summarize", summarize)
    
    # Add edges
    print("➡️ Adding edges between nodes")
    workflow.add_edge("greet", "ask_question")
    workflow.add_edge("ask_question", "provide_help")
    workflow.add_edge("provide_help", "summarize")
    
    # Set entry point
    print("🚪 Setting entry point: greet")
    workflow.set_entry_point("greet")
    
    # Compile the graph
    print("🔧 Compiling graph...")
    app = workflow.compile()
    
    # Initialize state
    print("\n🏁 Initializing state...")
    state = {
        "messages": [],
        "current_step": "",
        "thought_process": []
    }
    
    # Run the graph
    print("\n▶️ Running graph...")
    print("=================================")
    result = app.invoke(state)
    
    # Show final state
    print("\n=================================")
    print("✨ FINAL STATE:")
    print(f"Current step: {result['current_step']}")
    print("\nThought process:")
    for i, thought in enumerate(result["thought_process"], 1):
        print(f"  {i}. {thought}")
    print("\n=================================")
    print("Demo complete! This shows how LanGraph:")
    print("1. Processes state through a series of nodes")
    print("2. Follows edges to determine the flow")
    print("3. Updates and maintains state throughout the process")
    print("4. Produces a final result after traversing the graph")

if __name__ == "__main__":
    run_demo() 