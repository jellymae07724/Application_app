import streamlit as st

st.set_page_config(
    page_title="Skills",
    page_icon="💡",
    layout="wide"
)

# =========================
# 🎨 BACKGROUND CSS
# =========================
st.markdown("""
<style>

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #ffe6f0, #e6f0ff, #e6fff5, #fff5e6);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Text styling */
h1, h2, h3, p, div {
    color: #222;
}

/* Make progress bars nicer */
.stProgress > div > div > div > div {
    background-color: #6c63ff;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 💡 CONTENT
# =========================
st.title("💡 Skills")

st.subheader("💻 Programming")
st.write("Python")
st.progress(80)

st.write("JavaScript")
st.progress(70)

st.write("PHP")
st.progress(75)

st.subheader("🎨 Design")
st.write("Canva / UI Design")
st.progress(85)

st.subheader("🛠 Tools")
st.write("- GitHub")
st.write("- VS Code")
st.write("- Streamlit")

st.subheader("📊 Skill Self-Assessment")
skill = st.slider("Rate your confidence in coding:", 0, 100, 75)

if skill > 70:
    st.success("Great confidence! Keep building projects 🚀")
else:
    st.warning("Keep practicing — you're improving!")