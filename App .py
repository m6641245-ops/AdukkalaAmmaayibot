import streamlit as st
from groq import Groq

# വെബ്സൈറ്റ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="അടുക്കള അമ്മായി", page_icon="👵")

# അമ്മായിയുടെ ലോഗോ/ഫോട്ടോ
logo_url = "https://img.icons8.com/emoji/96/old-woman-medium-light-skin-tone.png"

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(logo_url, width=120)

st.title("👵 അടുക്കള അമ്മായി")
st.subheader("Sufiyan AI പ്രസന്റ്സ്")
st.write("---")

# API Key (Groq) - സൂഫിയാൻ, നിന്റെ കീ തന്നെയാണിത്
api_key = "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"
client = Groq(api_key=api_key)

# ചാറ്റ് മെസ്സേജുകൾ സേവ് ചെയ്യാൻ
if "messages" not in st.session_state:
    st.session_state.messages = []

# പഴയ മെസ്സേജുകൾ കാണിക്കാൻ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# യൂസർ ടൈപ്പ് ചെയ്യുമ്പോൾ
if prompt := st.chat_input("എന്താ മക്കളേ ചോദിക്കാനുള്ളത്?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # അമ്മായിയുടെ മറുപടി
    with st.chat_message("assistant"):
        instruction = (
            "നീ സൂഫിയാൻ (Sufiyan) നിർമ്മിച്ച ഒരു AI അമ്മായിയാണ്. "
            "എല്ലാവരെയും 'മക്കളേ' എന്ന് വിളിക്കുക. നല്ല നാടൻ മലയാളത്തിൽ തമാശയായി സംസാരിക്കുക. "
            "നിന്നെ ഉണ്ടാക്കിയത് സൂഫിയാൻ ആണെന്ന് ഗമയിൽ പറയണം."
        )
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": instruction}] + 
                     [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
# Food related or Exit related responses handle cheyyaan
user_input = prompt.lower()

if any(word in user_input for word in ['biriyani', 'food', 'recipe']):
    response = "Sufiyan ippol server develop cheyyukayanu. Server update kazhinju namukku food-ine patti samsarikkaam! 😉"
elif any(word in user_input for word in ['bye', 'pokunnu', 'tata']):
    response = "Sufiyan ningale kaathu ivide thanneundu. Enthangilum sahaayam undenkil veendum varoo!"
else:
    # Pazhaya Groq AI response ivide varanam
    response = chat_completion.choices[0].message.content
