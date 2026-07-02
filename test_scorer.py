from utils.scorer import screen_resumes

job_description = """
We are looking for a java developer with experience in
spring boot, MySQL, and web development. Knowledge of
React, scikit-learn, and Git is a plus.
"""

results = screen_resumes(job_description, ["sampl resume.pdf"])

for r in results:
    print(f"\nResume: {r['name']}")
    print(f"Match Score: {r['score']}%")
    print(f"Matched Skills: {r['matched_skills']}")

