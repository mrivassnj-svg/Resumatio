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
        import math
from core.parser import normalize_text

class SystemResolutionEngine:
    """
    Calculates the 'Semantic Distance' between the Resume Ontology 
    and the Job Description requirements.
    """
    
    def __init__(self, weights: dict = None):
        # Allow weighting specific categories (e.g., Tech Skills > Education)
        self.weights = weights or {"skills": 0.7, "experience": 0.3}

    def calculate_semantic_distance(self, resume_tokens: list, target_tokens: list) -> float:
        """
        Uses Cosine Similarity logic to find how close two profiles are.
        Distance 0.0 = Perfect Match | Distance 1.0 = No Relation
        """
        res_set = set(resume_tokens)
        tar_set = set(target_tokens)
        
        intersection = res_set.intersection(tar_set)
        if not tar_set: return 1.0
        
        # Simple similarity coefficient
        similarity = len(intersection) / len(tar_set)
        return round(1.0 - similarity, 4)

    def resolve_system_gaps(self, resume_data: dict, job_desc: str):
        """
        The core 'Optimizer' function.
        """
        # 1. Normalize the Job Description
        target_counts = normalize_text(job_desc)
        target_tokens = list(target_counts.keys())
        
        # 2. Extract and Normalize Resume Content
        resume_prose = f"{resume_data.get('skills', '')} {resume_data.get('experience', '')}"
        resume_counts = normalize_text(resume_prose)
        resume_tokens = list(resume_counts.keys())
        
        # 3. Calculate Resolution
        distance = self.calculate_semantic_distance(resume_tokens, target_tokens)
        match_percentage = (1 - distance) * 100
        
        # 4. Identify 'Missing Nodes' (Gaps)
        gaps = [token for token in target_tokens if token not in resume_tokens]
        
        return {
            "resolution_score": f"{match_percentage:.2f}%",
            "semantic_distance": distance,
            "critical_gaps": gaps[:8], # Top 8 missing keywords
            "status": "OPTIMAL" if distance < 0.3 else "UNSTABLE"
        }
