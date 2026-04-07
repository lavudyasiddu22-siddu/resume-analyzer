from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeAnalyzer:

    def __init__(self, resume, job_desc):
        self.resume = resume
        self.job_desc = job_desc

    def calculate_similarity(self):
        if not self.resume.text or not self.job_desc.description:
            return 0

        text = [self.resume.text, self.job_desc.description]

        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform(text)

        similarity = cosine_similarity(vectors[0], vectors[1])
        return round(similarity[0][0] * 100, 2)

    def skill_analysis(self):
        resume_words = set(self.resume.text.split())
        job_words = set(self.job_desc.description.split())

        matched = list(resume_words & job_words)
        missing = list(job_words - resume_words)

        return matched[:10], missing[:10]