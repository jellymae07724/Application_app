import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🏠",
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

/* Improve text visibility */
h1, h2, h3, p, div {
    color: #222;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 🏠 CONTENT
# =========================
st.title("🏠 Welcome to My Portfolio")
st.subheader("Hi, I'm Jelly Mae 👋")
st.write("Aspiring Developer | Designer")

st.image("portfolio_app/images/profile.png", width=200, caption="My Portfolio Banner")

st.markdown("""
### 👨‍💻 About This Portfolio
This web application showcases:
- My background and journey
- Technical skills
- Projects I've built
- Ways to contact me

Use the **sidebar** to navigate through different sections.
""")

st.markdown("### 🎯 What are you looking for?")
choice = st.radio(
    "Select a section:",
    ["About Me", "Skills", "Projects", "Contact"]
)

if choice == "About Me":
    st.info("👉 Go to the About page from the sidebar.")
elif choice == "Skills":
    st.success("👉 Check out my Skills section!")
elif choice == "Projects":
    st.warning("👉 Explore my Projects!")
elif choice == "Contact":
    st.error("👉 Visit the Contact page to reach me!")

st.markdown("---")
st.caption("© 2026 Jelly Mae | Streamlit Portfolio App")
