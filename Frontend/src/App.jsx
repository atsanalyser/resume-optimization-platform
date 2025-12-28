import React, { useState } from 'react'
import { postParseResume, postAnalyzeResume, postAnalyzeWithJD } from './api'

export default function App() {
  const [resume, setResume] = useState('')
  const [jd, setJd] = useState('')
  const [output, setOutput] = useState(null)
  const [loading, setLoading] = useState(false)

  async function handleParse() {
    setLoading(true)
    setOutput(null)
    try {
      const data = await postParseResume(resume)
      setOutput(data)
    } catch (e) {
      setOutput({ error: e.message })
    } finally {
      setLoading(false)
    }
  }

  async function handleAnalyze() {
    setLoading(true)
    setOutput(null)
    try {
      const data = await postAnalyzeResume(resume)
      setOutput(data)
    } catch (e) {
      setOutput({ error: e.message })
    } finally {
      setLoading(false)
    }
  }

  async function handleAnalyzeWithJD() {
    setLoading(true)
    setOutput(null)
    try {
      const data = await postAnalyzeWithJD(resume, jd)
      setOutput(data)
    } catch (e) {
      setOutput({ error: e.message })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Resume Optimizer</h1>

      <label>Paste resume text</label>
      <textarea value={resume} onChange={(e) => setResume(e.target.value)} rows={12} />

      <div className="buttons">
        <button onClick={handleParse} disabled={loading || !resume}>Parse Resume</button>
        <button onClick={handleAnalyze} disabled={loading || !resume}>Analyze Resume</button>
      </div>

      <label>Job description (optional for JD analysis)</label>
      <textarea value={jd} onChange={(e) => setJd(e.target.value)} rows={6} />
      <div className="buttons">
        <button onClick={handleAnalyzeWithJD} disabled={loading || !resume || !jd}>Analyze With JD</button>
      </div>

      <div className="output">
        <h2>Result</h2>
        {loading && <div className="muted">Loading...</div>}
        {!loading && output && (
          <pre>{JSON.stringify(output, null, 2)}</pre>
        )}
      </div>
    </div>
  )
}
