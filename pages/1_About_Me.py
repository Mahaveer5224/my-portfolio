import streamlit as st

st.title("👨‍💻 About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("Appu.jpg", width=180)
with col2:
    st.subheader("Appandairaj J")
    st.write("""
    💼 Application & Production Support Engineer  
    🏦 Banking & OTT Domain Experience  
    🛠️ 4+ Years Experience  
    """)

st.markdown("---")

st.header("🚀 Skills")

st.markdown("""
- 🖥️ Linux, Windows  
- 📊 Monitoring: AppDynamics, Splunk, ITRS  
- ⚙️ Autosys, Shell Scripting  
- 🗄️ SQL, Teradata  
- 🔗 API Testing (Postman)  
- 🐍 Python (Learning Advanced)  
""")

st.header("🎯 Career Goal")

st.write("""
I am transitioning towards DevOps and Cloud Engineering, 
focusing on tools like Jenkins, Docker, and automation.
""")