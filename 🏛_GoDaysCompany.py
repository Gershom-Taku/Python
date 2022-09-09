import importlib
from turtle import left, right
from click import style
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie
from sympy import N
from PIL import Image
import base64
import streamlit.components.v1 as components
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv
import pandas as pd
#from st_aggrid import AgGrid
import plotly.express as px
import io 

st.set_page_config(page_title ="WELCOME TO GoDays LANDING PAGE",page_icon= ":tada:",layout = 'wide') 
#st.sidebar.markdown("<img src= 'C:\\Users\\ADMIN\\Desktop\\images\\pic11.jpg' width = 100 />",unsafe_allow_html=True)

#Loading Assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)  
local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_kw5jwkm0.json")
#image_contact_form =  Image.open("images\pic7.png")
image_lottie_animation  = Image.open("images\pic3.png")

with st.container(): 
     html_temp = """
        <div style = "background-color:royalblue;padding:10px;border-radius:30px;width :auto;">
        <h1 style = "color:white;text-align:center;font-size:40px;">GoDays Is Your Best Site </h1>
        </div>
        """
     components.html(html_temp)
     st.write("---")
     left_column,right_column = st.columns(2)
     with left_column:
        #st.header("GoDays.")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">GoDays :</p>', unsafe_allow_html=True)
       # st.subheader("Get Connected With GoDays Now and Explore With Others:")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Get Connected With GoDays Now and Explore With Others:</p>', unsafe_allow_html=True)
        st.write("**Technology in your pocket is your privacy:**")
        st.write("""
                 
                **  **
                
                 """)
        
with right_column:
    st_lottie(lottie_coding,height= 300,key = "coding")
 #----------------------------------------------------------------------------------   
with st.container():
    st.write("---")
#    st.header("COMPANY INFORMATION")
    st.write("#####")
    image_column ,text_column = st.columns((1,2))
    with image_column:
        st.image(image_lottie_animation,width=300)
        
    with text_column:
        lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_mf5j5kua.json")

        #st.header("PRODUCTIVITY!")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">PRODUCTIVITY:</p>', unsafe_allow_html=True)
        #st.subheader("The new update for your productivity")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">The new update for your productivity:</p>', unsafe_allow_html=True)
        
        st.write("""
                 **Due to user-friendly design,it becomes intuitevely clear on how to use the 
                 the application.And so your team will be able to become 20% more productive than their peers
                 on the  market.**
                
                 - Thanks to our algorithims,you will be able to get rid of emotional burnout
                   from the team in advance.
                 
                 """
               )
        with text_column:
         st_lottie(lottie_coding,height= 300,key = "task")
        
         st.markdown("[Learn more>](https://godays.com)")
        
#----------------------------------------------------------------------------------------------------

#image_contact_form =  Image.open("images\pic7.png")
image_lottie_animation  = Image.open(r"images\pic5.png")
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_gqi90xdb.json")

with st.container():
     st.write("---")
     left_column,right_column = st.columns((1,2))
     with left_column:
#        st.header("Productivity!")
 #       st.subheader("What about productivity?:")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">What about productivity?:</p>', unsafe_allow_html=True)
        
    
        st.write("#####")
        st.write("""
                 
                **After you add a task for employees, our algorithm will begin to analyze
                the person according to the Assessment Center Methodology proccess.
                 After completing a series of tasks,
                you will be provided with all the data on the employee's performance.**
                
                 """)
        st.markdown("")
        with right_column:
            st_lottie(lottie_coding,height= 300,key = "productivity")
 #         st.image(image_lottie_animation,output_format="auto")
   
   
#---------------------------------------------------------------------------------------------------
image_lottie_animation  = Image.open(r"images\pic1.png")
with st.container():
    st.write("---")
#    st.header("COMPANY INFORMATION")
    st.write("#####")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(image_lottie_animation, width=300)
        
    with text_column:
        lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_VkOh76.json")
        #st.header("PRODUCTIVITY!")
       # st.subheader("Up to a number of 8 people and above in a team:")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Up to a number of 8 people and above in a team:</p>', unsafe_allow_html=True)
    
        st.write("""
                 **Communication with your team has become better than ever🤝.**
                
                One of the important elements of a successful team is to quickly receive or
                share information,
                and give thanks to modern security keys, you can not worry about data leakage.
            
                 """
                 )
        
        st.button(label= 'More about the FREE version', key=None, help=None, on_click=None, args=None, kwargs=None,  disabled=False)
        with text_column:
            st_lottie(lottie_coding,height= 300,key = "favourite")
        
#---------------------------------------------------------------------------------------------------------------
image_lottie_animation  = Image.open(r"images\pic6.png")

with st.container():
    st.write("---")
    left_column,right_column = st.columns((1,2))
    with right_column:
        lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_Hg1eiy.json")
#        st.header("Productivity!")
       # st.subheader("Already had an access of about 30 and above people in ONE organization:")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Already had an access of about 30 and above people in ONE organization:</p>', unsafe_allow_html=True)
        
        st.write("####")
        st.write("""
                 **Another very important part of a successful team is All with You.**
                 
                Up to 200 GB of cloud storage. And this means that all documents that are important
                for the company will always be with you, where you can view, edit, send and,
                most importantly, encrypt for additional protection at any time of the day.
                Given that ,the **Cloud Storage is already encrypted,which means that
                there is the possibility of additional protection for your  Very Important Documents**.
                
                 """)
        st.markdown("")
        st.write("[Learn More >](https://godays.com)")
        st.button(label= 'More about BUSINESS', key=None, help=None, on_click=None, args=None, kwargs=None,  disabled=False)
        with left_column:
          st.image(image_lottie_animation,output_format="auto",caption=None, width=350, clamp=False, channels="RGB")
          with right_column:
            st_lottie(lottie_coding,height= 250,key = "storage")
       
#--------------------------------------------------------------------------------------------------------------
#image_lottie_animation  = Image.open("images\pic9.png")

#image_lottie_animation  = Image.open("images\pic10.png")
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_4tz0wb4f.json")

with st.container():
    st.write("---")
    st.write("📱Widget.")
    left_column,right_column = st.columns((1,2))
    with left_column:
  
     #st.subheader("Due to convenient widgets, you will never miss important news:")
     st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
     st.markdown('<p class="font">Due to convenient widgets, you will never miss important news:</p>', unsafe_allow_html=True)
        
     st.write("####")
     st.write("""
             
                 **Widgets will help you at any time, because you don't have to open applications for nothing.
                 For example, to find out the plan for today or not to miss important messages from your team**
                 
                 """)
   
    with right_column: 
     st_lottie(lottie_coding,height= 300,key = "widget") 
#---------------------------------------------------------------------------------------------------------------------
image_lottie_animation  = Image.open(r"images\pic8.png")

with st.container():
    st.write("---")
    st.write("💪Emotional Health.")
    left_column,right_column = st.columns((1,2))
    with right_column:
        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_yIyBUk.json")
#        st.header("Productivity!")
       # st.subheader("🤾‍♀️Health:")
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">🤾‍♀️Health:</p>', unsafe_allow_html=True)
        st.write("####")
        st.write("""
                 
                **Hundreds of hours of research into human emotional health have helped 
                us to  understand and answer
                the three big questions of how, when, and why ?.**
                
            - How to overcome emotional burnout?
            - When to expect emotional burnout?
            - Why does emotional burnout occur?
                 """)
        st.button(label= 'And we have a special weapon for such a strong ENEMY', key=None, help=None, on_click=None, args=None, kwargs=None,  disabled=False)
        
        with left_column:
         st.image(image_lottie_animation,output_format="auto",caption=None, width=350, clamp=False, channels="RGB")
         with right_column: 
          st_lottie(lottie_coding,height= 300,key = "sport")
         st.markdown("")
    
#------------------------------------------------------------------------------------------------------------------------------------------------------     
        
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_2iszWM.json")
              
with st.container():
     st.write("---")   
    # st.header("Get in touch with GoDays team Now!:")
     st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
     st.markdown('<p class="font">Get in touch with GoDays team Now!:</p>', unsafe_allow_html=True)
     st.write("##") 
     
     contact_form = """
     <input type = "hidden" name = " _capture" value = "false">
     <form action="https://formsubmit.co/chototakudzwa8@gmail.com" method="POST">
     <input type="text" name="name" placeholder = "Your full name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <input type = "text" name = "company" placeholder = "Your company" required">
     <textarea  name = "message" placeholder = "Enter message" required></textarea>
     <button type="submit">Send</button>
</form>
     """   

     left_column ,right_column = st.columns((1,2))
     with left_column:
         st.markdown(contact_form,unsafe_allow_html = True)
     with right_column:
         st.empty()
             
     with right_column:
      st_lottie(lottie_coding,height= 300,key = "sent email")
         
hide_menu_style =    """
           <style>
           #MainMenu {visibility : hidden;}
           Footer:{visibility:hidden;}
           </style>
           
                     """
st.markdown(hide_menu_style,unsafe_allow_html=True)
            
with st.container():
     st.write("---")   
    # st.header("DOWNLOADS:")
     st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: blue;} 
        </style> """, unsafe_allow_html=True)
     st.markdown('<p class="font">DOWNLOADS:</p>', unsafe_allow_html=True)
     st.write("##") 

#creating a sample dataframe to download
df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [19.07, 72.87],columns=['latitude', 'longitude'])

#function to convert any dataframe to a csv file
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

#converting the sample dataframe
csv = convert_df(df)

#adding a download button to download csv file
st.download_button( 
    label="Download data as CSV",
    data=csv,
    file_name='sample_df.csv',
    mime='text/csv',
)

#defining sample text that to download
text_content = "Sample text"

#adding a download button to download text
st.download_button('Download sample text', text_content)

#adding a download button to download an image
#with open("imagename.png", "rb") as file:
 #   btn = st.download_button(
  #          label="Download image",
   #         data=file,
    #        file_name="imagename.png",
     #       mime="image/png"
      #    )
   
st.markdown('''
<style>
.element-container {
    background-color: white;
    opacity: 1;
}
.st-b7 {
    color: blue;
}
.css-nlntq9 {
    font-family: Source Sans Pro;
}
</style>
''', unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_bsPjV4.json")
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_P2uXE5.json")

st.write("------")
footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: none;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color:#5486ea ;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>DEVELOPED WITH GoDays COMPANY BY <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Takudzwa Gershom Choto </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
          