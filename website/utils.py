import spacy , re
from pypdf import PdfReader

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text 


def extract_skills(job_description):
    
    doc = nlp(job_description)

    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    named_entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'SKILL', 'LANGUAGE']]

    skills = list(set(noun_chunks + named_entities))
    # print(skills)
    return skills


def extract_contact_details(resume_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(resume_text)

    contact_details = {}

    # Extract email addresses using regex pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_matches = re.findall(email_pattern, resume_text)
    contact_details['email'] = email_matches

    # Extract phone numbers using regex pattern
    phone_pattern = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b'
    phone_matches = re.findall(phone_pattern, resume_text)
    contact_details['phone'] = ["".join(match) for match in phone_matches]

    return contact_details