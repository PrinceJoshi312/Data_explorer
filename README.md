# 📊 Data Explorer Dashboard

A simple yet powerful Streamlit-based app to help analysts, data scientists, students, and business users explore any dataset without writing code.

Just upload a CSV file, and this app instantly gives you access to summaries, visual insights, and interactive charts — helping you understand patterns, spot outliers, and draw conclusions from your data.

---

## 💡 What It Does

* 📁 Upload any CSV file (auto-detects delimiter: `,`, `;`, `|`, `\t`)
* 🧾 Instantly view:

  * Shape, column names, and data types
  * Missing value counts
  * Descriptive statistics (mean, median, std, etc.)
* 📈 Choose from multiple visualizations:

  * Histogram
  * Scatter Plot
  * Box Plot
  * Count Plot (for categorical data)
  * Correlation Heatmap

---

## ⚙️ How It Works

* Built with **Streamlit** for an interactive web experience
* Uses **Pandas** for efficient data manipulation
* **Plotly** and **Seaborn** for dynamic, professional-grade visualizations
* Auto-handles messy CSV formats and malformed input using Python’s `csv.Sniffer`

---

## 🚀 Run It Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/PrinceJoshi312/Data_explorer.git
   cd Data_explorer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run app.py
   ```

Then open your browser and go to `http://localhost:8501`

---

## 👥 Who This Is For

* Data analysts and data scientists doing quick EDA
* Students working on ML projects
* Business analysts needing visual insights
* Anyone who wants to explore data **without writing code**

---

## 🙌 Contribute

Feel free to fork this repo, improve features, or add new visualizations like:

* Time series plots
* PDF or Excel export
* Machine learning model integration
* Dataset cleaner/imputer

Pull requests are welcome!
