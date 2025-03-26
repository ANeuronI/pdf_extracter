# PDF Transaction Extractor

This project provides a Python script to extract transaction details from PDF files and save them into an Excel format. It utilizes the `pdfminer` library for PDF text extraction and `pandas` for data manipulation and saving to Excel.

## Features

- Extracts raw text from PDF files.
- Parses transaction details including date, description, amount, and type (Debit/Credit) using regular expression.
- Saves the structured transaction data into an Excel file.

## Requirements

- Python 3.x
- `pdfminer.six`
- `pandas`

You can install the required libraries using pip:

```bash
pip install pdfminer.six pandas
