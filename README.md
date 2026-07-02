🤖 AI Candidate Ranking System

An AI-powered Resume Screening and Candidate Ranking application that automates the hiring process by analyzing resumes against a given Job Description (JD).
The system uses Natural Language Processing (NLP), Semantic Similarity, Skill Matching, and Experience Analysis to rank candidates and provide hiring recommendations.


🚀 Features

* Upload multiple candidate resumes (PDF format)
* Parse resume content automatically
* Extract and compare skills with Job Description
* Calculate semantic similarity using Sentence Transformers
* Analyze candidate experience
* Generate candidate rankings
* Provide hiring recommendations
* Interactive Streamlit dashboard
* Download ranked candidate results as CSV


🛠️ Technologies Used

* Python
* Streamlit
* Sentence Transformers
* Scikit-learn
* PyMuPDF
* Pandas
* Plotly
* NLP & Machine Learning


📂 Project Structure

```bash
AI-Candidate-Ranking-System/
│
├── app.py                 # Streamlit Application
├── ranking.py             # Candidate Scoring Logic
├── resume_parser.py       # Resume Text Extraction
├── resume_ranking.py      # Semantic Similarity Module
├── skills.py              # Skill Extraction Module
├── requirements.txt       # Dependencies
├── outputs/
│   └── ranked_candidates.csv
└── README.md
```


⚙️ How It Works

Step 1: Enter Job Description
Paste the desired job description into the application.

Step 2: Upload Resumes
Upload one or more candidate resumes in PDF format.

Step 3: AI Analysis
The system performs:
* Resume Text Extraction
* Skill Matching
* Semantic Similarity Analysis
* Experience Detection

Step 4: Candidate Ranking
Each candidate receives:
* Semantic Score
* Skill Match Percentage
* Experience Score
* Final Ranking Score
* Hiring Recommendation


📊 Scoring Methodology

The final candidate score is calculated using:

```text
Final Score =
(40% Semantic Similarity)
+ (40% Skill Match)
+ (20% Experience Score)
```

Recommendation Criteria

| Score Range | Recommendation  |
| ----------- | --------------- |
| ≥ 50        | Strong Hire     |
| 30 – 49     | Consider        |
| < 30        | Not Recommended |


🧠 AI Models Used

Sentence Transformer

Model:

```python
all-MiniLM-L6-v2
```

Used for semantic similarity comparison between:

* Job Description
* Resume Content


🔧 Installation

Clone Repository

```bash
git clone https://github.com/your-username/AI-Candidate-Ranking-System.git
cd AI-Candidate-Ranking-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```


▶️ Run Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.


📈 Output

The system generates:
* Ranked Candidate Table
* Candidate Score Visualization
* Best Candidate Recommendation
* Detailed Skill Analysis
* Downloadable CSV Report


🎯 Use Cases

* HR Recruitment
* Resume Screening
* Talent Acquisition
* Internship Hiring
* Campus Placements
* Technical Recruitment


🔮 Future Enhancements

* OCR Support for Scanned Resumes
* Resume Summarization using LLMs
* Candidate Chatbot Evaluation
* ATS Compatibility Scoring
* Real-Time Recruitment Dashboard
* Advanced Skill Gap Analysis


⭐ Support

If you found this project useful, please give it a ⭐ on GitHub and share it with others.


