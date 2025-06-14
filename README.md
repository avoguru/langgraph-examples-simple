# Simple LangGraph Example

A minimal, visual example demonstrating the core concepts of LangGraph: nodes and edges. Visit [lastmileagents.com](https://lastmileagents.com) to visualize and learn how it works.

## What is LangGraph?

LangGraph is a framework for building stateful, multi-step applications with language models. It enables you to create intelligent agents that can:
- Break down complex tasks into manageable steps
- Maintain context and state throughout a conversation
- Make decisions based on accumulated information
- Follow structured workflows while remaining flexible

By connecting nodes (processing units) with edges (connections), LangGraph allows you to build sophisticated agent workflows that can handle complex tasks while maintaining a clear, traceable execution path.

## Core Concepts

### 1. State
The state is the central data structure that flows through the graph. Think of it as a container that holds all the information needed by your application.

```python
class ConversationState(TypedDict):
    messages: List[Dict]
    current_step: str
    thought_process: List[str]
```

**Key Points about State:**
- State is immutable within each node
- State flows through the graph, accumulating information
- State provides context for each node's processing
- State can be used to track progress and maintain context

### 2. Nodes
Nodes are the processing units of the graph. Each node is a function that:
- Takes the current state as input
- Processes the state
- Returns the updated state

```python
def greet(state: ConversationState) -> ConversationState:
    state["thought_process"].append("I should greet the user first")
    state["current_step"] = "greeting"
    return state
```

**Key Points about Nodes:**
- Nodes are pure functions (same input always produces same output)
- Nodes can only access the state passed to them
- Nodes can't communicate directly with other nodes
- Nodes can't modify state outside their scope

### 3. Edges
Edges define the possible transitions between nodes. They create the structure of your graph.

```python
workflow.add_edge("greet", "ask_question")
```

**Key Points about Edges:**
- Edges define the flow of execution
- Edges are one-way connections
- Edges determine the sequence of node execution
- Edges can be conditional (though not in this simple example)

## Example Flow

In this simple example, we have a linear flow:

```
[State] → [greet] → [State] → [ask_question] → [State] → [provide_help] → [State] → [summarize] → [Final State]
```

Each node:
1. Receives the current state
2. Processes it
3. Returns an updated state
4. The next node in the sequence receives the updated state

## Limitations

### 1. Linear Flow
This example demonstrates a simple linear flow. It cannot:
- Make decisions based on state
- Branch into different paths
- Handle complex workflows
- Process multiple paths simultaneously

### 2. State Management
- State must be serializable
- Large state objects can impact performance
- State updates must be explicit
- No shared state between nodes

### 3. Node Design
- Nodes can't maintain internal state
- Nodes can't communicate directly
- Nodes must be pure functions
- No async operations

## When to Use This Pattern

This simple linear pattern is best for:
- Straightforward, sequential processes
- Clear, predictable workflows
- Simple state transformations
- Learning and understanding LangGraph basics

## How to Run

1. Create a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the example:
```bash
python simple_langgraph_demo.py
```

## What You'll See

The example provides visual feedback about:
- Graph creation and compilation
- State initialization
- Node execution with visual indicators
- State updates at each step
- Final state after graph execution

## Understanding the Output

The output shows:
1. Graph setup process
2. Initial state creation
3. Node execution sequence
4. State updates at each step
5. Final state summary

Each node execution shows:
- When the node starts
- What state changes it makes
- When the node completes

## Next Steps

After understanding this simple example, you might want to explore:
1. Conditional branching
2. Complex state management
3. Error handling
4. Async operations
5. More complex workflows

## Contributing

Feel free to:
- Add more examples
- Improve documentation
- Add visualization features
- Report issues
- Suggest improvements

## License

This project is licensed under the MIT License. 