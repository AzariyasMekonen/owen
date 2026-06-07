import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from './ui/card';
import { Input } from './ui/input';
import { Button } from './ui/button';
import { Plus, Trash2, Shield, Share2, Code2, Layers } from 'lucide-react';

interface ArchViewProps {
  architecture: any;
  onChange: (newArch: any) => void;
}

export const ArchView: React.FC<ArchViewProps> = ({ architecture, onChange }) => {
  if (!architecture) return null;

  const updateField = (category: string, index: number, field: string, value: any) => {
    const newArch = { ...architecture };
    newArch[category][index][field] = value;
    onChange(newArch);
  };

  const addItem = (category: string, defaultItem: any) => {
    const newArch = { ...architecture };
    newArch[category] = [...(newArch[category] || []), defaultItem];
    onChange(newArch);
  };

  const removeItem = (category: string, index: number) => {
    const newArch = { ...architecture };
    newArch[category] = newArch[category].filter((_: any, i: number) => i !== index);
    onChange(newArch);
  };

  return (
    <div className="space-y-8">
      <Card className="border-none shadow-xl bg-white/80 backdrop-blur-md">
        <CardHeader>
          <Input
            value={architecture.name}
            onChange={(e) => onChange({...architecture, name: e.target.value})}
            className="text-3xl font-black border-none p-0 focus-visible:ring-0 h-auto bg-transparent tracking-tight"
          />
        </CardHeader>
        <CardContent>
          <textarea
            value={architecture.summary}
            onChange={(e) => onChange({...architecture, summary: e.target.value})}
            className="w-full text-slate-600 bg-transparent border-none resize-none focus:outline-none text-base leading-relaxed"
            rows={4}
          />
          <div className="mt-4 flex flex-wrap gap-2">
            {architecture.stack?.map((tech: string, i: number) => (
              <span key={i} className="px-3 py-1 bg-slate-100 rounded-full text-xs font-bold text-slate-600 uppercase tracking-wider">{tech}</span>
            ))}
            <Button variant="ghost" size="sm" className="h-6 text-[10px]" onClick={() => addItem('stack', 'New Tech')}>+ ADD TECH</Button>
          </div>
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <EditableSection
          title="Requirements"
          items={architecture.requirements}
          onUpdate={(i, f, v) => updateField('requirements', i, f, v)}
          onAdd={() => addItem('requirements', { id: `REQ-${Date.now()}`, description: 'New Requirement', priority: 'Medium' })}
          onRemove={(i) => removeItem('requirements', i)}
          renderItem={(item, i, update) => (
            <div className="flex gap-2 items-center">
              <Input value={item.description} onChange={(e) => update('description', e.target.value)} className="flex-1 bg-transparent border-slate-200" />
            </div>
          )}
        />

        <EditableSection
          title="Security Features"
          icon={<Shield className="h-4 w-4" />}
          items={architecture.security_features || []}
          onUpdate={(i, f, v) => updateField('security_features', i, f, v)}
          onAdd={() => addItem('security_features', { feature: 'Authentication', description: 'JWT based', type: 'Authentication' })}
          onRemove={(i) => removeItem('security_features', i)}
          renderItem={(item, i, update) => (
            <div className="flex flex-col gap-1">
              <Input value={item.feature} onChange={(e) => update('feature', e.target.value)} className="font-bold border-none h-6 p-0" />
              <Input value={item.description} onChange={(e) => update('description', e.target.value)} className="text-xs text-slate-500 border-none h-4 p-0" />
            </div>
          )}
        />

        <EditableSection
          title="Routes & API"
          items={architecture.routes}
          onUpdate={(i, f, v) => updateField('routes', i, f, v)}
          onAdd={() => addItem('routes', { path: '/new', method: 'GET', description: '' })}
          onRemove={(i) => removeItem('routes', i)}
          renderItem={(item, i, update) => (
            <div className="flex gap-2 items-center">
              <span className="text-[10px] font-black w-10 text-slate-400">{item.method}</span>
              <Input value={item.path} onChange={(e) => update('path', e.target.value)} className="flex-1 border-none bg-slate-50 h-8" />
            </div>
          )}
        />

        <EditableSection
          title="Data Schemas"
          items={architecture.schemas}
          onUpdate={(i, f, v) => updateField('schemas', i, f, v)}
          onAdd={() => addItem('schemas', { table_name: 'new_table', columns: {}, relationships: [] })}
          onRemove={(i) => removeItem('schemas', i)}
          renderItem={(item, i, update) => (
            <Input value={item.table_name} onChange={(e) => update('table_name', e.target.value)} className="w-full font-mono text-sm" />
          )}
        />

        <EditableSection
          title="Integrations"
          icon={<Share2 className="h-4 w-4" />}
          items={architecture.integrations || []}
          onUpdate={(i, f, v) => updateField('integrations', i, f, v)}
          onAdd={() => addItem('integrations', { service: 'Stripe', protocol: 'HTTPS', description: 'Payments' })}
          onRemove={(i) => removeItem('integrations', i)}
          renderItem={(item, i, update) => (
            <div className="flex gap-2 items-center">
              <Input value={item.service} onChange={(e) => update('service', e.target.value)} className="flex-1" />
            </div>
          )}
        />

        <EditableSection
          title="Algorithms"
          icon={<Code2 className="h-4 w-4" />}
          items={architecture.algorithms || []}
          onUpdate={(i, f, v) => updateField('algorithms', i, f, v)}
          onAdd={() => addItem('algorithms', { name: 'PBKDF2', logic: 'Password hashing', complexity: 'O(N)' })}
          onRemove={(i) => removeItem('algorithms', i)}
          renderItem={(item, i, update) => (
            <div className="flex gap-2 items-center">
              <Input value={item.name} onChange={(e) => update('name', e.target.value)} className="flex-1" />
            </div>
          )}
        />
      </div>
    </div>
  );
};

interface EditableSectionProps {
  title: string;
  icon?: React.ReactNode;
  items: any[];
  onUpdate: (index: number, field: string, value: any) => void;
  onAdd: () => void;
  onRemove: (index: number) => void;
  renderItem: (item: any, index: number, update: (field: string, value: any) => void) => React.ReactNode;
}

const EditableSection: React.FC<EditableSectionProps> = ({ title, icon, items, onUpdate, onAdd, onRemove, renderItem }) => (
  <Card className="border-slate-100 shadow-sm hover:shadow-md transition-shadow">
    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-4 border-b border-slate-50 mb-4 py-3">
      <div className="flex items-center gap-2">
        {icon || <Layers className="h-4 w-4 text-slate-400" />}
        <CardTitle className="text-xs font-bold uppercase tracking-widest text-slate-500">{title}</CardTitle>
      </div>
      <Button variant="ghost" size="icon" onClick={onAdd} className="h-6 w-6">
        <Plus className="h-3 w-3" />
      </Button>
    </CardHeader>
    <CardContent className="space-y-4">
      {items.map((item, i) => (
        <div key={i} className="group relative flex items-center gap-2">
          <div className="flex-1">
            {renderItem(item, i, (f, v) => onUpdate(i, f, v))}
          </div>
          <Button
            variant="ghost"
            size="icon"
            onClick={() => onRemove(i)}
            className="h-6 w-6 opacity-0 group-hover:opacity-100 transition-opacity text-destructive"
          >
            <Trash2 className="h-3 w-3" />
          </Button>
        </div>
      ))}
    </CardContent>
  </Card>
);
