import random
import streamlit as st
import pandas as pd
from datetime import date
today = date.today()
date = today.strftime("%B %d, %Y")
data = pd.read_csv("mar.csv")
listofhs = data["mr_horoscope"].values.tolist()
horoscope = random.choice(listofhs)
st.title("दैनिक राशी भविष्य")
st.header("ऋषि विनायक महाराज ")
st.subheader(f"दिनांक {date}")
zodiac_sign = st.sidebar.selectbox("तुमची रास निवडा ",("मेष","वृषभ","मिथुन","कर्क","सिंह","कन्या","तूळ","वृश्चिक","धनू","मकर","कुंभ","मीन"))
st.title(f"{zodiac_sign} राशी")
image = f"marathi\\{zodiac_sign}.png"
st.image(image)
lucky_number = random.randint(1,100)
listofcolor = ["नारिंगी","निळा","पोपटी","पांढरा","लाल","मोरपिशी","निळा","किरमिजी","पिवळा","राखाडी","जांभळा","सोनेरी"]
lucky_color = random.choice(listofcolor)
st.write(f"{horoscope}")
st.write(f"आजचा शुभ अंक {lucky_number} आहे.")
st.write(f"आजचा शुभ रंग {lucky_color}  आहे. ")
