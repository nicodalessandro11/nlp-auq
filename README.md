# NLP Model with SQL Database Integration

This project implements a Natural Language Processing (NLP) model using Hugging Face and LangChain to interact with a SQL database through natural language queries.

## 🚀 Features

- Integration with Hugging Face models (DeepSeek Coder)
- SQL database connection through LangChain
- Natural language query processing
- Intelligent SQL agent for query execution

## 📋 Prerequisites

- Python 3.11+
- pip (Python package manager)
- Hugging Face account with access token
- SQL database (configured in Supabase)

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd nlp-model
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
make install
```

4. Configure environment variables:
   - Create `.env` file based on `.env.example`
   - Add your credentials:
     ```
     SUPABASE_URI=your_supabase_uri
     HF_TOKEN=your_huggingface_token
     ```

## 🎯 Usage

To run the model:

```bash
make run
```

To test a specific query, modify the `question` variable in `main.py`.

## 🛠️ Make Commands

- `make install`: Install all dependencies
- `make run`: Run the model
- `make clean`: Clean temporary files and cache
- `make setup`: Set up virtual environment and dependencies

## 📝 Notes

- Make sure you have the correct credentials in the `.env` file
- The model uses DeepSeek Coder 6.7B, which requires significant resources
- Queries should be in Spanish as the model is configured for this language

## 🤝 Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

## 📄 License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details. 