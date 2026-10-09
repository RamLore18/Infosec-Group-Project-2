# Infosec Group Project 2: Salary Prediction Web App

## About the Project

This project is a machine learning-based web application developed using Python and Streamlit to predict estimated annual salaries based on selected personal and professional characteristics.

Users can provide their age, gender, education level, job title, and years of professional experience through an interactive interface. The application processes these inputs using a pre-trained machine learning model and displays an estimated annual salary in US dollars.

The project combines data exploration, model training, and web application development to demonstrate how machine learning can be applied to a real-world prediction problem.

## Features

* **Interactive web interface:** Allows users to enter their details using Streamlit widgets.
* **Personal and professional inputs:** Collects age, gender, education level, job title, and years of experience.
* **Machine learning predictions:** Uses a saved model to estimate annual salary.
* **Model training notebook:** Includes a Jupyter Notebook for exploring the dataset and developing the prediction model.
* **Instant results:** Displays the estimated salary when the user clicks the prediction button.

## Technologies Used

* **Python** – Programming language used for the project.
* **Pandas** – Data manipulation
* **Jupyter Notebook** – Used for data exploration and model development.
* **Streamlit** – Used to build the interactive web application.
* **Pickle** – Used to save and load the trained model.

## Repository Structure

```text
Infosec-Group-Project-2/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .github/
│   └── CODEOWNERS
│
├── .gitignore
├── LICENSE
├── model_training.ipynb
├── model.pkl
├── README.md
├── requirements.txt
├── salaryData.csv
├── streamlit_app.py
└── web_app.py
```
## How It Works

The project follows a machine learning workflow:

1. **Data preparation:** The salary dataset is explored and prepared for modelling.
2. **Model training:** The `model_training.ipynb` notebook contains the model development workflow.
3. **Model storage:** The trained model is saved as `model.pkl` for later use.
4. **User input:** The web application collects the user's selected characteristics.
5. **Input transformation:** The selected values are converted into numerical representations expected by the model.
6. **Salary prediction:** The trained model generates an estimated annual salary.
7. **Result display:** The application displays the prediction in US dollars.

## Input Features

The web application supports the following inputs:

| Feature             | Available options or range       |
| ------------------- | -------------------------------- |
| Gender              | Female, Male                     |
| Age                 | 21–55 years                      |
| Education level     | Bachelor's, Master's, PhD        |
| Job title           | Five predefined job titles       |
| Years of experience | 0–25 years, in increments of 0.5 |

The available job titles are Director of Marketing, Director of Operations, Senior Data Scientist, Senior Financial Analyst, and Senior Software Engineer.

## Getting Started

### Prerequisites

Ensure that you have Python and Git installed on your computer, along with access to the repository and its required files.

### 1. Clone the Repository

```bash
git clone https://github.com/RamLore18/Infosec-Group-Project-2.git
```

### 2. Navigate to the Project Directory

```bash
cd Infosec-Group-Project-2
```

### 3. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Web Application

To launch the salary prediction application, run:

```bash
streamlit run web_app.py
```

Streamlit will provide a local URL, typically `http://localhost:8501`, where you can interact with the application in your browser.

## Example Usage

1. Open the application in your browser.
2. Select your gender and age.
3. Choose your education level and job title.
4. Adjust the years-of-experience slider.
5. Click **Predict Salary**.
6. View the estimated annual salary displayed by the application.

## Group Members

This project was collaboratively developed by:

* **Mukisa Lore** (RamLore18) – [GitHub Profile](https://github.com/RamLore18)
* **Joy Gitau** (JWTRG) – [GitHub Profile](https://github.com/JWTRG)
* **Faith Jaher** (FaithJaher) – [GitHub Profile](https://github.com/FaithJaher)
* **Tristar Wanjohi** (Tristar204) – [GitHub Profile](https://github.com/Tristar204)
* **Natasha Wangare** (tasha-102) – [GitHub Profile](https://github.com/tasha-102)

## Acknowledgements

This project was completed as part of a collaborative group assignment exploring machine learning, data analysis, and the development of interactive web applications.
