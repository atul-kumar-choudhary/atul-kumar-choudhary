import React from 'react';
import { Terminal, Code, User, Mail, Search, Plus, Bell, CheckCircle2, ChevronRight } from 'lucide-react';

export default function Home() {
  return (
    <div className="flex h-screen bg-bg-base text-text-main font-mono overflow-hidden">
      {/* SIDEBAR */}
      <aside className="w-80 border-r border-bg-card-border bg-bg-card flex flex-col h-full overflow-y-auto terminal-scroll hidden md:flex">
        <div className="p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-12 h-12 bg-bg-base border border-brand rounded flex items-center justify-center">
              <Terminal className="text-brand w-6 h-6 glow-text" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white tracking-tight">CYBERCORE//AI</h2>
              <div className="text-xs text-brand uppercase tracking-widest glow-text flex items-center gap-1">
                <span className="w-1.5 h-1.5 bg-brand rounded-full animate-pulse"></span>
                System Active
              </div>
            </div>
          </div>

          <div className="mb-8">
            <h1 className="text-2xl font-bold text-white mb-1">Atul Kumar</h1>
            <p className="text-text-muted text-sm mb-3">atul-kumar-choudhary <span className="bg-bg-card-border px-1.5 py-0.5 rounded text-xs">he/him</span></p>
            <div className="inline-flex items-center gap-1 text-xs text-bg-base bg-brand px-2 py-1 rounded font-bold mb-4">
              <CheckCircle2 className="w-3 h-3" />
              Full Stack AI Engineer
            </div>
            <p className="text-sm text-text-muted leading-relaxed mb-4">
              Building intelligent full-stack applications with React, Next.js, FastAPI, & reactive UI. Specializing in LLM orchestration, agentic workflows, and fast RAG vector pipelines. Fast learner shipping production code daily.
            </p>

            <button className="w-full bg-brand text-bg-base font-bold py-2 rounded mb-2 hover:opacity-90 transition-opacity">
              Hire Me
            </button>
            <button className="w-full border border-bg-card-border text-text-main font-bold py-2 rounded hover:bg-bg-card-hover transition-colors">
              Portfolio
            </button>
          </div>

          <div className="flex items-center gap-4 text-sm text-text-muted mb-6">
            <div><span className="text-white font-bold">142</span> Followers</div>
            <div><span className="text-white font-bold">218</span> Following</div>
            <div>★ 142</div>
          </div>

          <div className="space-y-2 text-sm text-text-muted mb-8">
            <div className="flex items-center gap-2"><span className="text-brand">📍</span> India (UTC+5:30) - Remote</div>
            <div className="flex items-center gap-2"><span className="text-brand">🎓</span> B.Tech Computer Science</div>
            <div className="flex items-center gap-2"><span className="text-brand">🌐</span> <a href="#" className="hover:text-brand transition-colors glow-text">dev@atulchoudhary.com</a></div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-3 text-xs font-bold text-brand uppercase tracking-widest border-b border-bg-card-border pb-2">
              <span>Engineering Foundations</span>
              <span>GPA 3.85</span>
            </div>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between"><span>Algorithms & Data Structures</span><span className="text-brand">A</span></div>
              <div className="flex justify-between"><span>Distributed Database Systems</span><span className="text-brand">A</span></div>
              <div className="flex justify-between"><span>Neural Networks & LLM Tuning</span><span className="text-brand">A+</span></div>
            </div>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="flex-1 flex flex-col h-full overflow-hidden bg-bg-base relative">
        
        {/* TOP NAV */}
        <header className="h-14 border-b border-bg-card-border bg-bg-card flex items-center justify-between px-6 sticky top-0 z-10">
          <div className="flex items-center gap-4">
            <span className="text-brand font-bold glow-text">CYBERCORE//AI</span>
            <div className="relative w-64 hidden sm:block">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-text-muted" />
              <input type="text" placeholder="Type / to search repositories" className="w-full bg-bg-base border border-bg-card-border rounded px-9 py-1 text-sm focus:outline-none focus:border-brand text-white" />
            </div>
          </div>
          <div className="flex items-center gap-4 text-text-muted">
            <Plus className="w-5 h-5 hover:text-white cursor-pointer" />
            <div className="relative">
              <Bell className="w-5 h-5 hover:text-white cursor-pointer" />
              <span className="absolute -top-1 -right-1 w-2 h-2 bg-brand rounded-full animate-pulse"></span>
            </div>
            <div className="w-6 h-6 bg-bg-card-border rounded-full ml-2 border border-brand glow-border"></div>
          </div>
        </header>

        {/* SUB NAV */}
        <nav className="flex items-center gap-6 px-6 py-3 border-b border-bg-card-border bg-bg-base text-sm text-text-muted sticky top-14 z-10">
          <span className="text-white border-b-2 border-brand pb-3 -mb-3 font-medium">Overview</span>
          <span className="hover:text-white cursor-pointer">Repositories <span className="bg-bg-card-border px-1.5 py-0.5 rounded text-xs ml-1">19</span></span>
          <span className="hover:text-white cursor-pointer">Projects</span>
          <span className="hover:text-white cursor-pointer">Packages</span>
          <span className="hover:text-white cursor-pointer">Stars <span className="bg-bg-card-border px-1.5 py-0.5 rounded text-xs ml-1">142</span></span>
        </nav>

        {/* SCROLLABLE TERMINAL AREA */}
        <div className="flex-1 overflow-y-auto terminal-scroll p-6 lg:p-10">
          
          {/* TERMINAL WINDOW */}
          <div className="border border-bg-card-border rounded-lg bg-bg-card shadow-2xl overflow-hidden mb-10">
            {/* TERMINAL HEADER */}
            <div className="bg-[#161b22] border-b border-bg-card-border px-4 py-2 flex items-center justify-between">
              <div className="flex gap-2">
                <div className="w-3 h-3 rounded-full bg-red-500"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
              </div>
              <div className="text-xs text-text-muted flex items-center gap-2">
                <span className="text-brand">atul-kumar-choudhary</span> / README.md <span className="bg-brand/10 text-brand px-1 py-0.5 rounded">UPDATED JUST NOW</span>
              </div>
              <div></div>
            </div>

            {/* TERMINAL BODY */}
            <div className="p-6 lg:p-8 space-y-8">
              
              <div>
                <div className="inline-flex items-center gap-2 text-xs text-brand bg-brand/10 px-2 py-1 rounded mb-4 font-bold border border-brand/20 glow-border">
                  <span className="w-1.5 h-1.5 bg-brand rounded-full animate-pulse"></span>
                  V0.2: FULL STACK AI ENGINEER :: REACTIVE FRONTENDS & BACKENDS //
                </div>
                <h1 className="text-3xl lg:text-4xl font-bold text-white tracking-tight mb-4">
                  Atul Kumar Choudhary — Full Stack AI Engineer
                </h1>
                <p className="text-text-muted leading-relaxed max-w-4xl text-sm lg:text-base">
                  Designing and engineering intelligent full-stack applications from concept to deployment. I pair modern reactive frontends (Next.js 14/15, Tailwind, TypeScript) with resilient AI backends (FastAPI, LangChain, Vector retrieval pipelines, and agent loops). Driven by curiosity, fast feedback cycles, and craft.
                </p>
              </div>

              <div className="flex flex-wrap gap-3">
                <a href="#" className="flex items-center gap-2 bg-[#1c2128] border border-bg-card-border hover:border-brand px-3 py-1.5 rounded text-sm text-text-main transition-colors">
                  <Mail className="w-4 h-4 text-brand" /> Email Me
                </a>
                <a href="#" className="flex items-center gap-2 bg-[#1c2128] border border-bg-card-border hover:border-brand px-3 py-1.5 rounded text-sm text-text-main transition-colors">
                  <User className="w-4 h-4 text-brand" /> LinkedIn
                </a>
                <a href="#" className="flex items-center gap-2 bg-[#1c2128] border border-bg-card-border hover:border-brand px-3 py-1.5 rounded text-sm text-text-main transition-colors">
                  <Code className="w-4 h-4 text-brand" /> GitHub
                </a>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-[#0d1117] border border-bg-card-border rounded p-4 border-l-2 border-l-brand">
                  <div className="text-xs text-text-muted uppercase tracking-wider mb-1">Full-Stack AI Projects</div>
                  <div className="text-2xl font-bold text-white mb-1">5+ Shipped</div>
                  <div className="text-brand text-xs">End-to-end Live Apps</div>
                </div>
                <div className="bg-[#0d1117] border border-bg-card-border rounded p-4">
                  <div className="text-xs text-text-muted uppercase tracking-wider mb-1">Weekly Cadence</div>
                  <div className="text-2xl font-bold text-white mb-1">30+ Commits</div>
                  <div className="text-text-muted text-xs">Consistent Git Strikes</div>
                </div>
                <div className="bg-[#0d1117] border border-bg-card-border rounded p-4">
                  <div className="text-xs text-text-muted uppercase tracking-wider mb-1">Open Source Pro</div>
                  <div className="text-2xl font-bold text-white mb-1">10+ Merged</div>
                  <div className="text-text-muted text-xs">Ecosystem Contributions</div>
                </div>
              </div>

              <div className="bg-[#0d1117] p-4 rounded border border-bg-card-border text-sm space-y-2">
                <div className="flex gap-2">
                  <span className="text-brand">▶ CORE FOCUS:</span>
                  <span className="text-white">Agent Workflows • RAG Architectures • Full-Stack TypeScript</span>
                </div>
                <div className="flex gap-2">
                  <span className="text-brand">▶ WORK STATUS:</span>
                  <span className="text-brand font-bold glow-text">Available for US/Remote Full-Time Roles</span>
                </div>
              </div>

              {/* JSON BLOCK */}
              <div className="bg-bg-base border border-bg-card-border rounded p-4 font-mono text-sm overflow-x-auto">
                <div className="flex text-text-muted mb-4 text-xs">
                  <div className="mr-8"><span className="text-brand">atul@cybercore</span>:~$</div>
                  <div>cat profile_info.json</div>
                </div>
                <pre className="text-[#e6edf3]">
{`{
  "engineer": `}<span className="text-brand">"Atul Kumar Choudhary"</span>{`,
  "role": `}<span className="text-brand">"Full Stack AI Engineer"</span>{`,
  "mindset": `}<span className="text-brand">"Build real products, measure with quantitative evals, iterate relentlessly."</span>{`,
  "technical_strengths": [
    `}<span className="text-brand">"Full-stack reactivity with React, Next.js, TypeScript, Tailwind"</span>{`,
    `}<span className="text-brand">"Production LLM integration via FastAPI, LangChain, OpenAI & Claude APIs"</span>{`,
    `}<span className="text-brand">"Vector search orchestration using Pinecone, ChromaDB, and hybrid pipelines"</span>{`,
    `}<span className="text-brand">"Containerization and scalable microservices deployed via GitHub Actions"</span>{`
  ],
  "open_to": [`}<span className="text-brand">"Full-Time Engineer"</span>{`, `}<span className="text-brand">"Applied AI Engineer"</span>{`, `}<span className="text-brand">"Full-Stack AI"</span>{`]
}`}
                </pre>
              </div>

            </div>
          </div>

          {/* FEATURED PROJECTS */}
          <div className="mb-10">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                <span className="text-brand">⬢</span> Featured Full-Stack AI Projects
              </h2>
              <a href="#" className="text-brand text-sm hover:underline glow-text">View Demos on Github →</a>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Project 1 */}
              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 hover:border-brand/50 transition-colors">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded bg-[#161b22] border border-bg-card-border flex items-center justify-center">
                      <span className="text-xl">🤖</span>
                    </div>
                    <div>
                      <h3 className="font-bold text-white text-lg">AI Agentic Workflow Runner</h3>
                    </div>
                  </div>
                  <span className="bg-brand/10 text-brand text-xs px-2 py-1 rounded border border-brand/20">LIVE DEMO</span>
                </div>
                <p className="text-text-muted text-sm mb-6 h-16">
                  Autonomous multi-agent execution orchestration. Generates step-by-step DAG task plans, executes self-correcting code analysis, and streams insights.
                </p>
                <div className="flex flex-wrap gap-2 mb-6">
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main">FastAPI</span>
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main">LangChain</span>
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-brand border-brand/30">Next.js 14</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                  <span className="text-text-muted">Stars: 84 • 14 Forks</span>
                  <a href="#" className="text-brand hover:underline">Live Demo ↗</a>
                </div>
              </div>

              {/* Project 2 */}
              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 hover:border-brand/50 transition-colors">
                <div className="flex justify-between items-start mb-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded bg-[#161b22] border border-bg-card-border flex items-center justify-center">
                      <span className="text-xl">🔍</span>
                    </div>
                    <div>
                      <h3 className="font-bold text-white text-lg">Enterprise RAG Search</h3>
                    </div>
                  </div>
                  <span className="bg-blue-500/10 text-blue-400 text-xs px-2 py-1 rounded border border-blue-500/20">PRODUCTION</span>
                </div>
                <p className="text-text-muted text-sm mb-6 h-16">
                  Enterprise documentation hybrid search engine. Combines BM25 keyword matching with dense OpenAI text embeddings in Pinecone to reduce hallucinations.
                </p>
                <div className="flex flex-wrap gap-2 mb-6">
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main">Pinecone</span>
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main">OpenAI API</span>
                  <span className="px-2 py-1 bg-[#161b22] border border-bg-card-border rounded text-xs text-brand border-brand/30">TypeScript</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                  <span className="text-text-muted">P95 Latency: 200ms</span>
                  <a href="#" className="text-brand hover:underline">Live Demo ↗</a>
                </div>
              </div>
            </div>
          </div>

          {/* TECH STACK */}
          <div className="mb-10">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                <span className="text-brand">⬢</span> Technical Stack & Applied AI Arsenal
              </h2>
              <span className="text-brand text-xs px-2 py-1 border border-brand rounded bg-brand/10">PRODUCTION SKILLS</span>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-32 h-32 bg-brand/5 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <div className="flex justify-between items-center mb-6 border-b border-bg-card-border pb-2">
                  <h3 className="text-white font-bold flex items-center gap-2"><span className="text-brand">🧠</span> AI & LLM Engineering</h3>
                  <span className="text-xs text-text-muted uppercase">Orchestration</span>
                </div>
                <div className="flex flex-wrap gap-3">
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-brand"></span> OpenAI / Anthropic APIs</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-brand"></span> LangChain & LlamaIndex</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-blue-400"></span> RAG Pipelines & Evals</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-purple-400"></span> Pinecone & ChromaDB</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-yellow-400"></span> Hugging Face</span>
                </div>
              </div>

              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <div className="flex justify-between items-center mb-6 border-b border-bg-card-border pb-2">
                  <h3 className="text-white font-bold flex items-center gap-2"><span className="text-blue-400">⚛️</span> Frontend & Reactive UI</h3>
                  <span className="text-xs text-text-muted uppercase">Modern Client</span>
                </div>
                <div className="flex flex-wrap gap-3">
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-blue-400"></span> Next.js 14/15 App Router</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-blue-500"></span> TypeScript Strict</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-cyan-400"></span> Tailwind CSS & Shadcn</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-indigo-400"></span> Zustand & React Query</span>
                </div>
              </div>

              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-32 h-32 bg-green-500/5 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <div className="flex justify-between items-center mb-6 border-b border-bg-card-border pb-2">
                  <h3 className="text-white font-bold flex items-center gap-2"><span className="text-green-400">⚙️</span> Backend & Data Systems</h3>
                  <span className="text-xs text-text-muted uppercase">APIs & Data</span>
                </div>
                <div className="flex flex-wrap gap-3">
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-green-400"></span> Python / FastAPI</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-green-500"></span> Node.js / Express</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-emerald-400"></span> PostgreSQL & Prisma</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-red-400"></span> Redis Caching</span>
                </div>
              </div>

              <div className="border border-bg-card-border bg-bg-card rounded-lg p-6 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-32 h-32 bg-orange-500/5 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <div className="flex justify-between items-center mb-6 border-b border-bg-card-border pb-2">
                  <h3 className="text-white font-bold flex items-center gap-2"><span className="text-orange-400">🚀</span> DevOps, Cloud & Tooling</h3>
                  <span className="text-xs text-text-muted uppercase">Shipping Pipeline</span>
                </div>
                <div className="flex flex-wrap gap-3">
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-blue-500"></span> Docker & Compose</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-gray-300"></span> GitHub Actions CI/CD</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-orange-400"></span> AWS (S3, EC2)</span>
                  <span className="px-3 py-1.5 bg-[#161b22] border border-bg-card-border rounded text-xs text-text-main flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-black border border-gray-600"></span> Vercel Platform</span>
                </div>
              </div>
            </div>
          </div>

          {/* FOOTER CTA */}
          <div className="border border-brand/30 bg-brand/5 rounded-lg p-8 relative overflow-hidden mb-10">
            <div className="absolute top-0 left-0 w-1 h-full bg-brand"></div>
            <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
              <div>
                <div className="text-xs text-brand font-bold mb-2 flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-brand animate-pulse"></span> READY FOR DAY 1 IMPACT
                </div>
                <h2 className="text-2xl font-bold text-white mb-2">Looking for a Full Stack AI Engineer?</h2>
                <p className="text-text-muted text-sm max-w-2xl">
                  I ship clean code quickly, communicate transparently, and bridge the gap between reactive modern frontends and powerful AI backends. Let's build something extraordinary together.
                </p>
                <div className="mt-4 flex gap-2">
                  <span className="bg-[#161b22] text-text-muted text-xs px-2 py-1 rounded border border-bg-card-border">Software Engineer</span>
                  <span className="bg-[#161b22] text-text-muted text-xs px-2 py-1 rounded border border-bg-card-border">Applied AI Engineer</span>
                  <span className="bg-[#161b22] text-text-muted text-xs px-2 py-1 rounded border border-bg-card-border">Full-Stack Dev</span>
                </div>
              </div>
              <div className="flex flex-col gap-3 min-w-48">
                <a href="mailto:dev@atulchoudhary.com" className="bg-brand text-bg-base font-bold text-center py-2 px-4 rounded hover:bg-white transition-colors glow-border">
                  dev@atulchoudhary.com
                </a>
                <a href="https://github.com/atul-kumar-choudhary" className="bg-[#161b22] border border-bg-card-border text-text-main text-center font-bold py-2 px-4 rounded hover:bg-bg-card-border transition-colors">
                  GitHub Profile
                </a>
              </div>
            </div>
          </div>

        </div>
      </main>
    </div>
  );
}
