from core.parser import normalize_text
from core.ontology_schema import EntityType

class ResolutionEngine:
    def __init__(self, ontology_data):
        self.kb = ontology_data  # Knowledge Base

    def resolve_gaps(self, resume_data: dict, job_description: str):
        """Identifies missing semantic nodes required for the target role."""
        jd_tokens = normalize_text(job_description)
        resume_tokens = normalize_text(str(resume_data))
        
        missing = [term for term in jd_tokens if term not in resume_tokens]
        score = len(set(resume_tokens) & set(jd_tokens)) / len(set(jd_tokens))
        
        return {
            "match_score": round(score * 100, 2),
            "optimization_suggestions": missing[:10]
        }
