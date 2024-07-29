# 📚 PDF Processing Pipeline

Welcome to the **PDF Processing Pipeline** project! This tool helps you process PDF documents by splitting them into chapter-based chunks, extracting and summarizing text, feeding text to an LLM (Language Learning Model), extracting images, and generating a term weight dependent frequency glossary. Finally, it integrates all this into an interactive dashboard using Streamlit.

## 🚀 Features

- 📄 **PDF Splitting**: Splits PDF into chapter-based chunks.
- 📝 **Text Extraction and Reduction**: Extracts text and reduces it to key points.
- 🤖 **LLM Processing**: Feeds text to a Language Learning Model with defined output parameters.
- 🖼️ **Image Extraction**: Extracts images from PDF chapters.
- 📊 **Glossary Generation**: Creates a term weight dependent frequency glossary for each chapter.
- 🖥️ **Interactive Dashboard**: Allows users to interact with the processed PDF.

## 🛠️ Installation

First, clone the repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/pdf-processing-pipeline.git
cd pdf-processing-pipeline
```

Create and activate a virtual environment (optional but recommended):

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

## ⚙️ Usage

1. **Run the Streamlit App**:

   ```sh
   streamlit run streamlit_app.py
   ```

2. **Upload a PDF**: Choose a PDF file to upload via the Streamlit interface.

3. **Interact with the Dashboard**: View the extracted text, LLM outputs, images, and glossaries.

## 📁 Project Structure

```plaintext
📦 pdf-processing-pipeline
├── 📂 data
│   └── example.pdf                   # Example PDF for testing
├── 📂 images                         # Extracted images
├── 📂 notebooks                      # Jupyter notebooks for experimentation
├── 📂 scripts                        # Python scripts for various processing steps
│   ├── extract_text.py               # Text extraction script
│   ├── generate_glossary.py          # Glossary generation script
│   └── process_with_llm.py           # LLM processing script
├── 📄 requirements.txt               # List of dependencies
└── 📄 streamlit_app.py               # Streamlit app for interactive dashboard
```

## 📜 Detailed Workflow

### 1. Split PDF into Chapters

The PDF is split into chapter-based chunks using simple heuristics to detect chapter titles. This is done using the `fitz` (PyMuPDF) library.

### 2. Concurrent Processing

Chapters are processed concurrently using Python’s `concurrent.futures` for efficient processing. Each chapter undergoes:

- **Text Extraction and Reduction**: Extracts text from pages and reduces it.
- **LLM Processing**: Feeds the reduced text to an LLM (e.g., OpenAI’s GPT-3.5) for further processing.
- **Image Extraction**: Extracts images from the chapter’s pages.

### 3. Glossary Generation

A term weight dependent frequency glossary is generated for each chapter using NLP techniques.

### 4. Interactive Dashboard

All the processed data is displayed on a Streamlit dashboard, allowing users to interact with the PDF content holistically.

## 🙌 Acknowledgments

- [Streamlit](https://www.streamlit.io/) for the amazing dashboarding framework.
- [OpenAI](https://www.openai.com/) for the GPT-3.5 API.
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF processing.
- [NLTK](https://www.nltk.org/) for NLP tools.

## 👥 Contributors

- [Rishavs Bhagat](https://github.com/rbrox) - Project Maintainer

Feel free to contribute to this project by submitting issues or pull requests.

## 📬 Contact

For any inquiries, please contact [rishavsci@gmail.com](mailto:rishavsci@gmail.com).
