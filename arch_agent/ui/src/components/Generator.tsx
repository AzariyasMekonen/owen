import React, { useState } from 'react';

interface GeneratorProps {
  onGenerate: (idea: str) => void;
  loading: boolean;
}

export const Generator: React.FC<GeneratorProps> = ({ onGenerate, loading }) => {
  const [idea, setIdea] = useState('');

  return (
    <div className="p-4 border rounded-lg shadow-sm bg-white">
      <h2 className="text-xl font-bold mb-4">Architecture Generator</h2>
      <div className="flex flex-col gap-2">
        <textarea
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
          placeholder="Describe your idea..."
          className="w-full p-2 border rounded h-24"
        />
        <button
          onClick={() => onGenerate(idea)}
          disabled={loading}
          className="px-4 py-2 bg-green-600 text-white rounded disabled:bg-green-300"
        >
          {loading ? 'Generating...' : 'Generate Architecture'}
        </button>
      </div>
    </div>
  );
};
