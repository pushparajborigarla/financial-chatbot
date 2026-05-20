from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# ------------------------------------------------
# Load Financial Dataset
# ------------------------------------------------

file_path = r"C:\Users\LENOVO\Downloads\financial_analysis_2023_2025.csv"

df = pd.read_csv(file_path)

# Clean numeric columns
numeric_cols = [
    'Total Revenue',
    'Net Income',
    'Total Assets',
    'Total Liabilities',
    'Cash Flow'
]

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col])

# ------------------------------------------------
# Chatbot Logic
# ------------------------------------------------

def chatbot_response(query):

    query = query.lower()

    # Query 1
    if "total revenue of apple" in query:

        revenue = df[
            (df['Company'] == 'Apple') &
            (df['Year'] == 2025)
        ]['Total Revenue'].values[0]

        return (
            f"Apple's total revenue in 2025 was "
            f"{revenue:,} million USD, the highest "
            f"among the three companies."
        )

    # Query 2
    elif "microsoft net income changed" in query:

        start_income = df[
            (df['Company'] == 'Microsoft') &
            (df['Year'] == 2023)
        ]['Net Income'].values[0]

        end_income = df[
            (df['Company'] == 'Microsoft') &
            (df['Year'] == 2025)
        ]['Net Income'].values[0]

        return (
            f"Microsoft's net income increased from "
            f"{start_income:,} million USD in 2023 "
            f"to {end_income:,} million USD in 2025."
        )

    # Query 3
    elif "tesla operating cash flow" in query:

        cashflow = df[
            (df['Company'] == 'Tesla') &
            (df['Year'] == 2025)
        ]['Cash Flow'].values[0]

        return (
            f"Tesla's operating cash flow in 2025 "
            f"was {cashflow:,} million USD."
        )

    # Query 4
    elif "strongest financial performance" in query:

        return (
            "Apple demonstrated the strongest overall "
            "financial performance with the highest "
            "revenue and net income during 2023–2025."
        )

    # Query 5
    elif "microsoft financial growth" in query:

        return (
            "Microsoft showed strong and consistent "
            "growth in revenue, profitability, and "
            "operating cash flow from 2023 to 2025."
        )

    # Query 6
    elif "highest revenue" in query:

        return (
            "Apple had the highest revenue in 2025 "
            "with 416,161 million USD."
        )

    # Query 7
    elif "best growth" in query:

        return (
            "Microsoft showed the strongest and most "
            "consistent financial growth during the "
            "analysis period."
        )

    # Help Section
    elif "help" in query:

        return """
Available Queries:
<ul>
<li>1. What is the total revenue of Apple in 2025?</li>
<li>2. How has Microsoft net income changed from 2023 to 2025?</li>
<li>3. What is Tesla operating cash flow in 2025?</li>
<li>4. Which company demonstrated the strongest financial performance overall?</li>
<li>5. How did Microsoft perform in terms of financial growth?</li>
<li>6. Which company has the highest revenue?</li>
<li>7. Which company showed the best growth?</li>
</ul>
Type 'exit' to stop the chatbot.
"""

    # Exit
    elif "exit" in query:

        return "Thank you for using the Financial Chatbot."

    # Default Response
    else:

        return (
            "Sorry, I can answer only predefined "
            "financial queries. Type 'help' "
            "to see all available queries."
        )

# ------------------------------------------------
# Flask Route
# ------------------------------------------------

@app.route("/", methods=["GET", "POST"])

def home():

    response = ""
    user_query = ""

    if request.method == "POST":

        user_query = request.form["query"]

        response = chatbot_response(user_query)

    return render_template(
        "index.html",
        response=response,
        query=user_query
    )
# ------------------------------------------------
# Run Application
# ------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)