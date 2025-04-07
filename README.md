# Multi-Project Repository

This repository contains two main projects:

1. **Pipeline Architecture** (`pipeline-architecture/`)
   - Data processing pipeline implementation
   - Python-based components

2. **Deep Researcher TS** (`deep-researcher-ts/`)
   - AI research agent implementation
   - TypeScript/LangGraph-based

## Development Setup

### Python Projects
```bash
cd pipeline-architecture
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Node.js Projects
```bash
cd deep-researcher-ts
yarn install
```

## Contribution Guidelines

1. Create feature branches from `main`
2. Keep commits atomic and well-described
3. Update documentation when adding features
4. Run tests before pushing changes

## Project Structure

```
├── deep-researcher-ts/    # AI research agent
├── pipeline-architecture/ # Data processing
├── .gitignore             # Combined ignore rules
└── README.md              # This file
