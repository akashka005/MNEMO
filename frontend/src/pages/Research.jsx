import { useState } from 'react';
import { motion } from 'framer-motion';

export default function Research() {
  const [texts, setTexts] = useState('');
  const [nodes, setNodes] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const payload = {
        texts: texts.split('\n').filter(t => t.trim()),
        nodes: nodes.split('\n').filter(n => n.trim()),
        graph: [] // simplified for now
      };
      const res = await fetch('/api/research/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ error: err.message });
    }
    setLoading(false);
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
      <h1 className="mb-6">Research Orchestrator</h1>
      <div className="card max-w-3xl mb-6">
        <form onSubmit={handleAnalyze} className="flex flex-col gap-4">
          <div>
            <label className="block mb-2 font-medium">Texts (One per line)</label>
            <textarea 
              className="input" 
              rows="4" 
              value={texts} 
              onChange={e => setTexts(e.target.value)}
              placeholder="E.g. The mechanism of XYZ..."
            ></textarea>
          </div>
          <div>
            <label className="block mb-2 font-medium">Nodes (One per line)</label>
            <textarea 
              className="input" 
              rows="2" 
              value={nodes} 
              onChange={e => setNodes(e.target.value)}
              placeholder="E.g. Transformer&#10;Attention"
            ></textarea>
          </div>
          <button type="submit" className="btn self-start" disabled={loading}>
            {loading ? 'Analyzing...' : 'Run Analysis'}
          </button>
        </form>
      </div>

      {result && (
        <motion.div initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="card max-w-3xl">
          <h3>Analysis Result</h3>
          <pre className="mt-4 p-4 bg-gray-100 rounded text-sm overflow-auto max-h-[500px]">
            {JSON.stringify(result, null, 2)}
          </pre>
        </motion.div>
      )}
    </motion.div>
  );
}
