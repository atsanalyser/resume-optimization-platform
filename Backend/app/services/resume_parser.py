class ResumeParser:
    def parse(self, resume_text: str) -> dict:
        sections = {
            "summary": "",
            "skills": "",
            "experience": "",
            "education": ""
        }

        current_section = None

        for line in resume_text.split("\n"):
            l = line.strip().lower()

            if "summary" in l:
                current_section = "summary"
                continue
            elif "skill" in l:
                current_section = "skills"
                continue
            elif "experience" in l:
                current_section = "experience"
                continue
            elif "education" in l:
                current_section = "education"
                continue

            if current_section:
                sections[current_section] += " " + line.strip()

        return sections
