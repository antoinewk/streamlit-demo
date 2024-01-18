# RAG webapp


## Installation
With `conda`, default name is "rag_webapp":
```bash
conda env create -f requirements.yaml [--name ENV_NAME]
```
then, using `poetry`:
```bash
poetry install
```

## Usage
Run with:
```bash
poetry -m streamlit run app.py
```

## Information
This demo is based on the repository [streamlit-elements](https://github.com/okld/streamlit-elements), which wraps Material UI widgets (MUI).
As such, you have access to any icons from MUI, as seen on this [page](https://mui.com/material-ui/material-icons/).

## Extending
See this for wrapping/changing new components:
https://docs.streamlit.io/library/components/create