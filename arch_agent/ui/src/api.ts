const API_BASE = 'http://localhost:8000';

export async function scanRepo(path: string) {
  const response = await fetch(`${API_BASE}/scan?path=${encodeURIComponent(path)}`, {
    method: 'POST',
  });
  if (!response.ok) throw new Error('Scan failed');
  return response.json();
}

export async function generateArchitecture(idea: string) {
  const response = await fetch(`${API_BASE}/generate-architecture?idea=${encodeURIComponent(idea)}`, {
    method: 'POST',
  });
  if (!response.ok) throw new Error('Generation failed');
  return response.json();
}
