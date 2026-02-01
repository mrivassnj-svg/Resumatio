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
