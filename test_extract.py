from utils.extractor import extract_text
from utils.cleaner import extract_skills


text = extract_text("readOnly.pdf")
skills = extract_skills(text)

print("First 300 chars of resume:")
print(text[:300])
print("\nSkills found:")
print(skills)

