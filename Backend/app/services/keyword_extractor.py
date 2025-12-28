import re

STOPWORDS = {
    "and", "or", "for", "with", "a", "an", "the",
    "to", "of", "in", "on", "is", "are"
}


class KeywordExtractor:
    def extract(self, sections: dict) -> list:
        combined = " ".join(sections.values()).lower()
        combined = re.sub(r"[^\w\s]", "", combined)

        words = combined.split()

        keywords = [
            w for w in words
            if w not in STOPWORDS and len(w) > 2
        ]

        return list(set(keywords))
