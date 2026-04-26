# AI-Powered Talent Scouting & Engagement Agent
Submission for Deccan AI Catalyst Hackathon

📌 Project Overview
The traditional recruitment lifecycle is manually intensive, biased, and struggles to effectively gauge passive candidate intent. This project introduces an autonomous AI agent designed to revolutionize the sourcing pipeline.

The system ingests an unstructured Job Description (JD), discovers matching candidates from a database, and engages them in a simulated multi-turn conversation. It outputs a highly actionable, ranked shortlist scored on two critical dimensions: Match Score and Interest Score, complete with Explainable AI (XAI) reasoning for transparent decision-making. This directly aligns with the evaluation criteria for Ease of Use, Transparency, and Explainability.

🏗️ Architecture & Agentic Flow
The application utilizes a sequential multi-agent orchestration architecture to handle the end-to-end workflow:

JD Parsing Agent: Ingests raw JD text and deconstructs it into a structured schema of weighted technical requirements.

Candidate Discovery & Matching Agent: Evaluates candidate profiles against the weighted JD schema. It calculates the Match Score by checking for semantic skill overlap and exact keyword relevance, ignoring demographic data to mitigate bias.

Conversational Engagement Agent: Initiates a simulated, personalized multi-turn chat with candidates who pass the baseline Match Score threshold. It evaluates responses dynamically to calculate the Interest Score.

Master Orchestrator: Synthesizes the data, ranks the candidates by their combined aggregate scores, and generates the final JSON output.

🧮 Proprietary Scoring Logic
Match Score (0.0 - 5.0): Calculated using a hybrid model. It assigns dynamic weights to each job requirement (e.g., Python = 0.40, Cloud = 0.15). The system evaluates the candidate's skills and raw resume text against these weighted requirements to generate a normalized score. Candidates must score at least 3.5 to proceed to outreach.

Interest Score (0.0 - 5.0): Calculated during the simulated conversational phase. The agent evaluates the candidate's explicit confirmation of logistical constraints (salary expectations, hybrid work alignment) and implicit enthusiasm signals derived from the text to generate the final intent score.

🚀 Local Setup Instructions (macOS)
This prototype is built using lightweight Python for maximum reliability and ease of demonstration, ensuring high technical sophistication and quality of implementation.

Navigate to the project directory:

Bash
cd /Users/shaan/catalyst_project
Create and activate the virtual environment:

Bash
python3 -m venv venv
source venv/bin/activate
Install the required dependency:

Bash
pip install pydantic
Execute the talent scouting agent:

Bash
/Users/shaan/catalyst_project/venv/bin/python main.py
(Alternatively, just run python3 main.py while the virtual environment is active).

📊 Sample Output
The agent provides terminal-based progress tracking and outputs a final ranked JSON shortlist:

JSON
. Gaps in. Highly enthusiastic. Excellent communication and confirmed budget."
  },
  {
    "Candidate": "Priya Patel",
    "Match Score": 4.0,
    "Interest Score": 4.5,
    "Explainability": "Match in ['Python', 'Machine Learning']. Gaps in. Strong interest. Pragmatic communication and aligned on salary."
  }
]
