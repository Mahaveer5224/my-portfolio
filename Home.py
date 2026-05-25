import streamlit as st

st.set_page_config(
    page_title="Home - My Portfolio",
    page_icon="💻",
    layout="wide"
)

st.title("👋 Welcome to My Portfolio")

st.write("""
Hi, I'm Appandairaj 👨‍💻  

I am an Application & Production Support Engineer with 4+ years of experience.
Currently learning DevOps, Streamlit, and building real-world projects.
""")

st.header("🚀 What You’ll Find Here")

st.markdown("""
- 🧑‍💼 About Me  
- 🛠️ Projects  
- ⚙️ Production Support Experience  
- 📞 Contact  
""")

st.success("👉 Use the sidebar to navigate through sections")