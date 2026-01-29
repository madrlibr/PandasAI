# PandasAI
An intelligent data assistant that translates Indonesian natural language queries into Pandas operations. This version replaces the previous keyword-matching logic with a Machine Learning model for improved intent classification.

## Requirements
    Python 3.x
    Pandas
    Streamlit
    Scikit-learn


## Footage
<img width="1555" height="1009" alt="Screenshot (1182)" src="https://github.com/user-attachments/assets/2bf87720-ed09-45f9-ab76-e86ed7438b76" />

## Installation

1. Clone this repository:
```bash
git clone https://github.com/madrlibr/PandasAI.git

```


2. Navigate to the project directory:
```bash
cd PandasAI

```


3. Install the required dependencies:
```bash
pip install -r requirements.txt

```



## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py

```

2. Upload your CSV file through the sidebar or use the dummy dataset i provided.
3. Type commands in the chat input using Indonesian, such as:
* "tampilkan seluruh data" (show all data)
* "Hapus baris dengan nilai NaN" (delete row with NaN value)
* "deskripsi data" (get statistical description)


## Versions
This repository contains two versions of the chatbot:
1. **Main Branch (Recommended)**: Powered by a Machine Learning model for better intent recognition.
2. **Rule-Based Branch**: The original version using string-matching logic. You can access it by switching to the `rule-based` branch.


## NOTICE
This project use dataset with Apache 2.0 license for the dummy dataset

dataset source: https://www.kaggle.com/datasets/neurocipher/student-performance


## LICENSE
This project is licensed under the MIT LICENSE.
