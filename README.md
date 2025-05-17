# MoonLight Energy Solutions - Solar Challenge Week 1

This repository contains the work for the Week 1 challenge set by 10Acadamy. As an Analytics Engineer, the project focuses on analyzing environmental data from solar farms to understand key trends, explore relationships between variables, and identify insights. The ultimate goal is to develop a data-driven strategy report recommending high-potential regions for future solar installations, thereby contributing to MoonLight Energy Solutions' operational efficiency and sustainability objectives.

---

## Development Environment Setup

To get the development environment running, follow these steps:

1.  **Clone the Repository:**
    Open your terminal or command prompt and clone the project from GitHub:
    ```bash
    git clone https://github.com/FasikaBelayneh/solar-challenge-week1.git
    ```
2.  **Navigate into the Project Directory:**
    ```bash
    cd solar-challenge-week1
    ```

3.  **Set up a Python Virtual Environment:**
    It is highly recommended to use a virtual environment to manage project dependencies. You can use either `venv` (built-in) or `conda`.

    * **Option A: Using `venv`**
        Create the virtual environment:
        ```bash
        python -m venv .venv
        ```
        Activate the virtual environment:
        * **On macOS and Linux:**
            ```bash
            source .venv/bin/activate
            ```
        * **On Windows (Command Prompt):**
            ```bash
            .venv\Scripts\activate.bat
            ```
        * **On Windows (PowerShell):**
            ```powershell
            .venv\Scripts\Activate.ps1
            ```

    * **Option B: Using `conda`**
        Create a new conda environment (you can specify a Python version, e.g., `python=3.9`):
        ```bash
        conda create -n solar-challenge python=3.9
        ```
        Activate the conda environment:
        ```bash
        conda activate solar-challenge
        ```

4.  **Install Dependencies:**
    With your virtual environment activated, install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```





