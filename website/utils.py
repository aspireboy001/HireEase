import spacy
import re
from pypdf import PdfReader

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text().lower() + "\n"
    return text 



def extract_skills(job_description):
    doc = nlp(job_description.lower())

    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    named_entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'SKILL', 'LANGUAGE']]

    skills = list(set(noun_chunks + named_entities))
    
    return skills

def extract_skills_with_score(resume_text, job_description):
    # Preprocessing
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Extract skills from job description
    job_skills_list = re.findall(r'\b\w+\b', job_description)  # Example: Extracting individual words as skills
    resume_skill_list = set(re.findall(r'\b\w+\b', resume_text))
    # Skill extraction and scoring
    total_score = 0
    for skill in resume_skill_list:
        if skill in job_skills_list:
            total_score += 1 

    if len(job_skills_list) > 0:
        total_score = total_score/len(job_skills_list) * 100 
        
    return round(total_score,3)



def extract_contact_details(resume_text):
    doc = nlp(resume_text.lower())

    contact_details = {}

    # Extract email addresses using regex pattern
    email_pattern = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'
    email_matches = re.findall(email_pattern, resume_text)
    contact_details['email'] = email_matches

    # Extract phone numbers using regex pattern
    phone_pattern = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b'
    phone_matches = re.findall(phone_pattern, resume_text)
    contact_details['phone'] = ["".join(match) for match in phone_matches]
    contact_details['phone'] = ["+" + phone_number for phone_number in contact_details['phone']]

    return contact_details
