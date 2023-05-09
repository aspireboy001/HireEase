import spacy
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
