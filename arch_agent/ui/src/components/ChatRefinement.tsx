import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from './ui/card';
import { Button } from './ui/button';
import { Input } from './ui/input';

interface ChatRefinementProps {
  onRefine: (feedback: string) => void;
  loading: boolean;
}

export const ChatRefinement: React.FC<ChatRefinementProps> = ({ onRefine, loading }) => {
  const [feedback, setFeedback] = useState('');

  return (
    <Card className="mt-4 border-slate-200 shadow-lg">
      <CardHeader>
        <CardTitle className="text-sm font-bold uppercase tracking-widest text-slate-500">Refine Architecture</CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col gap-2">
        <Input
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          placeholder="Suggest changes (e.g., 'Add a Redis cache', 'Use Go instead')..."
          className="bg-slate-50 border-slate-200"
        />
        <Button onClick={() => onRefine(feedback)} disabled={loading} variant="default" className="w-full">
          {loading ? 'Refining...' : 'Refine with AI'}
        </Button>
      </CardContent>
    </Card>
  );
};
