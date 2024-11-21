from tkinter import VERTICAL
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from class3 import LoginBusinessScreen
from kivy.animation import Animation


# Set and fix the window size
Window.size = (500, 1000)
Window.minimum_width, Window.minimum_height = Window.size
Window.maximum_width, Window.maximum_height = Window.size

# KV language string
KV = '''
ScreenManager:
    MenuScreen:
    OtherScreen:
    AnotherScreen:
    LoginBusinessScreen:
    CautareClientiScreen:
    VizClientiScreen:
    InfoCautare1:
    InfoCautare2:
    InfoCautare3:
    InfoViz1:
    InfoViz2:
    InfoViz3:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 300

            MDLabel:
             
                text: 'FLYING BUSINESS,'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
      
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
             
            MDLabel:
                text: 'YOUR SWEETEST COPILOT.'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.65, 'center_y': 0.3}

            MDLabel:
                text: 'I am here to help your business fly high. Log in or sign up and let`s travel far into the world of successful businesses. i`ll help you on the way ^^'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/indieflower'
                font_size: '22sp'
                pos_hint: {'center_x': 0.55, 'center_y': 0.3}

            Widget:
                size_hint: None, None
                size: 400, 300

            MDRaisedButton:
                text: 'SIGN UP'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('other')
                

            MDRaisedButton:
                text: 'LOG IN'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('another')

            Widget:
                size_hint: None, None
                size: 400, 300  

<OtherScreen>:
    name: 'other'
    ScrollView:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: False
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
                
            MDLabel:
                text: 'EMAIL:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            MDTextField:
                id: email2_textfield  # Give an id to the MDTextField
                hint_text: "Enter your text"
                multiline: False    
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
                
            MDLabel:
                text: 'PASSWORD:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
            MDTextField:
                id: password_signup_textfield
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
            MDLabel:
                text: 'CONFIRM PASSWORD:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: password2_signup_textfield
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
            MDLabel:
                text: 'CITY:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: city_signup_textfield
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
            MDLabel:
                text: 'COUNTRY:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: country_signup_textfield
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}   
            MDLabel:
                text: 'COMPANY DESCRIPTION:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: company_signup_textfield
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
            MDRaisedButton:
                text: 'SIGN UP'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                #on_release: app.switch_screen('other')
                on_release: app.compare_passwords()

            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('menu')

           
            
     ###########################################################################       
<AnotherScreen>:
    name: 'another'
    BoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: False
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 800, 800
                
            MDLabel:
                text: 'EMAIL:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            MDTextField:
                id: email_textfield  # Give an id to the MDTextField
                hint_text: "Enter your text"
                multiline: False    
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
                
            MDLabel:
                text: 'PASSWORD:'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                hint_text: "Enter your text"
                multiline: False   
                password: True
                size_hint: (None, None)  # Disable size_hint to use absolute size
                size: 300, 300  # Set the desired width and height
                pos_hint: {'center_x': 0.1, 'center_y': 0.2}
            Widget:
                size_hint: None, None
                size: 200, 200

            MDRaisedButton:
                text: 'LOG IN'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('loginbusiness')
                on_release: app.print_textfield_text(email_textfield.text)

            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('menu')

            Widget:
                size_hint: None, None
                size: 400, 300  
<LoginBusinessScreen>
    name: 'loginbusiness'
    BoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 300

            MDLabel:
                text: app.business_name
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}

            Widget:
                size_hint: None, None
                size: 400, 300

            MDRaisedButton:
                text: 'CAUTARE CLIENTI'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')

            MDRaisedButton:
                text: 'VIZUALIZARE CLIENTI'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('vizclienti')
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('another')
            Widget:
                size_hint: None, None
                size: 400, 300  
 
<CautareClientiScreen>
    name: 'cautareclienti'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 300

            MDLabel:
                text: 'nume client 1'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 1'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infocautare1')
            MDLabel:
                text: 'nume client 2'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 2'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infocautare2')
            MDLabel:
                text: 'nume client 3'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 3'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infocautare3')
            Widget:
                size_hint: None, None
                size: 400, 200
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('loginbusiness')
           
            Widget:
                size_hint: None, None
                size: 400, 300  
<VizClientiScreen>
    name: 'vizclienti'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 300

            MDLabel:
                text: 'nume client 1'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 1'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infoviz1')
            MDLabel:
                text: 'nume client 2'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 2'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infoviz2')
            MDLabel:
                text: 'nume client 3'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            MDRaisedButton:
                text: 'vizualizare detalii client 3'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('infoviz3')
            Widget:
                size_hint: None, None
                size: 400, 200
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('loginbusiness')
           
            Widget:
                size_hint: None, None
                size: 400, 300
        
        
<InfoCautare1>
    name: 'infocautare1'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600

            MDLabel:
                text: '**detalii despre client 1**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')
<InfoCautare2>
    name: 'infocautare2'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600
          
            MDLabel:
                text: '**detalii despre client 12**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')
<InfoCautare3>
    name: 'infocautare3'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600

            MDLabel:
                text: '**detalii despre client 3**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')
<InfoViz1>
    name: 'infoviz1'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600

            MDLabel:
                text: '**detalii despre client 1**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')
<InfoViz2>
    name: 'infoviz2'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600

            MDLabel:
                text: '**detalii despre client 2**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')
<InfoViz3>
    name: 'infoviz3'
    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(10)
            padding: dp(10)
            md_bg_color: 253.0/255.0, 233.0/255.0, 146.0/255.0, 1
            Widget:
                size_hint: None, None
                size: 400, 600

            MDLabel:
                text: '**detalii despre client 3**'
                theme_text_color: "Secondary"
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                font_size: '24sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            Widget:
                size_hint: None, None
                size: 400, 600
            MDRaisedButton:
                text: 'BACK'
                font_name: 'C:/Users/Andreea/source/repos/amor/amor/carter'
                size_hint_x: 0.5
                size_hint_y: 0.2
                size: 300, 148
                pos_hint: {'center_x': 0.7, 'center_y': 1}
                md_bg_color: 1, 165.0/255.0, 0, 1
                on_release: app.switch_screen('cautareclienti')

'''

class MenuScreen(Screen):
    pass

class OtherScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class LoginBusinessScreen(Screen):
    pass
class CautareClientiScreen(Screen):
    pass
class VizClientiScreen(Screen):
    pass
class InfoCautare1(Screen):
    pass
class InfoCautare2(Screen):
    pass
class InfoCautare3(Screen):
    pass
class InfoViz1(Screen):
    pass
class InfoViz2(Screen):
    pass
class InfoViz3(Screen):
    pass


class MyApp(MDApp):
    business_name = """"BUSINESS NAME
    BUSINESS NAME
    BUSINESS NAME"""
    def build(self):
        self.screen_manager = Builder.load_string(KV)
        
        return self.screen_manager
        
    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def print_textfield_text(self, text):
        print(f"Text in the MDTextField: {text}")

    def compare_passwords(self):
        password1 = self.root.get_screen('other').ids.password_signup_textfield.text
        password2 = self.root.get_screen('other').ids.password2_signup_textfield.text

        if password1 == password2:
            print('Passwords match!')
        else:
            print('Passwords do not match!')

        
        
MyApp().run()
