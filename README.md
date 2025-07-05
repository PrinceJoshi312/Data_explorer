
📊 Data Exploration & Visualization Dashboard
A powerful and interactive web-based tool built using Streamlit for quick data analysis. This app allows users to upload a CSV file and instantly explore it with summary statistics, charts, and visualizations — all without writing code.

🚀 Features
📁 Upload any CSV file (supports custom delimiters)

📌 View dataset shape, preview, column types, and null counts

📈 Interactive visualizations using Plotly and Seaborn:

Histogram

Scatter plot

Boxplot

Count bar chart

Correlation heatmap

🎛 Sidebar-based dynamic column selection

🧠 Auto-detects CSV delimiters (comma, semicolon, tab, etc.)

🧰 Tech Stack
Streamlit

Pandas

Plotly

Seaborn

Matplotlib

📂 Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/data-visualization-dashboard.git
cd data-visualization-dashboard
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Then open your browser and go to:
👉 http://localhost:8501

🧪 Sample Usage
Click on "Browse files" and upload a .csv file.

Use the sidebar to select chart types and columns.

View insights instantly on the main screen.

📸 Screenshot

Example with HR employee data

📌 Folder Structure
bash
Copy
Edit
data-visualization-dashboard/
│
├── app.py                # Streamlit application
├── requirements.txt      # Python dependencies
├── sample_data.csv       # (Optional) Example dataset
└── README.md             # This file
📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Prince Joshi
Feel free to connect with me on LinkedIn or GitHub.

