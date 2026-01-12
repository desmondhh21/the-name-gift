import streamlit as st
import random
import time

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Alexandria & Simone — Name Gift",
    page_icon="🎁",
    layout="centered",
)

# ---------------------------
# Data
# ---------------------------
DATA = {
    "Alexandria": {
        "emoji": "🛡️",
        "origin": "Greek (from Alexandros); also famously tied to the ancient city of Alexandria.",
        "core": "“Defender of people” / “protector of mankind.”",
        "root": "Greek roots: alexein (“to defend”) + andros (“man/people”).",
        "vibe": ["Bold", "Visionary", "Protective", "Timeless", "Brilliant"],
        "more": [
            "A name associated with strength and guardianship — someone who stands up for others.",
            "Echoes scholarship and legacy through the city of Alexandria (libraries, learning, history).",
            "Feels expansive and regal — like someone meant to lead with purpose.",
            "Carries “builder” energy: creating something that lasts.",
        ],
        "gift": "Alexandria — may you always feel protected, powerful, and surrounded by people who see your greatness. 💫",
        "nicknames": ["Alex", "Lexi", "Andria", "Allie"],
    },
    "Simone": {
        "emoji": "🎶",
        "origin": "French form of Simon; used widely across cultures.",
        "core": "Often interpreted as “one who hears” / “listening.”",
        "root": "From Hebrew Shimon: linked to hearing, listening, and being heard.",
        "vibe": ["Elegant", "Calm strength", "Creative", "Refined", "Soulful"],
        "more": [
            "Quiet power — someone who notices what others miss.",
            "Artistic, classy feel (often associated with music, poetry, and style).",
            "Represents wisdom through listening — a presence that makes people feel safe.",
            "Feels modern but timeless — simple, clean, and memorable.",
        ],
        "gift": "Simone — may life always return your kindness, amplify your voice, and honor your peace. ✨",
        "nicknames": ["Si", "Mona", "Simi"],
    },
}

# ---------------------------
# Style (colorful UI)
# ---------------------------
def inject_css():
    st.markdown(
        """
<style>
/* Background */
.stApp {
  background:
    radial-gradient(1200px 700px at 15% 10%, rgba(255, 0, 153, .22), transparent 60%),
    radial-gradient(900px 600px at 90% 25%, rgba(0, 255, 255, .18), transparent 60%),
    radial-gradient(1000px 650px at 50% 95%, rgba(0, 255, 128, .14), transparent 60%),
    linear-gradient(180deg, #0b1020 0%, #101b3a 100%);
  color: #eef2ff;
}

/* Reduce top padding */
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; }

/* Card */
.gift-card {
  border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.06);
  border-radius: 22px;
  padding: 18px;
  box-shadow: 0 18px 60px rgba(0,0,0,.55);
  backdrop-filter: blur(10px);
}

/* Gradient title */
.gradient-title {
  font-size: 2.0rem;
  font-weight: 800;
  line-height: 1.15;
  background: linear-gradient(90deg, #7c5cff, #22d3ee, #34d399, #ff4fd8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin: 0.2rem 0 0.4rem 0;
}

/* Subtitle */
.subtle {
  color: rgba(238,242,255,.78);
  margin-top: 0.2rem;
}

/* Section headers */
.section {
  letter-spacing: .14em;
  text-transform: uppercase;
  font-size: .78rem;
  color: rgba(238,242,255,.8);
  margin: 0.8rem 0 0.2rem 0;
}

/* Pills */
.pill {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.06);
  margin: 4px 6px 0 0;
  font-size: 0.85rem;
}

/* Highlight */
.highlight {
  border-left: 4px solid rgba(34,211,238,.85);
  padding: 10px 12px;
  border-radius: 14px;
  background: rgba(255,255,255,.04);
  margin-top: 10px;
}

/* Buttons */
.stButton>button {
  border-radius: 16px !important;
  padding: 0.65rem 0.9rem !important;
  border: 1px solid rgba(255,255,255,.16) !important;
  background: rgba(255,255,255,.08) !important;
  color: #eef2ff !important;
  transition: transform .12s ease, background .12s ease;
}
.stButton>button:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12) !important;
}

/* Primary action button wrapper */
.primary-btn .stButton>button {
  background: linear-gradient(90deg, rgba(124,92,255,.95), rgba(34,211,238,.85), rgba(255,79,216,.85)) !important;
  border: none !important;
  box-shadow: 0 14px 34px rgba(0,0,0,.35);
}
</style>
        """,
        unsafe_allow_html=True,
    )

inject_css()

# ---------------------------
# Session state
# ---------------------------
if "opened" not in st.session_state:
    st.session_state.opened = False

if "selected_name" not in st.session_state:
    st.session_state.selected_name = "Alexandria"

if "confetti" not in st.session_state:
    st.session_state.confetti = True

if "to_name" not in st.session_state:
    st.session_state.to_name = "Alexandria & Simone"

if "from_name" not in st.session_state:
    st.session_state.from_name = "Desmond"

# ---------------------------
# Helpers
# ---------------------------
def confetti_block(lines=14):
    emojis = ["🎉", "✨", "🎊", "💎", "🌈", "💫", "🧁", "🎈", "🍭", "🌟"]
    out = []
    for _ in range(lines):
        out.append(" ".join(random.choice(emojis) for _ in range(random.randint(8, 16))))
    return "\n".join(out)

def show_confetti():
    if st.session_state.confetti:
        st.success("🎉 Gift opened!")
        st.markdown(f"```text\n{confetti_block(12)}\n```")

def card_open():
    st.markdown('<div class="gift-card">', unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
top_left, top_right = st.columns([0.7, 0.3])
with top_left:
    st.markdown('<div class="gradient-title">Name Gift</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtle">A colorful reveal for <b>Alexandria</b> & <b>Simone</b> 🎁</div>',
        unsafe_allow_html=True,
    )
with top_right:
    st.session_state.confetti = st.toggle("Confetti", value=st.session_state.confetti)

st.write("")

# ---------------------------
# Personalization (To / From)
# ---------------------------
with st.expander("💌 Personalize (To / From)", expanded=False):
    st.session_state.to_name = st.text_input("To:", value=st.session_state.to_name)
    st.session_state.from_name = st.text_input("From:", value=st.session_state.from_name)

# ---------------------------
# Landing / Gift Gate
# ---------------------------
if not st.session_state.opened:
    card_open()
    st.markdown('<div class="section">A gift app</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
**To:** {st.session_state.to_name}  
**From:** {st.session_state.from_name}

Tap the button to open your gift, then choose a name to reveal its meanings, vibes, and message.
"""
    )

    st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
    if st.button("🎁 Open Gift", use_container_width=True):
        st.session_state.opened = True
        show_confetti()
        time.sleep(0.15)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.caption("Tip: You can edit the messages inside app.py before sharing the link.")
    card_close()

else:
    # ---------------------------
    # Main app
    # ---------------------------
    card_open()
    st.markdown('<div class="section">Choose a name</div>', unsafe_allow_html=True)

    names = list(DATA.keys())
    default_index = names.index(st.session_state.selected_name) if st.session_state.selected_name in names else 0

    selected = st.radio(
        "Which name would you like to reveal?",
        options=names,
        index=default_index,
        horizontal=True,
    )
    st.session_state.selected_name = selected

    left, right = st.columns([0.6, 0.4])
    with left:
        if st.button(f"Reveal {selected} {DATA[selected]['emoji']}", use_container_width=True):
            show_confetti()
    with right:
        if st.button("🔄 Reset Gift", use_container_width=True):
            st.session_state.opened = False
            st.rerun()

    st.markdown("---")

    d = DATA[selected]
    st.markdown(f"## {d['emoji']} {selected}")
    st.markdown(f"**To:** {st.session_state.to_name} &nbsp;&nbsp; | &nbsp;&nbsp; **From:** {st.session_state.from_name}")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section">Origin</div>', unsafe_allow_html=True)
        st.write(d["origin"])
        st.markdown('<div class="section">Core meaning</div>', unsafe_allow_html=True)
        st.write(d["core"])
    with c2:
        st.markdown('<div class="section">Root / interpretation</div>', unsafe_allow_html=True)
        st.write(d["root"])
        st.markdown('<div class="section">Nicknames</div>', unsafe_allow_html=True)
        st.write(", ".join(d["nicknames"]))

    st.markdown('<div class="section">Vibe</div>', unsafe_allow_html=True)
    for v in d["vibe"]:
        st.markdown(f'<span class="pill">{v}</span>', unsafe_allow_html=True)

    st.markdown('<div class="section">More meanings</div>', unsafe_allow_html=True)
    for item in d["more"]:
        st.write(f"• {item}")

    st.markdown('<div class="section">Gift message</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="highlight">{d["gift"]}</div>', unsafe_allow_html=True)

    st.caption("Want it more personal? Add one line about a memory or a compliment to make it hit harder.")
    card_close()

    st.write("")
    with st.expander("🚀 Deploy this from GitHub (Streamlit Cloud)"):
        st.markdown(
            """
1. Go to Streamlit Community Cloud  
2. Click **New app**  
3. Select your GitHub repo  
4. Branch: **main**  
5. Main file path: **app.py**  
6. Click **Deploy** — share the `.streamlit.app` link
"""
        )

