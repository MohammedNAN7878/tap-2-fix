import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import quote

st.set_page_config(page_title="TAP 2 FIX | Doorstep Mobile Repair", page_icon="📱", layout="wide")

WHATSAPP_NUMBER = "917026152588"  # +91 7026152588
PHONE_DISPLAY = "7026152588"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root{--blue:#0797ff;--blue2:#32b4ff;--line:#1c3448}
html,body,[class*="css"]{font-family:Inter,sans-serif}
.stApp{background:radial-gradient(ellipse at 75% 0%,#0b2033 0%,#05090e 43%,#030609 100%);color:#f5f8fc}
.block-container{max-width:1180px;padding-top:1.5rem;padding-bottom:3rem}
h1,h2,h3,p{color:#f5f8fc}
.brand{font-size:1.05rem;font-weight:900;letter-spacing:.08em}.brand span{color:var(--blue)}
.eyebrow{color:var(--blue2);font-size:.78rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.hero-title{font-size:clamp(2.7rem,6vw,5rem);line-height:.98;font-weight:900;letter-spacing:-.055em;margin:.7rem 0 1.2rem}
.hero-title span{color:var(--blue)}.subtle{color:#b8c6d4;font-size:1.05rem;line-height:1.7}
.panel{background:linear-gradient(145deg,rgba(12,24,36,.96),rgba(5,10,16,.96));border:1px solid var(--line);border-radius:18px;padding:1.2rem;height:100%}
.small-label{color:#8fa5b8;font-size:.8rem}
div.stButton>button,div.stFormSubmitButton>button{border-radius:999px;border:1px solid var(--blue);background:var(--blue);color:white;font-weight:800;min-height:2.8rem}
a{color:var(--blue2)!important}hr{border-color:#1b2d3e}
[data-testid="stTextInput"] input,[data-testid="stTextArea"] textarea,[data-testid="stSelectbox"] div[data-baseweb="select"]{background:#0b141e;color:#f5f8fc}
.footer{color:#8fa0b1;font-size:.82rem;text-align:center;padding-top:1rem}
</style>
""", unsafe_allow_html=True)

def wa_link(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

a,b=st.columns([2,3],vertical_alignment="center")
with a:
    st.markdown('<div class="brand">📱 TAP <span>2</span> FIX</div><div class="small-label">WE DELIVER. WE FIX. AT YOUR DOORSTEP.</div>',unsafe_allow_html=True)
with b:
    cols=st.columns(4)
    for col,label,anchor in zip(cols,["Home","Services","Book a Repair","Contact"],["#home","#services","#booking","#contact"]):
        with col: st.markdown(f'<div style="text-align:center;padding-top:.4rem"><a href="{anchor}" style="text-decoration:none;font-weight:700">{label}</a></div>',unsafe_allow_html=True)
st.markdown('<div id="home"></div>',unsafe_allow_html=True)
st.divider()

l,r=st.columns([1.05,.95],gap="large",vertical_alignment="center")
with l:
    st.markdown('<div class="eyebrow">MOBILE REPAIR & ACCESSORIES AT YOUR DOORSTEP</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero-title">BROKEN PHONE?<br><span>WE COME TO YOU.</span></div>',unsafe_allow_html=True)
    st.markdown('<p class="subtle">Display repair, screen guard installation, and mobile accessories delivered with convenience in Davanagere.</p>',unsafe_allow_html=True)
    x,y=st.columns(2)
    with x: st.link_button("🛠️ BOOK A REPAIR","#booking",use_container_width=True)
    with y: st.link_button("CHAT ON WHATSAPP ↗",wa_link("Hi TAP 2 FIX, I would like to enquire about your services."),use_container_width=True)
with r:
    st.markdown('<div class="panel" style="min-height:280px;display:flex;flex-direction:column;justify-content:center;background:radial-gradient(circle at 70% 35%,#12395c 0%,#0a1724 35%,#070c12 75%)"><div style="font-size:5.5rem;text-align:center">📱</div><div style="text-align:center;font-size:1.3rem;font-weight:900">TAP <span style="color:#0797ff">2</span> FIX</div><div style="text-align:center;color:#aebfd0;margin-top:.6rem">REPAIRS • PROTECTION • ACCESSORIES</div></div>',unsafe_allow_html=True)

st.markdown('<div id="services"></div><div class="eyebrow">OUR SERVICES</div>',unsafe_allow_html=True)
st.header("Mobile help, made convenient.")
s1,s2,s3=st.columns(3,gap="medium")
services=[
(s1,"📱","Display Repair & Replacement","Enquire about cracked, damaged, or malfunctioning displays.","Hi TAP 2 FIX, I want to enquire about display repair. My phone model is: "),
(s2,"🛡️","Screen Guard Installation","Ask about screen guard options and installation.","Hi TAP 2 FIX, I want to enquire about screen guard installation. My phone model is: "),
(s3,"🎧","Accessories Delivery","Ask about covers, chargers, cables, and available accessories.","Hi TAP 2 FIX, I want to enquire about accessories. I need: ")]
for col,icon,title,desc,msg in services:
    with col:
        st.markdown(f'<div class="panel"><div style="font-size:1.8rem">{icon}</div><h3>{title}</h3><p style="color:#b8c6d4;line-height:1.6">{desc}</p></div>',unsafe_allow_html=True)
        st.link_button("ENQUIRE ON WHATSAPP ↗",wa_link(msg),use_container_width=True)

st.markdown('<div id="booking"></div>',unsafe_allow_html=True)
st.divider()
st.markdown('<div class="eyebrow">ONE-STEP BOOKING</div>',unsafe_allow_html=True)
st.header("Tell us what you need and share your location")
st.markdown('<p class="subtle">Complete your details and choose your location in this single booking section. Location is optional and is shared only when you choose to send the WhatsApp message.</p>',unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("### Booking details and location")
    st.caption("Enter your details, service requirements, and location in one place. The location is optional.")

    with st.form("integrated_booking"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full name *")
            customer_phone = st.text_input("Contact number *")
            area = st.text_input("Area / locality in Davanagere *")
            brand = st.text_input("Phone brand and model")
        with c2:
            service = st.selectbox(
                "Service required *",
                [
                    "Display repair / replacement",
                    "Screen guard installation",
                    "Accessories delivery",
                    "Other",
                ],
            )
            preferred = st.text_input("Preferred date / time (optional)")
            details = st.text_area("Additional details (optional)", height=100)

        st.markdown("#### Location")
        loc_method = st.radio(
            "How would you like to share your location?",
            [
                "Use my current location",
                "Paste a Google Maps link",
                "Share location later in WhatsApp",
            ],
            key="loc_method_single_block",
        )
        location_link_input = st.text_input(
            "Google Maps location link (if available)",
            placeholder="Paste a Google Maps link here",
            key="location_link_single_block",
        )
        st.caption(
            "For current location, tap Get current location after submitting this form. "
            "Your browser will ask permission. You can also paste a Maps link or share later."
        )
        submitted = st.form_submit_button("PREPARE WHATSAPP BOOKING", use_container_width=True)

    # Current-location capture runs in the main page, with a supported component-to-Streamlit
    # return channel. The link is persisted in session state when received.
    if submitted:
        if not name.strip() or not customer_phone.strip() or not area.strip():
            st.error("Please complete your name, contact number, and area.")
        else:
            st.session_state["booking_data"] = {
                "name": name.strip(),
                "phone": customer_phone.strip(),
                "area": area.strip(),
                "brand": brand.strip(),
                "service": service,
                "preferred": preferred.strip(),
                "details": details.strip(),
                "loc_method": loc_method,
                "location_link": location_link_input.strip(),
            }
            st.session_state["booking_ready"] = True

    if st.session_state.get("booking_ready"):
        data = st.session_state["booking_data"]
        st.markdown("---")
        st.markdown("### Current location")
        if data.get("loc_method") == "Use my current location":
            st.write("Tap below to request your current location. If it is unavailable, paste a Google Maps link into the field above and prepare the booking again.")
            components.html(
                """
                <div style="font-family:Arial,sans-serif;padding:12px;border:1px solid #1c3448;border-radius:12px;background:#0b141e;color:#f5f8fc">
                  <button id="getloc" style="background:#0797ff;border:0;border-radius:24px;color:white;padding:12px 16px;font-weight:bold;cursor:pointer;width:100%">Get current location</button>
                  <p id="status" style="font-size:13px;color:#b8c6d4">Location is requested only when you tap the button.</p>
                  <script>
                    const btn = document.getElementById('getloc');
                    const status = document.getElementById('status');
                    btn.addEventListener('click', () => {
                      if (!navigator.geolocation) {
                        status.textContent = 'Location is not available in this browser. Paste a Google Maps link instead.';
                        return;
                      }
                      status.textContent = 'Requesting location permission...';
                      navigator.geolocation.getCurrentPosition(
                        (pos) => {
                          const url = 'https://www.google.com/maps?q=' +
                            pos.coords.latitude + ',' + pos.coords.longitude;
                          status.innerHTML = 'Location link created. Copy the link below into the Google Maps location field in the form, then prepare the booking again.';
                          const input = document.createElement('input');
                          input.value = url;
                          input.readOnly = true;
                          input.style.width = '100%';
                          input.style.padding = '8px';
                          input.style.marginTop = '8px';
                          input.style.boxSizing = 'border-box';
                          status.appendChild(input);
                          const copy = document.createElement('button');
                          copy.textContent = 'Copy Maps link';
                          copy.style.marginTop = '8px';
                          copy.style.padding = '8px 12px';
                          copy.onclick = async () => {
                            try { await navigator.clipboard.writeText(url); copy.textContent = 'Copied - paste it into the form'; }
                            catch (e) { input.select(); document.execCommand('copy'); copy.textContent = 'Copied - paste it into the form'; }
                          };
                          status.appendChild(copy);
                          const open = document.createElement('a');
                          open.href = url;
                          open.target = '_blank';
                          open.textContent = ' Open in Google Maps';
                          open.style.display = 'block';
                          open.style.marginTop = '8px';
                          open.style.color = '#32b4ff';
                          status.appendChild(open);
                        },
                        (err) => {
                          status.textContent = err.code === 1
                            ? 'Permission denied. Allow location permission or paste a Google Maps link.'
                            : 'Could not get location. Paste a Google Maps link instead.';
                        },
                        { enableHighAccuracy: true, timeout: 15000, maximumAge: 0 }
                      );
                    });
                  </script>
                </div>
                """,
                height=210,
            )

        # Use the link saved when the form was submitted. The current-location
        # component explicitly asks the user to copy/paste its link into the form.
        final_location = data.get("location_link", "").strip()
        if data.get("loc_method") == "Share location later in WhatsApp" or not final_location:
            location_text = "I will share my location in WhatsApp."
        else:
            location_text = final_location

        optional_lines = []
        if data["brand"]:
            optional_lines.append(f"Phone model: {data['brand']}")
        if data["details"]:
            optional_lines.append(f"Additional details: {data['details']}")
        optional_lines.append(
            f"Preferred time: {data['preferred']}"
            if data["preferred"]
            else "Preferred time: Flexible"
        )

        final_msg = (
            "TAP 2 FIX | SERVICE REQUEST\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "CUSTOMER DETAILS\n"
            f"Name: {data['name']}\n"
            f"Contact: {data['phone']}\n"
            f"Area: {data['area']}\n\n"
            "SERVICE DETAILS\n"
            f"Requested service: {data['service']}\n"
            + "\n".join(optional_lines)
            + "\n\nLOCATION\n"
            + location_text
            + "\n\nPlease confirm availability and pricing. Thank you!"
        )

        st.markdown("### WhatsApp message preview")
        st.text_area("Review your complete message", final_msg, height=280, disabled=True)
        st.link_button(
            "SEND BOOKING DETAILS + LOCATION TO WHATSAPP",
            wa_link(final_msg),
            use_container_width=True,
        )
        st.caption(
            "WhatsApp opens with the prepared message. You must press Send in WhatsApp. "
            "The app does not save bookings to a database or track location in the background."
        )

st.markdown('<div id="contact"></div>',unsafe_allow_html=True)
st.divider()
c1,c2,c3=st.columns([1.2,1,1.2])
with c1:
    st.markdown('<div class="eyebrow">ABOUT TAP 2 FIX</div>',unsafe_allow_html=True)
    st.markdown("**Convenient mobile services, at your doorstep.**")
    st.write("Enquire about phone repair, screen protection, and mobile accessories.")
with c2:
    st.markdown('<div class="eyebrow">SERVICE AREA</div>',unsafe_allow_html=True)
    st.markdown("📍 **Davanagere, Karnataka, India**")
with c3:
    st.markdown('<div class="eyebrow">GET IN TOUCH</div>',unsafe_allow_html=True)
    st.markdown(f"☎️ **{PHONE_DISPLAY}**")
    st.link_button("CHAT ON WHATSAPP ↗",wa_link("Hi TAP 2 FIX, I'd like to enquire about your services."),use_container_width=True)
st.markdown('<div class="footer">TAP 2 FIX · WE DELIVER. WE FIX. AT YOUR DOORSTEP.<br>Service area: Davanagere, Karnataka · Confirm pricing and availability before arranging service.</div>',unsafe_allow_html=True)
