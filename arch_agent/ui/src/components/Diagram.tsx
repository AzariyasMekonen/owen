import React, { useEffect, useState } from 'react';
import mermaid from 'mermaid';
import { Card, CardHeader, CardTitle, CardContent } from './ui/card';
import { Button } from './ui/button';
import { RefreshCcw } from 'lucide-react';

mermaid.initialize({
  startOnLoad: false,
  theme: 'neutral',
  securityLevel: 'loose',
  flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' }
});

interface DiagramProps {
  definition: string;
  architecture?: any;
}

export const Diagram: React.FC<DiagramProps> = ({ definition, architecture }) => {
  const [svg, setSvg] = useState('');
  const [localDefinition, setLocalDefinition] = useState(definition);

  const generateLocalDefinition = (arch: any) => {
    let lines = ["graph TD"];
    if (arch.infrastructure) {
      arch.infrastructure.forEach((infra: any) => {
        const comp = infra.component.replace(/\s+/g, '_');
        const depl = infra.deployment.replace(/\s+/g, '_');
        lines.push(`    ${comp} --> ${depl}`);
      });
    }
    if (arch.routes) {
      lines.push("    subgraph API_Routes");
      arch.routes.forEach((route: any) => {
        const path_id = route.path.replace(/\//g, '_').replace(/-/g, '_').replace(/:/g, '_') || 'root';
        lines.push(`        ${route.method}_${path_id}["${route.method} ${route.path}"]`);
      });
      lines.push("    end");
    }
    return lines.join("\n");
  };

  const handleRefresh = async () => {
    const def = architecture ? generateLocalDefinition(architecture) : definition;
    if (def) {
      try {
        const id = `mermaid-${Math.floor(Math.random() * 10000)}`;
        const { svg: renderedSvg } = await mermaid.render(id, def);
        setSvg(renderedSvg);
      } catch (error) {
        console.error("Mermaid render failed", error);
      }
    }
  };

  useEffect(() => {
    handleRefresh();
  }, [definition, architecture]);

  if (!definition && !architecture) return null;

  return (
    <Card className="overflow-hidden border-none shadow-lg bg-white">
      <CardHeader className="flex flex-row items-center justify-between border-b bg-slate-50/50">
        <CardTitle className="text-sm font-semibold text-slate-500 uppercase tracking-widest">System Topology</CardTitle>
        <Button variant="ghost" size="icon" onClick={handleRefresh}>
          <RefreshCcw className="h-4 w-4" />
        </Button>
      </CardHeader>
      <CardContent className="p-12 overflow-auto">
        <div
          dangerouslySetInnerHTML={{ __html: svg }}
          className="flex justify-center transition-all duration-500 ease-in-out"
        />
      </CardContent>
    </Card>
  );
};
