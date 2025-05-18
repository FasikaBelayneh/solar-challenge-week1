##Solar Analysis for MoonLight Energy Solutions
This repository contains the analysis of solar radiation data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar installations, aligning with MoonLight Energy Solutions' sustainability goals.
Table of Contents

Project Overview
Setup
Data Acquisition
Analysis Steps
Running the Analysis
Folder Structure
Contributing
License

Project Overview
MoonLight Energy Solutions aims to enhance operational efficiency and sustainability through targeted solar investments. This project analyzes solar radiation measurement data from Benin, Sierra Leone, and Togo to identify regions with high solar potential, focusing on Global Horizontal Irradiance (GHI) and other meteorological factors such as Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), ambient temperature, relative humidity, wind speed, and cleaning events.
The datasets are sourced from the World Bank-funded Solar Development in Sub-Saharan Africa project, covering data collected between 2021 and 2023 at locations including Malanville and Parakou (Benin), Kenema and Bumbuna (Sierra Leone), and Dapaong and Davié (Togo).
The analysis involves setting up a version-controlled environment, performing exploratory data analysis (EDA), comparing solar potential across countries, and optionally developing an interactive Streamlit dashboard to visualize insights.
Setup
To set up the project, follow these steps:

Clone the Repository:
[\[git clone https://github.com/yourusername/solar-challenge-week1.git\](https://github.com/FasikaBelayneh/solar-challenge-week1.git)](https://github.com/FasikaBelayneh/solar-challenge-week1.git)


Navigate to the Project Directory:
cd solar-challenge-week1


Create a Virtual Environment:
python -m venv venv


Activate the Virtual Environment:

On Windows:venv\Scripts\activate


On macOS/Linux:source venv/bin/activate




Install Dependencies:
pip install -r requirements.txt


Verify CI Workflow:

This repository includes a GitHub Actions workflow (.github/workflows/ci.yml) that automates dependency installation and testing.
Ensure your changes pass the CI checks before merging pull requests.



Note: Commit changes regularly and use branches for different tasks as outlined in the analysis steps to maintain a clean version control history.
Data Acquisition
The solar radiation measurement datasets for Benin, Sierra Leone, and Togo are available from ENERGYDATA.INFO. If direct download is not possible, contact energydata@worldbankgroup.org to request access.
Once obtained, place the datasets in the data/ directory with appropriate names, e.g., benin.csv, sierra_leone.csv, togo.csv.
Important: The data/ directory is included in .gitignore to prevent committing sensitive or large files to the repository.
Analysis Steps
The analysis is structured into the following tasks:
1. Environment Setup

Follow the setup instructions above to configure the development environment.
Verify that the GitHub Actions CI workflow runs successfully by pushing changes to GitHub.

2. Data Cleaning and Exploratory Data Analysis (EDA)
For each country (Benin, Sierra Leone, Togo), perform the following:

Create a branch: git checkout -b eda-<country> (e.g., eda-benin)
Create a Jupyter notebook: <country>_eda.ipynb
Load the dataset: pd.read_csv('data/<country>.csv')
Perform EDA, including:
Summary Statistics and Missing Values: Compute mean, median, standard deviation, and check for missing values using df.isna().sum().
Outlier Detection and Cleaning: Use Z-scores (|Z| > 3) to identify and handle outliers in GHI, DNI, DHI, ModA, ModB, WS, and WSgust.
Time Series Analysis: Plot GHI, DNI, DHI, and Tamb against Timestamp to identify daily, monthly, or seasonal patterns.
Cleaning Impact Analysis: Compare average ModA and ModB pre- and post-cleaning events.
Correlation and Relationship Analysis: Create a correlation heatmap and scatter plots (e.g., WS vs. GHI, RH vs. Tamb).
Wind and Distribution Analysis: Generate wind rose plots for WS/WD and histograms for GHI and WS.
Temperature Analysis: Assess the impact of relative humidity on temperature and solar radiation.
Bubble Chart: Visualize GHI vs. Tamb with bubble size representing RH or BP.


Export cleaned data: df.to_csv('data/<country>_clean.csv', index=False)

3. Cross-Country Comparison

Create a branch: git checkout -b compare-countries
Create a Jupyter notebook: compare_countries.ipynb
Load cleaned datasets: pd.read_csv('data/<country>_clean.csv')
Perform the following:
Metric Comparison: Create boxplots for GHI, DNI, and DHI, and compile a summary table with mean, median, and standard deviation.
Statistical Testing: Conduct a one-way ANOVA to assess significant differences in GHI across countries.
Key Observations: Summarize findings, such as which country has the highest median GHI or greatest variability.
Visual Summary: (Optional) Create a bar chart ranking countries by average GHI.



4. Interactive Dashboard (Optional)

Create a branch: git checkout -b dashboard-dev
Develop a Streamlit app in app/main.py with:
Interactive widgets (e.g., dropdown for country selection)
Visualizations (e.g., GHI boxplots, time series plots)
A table ranking regions by average GHI


Deploy to Streamlit Community Cloud if desired.

Running the Analysis

EDA Notebooks: Open each notebook (e.g., benin_eda.ipynb) in Jupyter Notebook or Google Colab.
Cross-Country Comparison: Open notebooks/compare_countries.ipynb in Jupyter Notebook or Google Colab.
Streamlit Dashboard (Optional): Run the following command from the project root:streamlit run app/main.py



Folder Structure
The project is organized as follows:
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── data/
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   └── togo_clean.csv
├── scripts/
│   └── __init__.py
└── tests/
    └── __init__.py

Note: The data/ directory should not be committed to the repository to avoid sharing sensitive or large files.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your changes: git checkout -b feature/your-feature
Make changes and commit with descriptive messages.
Push to your fork: git push origin feature/your-feature
Submit a pull request to the main repository.

Ensure that your code follows PEP 8 standards and includes appropriate documentation.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
