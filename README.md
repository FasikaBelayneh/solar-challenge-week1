# Solar Analysis for MoonLight Energy Solutions
This repository contains the analysis of solar radiation data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar installations, aligning with MoonLight Energy Solutions' sustainability goals. The project leverages solar radiation measurement datasets from the World Bank-funded Solar Development in Sub-Saharan Africa project, covering data collected between 2021 and 2023. The analysis includes setting up a version-controlled environment, performing exploratory data analysis (EDA), comparing solar potential across countries, and optionally developing an interactive Streamlit dashboard for visualization.
Table of Contents

## Project Overview
Quick Start
Prerequisites
Setup
Data Acquisition
Analysis Steps
Running the Analysis
Folder Structure
Important Notes
Documentation
Contributing
License

## Project Overview
MoonLight Energy Solutions is committed to enhancing operational efficiency and sustainability through strategic solar investments. This project analyzes solar radiation measurement data from Benin, Sierra Leone, and Togo to identify regions with high solar potential, focusing on Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), ambient temperature, relative humidity, wind speed, and cleaning events.
The datasets, sourced from the Solar Development in Sub-Saharan Africa project, cover data collected between 2021 and 2023 at locations including Malanville and Parakou (Benin), Kenema and Bumbuna (Sierra Leone), and Dapaong and Davié (Togo). The analysis involves:

Establishing a version-controlled environment using Git and GitHub.
Cleaning and exploring datasets for each country to uncover trends and patterns.
Comparing solar potential across countries using robust statistical methods.
Optionally developing an interactive Streamlit dashboard to visualize insights.

This project aligns with MoonLight Energy Solutions' long-term sustainability goals by providing data-driven insights for strategic solar investments, leveraging regional initiatives like Sierra Leone’s rural electrification (Renewable Energy Services), Benin’s grid expansion (Benin Power Compact), and Togo’s solar-powered health centers (Solar Energy in Togo).
## Quick Start

1. Clone the repository:git clone https://github.com/yourusername/solar-challenge-week1.git


2. Set up a virtual environment:python -m venv venv


3. Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate


4. Install dependencies:pip install -r requirements.txt


5. Obtain datasets from ENERGYDATA.INFO and place them in the data/ directory.
6. Run EDA notebooks:
7. Open notebooks/<country>_eda.ipynb (e.g., benin_eda.ipynb) in Jupyter Notebook or Google Colab.


8. Run cross-country comparison:
Open notebooks/compare_countries.ipynb.


9. Run the Streamlit dashboard:streamlit run app/main.py



## Prerequisites

Python: Version 3.9 or later.
Git: For version control and repository cloning.
Jupyter Notebook or Google Colab for running analysis notebooks.
Streamlit: For running the optional dashboard.
Internet Access: To download datasets and dependencies.

## Setup
To set up the project, follow these detailed steps:

1. Clone the Repository:
git clone https://github.com/yourusername/solar-challenge-week1.git


2. Navigate to the Project Directory:
cd solar-challenge-week1


3. Create a Virtual Environment:
python -m venv venv


4. Activate the Virtual Environment:

On Windows:venv\Scripts\activate


On macOS/Linux:source venv/bin/activate




5. Install Dependencies:
pip install -r requirements.txt

The requirements.txt file includes standard data science libraries such as pandas, numpy, matplotlib, seaborn, scipy, and streamlit.

6. Verify CI Workflow:

The repository includes a GitHub Actions workflow (.github/workflows/ci.yml) that automates dependency installation and testing.
Ensure changes pass CI checks before merging pull requests.



Note: Commit changes regularly and use branches for different tasks (e.g., setup-task, eda-benin, compare-countries) to maintain a clean version control history.


The data/ directory is included in .gitignore to prevent committing sensitive or large files.
Check for missing values and outliers using df.isna().sum() and Z-score-based detection (|Z| > 3).
Standardize units (e.g., W/m² for irradiance) and align time zones for comparability.
Be aware of environmental factors like dust aerosols and cloud cover, which may affect measurements, especially in West Africa (Dust Conditions).

Analysis Steps
The analysis is structured into prioritized tasks to ensure a logical workflow:
1. Environment Setup

Configure the development environment as described in the Setup section.
Verify the GitHub Actions CI workflow by pushing changes to GitHub.

2. Data Cleaning and Exploratory Data Analysis (EDA)
For each country (Benin, Sierra Leone, Togo):

Create a branch: git checkout -b eda-<country> (e.g., eda-benin).
Create a Jupyter notebook: <country>_eda.ipynb.
Load the dataset: pd.read_csv('data/<country>.csv').
Perform EDA, including:
Summary Statistics and Missing Values: Compute mean, median, standard deviation, and check for missing values using df.isna().sum().
Outlier Detection and Cleaning: Use Z-scores (|Z| > 3) to identify and handle outliers in GHI, DNI, DHI, ModA, ModB, WS, and WSgust. Impute missing values with median imputation.
Time Series Analysis: Plot GHI, DNI, DHI, and Tamb against Timestamp to identify daily, monthly, or seasonal patterns.
Cleaning Impact Analysis: Compare average ModA and ModB pre- and post-cleaning events to inform maintenance schedules.
Correlation Analysis: Create a correlation heatmap for GHI, DNI, DHI, TModA, TModB, Tamb, RH, and WS using seaborn.heatmap.
Wind and Distribution Analysis: Generate wind rose plots for WS/WD using windrose and histograms for GHI and WS.
Temperature Analysis: Assess the impact of relative humidity on temperature and solar radiation using scatter plots (e.g., RH vs. Tamb).
Bubble Chart: Visualize GHI vs. Tamb with bubble size representing RH or BP.


Export cleaned data: df.to_csv('data/<country>_clean.csv', index=False).

3. Cross-Country Comparison

Create a branch: git checkout -b compare-countries.
Create a Jupyter notebook: compare_countries.ipynb.
Load cleaned datasets: pd.read_csv('data/<country>_clean.csv').
Perform the following:
Metric Comparison: Create boxplots for GHI, DNI, and DHI using seaborn.boxplot and compile a summary table with mean, median, and standard deviation.
Statistical Testing: Check data normality with Shapiro-Wilk test (scipy.stats.shapiro). If normal, use one-way ANOVA (scipy.stats.f_oneway); otherwise, use Kruskal-Wallis test (scipy.stats.kruskal) to assess significant differences in GHI.
Key Observations: Summarize findings, such as which country has the highest median GHI or greatest variability.
Visual Summary: (Optional) Create a bar chart ranking countries by average GHI.



4. Interactive Dashboard 

Create a branch: git checkout -b dashboard-dev.
Develop a Streamlit app in app/main.py with:
Interactive widgets (e.g., dropdown for country selection).
Visualizations (e.g., GHI boxplots, time series plots).
A table ranking regions by average GHI.


Deploy to Streamlit Community Cloud if desired.

Running the Analysis

EDA Notebooks: Open each notebook (e.g., benin_eda.ipynb) in Jupyter Notebook or Google Colab.
Cross-Country Comparison: Open notebooks/compare_countries.ipynb in Jupyter Notebook or Google Colab.
Streamlit Dashboard (Optional): Run the following command from the project root:streamlit run app/main.py



Folder Structure
The project is organized as follows:



Directory/File
Description



.vscode/
Configuration files for Visual Studio Code.


.github/workflows/ci.yml
GitHub Actions workflow for CI/CD.


.gitignore
Specifies files and directories to ignore in version control.


requirements.txt
Lists Python dependencies.


README.md
Project documentation (this file).


notebooks/
Contains Jupyter notebooks for EDA and comparison.


app/
Contains Streamlit app files (main.py, utils.py).


data/
Stores datasets and cleaned data (not committed).


scripts/
Placeholder for additional scripts.


tests/
Placeholder for unit tests.


Note: The data/ directory should not be committed to the repository to avoid sharing sensitive or large files.
Important Notes

Data Quality: Validate datasets for missing values and outliers. Use median imputation and Z-score-based detection (|Z| > 3) to ensure reliability.
Standardization: Standardize units (e.g., W/m²) and align time zones across datasets for accurate comparisons.
Environmental Factors: Dust aerosols and cloud cover may affect measurements, particularly in West Africa. Cross-reference with satellite data if possible (SARAH Dataset).
Statistical Rigor: Use Shapiro-Wilk for normality checks and robust tests (ANOVA or Kruskal-Wallis) for cross-country comparisons.
Version Control: Use branches for each task (e.g., eda-benin, compare-countries) to maintain a clean commit history.



## Contributing
Contributions are welcome! To contribute:

## Fork the repository.
Create a new branch: git checkout -b feature/your-feature.
Make changes and commit with descriptive messages.
Push to your fork: git push origin feature/your-feature.
Submit a pull request to the main repository.


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
