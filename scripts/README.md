#Solar Challenge Week 1
This repository contains the code and analysis for MoonLight Energy Solutions' solar investment strategy, focusing on solar radiation data analysis for Benin, Sierra Leone, and Togo.
Setup Instructions

##Clone the Repository:
https://github.com/FasikaBelayneh/solar-challenge-week1.git
cd solar-challenge-week1


##Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


##Install Dependencies:
pip install -r requirements.txt


##Folder Structure:

data/: Store cleaned CSV files (ignored in .gitignore).
notebooks/: Jupyter notebooks for EDA.
scripts/: Python scripts for data processing.
app/: Streamlit dashboard code (Task 4).


##Running the Code:

Place cleaned datasets in data/.
Run notebooks in notebooks/ for EDA.
Run Streamlit app: streamlit run app/main.py.



##Tasks

Task 1: Git setup, virtual environment, and CI pipeline.
Task 2: EDA on solar radiation data for each country.
Task 3: Cross-country comparison of solar potential.
Task 4:  Streamlit dashboard.

