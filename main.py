import streamlit as st
from PIL import Image

# ---- SETTINGS ----
#LOGO_PATH = "logo.png"

st.set_page_config(
    page_title="Contrast‑Connect | Customer Intake",
    page_icon=":link:",
    layout="centered",
)

# ---- LOGO & TITLE ----
#logo = Image.open(LOGO_PATH)
col1, col2, col3 = st.columns([1,6,1])
#with col2:
#    st.image(logo, width=390)

st.markdown(
    "<h2 style='text-align:center; color:#355BB8;'>Customer Intake Form</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; color: #AAA; font-size: 1.1em;'>All information is confidential and processed securely.</p>",
    unsafe_allow_html=True,
)
st.write("---")

# ---- FORM ----
with st.form("intake_form"):
    st.subheader("1. Facility Information")
    facility_name = st.text_input("Facility / Hospital Name *", max_chars=80)
    address = st.text_input("Facility Address (City, State) *", max_chars=80)
    st.markdown("")

    st.subheader("2. Contact Information")
    contact_name = st.text_input("Primary Contact Name *", max_chars=50)
    contact_email = st.text_input("Contact Email *", max_chars=80)
    contact_phone = st.text_input("Contact Phone Number *", max_chars=25)
    st.markdown("")

    st.subheader("3. Service & Scheduling Needs")
    coverage = st.selectbox(
        "Type of Coverage Required *",
        ["Full Coverage", "Overflow Support", "Weekend/Holiday Only", "Custom/Other"],
    )
    hours_per_week = st.number_input(
        "Estimated Supervision Hours per Week *", min_value=1, max_value=168, step=1
    )
    start_time = st.time_input("Preferred Shift Start Time")
    end_time = st.time_input("Preferred Shift End Time")
    st.markdown("")

    st.subheader("4. Compliance & Workflow")
    own_rads = st.radio(
        "Will your own radiologists participate via our portal?",
        ["Yes", "No", "Unsure"],
    )
    compliance = st.multiselect(
        "Key Priorities (select all that apply)",
        [
            "CMS/ACR Regulatory Compliance",
            "HIPAA Secure Communication",
            "Audit-Ready Documentation",
            "Technologist Training/Support",
            "Real-Time Audio/Video Supervision",
        ],
    )
    st.markdown("")

    st.subheader("5. Additional Information")
    goals = st.text_area(
        "Please describe your primary goals or challenges (optional)",
        max_chars=250,
        placeholder="E.g., expand hours, streamline workflow, improve compliance, etc.",
    )
    extra = st.text_area(
        "Additional Notes or Special Requirements (optional)",
        max_chars=250,
    )
    st.write("---")

    agree = st.checkbox(
        "I confirm that I am authorized to submit this information and agree to its secure handling."
    )

    submitted = st.form_submit_button("Submit Intake Form", use_container_width=True)

    if submitted:
        required_fields = [facility_name, address, contact_name, contact_email, contact_phone]
        if not all(required_fields):
            st.error("Please complete all required fields (marked *).")
        elif not agree:
            st.error("Please confirm authorization and agreement.")
        else:
            st.success("Thank you! Your information has been submitted for review. Our team will contact you within 1 business day.")
            st.markdown(
                "<p style='color:#888; font-size:1em;'>If you have urgent questions, please contact support@contrast-connect.com.</p>",
                unsafe_allow_html=True,
            )

# ---- FOOTER ----
st.markdown(
    "<hr><p style='font-size:0.95em; color:#666;'>© 2025 Contrast‑Connect. All rights reserved.<br>This form is HIPAA-aware and all data is handled in compliance with healthcare regulations.</p>",
    unsafe_allow_html=True,
)
