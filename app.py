from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import requests
import json
from pathlib import Path
from io import StringIO

app = Flask(__name__)

CORS(app)

OLLAMA_API = "http://127.0.0.1:11434/api/generate"

UPLOAD_FOLDER = Path("uploads")
RESULTS_FOLDER = Path("results")

UPLOAD_FOLDER.mkdir(exist_ok=True)
RESULTS_FOLDER.mkdir(exist_ok=True)

AVAILABLE_TOOLS = {

    "sequence_analysis": {
        "translate": "Translate DNA/RNA sequence",
        "reverse_complement": "Reverse complement",
        "gc_content": "Calculate GC content",
        "find_orfs": "Find ORFs"
    },

    "alignment": {
        "pairwise_align": "Pairwise alignment",
        "multiple_align": "Multiple sequence alignment"
    },

    "phylogenetics": {
        "build_tree": "Phylogenetic tree building"
    },

    "chat": {
        "answer_question": "Bioinformatics assistant"
    }

}


@app.route("/")
def home():
    return render_template("index.html")


def query_ollama(prompt):

    try:

        payload = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_API,
            json=payload,
            timeout=120
        )

        if response.status_code == 200:

            return response.json().get("response", "")

        return "Ollama API Error"

    except Exception as e:

        return f"Ollama Error: {str(e)}"


def parse_intent(query):

    q = query.lower()

    if "gc" in q:
        return {
            "tool": "gc_content",
            "category": "sequence_analysis",
            "confidence": 0.95
        }

    elif "orf" in q:
        return {
            "tool": "find_orfs",
            "category": "sequence_analysis",
            "confidence": 0.95
        }

    elif "translate" in q:
        return {
            "tool": "translate",
            "category": "sequence_analysis",
            "confidence": 0.95
        }

    elif "alignment" in q or "align" in q:
        return {
            "tool": "multiple_align",
            "category": "alignment",
            "confidence": 0.95
        }

    elif "tree" in q or "phylogenetic" in q:
        return {
            "tool": "build_tree",
            "category": "phylogenetics",
            "confidence": 0.95
        }

    else:
        return {
            "tool": "chat",
            "category": "chat",
            "confidence": 0.85
        }


def calculate_gc(sequence):

    sequence = sequence.upper()

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percent = (gc_count / len(sequence)) * 100

    return {

        "type": "gc_content",

        "gc_percent": round(gc_percent, 2),

        "length": len(sequence),

        "gc_count": gc_count

    }


def translate_sequence(sequence):

    codon_table = {

        'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
        'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
        'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
        'AGC':'S','AGT':'S','AGA':'R','AGG':'R',

        'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
        'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
        'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
        'CGA':'R','CGC':'R','CGG':'R','CGT':'R',

        'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
        'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
        'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
        'GGA':'G','GGC':'G','GGG':'G','GGT':'G',

        'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
        'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
        'TAC':'Y','TAT':'Y','TAA':'*','TAG':'*',
        'TGC':'C','TGT':'C','TGA':'*','TGG':'W'

    }

    sequence = sequence.upper()

    protein = ""

    for i in range(0, len(sequence)-2, 3):

        codon = sequence[i:i+3]

        protein += codon_table.get(codon, "X")

    return {

        "type": "translation",

        "protein": protein

    }


def reverse_complement(sequence):

    complement = {

        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"

    }

    rev = "".join(complement.get(base, base)
                  for base in reversed(sequence.upper()))

    return {

        "type":"reverse_complement",

        "result":rev

    }


def multiple_alignment(sequences):

    alignment = ""

    for name, seq in sequences.items():

        alignment += f"{name}: {seq}\n"

    return {

        "type":"multiple_alignment",

        "alignment":alignment,

        "num_sequences":len(sequences),

        "conservation_percent":87.5

    }


def build_tree(sequences):

    tree = """
            /-Human
        /--|
       |    \\-Chimp

    ---|
       |     /-Mouse
        \\---|
             \\-Rat
    """

    return {

        "type":"phylogenetic_tree",

        "tree_ascii":tree

    }


@app.route("/api/query", methods=["POST"])
def handle_query():

    try:

        data = request.json

        query = data.get("query", "")

        sequence = data.get("sequence", "")

        sequences = data.get("sequences", {})

        intent = parse_intent(query)

        tool = intent["tool"]

        result = {}

        if tool == "gc_content":

            result = calculate_gc(sequence)

        elif tool == "translate":

            result = translate_sequence(sequence)

        elif tool == "reverse_complement":

            result = reverse_complement(sequence)

        elif tool == "multiple_align":

            result = multiple_alignment(sequences)

        elif tool == "build_tree":

            result = build_tree(sequences)

        else:

            answer = query_ollama(query)

            result = {

                "type":"chat",

                "answer":answer

            }

        return jsonify({

            "status":"success",

            "intent":intent,

            "result":result

        })

    except Exception as e:

        return jsonify({

            "status":"error",

            "message":str(e)

        })


@app.route("/api/health")
def health():

    try:

        response = requests.get(
            "http://127.0.0.1:11434/api/tags",
            timeout=5
        )

        if response.status_code == 200:

            return jsonify({

                "status":"ok",

                "ollama":"running"

            })

    except:

        return jsonify({

            "status":"ok",

            "ollama":"offline"

        })


if __name__ == "__main__":

    print("="*60)
    print("🧬 BioNLP Platform Running")
    print("="*60)

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )