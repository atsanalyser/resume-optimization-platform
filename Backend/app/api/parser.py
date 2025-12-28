from fastapi import APIRouter
from pydantic import BaseModel

from app.services.resume_parser import ResumeParser
from app.services.keyword_extractor import KeywordExtractor
from app.services.ats_scorer import ATSScorer
from app.services.jd_matcher import JDMatcher

router = APIRouter()

resume_parser = ResumeParser()
keyword_extractor = KeywordExtractor()
ats_scorer = ATSScorer()
jd_matcher = JDMatcher()


class ResumeInput(BaseModel):
    resume_text: str


class ResumeJDInput(BaseModel):
    resume_text: str
    job_description: str


@router.post("/parse-resume")
def parse_resume(data: ResumeInput):
    sections = resume_parser.parse(data.resume_text)
    return {"sections": sections}


@router.post("/analyze-resume")
def analyze_resume(data: ResumeInput):
    sections = resume_parser.parse(data.resume_text)
    keywords = keyword_extractor.extract(sections)
    ats = ats_scorer.score(sections, keywords)

    return {
        "ats_score": ats["ats_score"],
        "issues": ats["reasons"],
        "keyword_count": len(keywords)
    }


@router.post("/analyze-with-jd")
def analyze_with_jd(data: ResumeJDInput):
    sections = resume_parser.parse(data.resume_text)
    resume_keywords = keyword_extractor.extract(sections)

    ats = ats_scorer.score(sections, resume_keywords)
    jd_match = jd_matcher.match(resume_keywords, data.job_description)

    return {
        "ats_score": ats["ats_score"],
        "ats_issues": ats["reasons"],
        "jd_match_percentage": jd_match["match_percentage"],
        "missing_keywords": jd_match["missing_keywords"][:15],
        "matched_keywords": jd_match["matched_keywords"][:15]
    }
