# YouTube Addiction Type Discovery System

An interactive data analysis dashboard built with Streamlit that helps users discover their YouTube viewing habits, categorizes their addiction type, and calculates an addiction risk score based on their usage behavior.

## 📌 Features

- **Personalized Insights**: Enter a user index to fetch specific usage patterns.
- **Addiction Clustering**: Categorizes users into distinct types:
  - 😌 Balanced / Casual Consumer
  - 🦉 Night Owl
  - 🍿 Weekend Binger
  - 📱 Shorts Scroller
- **Risk Score & Status**: Calculates a current addiction risk score out of 100 and classifies the user status (Normal User, Moderate Usage, High Addiction Risk).
- **Future Risk Prediction**: Estimates future addiction risk based on current behaviors like late-night usage and shorts consumption ratio.
- **Interactive Visualizations**:
  - A scatter plot mapping your position against other users.
  - An addiction risk meter (gauge chart).
- **Modern UI**: Custom dark theme with glassmorphism effects and colorful metrics.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and loading user datasets.
- **Plotly**: For rendering interactive graphs (scatter plots and gauge meters).
- **Jupyter Notebook**: For exploratory data analysis and generating the clustered dataset (`Utube.ipynb`).

## 📁 Project Structure

- `app.py`: The main Streamlit application script containing the UI and logic.
- `Utube.ipynb`: Jupyter notebook used for initial data analysis, feature engineering, and clustering models.
- `youtube_users_final.csv`: The final processed dataset containing user features and assigned clusters used by the Streamlit app.
- Other CSV files (`mini_project.csv`, `youtube_features.csv`, etc.): Intermediate or raw data files.

## 🚀 How to Run

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd Mini_Project
   ```

2. **Install the required dependencies**:
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**: Open your browser and go to `http://localhost:8501`.

## 📊 Data Overview

The application analyzes various user metrics such as:
- Late Night Ratio
- Shorts Ratio
- Binge Session Length
- Sessions per Day
- Weekend Ratio

These features are combined to determine the user's cluster and calculate their overall addiction risk score.

---
Developed by **vangavaishnavi-2005**.
