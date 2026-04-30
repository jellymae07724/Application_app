import streamlit as st

st.set_page_config(page_title="My Skills", page_icon="💡", layout="wide")

# =========================
# 🎨 BACKGROUND + STYLE
# =========================
st.markdown("""
<style>

/* Animated background */
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

/* Card style */
.card {
    background: rgba(255, 255, 255, 0.75);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

/* Text styling */
h1, h2, h3, p, div {
    color: #222;
}

/* Center text */
.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 🧑‍💻 CONTENT
# =========================
st.markdown("<h1 class='center'>🧑‍💻 My Skills</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>✨ A snapshot of my abilities and growth ✨</p>", unsafe_allow_html=True)

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💻 Technical Skills")
    st.markdown("""
    - 🐍 Basic Programming (Python)
    - 🌐 Web Development (HTML, CSS, JavaScript)
    - 🎨 Basic UI/UX Design
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧠 Soft Skills")
    st.markdown("""
    - 🧩 Problem Solving  
    - 🤔 Critical Thinking  
    - 🤝 Teamwork and Collaboration  
    - ⏰ Time Management  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🚀 Learning Goals")
st.markdown("""
- 📈 Improve coding skills  
- 🧠 Learn new technologies  
- 🌟 Build more real-world projects  
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💡 Fun Fact")

if st.button("✨ Click to reveal"):
    st.success("🚀 I’m always eager to learn and improve my skills!")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<p style='text-align: center; color: #444;'>
🌱 Growing step by step in tech 🌱
</p>
""", unsafe_allow_html=True)