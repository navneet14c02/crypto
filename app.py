import streamlit as st

# Page Configuration
st.set_page_config(page_title="Taxi App Prototype", page_icon="🚖")

# Title and Design
st.title("🚖 Mera Sarthi Booking")
st.markdown("### *Ola/Rapido Jaisa Prototype*")

# 1. User Input Section
col1, col2 = st.columns(2)
with col1:
    pickup = st.text_input("📍 Pickup Location", placeholder="Kahan se?")
with col2:
    drop = st.text_input("🏁 Drop Location", placeholder="Kahan jana hai?")

# 2. Vehicle Selection
st.write("---")
st.subheader("Gaadi Select Karein")
vehicle_type = st.radio(
    "Choose your ride:",
    ["🏍️ Bike (₹5/km)", "🚗 Car (₹12/km)", "🛺 Auto (₹8/km)"],
    horizontal=True
)

# 3. Booking Logic
if st.button("🚖 BOOK NOW", type="primary", use_container_width=True):
    if not pickup or not drop:
        st.error("Kripya Pickup aur Drop location dono bharein!")
    else:
        # Dummy Logic for Calculation
        distance = 12  # Maan lete hain 12 km door hai
        
        # Rate nikalna
        if "Bike" in vehicle_type:
            rate = 5
        elif "Car" in vehicle_type:
            rate = 12
        else:
            rate = 8
            
        total_fare = distance * rate
        
        # Success Message
        st.balloons()
        st.success(f"✅ Booking Confirmed!")
        st.info(f"🛣️ Distance: {distance} km\n💰 Total Fare: ₹{total_fare}")
        st.write(f"Driver is on the way to **{pickup}**...")

# Sidebar for extra info
with st.sidebar:
    st.header("Driver Status")
    st.write("🟢 5 Drivers Nearby")
    st.map() # Ye ek dummy map dikhayega
