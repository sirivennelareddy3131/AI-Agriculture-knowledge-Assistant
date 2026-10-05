import streamlit as st
from ai_assistant import get_answer

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI Agriculture Knowledge Assistant",
    page_icon="🌱",
    layout="wide"
)
# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []
# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🌱 Agriculture Assistant")

    st.write("### Ask me about...")

    st.write("🌾 Crops")
    st.write("🌱 Soil")
    st.write("🧪 Fertilizers")
    st.write("💧 Irrigation")
    st.write("🐛 Pests")
    st.write("🦠 Plant Diseases")
    st.write("🚜 Farming Methods")
    st.write("🌿 Crop Management")

    st.divider()

    st.write("### 💡 Try asking")

    if st.button("What is nitrogen?"):
        st.session_state.selected_question = "What is nitrogen?"

    if st.button("How often should I water crops?"):
        st.session_state.selected_question = (
            "How often should I water crops?"
        )

    if st.button("What causes yellow leaves?"):
        st.session_state.selected_question = (
            "What causes yellow leaves?"
        )

    if st.button("How can I control pests?"):
        st.session_state.selected_question = (
            "How can I control pests?"
        )

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.info(
        "Ask your agriculture question in simple English. "
        "The assistant will give a short and easy answer."
    )


# ---------------- MAIN PAGE ----------------

st.title("🌱 AI Agriculture Knowledge Assistant")

st.write(
    "Your simple AI assistant for agriculture-related questions."
)

st.markdown(
    """
    **You can ask about:**  
    🌾 Crops &nbsp;&nbsp;
    🌱 Soil &nbsp;&nbsp;
    🧪 Fertilizers &nbsp;&nbsp;
    💧 Irrigation &nbsp;&nbsp;
    🐛 Pests &nbsp;&nbsp;
    🦠 Diseases
    """
)

st.divider()


# ---------------- WELCOME MESSAGE ----------------

if len(st.session_state.messages) == 0:

    st.subheader("👋 Welcome!")

    st.write(
        "I can help you understand basic agriculture topics "
        "using simple and easy language."
    )

    st.write("### 🌾 Example questions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "🌱 **Soil**\n\n"
            "What is soil testing?"
        )

    with col2:
        st.info(
            "🧪 **Fertilizer**\n\n"
            "What is nitrogen?"
        )

    with col3:
        st.info(
            "💧 **Irrigation**\n\n"
            "Why is irrigation important?"
        )


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ---------------- SELECTED QUESTION ----------------

selected_question = st.session_state.pop(
    "selected_question",
    None
)


# ---------------- CHAT INPUT ----------------

question = st.chat_input(
    "🌱 Ask your agriculture question..."
)


# If user clicks a suggested question
if selected_question:
    question = selected_question


# ---------------- GET ANSWER ----------------

if question:

    # Save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user question
    with st.chat_message("user"):
        st.write(question)

    # Get AI response
    with st.chat_message("assistant"):

        with st.spinner("🌱 Thinking..."):

            answer = get_answer(question)

        st.write(answer)

    # Save AI answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )