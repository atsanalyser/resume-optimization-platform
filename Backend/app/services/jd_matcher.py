import re


class JDMatcher:
    def match(self, resume_keywords: list, job_description: str) -> dict:
        jd = job_description.lower()
        jd = re.sub(r"[^\w\s]", "", jd)
        jd_words = set(jd.split())

        matched = list(set(resume_keywords) & jd_words)
        missing = list(jd_words - set(resume_keywords))

        match_percentage = int(
            (len(matched) / len(jd_words)) * 100
        ) if jd_words else 0

        return {
            "match_percentage": match_percentage,
            "matched_keywords": matched,
            "missing_keywords": missing
        }
