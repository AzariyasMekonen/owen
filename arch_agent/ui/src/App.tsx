import { useState } from 'react'
import { Scanner } from './components/Scanner'
import { Generator } from './components/Generator'
import { ArchView } from './components/ArchView'
import { Diagram } from './components/Diagram'
import { ChatRefinement } from './components/ChatRefinement'
import { scanRepo, generateArchitecture, refineArchitecture } from './api'

function App() {
  const [loading, setLoading] = useState(false)
  const [architecture, setArchitecture] = useState<any>(null)
  const [diagram, setDiagram] = useState<string>('')

  const handleScan = async (path: string) => {
    setLoading(true)
    try {
      const data = await scanRepo(path)
      setArchitecture(data)
      setDiagram('')
    } catch (error) {
      alert('Error scanning repo')
    } finally {
      setLoading(false)
    }
  }

  const handleGenerate = async (idea: string) => {
    setLoading(true)
    try {
      const data = await generateArchitecture(idea)
      setArchitecture(data.architecture)
      setDiagram(data.diagram)
    } catch (error) {
      alert('Error generating architecture')
    } finally {
      setLoading(false)
    }
  }

  const handleRefine = async (feedback: string) => {
    setLoading(true)
    try {
      const data = await refineArchitecture(architecture, feedback)
      setArchitecture(data.architecture)
      setDiagram(data.diagram)
    } catch (error) {
      alert('Error refining architecture')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-slate-50 py-8 px-4 text-slate-900 font-sans">
      <div className="max-w-6xl mx-auto">
        <header className="mb-12 text-center">
          <h1 className="text-5xl font-black tracking-tighter text-slate-900">ARCH_AGENT</h1>
          <p className="text-slate-500 font-medium mt-2 uppercase tracking-widest text-xs">Autonomous Architecture Synthesis</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
          <Scanner onScan={handleScan} loading={loading} />
          <Generator onGenerate={handleGenerate} loading={loading} />
        </div>

        {architecture && (
          <div className="space-y-12 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <section>
              <h2 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 px-1">Interactive Canvas</h2>
              <ArchView architecture={architecture} onChange={setArchitecture} />
            </section>

            <section>
              <h2 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 px-1">Architectural Visualization</h2>
              <Diagram definition={diagram} architecture={architecture} />
            </section>

            <section className="max-w-2xl mx-auto">
              <h2 className="text-sm font-bold uppercase tracking-widest text-slate-400 mb-4 px-1 text-center">AI Handoff</h2>
              <ChatRefinement onRefine={handleRefine} loading={loading} />
            </section>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
