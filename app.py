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
# Deep, detailed meaning content (Alexandria only)
# ---------------------------
HIERO_STRIP = "𓂀 𓋹 𓆣 𓅓 𓇳 𓏤 𓍿 𓊹 𓎛 𓄿 𓇋 𓂋 𓈖 𓋴"

ALEX = {
    "title": "Alexandria",
    "tagline": "A regal name. A timeless legacy.",
    "meaning_headline": "“Defender of people” / “protector of mankind.”",
    "meaning_long": (
        "Alexandria signifies a guardian-leader — one who protects people through wisdom, intellect, "
        "and moral authority. It represents strength that shields, leadership that serves, and power "
        "guided by responsibility rather than force."
    ),
    "linguistic": (
        "The name traces to Greek roots: 'alexein' meaning “to defend, to ward off, to shield,” and "
        "'andros' meaning “people / community.” Together, Alexandria implies “one who stands between "
        "harm and the people.” It’s a name of vigilance, strategy, and collective responsibility."
    ),
    "historical": (
        "The name also echoes the ancient African city of Alexandria in Egypt — a renowned center of "
        "learning, scholarship, and cultural exchange. That association adds a second layer: intellectual "
        "authority and a legacy of preserving wisdom for future generations."
    ),
    "african_context": (
        "Through a Ghanaian (Akan) lens of leadership, true power is protection, wisdom before action, "
        "and humility paired with strength. Alexandria fits naturally with these ideals: a name that "
        "feels crowned with duty — not for display, but for service to the community."
    ),
    "themes": [
        "Protective leadership",
        "Wisdom and intellect",
        "Responsibility before power",
        "Legacy and ancestral awareness",
        "Strength guided by humility",
    ],
    "vibe_words": [
        "Regal",
        "Wise",
        "Protective",
        "Grounded",
        "Legacy-bearing",
        "Magnetic",
    ],
    "royal_blessing": (
        "Alexandria — may you walk crowned with wisdom, guarded by discernment, and strengthened by the "
        "knowledge that your name carries protection, legacy, and honor. 👑✨"
    ),
}

ADINKRA = [
    {"icon": "🌀", "name": "Sankofa", "meaning": "Return and fetch it — learn from the past to build the future."},
    {"icon": "✨", "name": "Gye Nyame", "meaning": "Except for God — reverence, sovereignty, spiritual authority."},
    {"icon": "🗡️", "name": "Akofena", "meaning": "War sword — courage guided by honor and discipline."},
    {"icon": "🐏", "name": "Dwennimmen", "meaning": "Ram’s horns — strength with humility."},
    {"icon": "🏠", "name": "Eban", "meaning": "Fence — protection of home, family, and community."},
]

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
# Styling (fix cut-off + Ghanaian regal vibe)
# ---------------------------
def inject_css():
    st.markdown(
        """
<style>
/* ✅ Fix top cut-off: ensure content starts below Streamlit header */
.block-container{
  padding-top: 4.6rem !important;
  padding-bottom: 3rem !important;
}

/* Make the Streamlit header blend with theme */
header[data-testid="stHeader"]{
  background: rgba(7, 6, 17, .55) !important;
  backdrop-filter: blur(10px);
}

/* Background */
.stApp{
  background:
    radial-gradient(1100px 650px at 12% 12%, rgba(255, 203, 71, .18), transparent 60%),
    radial-gradient(900px 550px at 88% 18%, rgba(50, 255, 200, .08), transparent 60%),
    radial-gradient(1000px 700px at 50% 110%, rgba(255, 62, 132, .10), transparent 60%),
    linear-gradient(180deg, #070611 0%, #0c0b1f 40%, #0a1128 100%);
  color: #f6f2e8;
}

/* Title */
.title{
  font-size: 2.35rem;
  font-weight: 900;
  margin: 0.2rem 0 0.2rem 0;
  letter-spacing: 0.5px;
  background: linear-gradient(90deg, #f7d36b, #ffd98e, #d8a93f, #f7d36b);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.subtle{
  color: rgba(246, 242, 232, .78);
  margin-top: 0.2rem;
}

/* Ghanaian kente-inspired header band */
.kente-band{
  border-radius: 18px;
  padding: 12px 14px;
  border: 1px solid rgba(255, 217, 142, .22);
  background:
    linear-gradient(90deg, rgba(247,211,107,.20), rgba(0,0,0,0)),
    repeating-linear-gradient(
      135deg,
      rgba(247,211,107,.22) 0px,
      rgba(247,211,107,.22) 10px,
      rgba(255,62,132,.14) 10px,
      rgba(255,62,132,.14) 20px,
      rgba(50,255,200,.12) 20px,
      rgba(50,255,200,.12) 30px,
      rgba(0,0,0,0) 30px,
      rgba(0,0,0,0) 42px
    );
  box-shadow: 0 14px 44px rgba(0,0,0,.45);
}

/* Hieroglyph strip */
.hiero{
  margin-top: 10px;
  font-size: 1.05rem;
  letter-spacing: .20em;
  color: rgba(255, 217, 142, .85);
  text-align: center;
  padding: 10px 10px;
  border-radius: 16px;
  border: 1px solid rgba(255, 217, 142, .18);
  background: rgba(255, 217, 142, .05);
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
}

.section{
  letter-spacing: .16em;
  text-transform: uppercase;
  font-size: .78rem;
  color: rgba(246, 242, 232, .80);
  margin: 0.95rem 0 0.25rem 0;
}

/* Highlight */
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
</style>
        """,
        unsafe_allow_html=True,
    )

inject_css()

# ---------------------------
# Helpers
# ---------------------------
def regal_sparkle():
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
    st.markdown(f'<div class="title">👑 {ALEX["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtle">{ALEX["tagline"]}</div>', unsafe_allow_html=True)
with right:
    st.session_state.sparkle = st.toggle("Sparkle", value=st.session_state.sparkle)

st.markdown('<div class="kente-band"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="hiero">{HIERO_STRIP}</div>', unsafe_allow_html=True)
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
Open your gift to reveal the deeper meaning of *Alexandria* — regal, Ghanaian-centered, and timeless.
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

    st.caption("Tip: You can customize the blessing text in app.py before sharing the link.")
    close_card()

else:
    # ---------------------------
    # Reveal
    # ---------------------------
    open_card()

    st.markdown('<div class="section">The Meaning</div>', unsafe_allow_html=True)
    st.markdown(f"### {ALEX['meaning_headline']}")
    st.write(ALEX["meaning_long"])

    st.markdown('<div class="section">Linguistic Depth</div>', unsafe_allow_html=True)
    st.write(ALEX["linguistic"])

    st.markdown('<div class="section">Historical Legacy</div>', unsafe_allow_html=True)
    st.write(ALEX["historical"])

    st.markdown('<div class="section">African-Centered Interpretation</div>', unsafe_allow_html=True)
    st.write(ALEX["african_context"])

    st.markdown('<div class="section">Core Themes</div>', unsafe_allow_html=True)
    for t in ALEX["themes"]:
        st.write(f"• {t}")

    st.markdown('<div class="section">Regal Vibe</div>', unsafe_allow_html=True)
    for w in ALEX["vibe_words"]:
        st.markdown(f'<span class="pill">{w}</span>', unsafe_allow_html=True)

    st.markdown('<div class="section">Ghanaian Symbolism (Adinkra-inspired)</div>', unsafe_allow_html=True)
    st.write("These principles reflect noble leadership — protection, wisdom, humility, and legacy:")
    for item in ADINKRA:
        st.markdown(f"**{item['icon']} {item['name']}** — {item['meaning']}")

    st.markdown('<div class="section">Royal Blessing</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="highlight">{ALEX["royal_blessing"]}</div>', unsafe_allow_html=True)

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
