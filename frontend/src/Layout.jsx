import { useState } from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { Home, Database, Search, GitGraph, BrainCircuit, Menu } from 'lucide-react';
import './Layout.css';

export default function Layout() {
  const [isOpen, setIsOpen] = useState(true);

  const navItems = [
    { to: '/', icon: <Home size={20} />, label: 'Dashboard' },
    { to: '/graph', icon: <GitGraph size={20} />, label: 'Knowledge Graph' },
    { to: '/ingest', icon: <Database size={20} />, label: 'Ingestion' },
    { to: '/query', icon: <Search size={20} />, label: 'Query' },
    { to: '/research', icon: <BrainCircuit size={20} />, label: 'Research' },
  ];

  return (
    <div className="layout-container">
      <aside className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
        <div className="sidebar-header flex items-center justify-between">
          {isOpen && <h2>MENMO</h2>}
          <button onClick={() => setIsOpen(!isOpen)} className="toggle-btn" aria-label="Toggle Sidebar">
            <Menu size={24} />
          </button>
        </div>
        <nav className="sidebar-nav">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
              title={item.label}
            >
              <span className="icon">{item.icon}</span>
              {isOpen && <span className="label">{item.label}</span>}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="main-content">
        <Outlet />
      </main>
    </div>
  );
}
