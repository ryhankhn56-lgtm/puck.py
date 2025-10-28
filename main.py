import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_post

st.set_page_config(
        page_title="Pondering",
)

class MultiApp:

     def __init__(self):
          self.app = []
     def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

     def run():
         
         with st.sidebar:
             app = option_menu(
                 menu_title='pondering ',
                 options=['HOME','ACCOUNT','TRENDING','YOUR POSTS','ABOUT'],
                 icons=['house-fill','person-cicle','trophy-fill','chat-fill','info-circle-fill'],
                 menu_icon='chat-text-fill',
                 default_index=1,
                 styles={
                     "container": {"padding": "5!important","background-color":'black'},
         "icon": {"color": "white", "font-size": "23px"},
         "nav-link": {"color":"white","font-size": "20px", "text-align": "left","margin":"0px"},
         "nav-link-selected": {"background-color": "#02ab21"},}
                     
                )
             
             if app== 'HOME':
                 home.app()
             if app== 'ACCOUNT':
                 account.app()
             if app== 'TRENDING':
                 trending.app()
             if app== 'YOUR POSTS':
                 your_post()
             if app== 'ABOUT':
                 about()
        
   

    