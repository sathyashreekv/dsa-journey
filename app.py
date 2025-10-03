import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("DFS Visualization with Stack")

# -----------------------
# Input Graph
# -----------------------
graph_input = st.text_area(
    "Enter the graph in adjacency list format (e.g., A:B,C;B:D,E;C:F):",
    "A:B,C\nB:D,E\nC:F\nD:\nE:F\nF:",
    key="graph_input"
)

graph = {}
for line in graph_input.splitlines():
    if line.strip():
        node, neighbors = line.split(":")
        graph[node.strip()] = set(
            neighbor.strip() for neighbor in neighbors.split(",") if neighbor.strip()
        )

start_node = st.text_input("Enter the start node:", "A", key="start_node")

# -----------------------
# DFS with trace recording
# -----------------------
def dfs_with_trace(graph, start):
    visited = set()
    stack = [start]
    steps = []
    traversed_edges = []  # to record actual DFS path edges

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            steps.append((node, list(stack)))

            for neighbor in reversed(list(graph[node])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    traversed_edges.append((node, neighbor))

    return steps, traversed_edges

# -----------------------
# Run DFS
# -----------------------
if st.button("Run DFS"):
    steps, traversed_edges = dfs_with_trace(graph, start_node)

    st.subheader("DFS Order")
    order = [s[0] for s in steps]
    st.write(" → ".join(order))

    st.subheader("Step-by-Step Visualization")

    # Slider for interactive exploration
    step_idx = st.slider("Select Step", 1, len(steps), 1)
    node, stack_state = steps[step_idx - 1]

    st.write(f"Step {step_idx}: Popped `{node}`, Stack: {stack_state}")

    # -----------------------
    # Graph Visualization
    # -----------------------
    G = nx.DiGraph()
    for n, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(n, neighbor)

    pos = nx.spring_layout(G, seed=42)  # fix layout

    # Color nodes: current = green, visited = blue, unvisited = gray
    node_colors = [
        "lightgreen" if n == node else
        "lightblue" if n in order[:step_idx] else
        "lightgray"
        for n in G.nodes()
    ]

    # Highlight traversed edges step by step
    edge_colors = [
        "green" if (u, v) in traversed_edges[:step_idx-1] else "gray"
        for u, v in G.edges()
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=800, font_size=16,
        font_weight="bold", arrows=True, ax=ax
    )
    ax.set_title(f"DFS Step {step_idx}: Popped {node}")
    st.pyplot(fig)
