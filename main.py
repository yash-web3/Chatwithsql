import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Define Your Prompt
prompt = [
    """
    You are a top 1% expert in converting English questions to SQL query!
    """
]

## Streamlit App
st.set_page_config(page_title="Chatwith Database POC", page_icon=":bar_chart:")
st.sidebar.header("Project Description")
st.sidebar.markdown("""
Classic Models has offices around the world with dozens of employees. The customers of Classic Models are typically toy/gift stores.
""")

st.header("Gemini App To Retrieve SQL Data")

st.subheader("Features:")
st.markdown("- **Natural Language Processing:** Ask questions in English to retrieve SQL data.")
st.markdown("- **Database Integration:** Interact with a SQLite database.")
st.markdown("- **Streamlit UI:** Simple and intuitive user interface.")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response)
    response = read_sql_query(response, "ClassicModels.db")
    st.subheader("Database Details:")
    for row in response:
        st.write(row)
