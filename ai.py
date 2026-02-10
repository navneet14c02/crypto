import streamlit as st
import google.generativeai as genai
from dhanhq import dhanhq
import time

# --- PAGE SETUP ---
st.set_page_config(page_title="AI SMC Trader", layout="wide")
st.title("?? AI Smart Money Trading Dashboard")

# --- SIDEBAR (Keys & Config) ---
st.sidebar.header("API Settings")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")
dhan_client = st.sidebar.text_input("Dhan Client ID", value="1109282855")
dhan_token = st.sidebar.text_input("Dhan Access Token", type="password")

# --- STRATEGY CONTEXT (From your SMC Files) ---
smc_context = """
Strategy: SMC (Smart Money Concepts)
Rules: 
1. Look for HTF POI.
2. Wait for LTF ChoCh (Change of Character).
3. Identify Order Block with Imbalance.
4. Entry on retest of OB/FVG.
"""

# --- MAIN INTERFACE ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Market Selection")
    symbol = st.selectbox("Select Index/Stock", ["NIFTY 50", "BANK NIFTY", "RELIANCE", "BTC-USDT"])
    run_bot = st.button("Start AI Bot")

with col2:
    st.subheader("Live AI Analysis & Signals")
    status_box = st.empty()
    signal_history = st.container()

# --- LOGIC ---
if run_bot:
    if not gemini_key or not dhan_token:
        st.error("Please enter API keys in the sidebar!")
    else:
        # Initialize APIs
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        dhan = dhanhq(dhan_client, dhan_token)
        
        st.info(f"Monitoring {symbol} using SMC Strategy...")
        
        while True:
            try:
                # 1. Fetch Price
                data = dhan.get_ltp({"symbol": symbol})
                price = data['data']['last_price']
                
                # 2. Gemini Analysis
                prompt = f"{smc_context}\nLive Price: {price}\nAction required? (Reply 'ALERT: BUY/SELL' or 'WAIT')"
                response = model.generate_content(prompt)
                res_text = response.text.strip()
                
                # 3. Display Signal
                status_box.metric(label=f"Current {symbol} Price", value=price)
                
                if "WAIT" not in res_text.upper():
                    signal_history.success(f"?? {res_text} at {time.strftime('%H:%M:%S')}")
                    # Yahan aap dhan.place_order() call kar sakte hain auto-trade ke liye
                
                time.sleep(10) # Refresh rate
            except Exception as e:
                st.error(f"Error: {e}")
                break
