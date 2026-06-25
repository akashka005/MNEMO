import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { GitMerge, AlertTriangle, Lightbulb, Database } from 'lucide-react';
import './Dashboard.css';

const StatCard = ({ icon, label, value, color }) => (
  <motion.div
    className="stat-card"
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    whileHover={{ y: -3 }}
  >
    <div className="stat-icon" style={{ color }}>
      {icon}
    </div>
    <div className="stat-value">{value ?? '—'}</div>
    <div className="stat-label">{label}</div>
  </motion.div>
);

export default function Dashboard() {
  const [insights, setInsights] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch('/api/insights/');
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setInsights(data);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  if (loading) return (
    <div className="dashboard-loading">
      <div className="spinner" />
      <p>Loading knowledge insights...</p>
    </div>
  );

  if (error) return (
    <div className="dashboard-error">
      <AlertTriangle size={32} />
      <p>Could not load insights: {error}</p>
      <small>Is the backend running on port 8000?</small>
    </div>
  );

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="dashboard">
      <div className="dashboard-header">
        <h1>Knowledge Dashboard</h1>
        <p className="dashboard-subtitle">{insights?.summary}</p>
      </div>

      <div className="stats-row">
        <StatCard
          icon={<Database size={24} />}
          label="Total Nodes"
          value={insights?.total_nodes ?? 0}
          color="#3b82f6"
        />
        <StatCard
          icon={<AlertTriangle size={24} />}
          label="Contradictions"
          value={insights?.contradictions?.length ?? 0}
          color="#ef4444"
        />
        <StatCard
          icon={<GitMerge size={24} />}
          label="Bridges"
          value={insights?.bridges?.length ?? 0}
          color="#8b5cf6"
        />
        <StatCard
          icon={<Lightbulb size={24} />}
          label="Low Confidence"
          value={insights?.knowledge_gaps?.length ?? 0}
          color="#f59e0b"
        />
      </div>

      <div className="dashboard-grid">
        <div className="card">
          <h3 className="section-title">
            <AlertTriangle size={18} color="#ef4444" />
            Active Contradictions
          </h3>
          {insights?.contradictions?.length === 0 ? (
            <p className="empty-state">No contradictions detected yet.</p>
          ) : (
            <ul className="insight-list">
              {insights.contradictions.map((c, i) => (
                <li key={i} className="insight-item conflict">
                  <span className="insight-a">{c.a}</span>
                  <span className="insight-vs">CONTRADICTS</span>
                  <span className="insight-b">{c.b}</span>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="card">
          <h3 className="section-title">
            <GitMerge size={18} color="#8b5cf6" />
            Bridge Discoveries
          </h3>
          {insights?.bridges?.length === 0 ? (
            <p className="empty-state">No bridges discovered yet. Ingest knowledge from different domains!</p>
          ) : (
            <ul className="insight-list">
              {insights.bridges.map((b, i) => (
                <li key={i} className="insight-item bridge">
                  <span className="insight-a">{b.a}</span>
                  <span className="insight-vs">EMERGES FROM</span>
                  <span className="insight-b">{b.b}</span>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="card">
          <h3 className="section-title">
            <Lightbulb size={18} color="#f59e0b" />
            Low Confidence Nodes
          </h3>
          {insights?.knowledge_gaps?.length === 0 ? (
            <p className="empty-state">No low-confidence nodes found.</p>
          ) : (
            <ul className="gap-list">
              {insights.knowledge_gaps.map((g, i) => (
                <li key={i} className="gap-item">
                  <span className="gap-text">{g.text?.slice(0, 100)}...</span>
                  <div className="confidence-bar-wrap">
                    <div
                      className="confidence-bar"
                      style={{
                        width: `${Math.max((g.confidence || 0) * 100, 5)}%`,
                        background: g.confidence < 0.3 ? '#ef4444' : '#f59e0b'
                      }}
                    />
                    <span className="confidence-val">{((g.confidence || 0) * 100).toFixed(0)}%</span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </motion.div>
  );
}
