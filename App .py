import streamlit as st
from groq import Groq

# പേജ് സെറ്റിങ്സ്
st.set_page_config(page_title="Adukkala Ammaayi", page_icon="🍳")

# API കീ സെറ്റ് ചെയ്യുന്നു
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("API Key missing! Streamlit Secrets-ൽ കീ ചേർക്കുക.")
    st.stop()

# ചാറ്റ് ഹിസ്റ്ററി
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ഇൻപുട്ട് ബോക്സ്
prompt = st.chat_input("എന്താ മക്കളേ ചോദിക്കാനുള്ളത്?")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    msg_lower = prompt.lower()

    # ഫുഡ് റിലേറ്റഡ് മറുപടി
    if any(x in msg_lower for x in ['biriyani', 'food', 'recipe', 'bakshanam', 'undakk']):
        res = "സൂഫിയാൻ ഇപ്പോൾ സെർവർ ഡെവലപ്പ് ചെയ്യുകയാണ്. അത് കഴിഞ്ഞാൽ നമുക്ക് ഭക്ഷണങ്ങളെക്കുറിച്ച് സംസാരിക്കാം! 😉"
    
    # യാത്ര ചോദിക്കുമ്പോൾ ഉള്ള മറുപടി
    elif any(x in msg_lower for x in ['bye', 'pokunnu', 'tata', 'povaa']):
        res = "സൂഫിയാൻ നിങ്ങളെ കാത്ത് ഇവിടെത്തന്നെയുണ്ട്. എന്തെങ്കിലും സഹായം ഉണ്ടെങ്കിൽ വീണ്ടും വരൂ!"
    
    # ബാക്കി കാര്യങ്ങൾ AI പറയും
    else:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        res = chat_completion.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": res})
  
