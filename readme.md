# Production Agentic AI Template

> A battle-tested template for building agentic AI systems that actually ship to production — not just demos.

Built from real enterprise deployments. Covers everything that matters: **memory**, **evals**, **multi-agent orchestration**, and **observability**.

---

## 🔥 Why This Exists

Most agentic AI tutorials show you how to build a chatbot. This shows you how to build a **system**.

There's a massive gap between a working LangGraph prototype and a production-grade agentic pipeline. This template bridges that gap — covering the parts that actually break in production: memory drift, hallucination rates, agent coordination, cost blowouts, and observability blind spots.

---

## ⚡ Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangGraph, LangChain |
| Backend API | FastAPI |
| LLMs | Claude (Anthropic API), OpenAI, LLaMA |
| Memory & Vector Store | Pinecone, Weaviate, PostgreSQL |
| Observability | LangSmith, OpenTelemetry |
| LLMOps | MLflow, Weights & Biases, vLLM |
| Containerisation | Docker, Kubernetes |
| CI/CD | GitHub Actions |
| Cloud | AWS  |

---

## 🧠 What You'll Learn

### 1. Agent Memory Systems
- Short-term vs long-term memory architecture
- Context window optimisation strategies
- Thread-level history and agent-specific context
- Vector DB retrieval for persistent memory
- Summarisation pipelines for large context handling

### 2. Agent Evaluations (Top Priority)
- Automated eval frameworks for agent reasoning and reliability
- Trajectory evaluation — did the agent take the right steps?
- Output quality benchmarks (BLEU, ROUGE-L, custom metrics)
- Cost-aware evaluation — quality vs inference spend
- Regression testing across deployments

### 3. Multi-Agent Orchestration
- Planner → Executor → Validator agent patterns
- Parallel agent execution with asyncio.gather()
- QualityAgent gate — short-circuit bad inputs before LLM cost hits
- Declarative agent configuration via YAML (zero code changes for new rules)
- Supervisor and hierarchical agent architectures

### 4. Observability & Monitoring
- End-to-end LangSmith tracing across all agents
- Cost tracking per agent, per run, per client
- Error detection, replay debugging
- Production dashboards with pre-built SQL views
- Alerting on hallucination rate and confidence collapse

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                   FastAPI Layer                  │
│         (REST endpoints + async streaming)       │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│              LangGraph Orchestrator              │
│                                                  │
│  ┌─────────┐  ┌──────────┐  ┌───────────────┐  │
│  │Planner  │→ │Executor  │→ │ValidatorAgent │  │
│  │Agent    │  │Agent     │  │(DeepSeek-V3)  │  │
│  └─────────┘  └──────────┘  └───────────────┘  │
│                                                  │
│  ┌─────────────────────────────────────────┐    │
│  │     QualityAgent Gate (Pre-filter)      │    │
│  │  Short-circuits low-quality inputs      │    │
│  │  before any LLM cost is incurred        │    │
│  └─────────────────────────────────────────┘    │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│              Memory & Storage Layer              │
│   Vector DB (Pinecone/Weaviate) │ PostgreSQL     │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│           Observability (LangSmith)              │
│    Tracing │ Cost Tracking │ Eval Runs           │
└─────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/production-agentic-ai-template
cd production-agentic-ai-template
cp .env.example .env
docker-compose up --build
```

### Environment Variables
```env
ANTHROPIC_API_KEY=your_key
OPENAI_API_KEY=your_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
PINECONE_API_KEY=your_key
DATABASE_URL=postgresql://...
```

---

## 📁 Project Structure

```
├── agents/
│   ├── planner_agent.py
│   ├── executor_agent.py
│   ├── validator_agent.py
│   └── quality_gate.py
├── memory/
│   ├── short_term.py
│   ├── long_term.py
│   └── vector_store.py
├── evals/
│   ├── trajectory_eval.py
│   ├── output_quality.py
│   └── benchmarks/
├── api/
│   └── main.py (FastAPI)
├── observability/
│   └── langsmith_tracing.py
├── config/
│   └── agents.yaml
├── docker-compose.yml
└── .github/workflows/ci.yml
```

---

## 📊 Eval Framework

```python
from evals import TrajectoryEvaluator, OutputQualityEvaluator

evaluator = TrajectoryEvaluator(
    model="claude-sonnet-4-20250514",
    criteria=["reasoning", "tool_use", "goal_completion"]
)

results = evaluator.run(agent_trace)
print(results.score, results.reasoning)
```

---

## 🧪 Memory Architecture

```python
from memory import AgentMemory

memory = AgentMemory(
    short_term_window=10,        # Last N messages
    long_term_backend="pinecone", # Vector store
    summarisation_threshold=20,  # Summarise after N turns
)
```

---

## 📖 Inspired By

- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful agent orchestration
- [LangSmith](https://smith.langchain.com) — agent observability
- Anthropic's multi-agent research patterns
- Real enterprise deployments across 12+ production systems

---

## 🤝 Contributing

PRs welcome. If you're building production agentic systems and hit a pattern not covered here — open an issue or submit a PR.

---

## 📄 License

MIT — use it, fork it, ship it.

---

## ⭐ If this helped you

Star the repo. It helps more engineers find it and skip the painful parts of going to production.
