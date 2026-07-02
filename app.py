import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_text
from ranking import calculate_score

st.set_page_config(
    page_title="AI Candidate Ranking System",
    layout="wide"
)

st.title(
    "🤖 AI Candidate Ranking System"
)

st.markdown(
"""
### Intelligent Resume Screening using AI
Upload resumes and rank candidates automatically.
"""
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

uploaded_files = st.file_uploader(
    "Upload Candidate Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Resumes Uploaded",
            len(uploaded_files)
        )

if st.button(
    "Rank Candidates"
):

    if not job_description:

        st.error(
            "Please enter Job Description"
        )

    elif not uploaded_files:

        st.error(
            "Please upload resumes"
        )

    else:

        results = []

        candidate_details = []

        for file in uploaded_files:

            resume_text = extract_text(
                file
            )

            result = calculate_score(
                job_description,
                resume_text
            )

            results.append({

                "Candidate":
                file.name,

                "Final Score":
                result[
                    "final_score"
                ],

                "Semantic Score":
                result[
                    "semantic_score"
                ],

                "Skill Match %":
                result[
                    "skill_score"
                ],

                "Experience":
                result[
                    "experience"
                ],

                "Recommendation":
                result[
                    "recommendation"
                ]
            })

            candidate_details.append({

                "Candidate":
                file.name,

                "Matched Skills":
                result[
                    "matched_skills"
                ],

                "Missing Skills":
                result[
                    "missing_skills"
                ],

                "Recommendation":
                result[
                    "recommendation"
                ],

                "Experience":
                result[
                    "experience"
                ],

                "Final Score":
                result[
                    "final_score"
                ]
            })

        df = pd.DataFrame(
            results
        )

        df = df.sort_values(
            by="Final Score",
            ascending=False
        )

        df.insert(
            0,
            "Rank",
            range(
                1,
                len(df)+1
            )
        )

        st.success(
            "Ranking Complete!"
        )

        st.subheader(
            "Candidate Rankings"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # Bar Chart

        st.subheader(
            "Ranking Visualization"
        )

        fig = px.bar(
            df,
            x="Candidate",
            y="Final Score",
            title="Candidate Scores"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Best Candidate

        top = df.iloc[0]

        st.subheader(
            "🏆 Best Candidate"
        )

        st.info(
            f"""
Rank #1 : {top['Candidate']}

Final Score : {top['Final Score']}

Experience : {top['Experience']} Years

Recommendation : {top['Recommendation']}
"""
        )

        # Detailed Analysis

        st.subheader(
            "Candidate Analysis"
        )

        for candidate in candidate_details:

            with st.expander(
                candidate["Candidate"]
            ):

                st.write(
                    "Final Score:",
                    candidate[
                        "Final Score"
                    ]
                )

                st.write(
                    "Experience:",
                    candidate[
                        "Experience"
                    ],
                    "Years"
                )

                st.write(
                    "Recommendation:",
                    candidate[
                        "Recommendation"
                    ]
                )

                st.write(
                    "Matched Skills:"
                )

                st.success(
                    ", ".join(
                        candidate[
                            "Matched Skills"
                        ]
                    )
                )

                st.write(
                    "Missing Skills:"
                )

                st.error(
                    ", ".join(
                        candidate[
                            "Missing Skills"
                        ]
                    )
                )

        # Save CSV

        df.to_csv(
            "outputs/ranked_candidates.csv",
            index=False
        )

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            "Download Ranked CSV",
            csv,
            "ranked_candidates.csv",
            "text/csv"
        )