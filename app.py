import streamlit as st
import random
import time

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Alexandria — A Regal Name Gift",
    page_icon="👑",
    layout="centered",
)

# ---------------------------
# Content (Alexandria only)
# ---------------------------
ALEXANDRIA = {
    "title": "Alexandria",
    "tagline": "A regal name. A timeless legacy.",
    "meaning": "“Defender of people” / “protector of mankind.”",
    "origin": "Greek (from Alexandros). The name also echoes the historic city of Alexandria — a symbol of knowledge and legacy.",
    "roots": "Greek roots: alexein (“to defend”) + andros (“man/people”).",
    "themes": [
        "Protection & leadership",
        "Wisdom & scholarship",
        "Legacy & excellence",
        "Grace under pressure",
    ],
    "vibe_words": ["Regal", "Wise", "Protective", "Magnetic", "Legacy-minded"],
    "gift_message": (
        "Alexandria — may your life be crowned with favor, your mind sharpened with wisdom, "
        "and your path guarded by strength. 👑✨"
    ),
}

# ---------------------------
# Session state
# ---------------------------
if "opened" not in st.session_state:
    st.session_state.opened = False

if "to_name" not in st.session_state:
    st.session_state.to_name = "Alexandria"

if "from_name" not in st.session_state:
    st.session_state.from_name = "Desmond"

if "sparkle" not in st.session_state:
    st.session_state.sparkle = True


# ---------------------------
# Styling (African-themed + regal)
# ---------------------------
def inject_css():
    st.markdown(
        """
<style>
/* Regal African-inspired palette + subtle pattern vibe */
.stApp{
  background:
    radial-gradient(1100px 650px at 12% 12%, rgba(255, 203, 71, .18), transparent 60%),
    radial-gradient(900px 550px at 88% 18%, rgba(50, 255, 200, .08), transparent 60%),
    radial-gradient(1000px 700px at 50% 110%, rgba(255, 62, 132, .10), transparent 60%),
    linear-gradient(180deg, #070611 0%, #0c0b1f 40%, #0a1128 100%);
  color: #f6f2e8;
}

/* Container spacing */
.block-container{ padding-top: 1.3rem; padding-bottom: 3rem; }

/* Crown title */
.title{
  font-size: 2.2rem;
  font-weight: 900;
  margin: 0.1rem 0 0.3rem 0;
  letter-spacing: 0.5px;
  background: linear-gradient(90deg, #f7d36b, #ffd98e, #d8a93f, #f7d36b);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

/* Subtext */
.subtle{
  color: rgba(246, 242, 232, .78);
  margin-top: 0.2rem;
}

/* Section label */
.section{
  letter-spacing: .16em;
  text-transform: uppercase;
  font-size: .78rem;
  color: rgba(246, 242, 232, .80);
  margin: 0.85rem 0 0.25rem 0;
}

/* Card */
.card{
  border: 1px solid rgba(255, 217, 142, .22);
  background: rgba(10, 10, 22, .45);
  border-radius: 22px;
  padding: 18px;
  box-shadow: 0 18px 60px rgba(0,0,0,.60);
  backdrop-filter: blur(10px);
  position: relative;
  overflow: hidden;
}

/* Subtle “textile” vibe using layered diagonals */
.card:before{
  content:"";
  position:absolute;
  inset:-60px;
  background:
    repeating-linear-gradient(
      135deg,
      rgba(255, 217, 142, .055) 0px,
      rgba(255, 217, 142, .055) 10px,
      rgba(0,0,0,0) 10px,
      rgba(0,0,0,0) 22px
    );
  opacity: .55;
  pointer-events: none;
  transform: rotate(0deg);
}

/* Highlight bar */
.highlight{
  border-left: 4px solid rgba(247, 211, 107, .95);
  padding: 10px 12px;
  border-radius: 14px;
  background: rgba(255, 217, 142, .06);
}

/* Pills */
.pill{
  display:inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255, 217, 142, .22);
  background: rgba(255, 217, 142, .06);
  margin: 4px 6px 0 0;
  font-size: .86rem;
  color: rgba(246, 242, 232, .92);
}

/* Buttons */
.stButton>button{
  border-radius: 16px !important;
  padding: 0.72rem 0.95rem !important;
  border: 1px solid rgba(255, 217, 142, .28) !important;
  background: rgba(255, 217, 142, .08) !important;
  color: #f6f2e8 !important;
  transition: transform .12s ease, background .12s ease, border-color .12s ease;
}
.stButton>button:hover{
  transform: translateY(-1px);
  background: rgba(255, 217, 142, .12) !important;
  border-color: rgba(255, 217, 142, .38) !important;
}

/* Primary button */
.primary .stButton>button{
  background: linear-gradient(90deg, rgba(247, 211, 107, .95), rgba(216, 169, 63, .95)) !important;
  border: none !important;
  color: #1a1204 !important;
  box-shadow: 0 14px 34px rgba(0,0,0,.45);
}
.primary .stButton>button:hover{
  transform: translateY(-1px) scale(1.01);
}

/* Inputs */
label, .stTextInput{
  color: rgba(246, 242, 232, .90) !important;
}
</style>
        """,
        unsafe_allow_html=True,
    )

inject_css()

# ---------------------------
# Helpers
# ---------------------------
def regal_sparkle():
    # lightweight “sparkle” lines to match the regal theme
    if not st.session_state.sparkle:
        return
    emojis = ["✨", "👑", "🌟", "🟡", "🟨"]
    lines = []
    for _ in range(10):
        lines.append(" ".join(random.choice(emojis) for _ in range(random.randint(10, 16))))
    st.markdown(f"```text\n{chr(10).join(lines)}\n```")


def open_card():
    st.markdown('<div class="card">', unsafe_allow_html=True)


def close_card():
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------
# Header
# ---------------------------
left, right = st.columns([0.72, 0.28])
with left:
    st.markdown(f'<div class="title">👑 {ALEXANDRIA["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtle">{ALEXANDRIA["tagline"]}</div>', unsafe_allow_html=True)
with right:
    st.session_state.sparkle = st.toggle("Sparkle", value=st.session_state.sparkle)

st.write("")

# ---------------------------
# Personalize
# ---------------------------
with st.expander("💌 Personalize (To / From)", expanded=False):
    st.session_state.to_name = st.text_input("To:", value=st.session_state.to_name)
    st.session_state.from_name = st.text_input("From:", value=st.session_state.from_name)

# ---------------------------
# Gift gate
# ---------------------------
if not st.session_state.opened:
    open_card()
    st.markdown('<div class="section">Royal Gift</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
**To:** {st.session_state.to_name}  
**From:** {st.session_state.from_name}  

A name is more than letters — it’s a **story**, a **crown**, a **calling**.
Open your gift to reveal *Alexandria*.
"""
    )

    st.markdown('<div class="primary">', unsafe_allow_html=True)
    if st.button("Open the Gift ✨", use_container_width=True):
        st.session_state.opened = True
        st.success("Gift opened 👑")
        regal_sparkle()
        time.sleep(0.12)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.caption("Tip: Edit the message in app.py to make it personal before sharing.")
    close_card()

else:
    # ---------------------------
    # Reveal
    # ---------------------------
    open_card()
    st.markdown('<div class="section">The Meaning</div>', unsafe_allow_html=True)
    st.markdown(f"### {ALEXANDRIA['meaning']}")

    st.markdown('<div class="section">Origin</div>', unsafe_allow_html=True)
    st.write(ALEXANDRIA["origin"])

    st.markdown('<div class="section">Roots</div>', unsafe_allow_html=True)
    st.write(ALEXANDRIA["roots"])

    st.markdown('<div class="section">Themes</div>', unsafe_allow_html=True)
    for t in ALEXANDRIA["themes"]:
        st.write(f"• {t}")

    st.markdown('<div class="section">Regal Vibe</div>', unsafe_allow_html=True)
    for w in ALEXANDRIA["vibe_words"]:
        st.markdown(f'<span class="pill">{w}</span>', unsafe_allow_html=True)

    st.markdown('<div class="section">Gift Message</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="highlight">{ALEXANDRIA["gift_message"]}</div>', unsafe_allow_html=True)

    st.write("")
    c1, c2 = st.columns([0.6, 0.4])
    with c1:
        if st.button("Sparkle again ✨", use_container_width=True):
            regal_sparkle()
    with c2:
        if st.button("Reset 🎁", use_container_width=True):
            st.session_state.opened = False
            st.rerun()

    close_card()
