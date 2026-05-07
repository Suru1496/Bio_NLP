# 🧬 BioNLP Platform

AI-Powered Bioinformatics Intelligence System using Flask, Ollama, NLP, and Bioinformatics Workflows.

---

# 🚀 Overview

BioNLP Platform is an interactive AI-driven bioinformatics web application that allows users to perform biological sequence analysis using natural language queries.

The platform combines:

- 🧠 Natural Language Processing (NLP)
- 🤖 Local Large Language Models (Ollama)
- 🧬 Bioinformatics Algorithms
- 🌳 Phylogenetic Analysis
- 🔗 Sequence Alignment
- 📊 GC Content Analysis
- 🧪 ORF Detection

Users can interact with the system using simple human language such as:

```text
Translate this DNA sequence
Calculate GC content
Build phylogenetic tree
Align these sequences
What is CRISPR?
```

---

# ✨ Features

## 🧬 Sequence Analysis
- DNA → Protein Translation
- Reverse Complement
- GC Content Calculation
- ORF Detection

## 🔗 Alignment
- Pairwise Alignment
- Multiple Sequence Alignment

## 🌳 Phylogenetics
- Phylogenetic Tree Generation
- Evolutionary Analysis

## 💬 AI Assistant
- Bioinformatics Question Answering
- Scientific Explanations
- NLP-based Intent Detection

## 📂 Interactive UI
- Modern futuristic design
- Glassmorphism UI
- Animated particles
- Interactive workflow cards
- Drag-and-drop FASTA upload

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────┐
                    │    Frontend      │
                    │   index.html     │
                    └────────┬─────────┘
                             │
                             │ API Calls
                             ▼
                    ┌──────────────────┐
                    │     Flask API    │
                    │      app.py      │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼

 ┌─────────────┐    ┌────────────────┐   ┌──────────────┐
 │ Bioinformatics│   │ NLP + Ollama  │   │ Tree Builder │
 │ Algorithms    │   │ Intent Parsing│   │ Alignment    │
 └─────────────┘    └────────────────┘   └──────────────┘
```

---

# 📁 Project Structure

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
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/BioNLP-Platform.git

cd BioNLP-Platform
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a file named:

```text
requirements.txt
```

Content:

```text
flask
flask-cors
requests
biopython
```

---

# 🤖 Install Ollama

Download Ollama:

👉 https://ollama.com

---

## Pull LLM Model

```bash
ollama pull llama3.2
```

---

## Start Ollama

```bash
ollama serve
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```text
http://127.0.0.1:5000
```

---

# 🧠 Example Queries

## Sequence Analysis

```text
Translate this DNA sequence
```

```text
Calculate GC content
```

## Alignment

```text
Align these sequences
```

## Phylogenetics

```text
Build phylogenetic tree
```

## AI Assistant

```text
What is CRISPR?
```

---

# 🔬 Supported Workflows

| Workflow | Description |
|---|---|
| GC Content | Calculates GC percentage |
| Translation | DNA → Protein |
| Alignment | Multiple sequence alignment |
| Phylogenetics | Tree generation |
| ORF Detection | Open Reading Frame prediction |
| AI Chat | Bioinformatics assistant |

---

# 🖥️ API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Frontend UI |
| `/api/query` | POST | Main analysis endpoint |
| `/api/health` | GET | Backend health status |

---

# 📊 Frontend Features

- Interactive Feature Cards
- Results / Logs / Statistics Tabs
- AI Thinking Animation
- Animated Particle Background
- Glassmorphism Design
- Dynamic Workflow Activation
- Real-Time Status Monitoring

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Flask | Backend API |
| HTML/CSS/JS | Frontend |
| Ollama | Local LLM |
| BioPython | Bioinformatics |
| Particle.js | Animated Background |
| Flask-CORS | Cross-Origin Support |

---

# 🚀 Future Improvements

- Protein Structure Visualization
- BLAST Integration
- NCBI API Integration
- PubMed Search
- PDF Report Generation
- User Authentication
- Database Integration
- Sequence Logo Generation
- 3D Phylogenetic Trees

---

# 🧪 Screenshots

(Add screenshots here later)

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and create a pull request.

---

# 📜 License

MIT License

---

# 👩‍🔬 Author

Developed for AI-driven Bioinformatics Research and NLP-based Biological Data Analysis.

---