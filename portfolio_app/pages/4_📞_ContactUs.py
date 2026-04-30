import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞", layout="wide")

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
}

/* Text styling */
h1, h2, h3, p, div {
    color: #222;
}

/* Center text */
.center {
    text-align: center;
}

/* Links */
a {
    text-decoration: none;
    color: #6C63FF;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 📞 HEADER
# =========================
st.markdown("<h1 class='center'>📞 Contact Me</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>✨ I'd love to connect with you! ✨</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 📌 LAYOUT
# =========================
col1, col2 = st.columns(2)

# Contact Form
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✉️ Send a Message")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("📩 Send Message"):
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been sent ✅")
        else:
            st.error("⚠️ Please fill in all fields.")

    st.markdown('</div>', unsafe_allow_html=True)

# Social Links
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌐 Connect with Me")

    st.markdown("""
    - 🐙 [GitHub](https://github.com/)
    - 📘 [Facebook](https://facebook.com/den.lopez.9695)
    - ✉️ Email: yourname@email.com
    """)

    st.info("💬 Feel free to reach out anytime!")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 💖 FOOTER
# =========================
st.markdown("""
<p style='text-align: center; color: #444; margin-top: 20px;'>
💖 Open for opportunities and collaborations
</p>
""", unsafe_allow_html=True)