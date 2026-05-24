import streamlit as st

st.set_page_config(layout="wide")
st.title("🚀 My Projects")

st.markdown("### Real-world projects based on my experience")

st.markdown("---")

def project_card(title, desc, tech, button_text):
    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:15px;
        background-color:#1e1e1e;
        margin-bottom:20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    ">
        <h3 style="color:white;">{title}</h3>
        <p style="color:#ccc;">{desc}</p>
        <p style="color:#00adb5;"><b>Tech:</b> {tech}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(button_text):
        st.success("More details coming soon 🚀")


# 🔹 Project 1
project_card(
    "⚙️ Jenkins CI/CD Pipeline",
    "Automated build and deployment pipeline using Jenkins integrated with GitHub.",
    "Jenkins, GitHub, Python",
    "View Jenkins Project"
)

# 🔹 Project 2
project_card(
    "📊 Production Monitoring Dashboard",
    "Streamlit dashboard to simulate real-time monitoring, incidents, and logs.",
    "Streamlit, Python",
    "View Dashboard"
)

# 🔹 Project 3
project_card(
    "🔗 API Testing Tool",
    "Tool to test APIs similar to Postman with request/response handling.",
    "Python, Requests",
    "View API Tool"
)