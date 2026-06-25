import { useEffect, useState, useRef } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import { motion } from 'framer-motion';

export default function GraphView() {
  const [graphData, setGraphData] = useState({ nodes: [], links: [] });
  const containerRef = useRef(null);
  const [dimensions, setDimensions] = useState({ width: 800, height: 600 });

  useEffect(() => {
    fetch('/api/graph/')
      .then(r => r.json())
      .then(data => {
        const nodes = data.nodes.map(n => ({ id: n.id, name: n.label, val: n.confidence || 1 }));
        const links = data.edges.map(e => ({ source: e.source, target: e.target, name: e.relation }));
        setGraphData({ nodes, links });
      })
      .catch(console.error);
  }, []);

  useEffect(() => {
    if (containerRef.current) {
      setDimensions({
        width: containerRef.current.clientWidth,
        height: containerRef.current.clientHeight
      });
    }
  }, [containerRef]);

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex flex-col" style={{ height: '100%' }}>
      <h1 className="mb-4">Knowledge Graph</h1>
      <div className="card" style={{ flex: 1, padding: 0, overflow: 'hidden' }} ref={containerRef}>
        <ForceGraph2D
          graphData={graphData}
          width={dimensions.width}
          height={dimensions.height}
          nodeLabel="name"
          nodeAutoColorBy="id"
          linkDirectionalArrowLength={3.5}
          linkDirectionalArrowRelPos={1}
        />
      </div>
    </motion.div>
  );
}
