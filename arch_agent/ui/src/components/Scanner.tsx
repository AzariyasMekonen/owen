import React, { useState } from 'react';

interface ScannerProps {
  onScan: (path: str) => void;
  loading: boolean;
}

export const Scanner: React.FC<ScannerProps> = ({ onScan, loading }) => {
  const [path, setPath] = useState('.');

  return (
    <div className="p-4 border rounded-lg shadow-sm bg-white">
      <h2 className="text-xl font-bold mb-4">Repo Scanner</h2>
      <div className="flex gap-2">
        <input
          type="text"
          value={path}
          onChange={(e) => setPath(e.target.value)}
          placeholder="Repository Path"
          className="flex-1 p-2 border rounded"
        />
        <button
          onClick={() => onScan(path)}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded disabled:bg-blue-300"
        >
          {loading ? 'Scanning...' : 'Scan'}
        </button>
      </div>
    </div>
  );
};
