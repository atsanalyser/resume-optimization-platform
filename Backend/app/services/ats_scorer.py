class ATSScorer:
    def score(self, sections: dict, keywords: list) -> dict:
        score = 0
        reasons = []

        for section, content in sections.items():
            if not content.strip():
                reasons.append(f"Missing or weak section: {section}")
            else:
                score += 10

        if len(keywords) < 10:
            reasons.append(
                "Low keyword density — ATS may rank this resume low")
        else:
            score += 20

        total_words = sum(len(v.split()) for v in sections.values())
        if total_words < 100:
            reasons.append("Resume length not ATS-optimized")
        else:
            score += 20

        return {
            "ats_score": min(score, 100),
            "reasons": reasons
        }
