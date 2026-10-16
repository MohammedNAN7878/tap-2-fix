# TAP 2 FIX — Complete booking block

## Run on Mac
```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```
Then open http://localhost:8501.

## Booking flow
Customer details, service requirements, and location method are collected in one booking form.
After submission, the app shows a message preview and a WhatsApp link to +91 7026152588.

## Location
- Paste a Google Maps link to include it in the message.
- Choose "Share location later in WhatsApp" to include the fallback text.
- Current location requires browser permission. The widget generates a Maps link; due to browser iframe restrictions, the customer copies it and pastes it into the form before preparing the booking again.
- Location is optional and not continuously tracked.
- Bookings are not stored in a database.
