"""
Main document processing orchestrator for legal contract preprocessing.
"""

import os
import logging
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
import pandas as pd

from .pdf_extractor import PDFExtractor
from .docx_extractor import DOCXExtractor
from .text_cleaner import TextCleaner
from .clause_segmenter import ClauseSegmenter
from .variable_identifier import VariableIdentifier

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """
    Orchestrates the preprocessing of legal documents.

    This class manages the full preprocessing pipeline from raw document
    extraction to structured output ready for NLP model input.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the document processor with configuration settings.

        Args:
            config: Configuration dictionary with preprocessing settings
        """
        self.config = config or {}

        # Initialize extractors
        self.pdf_extractor = PDFExtractor(self.config.get("pdf_extractor", {}))
        self.docx_extractor = DOCXExtractor(self.config.get("docx_extractor", {}))

        # Initialize processors
        self.text_cleaner = TextCleaner(self.config.get("text_cleaner", {}))
        self.clause_segmenter = ClauseSegmenter(self.config.get("clause_segmenter", {}))
        self.variable_identifier = VariableIdentifier(
            self.config.get("variable_identifier", {})
        )

        logger.info("Document processor initialized")

    def process_document(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Process a single document through the entire preprocessing pipeline.

        Args:
            file_path: Path to the document file

        Returns:
            Dictionary containing processed document data
        """
        file_path = Path(file_path)
        logger.info(f"Processing document: {file_path}")

        # Extract text based on file type
        if file_path.suffix.lower() == ".pdf":
            raw_text, metadata = self.pdf_extractor.extract(file_path)
        elif file_path.suffix.lower() in [".docx", ".doc"]:
            raw_text, metadata = self.docx_extractor.extract(file_path)
        elif file_path.suffix.lower() in [".txt", ".md"]:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()
            metadata = {"filename": file_path.name}
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")

        # Clean text
        cleaned_text = self.text_cleaner.clean(raw_text)

        # Segment into clauses
        clauses = self.clause_segmenter.segment(cleaned_text)

        # Identify variables
        clauses_with_variables = [
            self.variable_identifier.identify(clause) for clause in clauses
        ]

        # Assemble processed document
        processed_document = {
            "metadata": metadata,
            "raw_text": raw_text,
            "cleaned_text": cleaned_text,
            "clauses": clauses,
            "clauses_with_variables": clauses_with_variables,
        }

        logger.info(f"Completed processing document: {file_path}")
        return processed_document

    def process_directory(
        self,
        directory_path: Union[str, Path],
        output_path: Optional[Union[str, Path]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Process all supported documents in a directory.

        Args:
            directory_path: Path to directory containing documents
            output_path: Optional path to save processed results

        Returns:
            List of processed document dictionaries
        """
        directory_path = Path(directory_path)
        logger.info(f"Processing documents in directory: {directory_path}")

        # Get all supported files
        supported_extensions = [".pdf", ".docx", ".doc", ".txt", ".md"]
        files = [
            f
            for f in directory_path.glob("**/*")
            if f.is_file() and f.suffix.lower() in supported_extensions
        ]

        # Process each file
        processed_documents = []
        for file_path in files:
            try:
                processed_doc = self.process_document(file_path)
                processed_documents.append(processed_doc)
            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")

        # Save results if output path provided
        if output_path:
            output_path = Path(output_path)
            output_path.mkdir(parents=True, exist_ok=True)

            # Save as JSON
            import json

            for i, doc in enumerate(processed_documents):
                # Convert to serializable format
                serializable_doc = {
                    "metadata": doc["metadata"],
                    "raw_text": doc["raw_text"],
                    "cleaned_text": doc["cleaned_text"],
                    "clauses": [c for c in doc["clauses"]],
                    "clauses_with_variables": [
                        {
                            "text": c["text"],
                            "variables": [
                                {
                                    "name": v["name"],
                                    "value": v["value"],
                                    "type": v["type"],
                                }
                                for v in c.get("variables", [])
                            ],
                        }
                        for c in doc["clauses_with_variables"]
                    ],
                }

                output_file = output_path / f"processed_doc_{i}.json"
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(serializable_doc, f, indent=2)

        logger.info(f"Processed {len(processed_documents)} documents")
        return processed_documents
