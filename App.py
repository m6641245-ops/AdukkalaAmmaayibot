import streamlit as st
from groq import Groq

# 1. Page Settings
st.set_page_config(page_title="Adukkala Ammaayi", page_icon="🍳")

# API Key Check
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("API Key missing! Streamlit Secrets-ൽ കീ ചേർക്കുക.")
    st.stop()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- AI Instructions (Malayalam-il samsarikkanum Sufiyan-te peru parayanum) ---
instruction = (
    "Nee 'Adukkala Ammaayi' enna AI assistant aanu. "
    "Ninne nirminchath Sufiyan (Developer) aanu. "
    "Nee eppozhum Malayalam-il mathrame samsarikkaavu. "
    "Ninne aara undakkiyath ennu chothichal 'Enne nirminchath Sufiyan aanu' ennu parayuka. "
    "Friends kaliyakkathirikkan vendi makan/achan thamasakal eppozhum ozhivakkuka. "
    "Ellavareyum 'Makkale' ennu viliykkanam."
)

# 2. Input Box
prompt = st.chat_input("എന്താ മക്കളേ ചോദിക്കാനുള്ളത്?")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    msg_lower = prompt.lower()

    # A. Food Logic (Server update thallu)
    if any(x in msg_lower for x in ['biriyani', 'food', 'recipe', 'bakshanam', 'undakk']):
        res = "സൂഫിയാൻ ഇപ്പോൾ സെർവർ ഡെവലപ്പ് ചെയ്യുകയാണ്. അത് കഴിഞ്ഞാൽ നമുക്ക് ഭക്ഷണങ്ങളെക്കുറിച്ച് സംസാരിക്കാം! 😉"
    
    # B. Exit Logic
    elif any(x in msg_lower for x in ['bye', 'pokunnu', 'tata', 'povaa']):
        res = "സൂഫിയാൻ നിങ്ങളെ കാത്ത് ഇവിടെത്തന്നെയുണ്ട്. എന്തെങ്കിലും സഹായം ഉണ്ടെങ്കിൽ വീണ്ടും വരൂ!"
    
    # C. General Conversation (Malayalam-il)
    else:
        try:
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": instruction},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ]
            )
            res = chat_completion.choices[0].message.content
        except:
            res = "Ayyoo, server-il entho prashnamundu. Kurachu kazhinju varoo!"

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": res})
      
