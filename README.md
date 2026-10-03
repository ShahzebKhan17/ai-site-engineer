# AI Site Engineer 🏗️

> **RAG-Powered Construction Intelligence Assistant**  
> *Core Architectural Principle: RAG finds engineering information; deterministic tools perform calculations; the LLM orchestrates and explains.*

---

## 🏛️ System Architecture

AI Site Engineer is engineered on an auditable **Three-Tier Architecture**:
1. **Hybrid Retrieval (RAG):** Surfaces exact drawing clauses, schedules, and specifications using dense vector similarity (pgvector) and sparse keyword search (BM25) fused with Reciprocal Rank Fusion (RRF).
2. **Deterministic Calculation Engine:** Pure Python modules implementing certified engineering standards (IS 1786, IS 456, IS 1200, ACI 318). LLMs are strictly forbidden from performing arithmetic.
3. **LLM Orchestration:** Intent recognition, structured tool calling, input validation, and conversational synthesis with traceable sheet/revision citations.

See [docs/ARCHITECTURE.md](file:///c:/Users/hp/Downloads/Switch/AI%20Site%20Engineer/docs/ARCHITECTURE.md) for full architectural specifications, entity relationship diagrams, and data flows.

---

## 🚀 Getting Started

### 1. Environment Requirements
- Python 3.11+ (Python 3.13 tested)
- Node.js v20+ (for Next.js frontend in later phases)
- PostgreSQL with `pgvector` extension (or local SQLite for dev testing)

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create & activate a virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate   # Windows
# or: source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### 3. Run Backend API Server
```bash
# From backend directory
python -m uvicorn app.main:app --reload --port 8000
```
Interactive API documentation will be available at:
* Swagger UI: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
* ReDoc: [http://localhost:8000/api/v1/redoc](http://localhost:8000/api/v1/redoc)

### 4. Run Test Suite
```bash
# From project root
python -m unittest discover -s backend/tests
```

---

## 🔒 Engineering Principles & Safety Rules
* **No Mental Math in Prompts:** Calculations are executed strictly by validated deterministic Python tools.
* **Strict Missing-Data Protocol:** The system never invents missing dimensions or bar marks; it flags them for verification with the structural consultant.
* **Revision Precedence:** By default queries target the latest approved revision and highlight superseded drawings.
