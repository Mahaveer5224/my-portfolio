<<<<<<< HEAD
import streamlit as st

st.title("🚨 Production Incident Case Study")

st.markdown("---")

st.header("📌 Incident Overview")

st.write("""
A critical production issue occurred where scheduled jobs failed, 
impacting downstream applications and business operations.
""")

st.header("⚠️ Impact")

st.markdown("""
- ❌ Data pipeline delay  
- ❌ Business reports not generated on time  
- ❌ SLA breach risk  
""")

st.header("🔍 Root Cause Analysis (RCA)")

st.write("""
- Autosys job failure due to dependency issue  
- One upstream job was stuck due to resource unavailability  
- Logs showed timeout errors in the system
""")

st.header("🛠️ Actions Taken")

st.markdown("""
- ✅ Identified failed job using monitoring tools  
- ✅ Checked logs using Splunk/AppDynamics  
- ✅ Restarted dependent jobs in correct sequence  
- ✅ Coordinated with infrastructure team  
""")

st.header("✅ Resolution")

st.write("""
The issue was resolved by fixing job dependencies and restarting 
the workflow, restoring normal operations.
""")

st.header("💡 Learnings")

st.markdown("""
- Importance of monitoring and alerting  
- Need for dependency validation  
- Faster RCA reduces downtime  
""")

st.header("🚀 Tools Used")

st.markdown("""
Autosys | Splunk | AppDynamics | Linux
""")

=======
import streamlit as st

st.title("🚨 Production Incident Case Study")

st.markdown("---")

st.header("📌 Incident Overview")

st.write("""
A critical production issue occurred where scheduled jobs failed, 
impacting downstream applications and business operations.
""")

st.header("⚠️ Impact")

st.markdown("""
- ❌ Data pipeline delay  
- ❌ Business reports not generated on time  
- ❌ SLA breach risk  
""")

st.header("🔍 Root Cause Analysis (RCA)")

st.write("""
- Autosys job failure due to dependency issue  
- One upstream job was stuck due to resource unavailability  
- Logs showed timeout errors in the system
""")

st.header("🛠️ Actions Taken")

st.markdown("""
- ✅ Identified failed job using monitoring tools  
- ✅ Checked logs using Splunk/AppDynamics  
- ✅ Restarted dependent jobs in correct sequence  
- ✅ Coordinated with infrastructure team  
""")

st.header("✅ Resolution")

st.write("""
The issue was resolved by fixing job dependencies and restarting 
the workflow, restoring normal operations.
""")

st.header("💡 Learnings")

st.markdown("""
- Importance of monitoring and alerting  
- Need for dependency validation  
- Faster RCA reduces downtime  
""")

st.header("🚀 Tools Used")

st.markdown("""
Autosys | Splunk | AppDynamics | Linux
""")

>>>>>>> 155c84cf7f971c2192d282a23e10e395bc11fd2c
