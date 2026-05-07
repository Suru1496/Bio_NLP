<div align="center">

# 🧬 BioNLP Platform

### Intelligent Bioinformatics Workflow System

<p align="center">

<img src="images/banner.png" width="1000"/>

</p>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask)
![BioPython](https://img.shields.io/badge/BioPython-Sequence%20Analysis-green?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-LLM-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

</div>

---

## 📖 About the Project

BioNLP Platform is an interactive computational biology environment designed for biological sequence analysis and intelligent workflow execution through natural language interaction.

The platform combines modern web technologies, computational biology algorithms, and local language models to create a streamlined research-oriented bioinformatics interface.

It enables users to perform tasks such as:

- DNA to protein translation
- GC content analysis
- Multiple sequence alignment
- Evolutionary tree generation
- ORF prediction
- Biological query interpretation

through a unified and interactive dashboard.

---

## 🌟 Highlights

- Interactive bioinformatics workflows
- Intelligent query interpretation
- Local LLM integration using Ollama
- Real-time analysis visualization
- Modern glassmorphism interface
- Dynamic feature activation
- FASTA sequence handling
- Integrated statistics and logs panel

---

# 🧬 Supported Functionalities

| Module | Capability |
|---|---|
| Sequence Analysis | Translation, reverse complement, GC analysis |
| Alignment Engine | Pairwise and multiple alignment |
| Phylogenetics | Tree construction and visualization |
| NLP Layer | Intent detection and workflow selection |
| AI Assistant | Scientific query answering |
| Visualization | Interactive frontend rendering |

---

# 🖥️ Application Interface

<div align="center">

<img src="images/interface.png" width="950"/>

</div>

---

# 🏗️ System Design

```text
                    ┌─────────────────────┐
                    │     Frontend UI     │
                    │   Interactive Web   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Flask API      │
                    │     Backend Core    │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼

 ┌───────────────┐   ┌──────────────────┐   ┌────────────────┐
 │ Sequence Core │   │ NLP Interpretation│   │ Tree Generation│
 │ BioAlgorithms │   │ Ollama + Parsing │   │ Evolution Model│
 └───────────────┘   └──────────────────┘   └────────────────┘
```

---

# 📂 Project Layout

```text
BioNLP_Platform/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── results/
│
├── images/
│   ├── banner.png
│   ├── interface.png
│   └── architecture.png
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/BioNLP-Platform.git

cd BioNLP-Platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Dependencies

```text
flask
flask-cors
requests
biopython
```

---

# 🤖 Ollama Configuration

Download Ollama:

https://ollama.com

---

## Pull Model

```bash
ollama pull llama3.2
```

---

## Start Ollama

```bash
ollama serve
```

---

# ▶️ Running the Platform

```bash
python app.py
```

---

# 🌐 Access Application

```text
http://127.0.0.1:5000
```

---

# 🔬 Example Queries

### Sequence Analysis

```text
Translate this DNA sequence
```

```text
Calculate GC content
```

---

### Alignment

```text
Align these sequences
```

---

### Phylogenetics

```text
Build phylogenetic tree
```

---

### Biological Queries

```text
What is CRISPR?
```

---

# 📊 Dashboard Components

- Results Viewer
- Execution Logs
- Statistics Panel
- Interactive Workflow Cards
- Backend Status Monitor
- Sequence Input Engine
- AI Thinking Animation

---

# 🧠 Processing Pipeline

```text
Natural Language Query
          ↓
Intent Interpretation
          ↓
Workflow Selection
          ↓
Sequence Processing
          ↓
Bioinformatics Analysis
          ↓
Interactive Visualization
```

---

# 🛠️ Technology Stack

| Technology | Role |
|---|---|
| Flask | API Backend |
| HTML/CSS/JS | Frontend Interface |
| BioPython | Sequence Processing |
| Ollama | Local LLM Runtime |
| Particle.js | Interactive Animations |
| GitHub | Version Control |

---

# 🚀 Future Expansion

- Protein Structure Visualization
- BLAST Integration
- NCBI Connectivity
- Literature Mining
- PDF Report Generation
- Multi-omics Support
- Interactive Tree Visualization
- Workflow Persistence
- Cloud Deployment

---

# 📸 Screenshots

<div align="center">

<img src="images/dashboard.png" width="950"/>

</div>

---

# 🤝 Contributions

Contributions, feature requests, and workflow improvements are welcome.

Fork the repository and submit a pull request.

---

# 📜 License

MIT License

---

<div align="center">

### BioNLP Platform

Computational Biology • NLP • Interactive Bioinformatics

<img src="images/footer.png" width="850"/>

</div>
