import streamlit as st

# പേജ് ടൈറ്റിൽ
st.set_page_config(page_title="Adukkala Ammaayi", page_icon="🍲")

# മെയിൻ ഭാഗം
st.title("🍲 അടുക്കള അമ്മായി (Adukkala Ammaayi)")
st.write("---")
st.subheader("സ്വാഗതം! ഇന്ന് നമ്മൾ എന്താണ് ഉണ്ടാക്കാൻ പോകുന്നത്?")

# ചോദ്യം ചോദിക്കാനുള്ള ബോക്സ്
dish = st.text_input("ഏത് വിഭവത്തിന്റെ റെസിപ്പിയാണ് നിങ്ങൾക്ക് വേണ്ടത്?", placeholder="ഉദാ: ബിരിയാണി, സാമ്പാർ...")

if dish:
    # നീ പറഞ്ഞ ആ പ്രത്യേക മറുപടി
    st.warning(f"ക്ഷമിക്കണം, സൂഫിയാൻ ഇപ്പോൾ സെർവറിനകത്ത് ചെറിയ അറ്റകുറ്റപ്പണികൾ ചെയ്തുകൊണ്ടിരിക്കുകയാണ്. നമുക്ക് ഈ സംഭാഷണം കുറച്ച് കഴിഞ്ഞ് തുടരാം.")

# സൈഡ് ബാർ
st.sidebar.title("വിവരങ്ങൾ")
st.sidebar.info("Developer: Sufiyan")
