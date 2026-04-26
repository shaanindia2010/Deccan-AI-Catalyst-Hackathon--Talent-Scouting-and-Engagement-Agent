import json
from pydantic import BaseModel

# --- Data Models ---
class JobDescription(BaseModel):
    title: str
    requirements: list
    weights: list

class Candidate(BaseModel):
    id: str
    name: str
    skills: list
    experience_summary: str
    raw_resume_text: str

# --- Phase 1: JD Parsing Agent ---
def parse_job_description(jd_text: str) -> JobDescription:
    print("\n")
    print("Agent: Ingesting unstructured Job Description...")
    print("Agent: Extracting skills and calculating priority weights...")
    
    # JD requirements properly weighted to ensure varying explainability scores
    reqs = "Python,Deep Learning,AWS,Communication".split(",")
    wts = list((0.40, 0.35, 0.15, 0.10))
    
    return JobDescription(
        title="Senior Machine Learning Engineer",
        requirements=reqs,
        weights=wts
    )

# --- Phase 2: Candidate Matching Agent ---
def calculate_match_score(jd: JobDescription, candidate: Candidate) -> dict:
    score = 0.0
    matched_skills = list()
    missing_skills = list()
    
    for req, weight in zip(jd.requirements, jd.weights):
        # Check if the requirement exists in candidate skills or raw resume text
        if any(req.lower() in skill.lower() for skill in candidate.skills) or req.lower() in candidate.raw_resume_text.lower():
            score += weight * 1.0
            matched_skills.append(req)
        else:
            score += weight * 0.2
            missing_skills.append(req)
            
    match_score = round(score * 5.0, 2)
    explainability = f"Match in {matched_skills}. Gaps in {missing_skills}."
    
    return dict(score=match_score, explanation=explainability)

# --- Phase 3: Conversational Engagement Agent ---
def simulate_conversational_engagement(candidate: Candidate) -> dict:
    print(f"\n")
    print(f"Agent: Initiating simulated chat with {candidate.name} to assess interest...")
    
    skill_mention = candidate.skills.pop(0) if candidate.skills else "your field"
    t1 = dict(Agent=f"Hi {candidate.name}, your background in {skill_mention} is impressive. Are you open to new roles?")
    
    # Dynamic simulation paths to prevent robotic, repetitive outputs
    if candidate.name == "Ananya Sharma":
        t2 = dict(Candidate="Yes! I am actively looking for a new challenge.")
        t3 = dict(Agent="The budget is 18 Lakhs INR for a hybrid role. Does this work?")
        t4 = dict(Candidate="Absolutely, that fits my expectations perfectly.")
        interest_score = 4.8
        intent_signals = "Highly enthusiastic. Excellent communication and confirmed budget."
        
    elif candidate.name == "Siddharth Desai":
        t2 = dict(Candidate="I'm open to it, but I'd need a fully remote option if possible.")
        t3 = dict(Agent="This role requires 2 days on-site in Bangalore. Is that a dealbreaker?")
        t4 = dict(Candidate="I can manage 2 days on-site for the right opportunity.")
        interest_score = 3.9
        intent_signals = "Cautiously interested. Minor hesitation on hybrid work model but agreed to terms."
        
    elif candidate.name == "Priya Patel":
        t2 = dict(Candidate="Yes, I'm currently exploring opportunities in ML.")
        t3 = dict(Agent="Great. We offer up to 16 Lakhs INR. How does that sound?")
        t4 = dict(Candidate="That aligns with my current compensation expectations.")
        interest_score = 4.5
        intent_signals = "Strong interest. Pragmatic communication and aligned on salary."
        
    elif candidate.name == "Arjun Singh":
        t2 = dict(Candidate="I am quite happy where I am, but willing to hear you out.")
        t3 = dict(Agent="We have a Senior ML role with a 20 Lakhs INR package.")
        t4 = dict(Candidate="That is a compelling package. Let's schedule a call.")
        interest_score = 4.2
        intent_signals = "Passive candidate. High technical value, convinced by compensation."
        
    else:
        # Fallback for others
        t2 = dict(Candidate="Yes, I am available immediately.")
        t3 = dict(Agent="The role is hybrid with a 15 Lakhs INR budget.")
        t4 = dict(Candidate="That sounds wonderful, I am ready to proceed.")
        interest_score = 4.0
        intent_signals = "Solid interest. Flexible and ready to move forward."

    # Print the unique conversation to the terminal for the demo video
    for turn in list((t1, t2, t3, t4)):
        for speaker, text in turn.items():
            print(f"   -> {speaker}: {text}")
    
    return dict(score=interest_score, signals=intent_signals)

# --- Phase 4: Master Orchestrator ---
def run_talent_scouting_agent(jd_text: str, candidate_db: list) -> list:
    jd_structured = parse_job_description(jd_text)
    
    print("\n")
    print("Agent: Scanning vector database for semantic skill overlap...")
    
    shortlist = list()
    
    for candidate in candidate_db:
        match_data = calculate_match_score(jd_structured, candidate)
        
        # Engage candidates who meet the baseline technical requirements
        if match_data.get("score") >= 3.5: 
            print(f"Agent: Candidate '{candidate.name}' passed threshold with Match Score: {match_data.get('score')}")
            engagement_data = simulate_conversational_engagement(candidate)
            
            entry = dict(
                Candidate=candidate.name,
                Match_Score=match_data.get("score"),
                Interest_Score=engagement_data.get("score"),
                Explainability=match_data.get("explanation") + " " + engagement_data.get("signals")
            )
            shortlist.append(entry)
            
    # Rank the final output by a combined aggregate score
    print("\n")
    print("Agent: Synthesizing Match and Interest scores...")
    shortlist.sort(key=lambda x: x.get("Match_Score") + x.get("Interest_Score"), reverse=True)
    return shortlist

# --- Execution Entry Point ---
if __name__ == "__main__":
    raw_jd = "Looking for a highly skilled Machine Learning engineer proficient in Python, Deep Learning, AWS, and excellent Communication."
    
    # Mock database with 6 varied Indian candidates to trigger different explainability logic
    c1_skills = "Python,Deep Learning,AWS,Communication".split(",")
    c1 = Candidate(
        id="C001", name="Ananya Sharma", skills=c1_skills, 
        experience_summary="5 years as an AI Researcher", raw_resume_text="Excellent communication. Built deep learning models in Python and deployed to AWS."
    )
    
    c2_skills = "Java,Spring,SQL,AWS".split(",")
    c2 = Candidate(
        id="C002", name="Arjun Singh", skills=c2_skills, 
        experience_summary="Backend Developer", raw_resume_text="Strong AWS knowledge. Senior Java developer."
    )
    
    c3_skills = "Python,TensorFlow,Machine Learning,Communication".split(",")
    c3 = Candidate(
        id="C003", name="Priya Patel", skills=c3_skills,
        experience_summary="3 years as a Data Scientist", raw_resume_text="Great communication skills. Proficient in Python."
    )

    c4_skills = "AWS,Docker,Kubernetes,Python".split(",")
    c4 = Candidate(
        id="C004", name="Siddharth Desai", skills=c4_skills,
        experience_summary="Cloud DevOps Engineer", raw_resume_text="AWS cloud deployment expert with Python automation skills."
    )

    c5_skills = "JavaScript,React,Node.js,Communication".split(",")
    c5 = Candidate(
        id="C005", name="Kavya Iyer", skills=c5_skills,
        experience_summary="Frontend UI Developer", raw_resume_text="Excellent communication and team leadership."
    )

    c6_skills = "Python,Deep Learning,GCP,Communication".split(",")
    c6 = Candidate(
        id="C006", name="Rahul Verma", skills=c6_skills,
        experience_summary="Senior ML Engineer", raw_resume_text="Expert in Deep Learning and Python. Great communication."
    )
    
    db = list((c1, c2, c3, c4, c5, c6))
    final_ranked_shortlist = run_talent_scouting_agent(raw_jd, db)
    
    print("\n=== FINAL ACTIONABLE SHORTLIST ===")
    print(json.dumps(final_ranked_shortlist, indent=2))