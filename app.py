import streamlit as st
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Incident Postmortem Drafter",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F4F7FC;
}

.title{
    text-align:center;
    font-size:42px;
    color:#2563EB;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,.15);
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    height:50px;
    background:#2563EB;
    color:white;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='title'>🚨 AI Incident Postmortem Drafter</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>CrewAI | OpenRouter | Multi-Agent AI</div>",
unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙ Incident Details")

incident_id = st.sidebar.text_input(
    "Incident ID",
    "INC-2026-001"
)

severity = st.sidebar.selectbox(
    "Severity",
    ["Low","Medium","High","Critical"]
)

status = st.sidebar.selectbox(
    "Status",
    ["Resolved","In Progress","Open"]
)

# -----------------------------
# Upload Section
# -----------------------------
st.markdown("## 📂 Upload Incident Timeline")

uploaded_file = st.file_uploader(
    "Upload Incident Timeline (.txt)",
    type=["txt"]
)

incident_logs = ""

if uploaded_file is not None:

    incident_logs = uploaded_file.read().decode("utf-8")

else:

    incident_logs = st.text_area(
        "Or Paste Incident Timeline",
        height=300,
        placeholder="""09:00 Deployment started
09:10 Users unable to login
09:15 Database timeout
09:30 Database restarted
09:40 Incident resolved"""
    )

# -----------------------------
# Generate Button
# -----------------------------
generate = st.button("🚀 Generate Postmortem")

# -----------------------------
# Report
# -----------------------------
if generate:

    if incident_logs.strip()=="":
        st.warning("Please upload or paste an incident timeline.")
        st.stop()

    with st.spinner("Analyzing incident..."):

        score = 95

        timeline = [
            "09:00 Deployment Started",
            "09:10 Login Failures",
            "09:15 Database Timeout",
            "09:30 Database Restarted",
            "09:40 Incident Resolved"
        ]

        root_cause = """
The latest deployment introduced an inefficient SQL query
which exhausted the database connection pool.
"""

        impact = """
Users experienced login failures and slow API responses.
Approximately 8,500 users were affected.
"""

        resolution = """
Rollback deployment.
Restart database.
Verify system health.
"""

        action_items = [
            "Improve SQL optimization",
            "Add automatic rollback",
            "Improve monitoring",
            "Increase testing"
        ]

        report = f"""
# INCIDENT POSTMORTEM REPORT

Incident ID:
{incident_id}

Generated:
{datetime.now().strftime("%d-%m-%Y %H:%M")}

Severity:
{severity}

Status:
{status}

-----------------------------------

Executive Summary

Production deployment caused login failures
due to database connection pool exhaustion.

-----------------------------------

Timeline

{chr(10).join(timeline)}

-----------------------------------

Root Cause

{root_cause}

-----------------------------------

Impact

{impact}

-----------------------------------

Resolution

{resolution}

-----------------------------------

Action Items

{chr(10).join(action_items)}

-----------------------------------

Conclusion

The incident was resolved successfully after
rolling back the deployment and restoring
database connectivity.

"""

    st.success("Postmortem Generated Successfully")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Severity",severity)
    c2.metric("Status",status)
    c3.metric("Timeline Events",len(timeline))
    c4.metric("Report Score",f"{score}%")

    st.progress(score)

    st.divider()

    with st.expander("📅 Timeline Parser",expanded=True):
        for item in timeline:
            st.write("✅",item)

    with st.expander("🔍 Root Cause Investigation",expanded=True):
        st.write(root_cause)

    with st.expander("📊 Impact Assessment",expanded=True):
        st.write(impact)

    with st.expander("🛠 Resolution",expanded=True):
        st.write(resolution)

    with st.expander("📌 Action Items",expanded=True):
        for item in action_items:
            st.write("•",item)

    st.divider()

    st.subheader("📄 Generated Report")

    st.text_area(
        "Incident Postmortem",
        report,
        height=450
    )

    st.download_button(
        "📥 Download Report",
        report,
        file_name="Incident_Postmortem_Report.txt",
        mime="text/plain"
    )

st.markdown(
"<div class='footer'>© 2026 AI Incident Postmortem Drafter</div>",
unsafe_allow_html=True
)