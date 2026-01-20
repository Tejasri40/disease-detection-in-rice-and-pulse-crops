import streamlit as st
from PIL import Image
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Image as RLImage,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from src.services.auth_service import AuthService
from src.services.prediction_service import PredictionService
from src.model_config import MODELS, get_model_path
from auth import create_users_table
from data.disease_info import DISEASE_INFO


# ---------------- DB INIT ----------------
create_users_table()
auth_service = AuthService()
prediction_service = PredictionService()

st.set_page_config(page_title="Crop Disease Detection", layout="wide")


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- AUTH ----------------
if not st.session_state.logged_in:
    st.title("🔐 User Authentication")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if auth_service.login(username, password):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Register"):
            if auth_service.register(new_user, new_pass):
                st.success("Account created. Please login.")
            else:
                st.error("Username already exists")

    st.stop()


# ---------------- SIDEBAR ----------------
st.sidebar.title("Menu")
page = st.sidebar.radio("Select Option", ["Disease Prediction", "Chatbot Assistance"])

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()


# ---------------- PDF FUNCTION ----------------
def generate_pdf(image_path, label, conf):
    file_name = "Disease_Report.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    info = DISEASE_INFO.get(label.lower(), {})

    # Title
    elements.append(Paragraph("<b>Disease Detection Report</b>", styles["Title"]))
    elements.append(Spacer(1, 15))

    # Image
    elements.append(RLImage(image_path, width=300, height=180))
    elements.append(Spacer(1, 20))

    # Table
    table = Table(
        [
            ["Crop", info.get("crop", "N/A")],
            ["Detected Disease", label],
            ["Confidence", f"{conf:.2f}%"]
        ],
        colWidths=[150, 250]
    )
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))

    # Description
    elements.append(Paragraph(f"<b>Description:</b> {info.get('description', 'N/A')}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Symptoms
    elements.append(Paragraph(f"<b>Symptoms:</b> {info.get('symptoms', 'N/A')}", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # Treatment Guidance
    elements.append(Paragraph("<b>Treatment Guidance:</b>", styles["Normal"]))
    elements.append(Spacer(1, 8))
    for step in info.get("treatment_guidance", []):
        elements.append(Paragraph(f"- {step}", styles["Normal"]))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 15))

    # Preventive Measures
    elements.append(Paragraph("<b>Preventive Measures:</b>", styles["Normal"]))
    elements.append(Spacer(1, 8))
    for step in info.get("prevention", []):
        elements.append(Paragraph(f"- {step}", styles["Normal"]))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 20))

    # Footer
    elements.append(
        Paragraph(
            f"<font size=9>Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}</font>",
            styles["Normal"]
        )
    )

    doc.build(elements)
    return file_name


# ---------------- UI RESPONSE ----------------
def show_curing_response(label):
    info = DISEASE_INFO.get(label.lower())
    if not info:
        return

    st.markdown("---")
    st.subheader("Crop Treatment Advisory")

    # Basic info
    st.markdown(f"**🌾 Crop:** {info['crop']}")
    st.markdown(f"**⚠️ Severity:** {info['severity']}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Description
    st.markdown("**📄 Description**")
    st.write(info["description"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Symptoms BELOW description
    st.markdown("**🔍 Symptoms**")
    st.write(info["symptoms"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Treatment Guidance
    st.markdown("### 🌱 Treatment Guidance")
    for step in info["treatment_guidance"]:
        st.write(f"• {step}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Preventive Measures
    st.markdown("### 🛡️ Preventive Measures")
    for step in info["prevention"]:
        st.write(f"• {step}")



# ---------------- DISEASE PREDICTION ----------------
if page == "Disease Prediction":
    st.title("🌾 Crop Disease Detection System")

    uploaded = st.file_uploader("Upload Leaf Image", ["jpg", "png", "jpeg"])
    model_choice = st.selectbox("Select Model", MODELS.keys())

    if uploaded:
        image = Image.open(uploaded)
        st.image(image, width=220)

        with open("temp.jpg", "wb") as f:
            f.write(uploaded.getbuffer())

        if st.button("Predict Disease"):
            model_path = get_model_path(model_choice)
            label, conf = prediction_service.predict(model_path, "temp.jpg")

            st.success(f"🦠 Disease Detected: {label}")
            st.info(f"🎯 Confidence: {conf:.2f}%")

            show_curing_response(label)

            with open(generate_pdf("temp.jpg", label, conf), "rb") as pdf:
                st.download_button(
                    "📄 Download Report as PDF",
                    pdf,
                    file_name="Disease_Report.pdf",
                    mime="application/pdf"
                )


# ---------------- CHATBOT ----------------
elif page == "Chatbot Assistance":
    st.title("🤖 Crop AI Assistant")
    st.components.v1.html("<h4>Chatbot integrated here</h4>", height=500)
