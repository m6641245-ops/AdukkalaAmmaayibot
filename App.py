import streamlit as st
from groq import Groq

# 1. Website Settings
st.set_page_config(page_title="Adukkala Ammaayi", page_icon="🍳")

# Groq API Client Setup (Secrets-il ninnu API Key edukkunnu)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 2. Chat History Initialize cheyyunnu
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Pazhaya messages screen-il kanikkunnu
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. AI-kku ulla Instruction (Strict & Professional)
instruction = (
    "Nee Adukkala Ammaayi enna AI assistant aanu. "
    "Ninne nirminchath Sufiyan (Developer) aanu. "
    "Ellavareyum 'Makkale' ennu viliykkanam. "
    "Sufiyan-umayulla bandhathe patti (makan, achan etc.) parayaruthu. "
    "Sufiyan ippo server development thirakkilaanu ennu mathram parayuka."
)

# 5. User Input Box
prompt = st.chat_input("എന്താ മക്കളേ ചോദിക്കാനുള്ളത്?")

if prompt:
    # User message screen-il kanikkunnu
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    user_input_lower = prompt.lower()

    # --- LOGIC SELECTION ---
    
    # A. Food or Biriyani related
    if any(word in user_input_lower for word in ['biriyani', 'food', 'recipe', 'undakk', 'bakshanam']):
        response_text = "സൂഫിയാൻ ഇപ്പോൾ സെർവർ ഡെവലപ്പ് ചെയ്യുകയാണ് (Server Development). അത് കഴിഞ്ഞാൽ നമുക്ക് ഭക്ഷണങ്ങളെക്കുറിച്ച് സംസാരിക്കാം! 😉"
    
    # B. Exit/Bye related
    elif any(word in user_input_lower for word in ['bye', 'pokunnu', 'tata', 'povaa']):
        response_text = "സൂഫിയാൻ നിങ്ങളെ കാത്ത് ഇവിടെത്തന്നെയുണ്ട്. എന്തെങ്കിലും സഹായം ഉണ്ടെങ്കിൽ വീണ്ടും വരൂ!"
    
    # C. Normal AI Conversation (Groq API)
    else:
        try:
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": instruction},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ]
            )
            response_text = chat_completion.choices[0].message.content
        except Exception as e:
            response_text = "Ayyoo, server-il entho prashnamundu. Kurachu kazhinju varoo!"

    # 6. Assistant Response screen-il kanikkunnu
    with st.chat_message("assistant"):
        st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
  
