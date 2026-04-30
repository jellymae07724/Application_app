import streamlit as st
import math

st.set_page_config(page_title="My Projects", page_icon="📁", layout="wide")

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

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.75);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

/* Text */
h1, h2, h3, p, div {
    color: #222;
}

/* Center */
.center {
    text-align: center;
}

/* Result box */
.result-box {
    font-size: 20px;
    font-weight: bold;
    color: #6C63FF;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 📁 HEADER
# =========================
st.markdown("<h1 class='center'>📁 My Projects</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>✨ Explore my sample work ✨</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 🧮 PROJECT CARD
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🧮 Multi-Function Calculator App")
st.write("A simple calculator that performs basic and advanced operations.")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("🔢 Enter first number")

with col2:
    num2 = st.number_input("🔢 Enter second number")

operation = st.selectbox("⚙️ Choose operation", [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Power",
    "Square Root (num1 only)"
])

if st.button("🧮 Calculate"):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "❌ Cannot divide by zero"

    elif operation == "Power":
        result = num1 ** num2

    elif operation == "Square Root (num1 only)":
        result = math.sqrt(num1) if num1 >= 0 else "❌ Negative number not allowed"

    st.markdown(f"<p class='result-box'>Result: {result}</p>", unsafe_allow_html=True)

    if st.checkbox("📖 Show Details"):
        st.info(f"You selected **{operation}** operation.")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 🚀 FOOTER
# =========================
st.markdown("""
<p style='text-align: center; color: #444;'>
🚀 More projects coming soon...
</p>
""", unsafe_allow_html=True)