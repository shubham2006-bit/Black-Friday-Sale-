# Black-Friday-Sales-Analysis

# 🛍️ Black Friday Sales Data Analysis

An end-to-end exploratory data analysis (EDA) project on Black Friday retail sales data using **Python, Pandas, and Matplotlib**. The project covers data cleaning, outlier detection, statistical summary, and visualizations to uncover customer purchasing behavior.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Workflow](#-project-workflow)
- [Visualizations](#-visualizations)
- [Key Insights](#-key-insights)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Project Overview

Black Friday is one of the biggest shopping events of the year. This project analyzes transaction-level sales data to understand **who buys, what they buy, and how much they spend**. The insights can help retailers with targeted marketing, inventory planning, and customer segmentation.

---

## 🎯 Objectives

- Clean and preprocess the raw sales dataset
- Handle missing values and remove duplicate records
- Detect outliers in purchase amounts using the IQR method
- Analyze sales by gender, age group, city category, product category, and occupation
- Present findings through clear, easy-to-read visualizations

---

## 📂 Dataset

The dataset contains customer demographics and purchase details for Black Friday transactions.

| Column | Description |
|--------|-------------|
| `User_ID` | Unique customer ID |
| `Product_ID` | Unique product ID |
| `Gender` | Gender of the customer |
| `Age` | Age group of the customer |
| `Occupation` | Occupation code of the customer |
| `City_Category` | City category (A, B, C) |
| `Stay_In_Current_City_Years` | Years the customer has lived in the current city |
| `Marital_Status` | Marital status (0 = Single, 1 = Married) |
| `Product_Category_1` | Primary product category |
| `Product_Category_2` | Secondary product category (missing values filled with 0) |
| `Product_Category_3` | Tertiary product category (missing values filled with 0) |
| `Purchase` | Purchase amount (target/analysis variable) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Programming language |
| **Pandas** | Data loading, cleaning, and aggregation |
| **Matplotlib** | Data visualization |

---

## 🔄 Project Workflow

1. **Load Dataset**: read the CSV file and inspect shape and first records
2. **Check Data Types**: verify column types
3. **Missing Value Analysis**: identify nulls in each column
4. **Handle Missing Values**: fill `Product_Category_2` and `Product_Category_3` nulls with `0`
5. **Duplicate Removal**: detect and drop duplicate rows
6. **Outlier Detection**: apply the **IQR method** on the `Purchase` column
   - `Lower Limit = Q1 - 1.5 × IQR`
   - `Upper Limit = Q3 + 1.5 × IQR`
7. **Descriptive Statistics**: summary of the `Purchase` column
8. **Visualization**: six charts covering the key business questions
9. **Insights**: automatically print the top-performing segments

---

## 📊 Visualizations

The script generates the following charts:

| # | Chart | Purpose |
|---|-------|---------|
| 1 | Gender-wise Sales | Compare total spending between genders |
| 2 | Age-wise Sales | Identify the highest-spending age group |
| 3 | City Category-wise Sales | Compare sales across city categories |
| 4 | Top 10 Product Categories | Find the best-selling product categories |
| 5 | Purchase Distribution | Understand the spread of purchase amounts |
| 6 | Top 10 Occupations by Sales | Identify the top-spending occupations |

> 💡 **Tip:** Save your charts in an `images/` folder and display them here:
>
> ```markdown
> ![Gender-wise Sales](images/gender_sales.png)
> ```

---

## 🔍 Key Insights

The script automatically prints the following insights at the end of the analysis:

- Highest spending **gender**
- Highest spending **age group**
- Highest sales **city category**
- Highest sales **product category**
- **Average** and **maximum** purchase amount
- **Number of outliers** in purchase data

> 📝 *Add your actual results here after running the script, for example:*
> - Highest spending gender: `...`
> - Highest spending age group: `...`
> - Top city category: `...`

---

## 📁 Project Structure

```
Black-Friday-Sales-Analysis/
│
├── BlackFriday.csv          # Dataset
├── analysis.py              # Main analysis script
├── images/                  # Saved charts (optional)
└── README.md                # Project documentation
```

---

## ▶️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/shubham2006-bit/Black-Friday-Sale-.git
cd Black-Friday-Sale-
```

**2. Install the required libraries**

```bash
pip install pandas matplotlib
```

**3. Run the script**

```bash
python analysis.py
```

> ⚠️ Make sure the CSV file name in the script matches your actual file name and that the file is in the same folder as the script.

---

## 🚀 Future Improvements

- Add correlation heatmap and advanced statistical analysis
- Build an interactive dashboard using Power BI, Tableau, or Streamlit
- Use Seaborn / Plotly for more interactive charts
- Apply machine learning to predict purchase amount
- Perform customer segmentation using clustering

---

## 👤 Author

**Shubham**

- GitHub: [@shubham2006-bit](https://github.com/shubham2006-bit)

---

⭐ If you found this project helpful, consider giving it a star!