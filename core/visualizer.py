import networkx as nx
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_ontology_graph(resume_data: dict):
    """
    Creates a visual Knowledge Graph of the resume ontology.
    """
    G = nx.Graph()
    
    # Root Node: The Identity
    owner = resume_data.get("identity", {}).get("name", "User")
    G.add_node(owner, type="Identity", color="#3b82f6") # Blue
    
    # Experience Nodes
    for exp in resume_data.get("experience", []):
        job_id = exp.get("organization", "Company")
        G.add_node(job_id, type="Experience", color="#10b981") # Green
        G.add_edge(owner, job_id, label="worked_at")
        
        # Link Technologies/Skills to Jobs
        for tech in exp.get("technologies", []):
            G.add_node(tech, type="Skill", color="#f59e0b") # Orange
            G.add_edge(job_id, tech, label="utilized")

    # Rendering the Graph to a PIL Image
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    colors = [node[1]['color'] for node in G.nodes(data=True)]
    
    nx.draw(G, pos, with_labels=True, node_color=colors, 
            node_size=2000, font_size=10, font_weight="bold")
    
    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return Image.open(buf)
