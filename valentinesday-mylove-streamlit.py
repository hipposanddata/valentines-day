import streamlit as st
import random
from datetime import date

st.set_page_config(
    page_title="Kaylee 💘",
    page_icon="💘",
    layout="centered",
)

# ----------------------------
# QUICK CUSTOMIZE THESE
# ----------------------------
VALENTINE_NAME = "My Favorite Person in the Whole Wide World"
FROM_NAME = "Oliver"
TITLE = "Kaylee, Will you be my Valentines?"
YES_TEXT = "YES 💖"
NO_TEXT = "No 🙈"
SECRET_PASSCODE = "1103"  # change or leave as-is
SPECIAL_DATE_IDEAS = [
    "Dinner and a movie night at home 🍿",
    "Going out to the science museum and late night ice cream.",
    "Making homemade pizzas and finishing a Netflix series together. ",
    "Making a scrapbook or photo album of our favorite memories",
    "Shopping and writing letters to our future selves.",
]
REASONS = [
    "You make the ordinary feel special.",
    "Your laugh is my favorite sound.",
    "You’re kind in ways people don’t always notice.",
    "I feel lucky doing life with you.",
    "You make me want to be softer and braver.",
]

# ----------------------------
# STYLES
# ----------------------------
st.markdown(
    """
    <style>
      .big-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-top: 0.2rem; }
      .sub { text-align:center; opacity:0.85; margin-bottom: 1rem; }
      .card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 18px 18px 12px 18px;
        margin: 12px 0;
      }
      .center { text-align: center; }
      .tiny { font-size: 0.9rem; opacity:0.8; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# SESSION STATE
# ----------------------------
if "answered" not in st.session_state:
    st.session_state.answered = None  # None / "yes" / "no"
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "reason_idx" not in st.session_state:
    st.session_state.reason_idx = 0

# ----------------------------
# HEADER
# ----------------------------
st.markdown(f"<div class='big-title'>🌷 {TITLE} 🌷</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub'>For <b>{VALENTINE_NAME}</b> — from <b>{FROM_NAME}</b></div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### A very serious question…")
st.markdown("I have a proposal that may lead to **excessive smiling**, **gummy bears**, and possibly **hand-holding**.")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# BUTTONS
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button(YES_TEXT, use_container_width=True):
        st.session_state.answered = "yes"

with col2:
    # Make "No" progressively less appealing (playful, not mean)
    no_label = NO_TEXT
    if st.session_state.no_count >= 1:
        no_label = "No (are you sure?) 😅"
    if st.session_state.no_count >= 2:
        no_label = "No (last chance) 🥺"
    if st.session_state.no_count >= 3:
        no_label = "No (this button is tired) 😴"

    if st.button(no_label, use_container_width=True):
        st.session_state.no_count += 1
        st.session_state.answered = "no"

# ----------------------------
# REACTIONS
# ----------------------------
if st.session_state.answered == "yes":
    st.balloons()
    st.success("Love you to the Moon and back!  💖")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Okay, then it’s official:")
    st.markdown("You’re my Valentine. More details to follow...")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Pick your vibe for our date:")
    idea = st.radio(
        "Choose one (or pretend to choose and I’ll still plan it 😄):",
        SPECIAL_DATE_IDEAS,
        index=0,
    )
    when = st.date_input("When should we do it?", value=date.today())
    snack = st.text_input("Mandatory snack/dessert request:", placeholder="e.g., brownies, boba, ice cream…")

    if st.button("Lock it in 💌"):
        st.markdown("---")
        st.markdown("#### ✅ Date Plan Saved (in our hearts)")
        st.write(f"**Vibe:** {idea}")
        st.write(f"**When:** {when}")
        st.write(f"**Snack:** {snack if snack.strip() else 'Dealer’s choice'}")

        st.write("be sure to take a screenshot of this and send it to me!")
        st.markdown("💘")

    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.answered == "no":
    st.warning("Respectfully, this feature is still in progress.")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Tiny argument in favor of “Yes”")
    st.markdown(random.choice([
        "Counterpoint: Never-ending back massages?",
        "Counterpoint: It comes with snacks. 🍫",
        "Counterpoint: A trip to Whataburger for their Strawberry Milkshakes?",
        "Counterpoint: This is clearly a misclick.",
    ]))
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# REASONS REVEAL
# ----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### A few reasons (tap to reveal)")
c1, c2 = st.columns([2, 1])
with c1:
    st.markdown(f"**Reason #{st.session_state.reason_idx + 1}:**")
    st.write(REASONS[st.session_state.reason_idx])
with c2:
    if st.button("Next reason 👉", use_container_width=True):
        st.session_state.reason_idx = (st.session_state.reason_idx + 1) % len(REASONS)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# SECRET NOTE
# ----------------------------
with st.expander("🔒 Secret note"):
    st.write("Hint: It's a date that's special to us.")
    entered = st.text_input("Enter passcode:", type="password")
    if entered:
        if entered == SECRET_PASSCODE:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 💌 The secret message")
            st.write(
                "Kaylee,\n\n"
                "I’m so grateful for you. I love the way you show up — for me, for others, for yourself. "
                "You're incredibly special, and I feel so lucky to be your person. "
                "Looking forward to all the adventures ahead of us.\n\n"
                "Happy Valentine’s Day!\n\n"
                "Always yours,\n"
                "Oliver"
            )
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Nope — nice try 😄")

st.markdown("<div class='center tiny'>Made with 💘 by yours truly</div>", unsafe_allow_html=True)
