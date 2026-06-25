import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, AlertTriangle, BookOpen, ToggleLeft, ToggleRight } from 'lucide-react';
import './Query.css';

export default function Query() {
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const [socraticMode, setSocraticMode] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleQuery = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    const userMsg = { role: 'user', text: question };
    setMessages(prev => [...prev, userMsg]);
    setQuestion('');
    setLoading(true);

    try {
      const res = await fetch('/api/query/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: userMsg.text, mode: socraticMode ? 'socratic' : 'factual' })
      });
      const data = await res.json();
      setMessages(prev => [...prev, {
        role: 'agent',
        text: data.answer,
        sources: data.sources || [],
        contradictions: data.contradictions || [],
        mode: socraticMode ? 'socratic' : 'factual'
      }]);
    } catch (err) {
      setMessages(prev => [...prev, { role: 'agent', text: `Error: ${err.message}`, sources: [] }]);
    }
    setLoading(false);
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="query-page">
      <div className="query-header">
        <div>
          <h1>Knowledge Query</h1>
          <p>Ask questions about your ingested knowledge.</p>
        </div>
        <button
          className={`mode-toggle ${socraticMode ? 'active' : ''}`}
          onClick={() => setSocraticMode(!socraticMode)}
          title="Toggle Socratic mode"
        >
          {socraticMode ? <ToggleRight size={20} /> : <ToggleLeft size={20} />}
          {socraticMode ? 'Socratic Mode' : 'Factual Mode'}
        </button>
      </div>

      <div className="chat-thread">
        {messages.length === 0 && (
          <div className="chat-empty">
            <BookOpen size={48} strokeWidth={1} />
            <p>Ask anything from your knowledge graph.</p>
          </div>
        )}
        <AnimatePresence>
          {messages.map((msg, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className={`message ${msg.role}`}
            >
              <div className="message-bubble">
                <p style={{ whiteSpace: 'pre-wrap' }}>{msg.text}</p>
              </div>
              {msg.role === 'agent' && msg.sources?.length > 0 && (
                <div className="sources-row">
                  <span className="sources-label">Sources:</span>
                  {msg.sources.slice(0, 5).map((s, j) => (
                    <span key={j} className="source-chip">{s.slice(0, 8)}…</span>
                  ))}
                </div>
              )}
              {msg.contradictions?.length > 0 && (
                <div className="contradiction-alert">
                  <AlertTriangle size={14} />
                  <span>Active contradiction: "{msg.contradictions[0]?.a}" vs "{msg.contradictions[0]?.b}"</span>
                </div>
              )}
            </motion.div>
          ))}
        </AnimatePresence>
        {loading && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="message agent">
            <div className="message-bubble typing">
              <span /><span /><span />
            </div>
          </motion.div>
        )}
        <div ref={bottomRef} />
      </div>

      <form onSubmit={handleQuery} className="query-form">
        <input
          type="text"
          className="query-input"
          value={question}
          onChange={e => setQuestion(e.target.value)}
          placeholder="Ask a question about your knowledge..."
          disabled={loading}
        />
        <button type="submit" className="btn send-btn" disabled={loading || !question.trim()}>
          <Send size={18} />
        </button>
      </form>
    </motion.div>
  );
}
