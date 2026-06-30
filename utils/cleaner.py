import re

SKILLS_LIST = [
    "python", "java", "c++", "javascript", "react", "node.js",
    "machine learning", "deep learning", "nlp", "opencv",
    "pandas", "numpy", "scikit-learn", "flask", "django",
    "sql", "mysql", "mongodb", "firebase", "git", "docker",
    "html", "css", "tensorflow", "pytorch", "langchain"
]

def clean_text(text):
    text = text.loweer()
    text = re.sub(r'\s+', ' ', text)    
    text = re.sub(r'[^\w\s]', ' ', text)   
    return text.strip()

def extract_skills(text):
    text = clean_text(text)
    found = [skill for skill in SKILLS_LIST if skill in text]
    return found 

 