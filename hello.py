import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='My Webpage',page_icon=':tada:',layout='wide')


def load_lottieurl(url):
 r=requests.get(url)
 if r.status_code!=200:
  return None
 return r.json()

def local_css(file_name):
 with open(file_name) as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')
 

lottie_coding= load_lottieurl(  "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


with st.container():
  st.subheader('Hi!, I am Kesav :wave:')
  st.title('An Data Analyst and ML Engineer aspiring student')
  st.write('I am on the way of becoming a Data Analyst and Machine Learning Engineer and trying to implement Python in my daily life.')
  st.write('[Learn More from my Github repos ->](https://github.com/Kesav14)')

with st.container():
 st.write('---')
 left_column,right_column=st.columns(2)
 with left_column:
  st.header('What I do')
  st.write('##')
  st.write('''
  - I am a student from Coimbatore,Tamilnadu,India.
  - I am aspiring to be a Data Analyst and also the one to develop awesome Machine Learning models.
  - I also love to code in my free time.
  - I am currently learning Streamlit a Python library used to make good-looking web apps
            '''
           )
  st.write('[My Github Page](https://github.com/Kesav14)')

with right_column:
 st_lottie(lottie_coding,height=300,key='coding')

with st.container():
 st.write('---')
 st.header('My Projects')
 st.write('##')
 image_column,text_column=st.columns((1,2))
 with image_column:
  sales_dashboard=Image.open('images/sales.png')
  st.image(sales_dashboard,)
 with text_column:
  st.subheader('Sales Dashboard :bar_chart:')
  st.write('''
This is a sales dashboard where you can explore the sales by product and sales by hour
Click the below link to watch
           '''
           )
  st.markdown('[Click here -->](https://sales-dashboard-v1.onrender.com)')

with st.container():
 st.write('---')
 image_column,text_column=st.columns((1,2))
 with image_column:
  weather_app=Image.open('images/weather-app.png')
  st.image(weather_app)
 with text_column:
  st.subheader('Weather App using Tkinter Library ')
  st.write(f'''
          This is a python weather app made with the Python library called Tkinter 
           , used t make GUI apps. 
           Click the below link to download the file with a good background image.
           The link will direct you to my Github repository.''')
  st.markdown('[Click here -->](https://github.com/Kesav14/weatherapp)')
st.write('---')
st.subheader('Contact Me!')

contact_form= '''
<form action="https://api.web3forms.com/submit" method="POST">

  <input type="hidden" name="access_key" value="d08b3993-1ed1-4dac-b1bd-333524d98657">

  <input type="hidden" name="subject" value="About me Contact" autocomplete="off">

  <input type="text" name="name" placeholder="Your Name" required autocomplete="off">

  <input type="email" name="email" placeholder="Your Email" required autocomplete="off">

  <textarea name="message" placeholder="Your Message" required autocomplete="off"></textarea>

  <button type="submit">Submit</button>

</form>'''

left_column,right_column=st.columns(2)
with left_column:
 st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
 st.empty()