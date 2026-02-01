import gradio as gr
from core.engine import SystemResolutionEngine

# Initialize Engine
engine = SystemResolutionEngine()

def run_optimization(resume_text, job_description):
    # Mocking the data structure that would come from your Ontology
    data = {"experience": resume_text, "skills": ""}
    results = engine.resolve_system_gaps(data, job_description)
    
    return (
        results["resolution_score"], 
        ", ".join(results["critical_gaps"]),
        results["status"]
    )

# Build UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🛠️ R3sum3OS: System Resolution Engine")
    
    with gr.Row():
        with gr.Column():
            res_input = gr.Textbox(label="Current Resume Text", lines=10)
            jd_input = gr.Textbox(label="Target Job Description", lines=10)
            submit = gr.Button("Resolve System Gaps", variant="primary")
            
        with gr.Column():
            score_out = gr.Label(label="Match Resolution")
            status_out = gr.Textbox(label="System Status")
            gap_out = gr.Textbox(label="Identified Missing Ontology Nodes")

    submit.click(
        run_optimization, 
        inputs=[res_input, jd_input], 
        outputs=[score_out, gap_out, status_out]
    )

if __name__ == "__main__":
    demo.launch()
import gradio as gr
from core.visualizer import generate_ontology_graph
from core.engine import SystemResolutionEngine

# Load Engine
engine = SystemResolutionEngine()

def process_and_visualize(resume_text, job_desc):
    # 1. Resolve Gaps (From previous step)
    # Note: In a real app, you'd parse resume_text into a dict first
    mock_data = {
        "identity": {"name": "Candidate"},
        "experience": [{"organization": "TechCorp", "technologies": ["Python", "Gradio", "NLP"]}]
    }
    
    results = engine.resolve_system_gaps(mock_data, job_desc)
    graph_img = generate_ontology_graph(mock_data)
    
    return (
        results["resolution_score"],
        ", ".join(results["critical_gaps"]),
        graph_img
    )

# UI Layout
with gr.Blocks() as demo:
    gr.Markdown("## 🌐 R3sum3OS: Ontology Visualization & Resolution")
    
    with gr.Tab("Resolution Engine"):
        with gr.Row():
            with gr.Column():
                res_in = gr.Textbox(label="Resume Raw Text")
                jd_in = gr.Textbox(label="Job Description")
                btn = gr.Button("Analyze System")
            
            with gr.Column():
                score_out = gr.Label(label="Match Quality")
                gap_out = gr.Textbox(label="Missing Nodes")
    
    with gr.Tab("System Map (Graph)"):
        map_out = gr.Image(label="Ontology Knowledge Graph")

    btn.click(process_and_visualize, inputs=[res_in, jd_in], outputs=[score_out, gap_out, map_out])

demo.launch()
