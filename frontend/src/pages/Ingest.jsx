import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, Link, FileText, GitMerge, AlertTriangle, ArrowUpRight, Zap } from 'lucide-react';
import './Ingest.css';

const CKE_COLORS = {
  MERGE: { bg: '#dbeafe', text: '#1d4ed8', icon: <GitMerge size={16} /> },
  EXTEND: { bg: '#dcfce7', text: '#15803d', icon: <ArrowUpRight size={16} /> },
  CONFLICT: { bg: '#fee2e2', text: '#b91c1c', icon: <AlertTriangle size={16} /> },
  EMERGE: { bg: '#ede9fe', text: '#6d28d9', icon: <Zap size={16} /> },
  NONE: { bg: '#f1f5f9', text: '#475569', icon: <FileText size={16} /> },
};

export default function Ingest() {
  const [tab, setTab] = useState('text'); // 'text' | 'url'
  const [text, setText] = useState('');
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);

  const handleIngest = async (e) => {
    e.preventDefault();
    setLoading(true);
    const payload = tab === 'text'
      ? { text, source: 'manual' }
      : { text: url, source: url };

    try {
      const res = await fetch('/api/ingest/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      setResults(prev => [{ ...data, timestamp: new Date().toLocaleTimeString() }, ...prev]);
      if (res.ok) { setText(''); setUrl(''); }
    } catch (err) {
      setResults(prev => [{ status: 'error', message: err.message, timestamp: new Date().toLocaleTimeString() }, ...prev]);
    }
    setLoading(false);
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="ingest-page">
      <div className="ingest-header">
        <h1>Knowledge Ingestion</h1>
        <p>Add knowledge and watch MNEMO classify it with CKE operations in real time.</p>
      </div>

      <div className="ingest-layout">
        <div className="ingest-form-area">
          <div className="tab-switcher">
            <button className={`tab-btn ${tab === 'text' ? 'active' : ''}`} onClick={() => setTab('text')}>
              <FileText size={16} /> Text
            </button>
            <button className={`tab-btn ${tab === 'url' ? 'active' : ''}`} onClick={() => setTab('url')}>
              <Link size={16} /> URL
            </button>
          </div>

          <form onSubmit={handleIngest} className="ingest-form">
            {tab === 'text' ? (
              <textarea
                className="ingest-textarea"
                rows={10}
                value={text}
                onChange={e => setText(e.target.value)}
                placeholder="Paste your research notes, article text, observations..."
                required
              />
            ) : (
              <input
                type="url"
                className="input ingest-url"
                value={url}
                onChange={e => setUrl(e.target.value)}
                placeholder="https://arxiv.org/abs/..."
                required
              />
            )}
            <button type="submit" className="btn ingest-btn" disabled={loading}>
              {loading ? (
                <><span className="btn-spinner" /> Ingesting & Analyzing...</>
              ) : (
                <><Upload size={16} /> Ingest Knowledge</>
              )}
            </button>
          </form>
        </div>

        <div className="cke-feed">
          <h3>CKE Operation Feed</h3>
          <AnimatePresence>
            {results.length === 0 && (
              <p className="feed-empty">CKE events will appear here after each ingestion.</p>
            )}
            {results.map((r, i) => {
              const op = r.cke_operation || 'NONE';
              const colors = CKE_COLORS[op] || CKE_COLORS.NONE;
              return (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  className="feed-item"
                >
                  <div className="feed-item-header">
                    <span className="cke-badge" style={{ background: colors.bg, color: colors.text }}>
                      {colors.icon} {op}
                    </span>
                    <span className="feed-time">{r.timestamp}</span>
                  </div>
                  <p className="feed-msg">{r.message || r.cke_explanation}</p>
                  {r.node_id && <code className="feed-id">{r.node_id}</code>}
                </motion.div>
              );
            })}
          </AnimatePresence>
        </div>
      </div>
    </motion.div>
  );
}
