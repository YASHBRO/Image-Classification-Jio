import pydot


# Define a method to create ER Diagram (example based on your project workflow)
def create_er_diagram():
    # Create a graph using pydot
    graph = pydot.Dot(graph_type="digraph", comment="MRG_LLM_Project_Workflow")

    # Define the nodes representing various components
    graph.add_node(pydot.Node("A", label="MIMIC-IV Dataset"))
    graph.add_node(pydot.Node("B", label="WFDB Signals (via wfdb)"))
    graph.add_node(pydot.Node("C", label="ECG Leads Plotting (via ecg_plot)"))
    graph.add_node(pydot.Node("D", label="Triplet Generation (via Pillow)"))
    graph.add_node(pydot.Node("E", label="Token Counting (via tiktoken)"))
    graph.add_node(pydot.Node("F", label="GPT-4 Output Generation"))
    graph.add_node(pydot.Node("G", label="Diagnostic Output in JSON"))

    # Define edges to represent the flow between the components
    graph.add_edge(pydot.Edge("A", "B"))
    graph.add_edge(pydot.Edge("B", "C"))
    graph.add_edge(pydot.Edge("C", "D"))
    graph.add_edge(pydot.Edge("D", "E"))
    graph.add_edge(pydot.Edge("E", "F"))
    graph.add_edge(pydot.Edge("F", "G"))

    # Output the graph as a PNG file
    graph.write_png("mrg_llm_project_workflow.png")
    print("ER Diagram saved as 'mrg_llm_project_workflow.png'")


# Create and display the diagram
create_er_diagram()
