import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './Layout';
import Dashboard from './pages/Dashboard';
import GraphView from './pages/GraphView';
import Ingest from './pages/Ingest';
import Query from './pages/Query';
import Research from './pages/Research';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="graph" element={<GraphView />} />
          <Route path="ingest" element={<Ingest />} />
          <Route path="query" element={<Query />} />
          <Route path="research" element={<Research />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
