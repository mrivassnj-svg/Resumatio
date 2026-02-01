import gradio as gr
from core.engine import ResolutionEngine

def build_ui(engine_instance):
    with gr.Blocks(title="R3sum3OS Resolution Engine") as demo:
        gr.Markdown("# 🚀 Ontology-Driven Resume Optimizer")
        
        with gr.Row():
            with gr.Column():
                resume_input = gr.File(label="Upload Resume (PDF/DOCX)")
                jd_input = gr.Textbox(label="Target Job Description", lines=5)
                btn = gr.Button("Analyze & Optimize")
            
            with gr.Column():
                score_output = gr.Label(label="System Resolution Score")
                suggestions = gr.HighlightedText(label="Missing Ontology Nodes")
        
        btn.click(
            fn=engine_instance.resolve_gaps,
            inputs=[resume_input, jd_input],
            outputs=[score_output, suggestions]
        )
    return demo
