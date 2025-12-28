export async function postParseResume(resume_text) {
  const res = await fetch('/api/parse-resume', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ resume_text })
  })
  return res.json()
}

export async function postAnalyzeResume(resume_text) {
  const res = await fetch('/api/analyze-resume', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ resume_text })
  })
  return res.json()
}

export async function postAnalyzeWithJD(resume_text, job_description) {
  const res = await fetch('/api/analyze-with-jd', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ resume_text, job_description })
  })
  return res.json()
}
