import re

SKILLS_LIST = [
    "python", "java", "c++", "javascript", "react", "node.js",
    "machine learning", "deep learning", "nlp", "opencv",
    "pandas", "numpy", "scikit-learn", "flask", "django",
    "sql", "mysql", "mongodb", "firebase", "git", "docker",
    "html", "css", "tensorflow", "pytorch", "langchain"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)    
    text = re.sub(r'[^\w\s]', ' ', text)   
    return text.strip()

def extract_skills(text):
    text = clean_text(text)
    found = []
    for skill in SKILLS_LIST:
        # match whole word only to avoid java matching inside javascript
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)
    return found

