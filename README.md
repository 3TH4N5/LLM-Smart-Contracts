# Smart Legal Contracts NLP Project

## Project Overview

This project aims to develop an NLP pipeline for converting natural language legal agreements into Smart Legal Contracts using the Accord Project framework. The system leverages advanced Natural Language Processing (NLP) techniques and Large Language Models (LLMs) to streamline contract creation and management.

## Features

- Contract classification and similarity search
- Named Entity Recognition (NER) for identifying contract elements
- Question Answering (QA) models for extracting contract data
- Integration with Accord Project's Cicero, Concerto, and Ergo frameworks
- Web interface for reviewing and editing extracted contract elements

## Project Structure

```
smart-legal-contracts-nlp/
│
├── .venv/                        # Python virtual environment
│
├── .vscode/                      # VS Code configuration
│   ├── settings.json             # Editor settings
│   └── tasks.json                # Custom tasks
│
├── data/
│   ├── raw/
│   │   ├── contracts/            # Raw legal contracts
│   │   │   └── cuad/             # CUAD dataset
│   │   └── templates/            # Accord Project templates
│   │       ├── acceptance-of-delivery/
│   │       ├── bill-of-lading/
│   │       ├── car-rental-tr/
│   │       └── ...               # Other templates
│   │
│   ├── processed/                # Processed data
│   ├── models/                   # Saved ML models
│   └── embeddings/               # Vector embeddings
│
├── notebooks/                    # Jupyter notebooks for exploration
│   ├── 01_data_exploration.ipynb
│   ├── 02_entity_extraction.ipynb
│   ├── 03_template_matching.ipynb
│   └── 04_cicero_generation.ipynb
│
├── src/
│   ├── preprocessing/            # Text preprocessing
│   │   ├── __init__.py
│   │   ├── text_cleaner.py       # Clean and normalize text
│   │   ├── pdf_extractor.py      # Extract text from PDFs
│   │   └── clause_segmenter.py   # Segment contracts into clauses
│   │
│   ├── models/                   # ML models
│   │   ├── __init__.py
│   │   ├── entity_extractor.py   # Extract legal entities
│   │   ├── template_matcher.py   # Match contracts to templates
│   │   └── data_extractor.py     # Extract Concerto data
│   │
│   ├── pipelines/                # Processing pipelines
│   │   ├── __init__.py
│   │   └── contract_processor.py # Main processing pipeline
│   │
│   └── utils/                    # Utilities
│       ├── __init__.py
│       ├── cicero_generator.py   # Generate Cicero markup
│       ├── concerto_generator.py # Generate Concerto models
│       └── evaluation.py         # Evaluation metrics
│
├── app/                          # Web application
│   ├── __init__.py
│   ├── main.py                   # FastAPI app
│   ├── routes.py                 # API endpoints
│   └── templates/                # HTML templates
│       └── index.html            # Main page
│
├── scripts/                      # Utility scripts
│   ├── download_models.py        # Download ML models
│   ├── download_cuad.py          # Download CUAD dataset
│   └── process_batch.py          # Process batch of contracts
│
├── tests/                        # Unit tests
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_models.py
│   └── test_pipelines.py
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── setup.py                      # Package installation
└── .gitignore                    # Git ignore file
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-legal-contracts-nlp.git
cd smart-legal-contracts-nlp
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Download required model files

```bash
python scripts/download_models.py
```

## Project Goals

- Develop an AI pipeline for converting natural language agreements into smart contracts
- Extend knowledge graphs and NLP techniques to improve clause classification
- Implement privacy-preserving techniques for data handling
- Establish a benchmark for smart legal contracts to foster industry collaboration
- Incorporate state-of-the-art AI models to optimize performance

## Accord Project Integration

This project works with the Accord Project's three main components:

- **Cicero**: Natural language template expression
- **Concerto**: Data modeling language
- **Ergo**: Domain-specific language for contract logic

## License

## Acknowledgments

- The Accord Project (https://accordproject.org)
- MSc Business Analytics program at University College London
