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
│   │   ├── contracts/           # Raw legal contracts
│   │   │   ├── cuad/            # CUAD dataset
│   │   │   ├── standardized/    # Standardized contracts
│   │   │      ├── edgar/        # SEC filings
│   │   │      ├── onenda/       # OneNDA documents
│   │   │      └── safe/         # SAFE agreements
│   │   │
│   │   │
│   │   └── templates/            # Accord Project templates
│   │       ├── acceptance-of-delivery/
│   │       ├── bill-of-lading/
│   │       ├── car-rental-tr/
│   │       └── ...               # Other templates
│   │
│   ├── processed/                # Processed data
│   │   ├── extracted_text/       # Plain text from docs
│   │   ├── cleaned_text/         # Cleaned text
│   │   ├── clauses/              # Extracted clauses
│   │   └── templates/            # Generated templates
│   │
│   ├── models/                   # Saved ML models
│   │   ├── ner/                  # Named entity recognition
│   │   ├── classification/       # Clause classification
│   │   └── generation/           # Template generation
│   │
│   └── embeddings/               # Vector embeddings
│       ├── clause_embeddings/    # Clause-level embeddings
│       └── document_embeddings/  # Document-level embeddings
│
├── notebooks/                    # Jupyter notebooks for exploration
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing_evaluation.ipynb
│   ├── 03_entity_extraction.ipynb
│   ├── 04_template_matching.ipynb
│   └── 05_cicero_generation.ipynb
│
├── src/
│   ├── preprocessing/            # Text preprocessing
│   │   ├── __init__.py
│   │   ├── document_processor.py # Main orchestration
│   │   ├── pdf_extractor.py      # Extract text from PDFs
│   │   ├── docx_extractor.py     # Extract text from DOCX
│   │   ├── text_cleaner.py       # Clean and normalize text
│   │   ├── clause_segmenter.py   # Segment contracts into clauses
│   │   └── variable_identifier.py # Identify variables in text
│   │
│   ├── models/                   # ML models
│   │   ├── __init__.py
│   │   ├── entity_extractor.py   # Extract legal entities
│   │   ├── template_matcher.py   # Match contracts to templates
│   │   ├── data_model_extractor.py # Extract Concerto data
│   │   ├── clause_classifier.py  # Classify clauses by type
│   │   ├── cicero_generator.py   # Generate CiceroMark
│   │   ├── concerto_generator.py # Generate Concerto models
│   │   ├── ergo_generator.py     # Generate Ergo logic
│   │   └── state_machine_generator.py # Generate FSMs
│   │
│   ├── pipelines/                # Processing pipelines
│   │   ├── __init__.py
│   │   ├── contract_processor.py # Main processing pipeline
│   │   ├── template_generation_pipeline.py
│   │   ├── instance_processing_pipeline.py
│   │   └── model_generation_pipeline.py
│   │
│   ├── utils/                    # Utilities
│   │   ├── __init__.py
│   │   ├── file_utils.py         # File operations
│   │   ├── nlp_utils.py          # NLP helpers
│   │   └── evaluation.py         # Evaluation metrics
│   │
│   └── config/                   # Configuration
│       ├── __init__.py
│       ├── settings.py           # Global settings
│       └── model_config.py       # Model configurations
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
│   ├── preprocessing/            # Tests for preprocessing
│   │   ├── test_pdf_extractor.py
│   │   ├── test_docx_extractor.py
│   │   ├── test_text_cleaner.py
│   │   ├── test_clause_segmenter.py
│   │   └── test_variable_identifier.py
│   │
│   ├── models/                   # Tests for models
│   │   ├── test_entity_extractor.py
│   │   └── test_template_matcher.py
│   │
│   └── pipelines/                # Tests for pipelines
│       └── test_contract_processor.py
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
