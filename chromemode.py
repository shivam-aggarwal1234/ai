from selenium import webdriver as wb
from pywinauto.keyboard import SendKeys as sk
import pyttsx3
import speech_recognition as sr


#temp = 'open new tab'
#temp =temp.split()

def chmode():
    print('inside chrome file')
    engine = pyttsx3.init()
    re = sr.Recognizer()
    driver = wb.Chrome()

    driver.maximize_window()
    i=0
   
    while True:


        try:
            with sr.Microphone() as source:
                re.adjust_for_ambient_noise(source,duration=2)
                if i is 0:
                    engine.say('what can i serach')
                    engine.runAndWait()

                audio = re.listen(source)
                x = re.recognize_google(audio)
        except:
                print('cannot understand')

        #x = input('enter seaarch ')
        print(x)
        if(x=='exit' or x=='close'):
            break
        else:

            if(i!=0):
                sk('^t')
            windows = driver.window_handles
            driver.switch_to_window(windows[i])
            i+=1
            driver.get('http://www.google.com')
            driver.find_element_by_name('q').send_keys(x)
            driver.find_element_by_name('q').submit()
            #driver.implicitly_wait(5)
            driver.find_element_by_xpath("(//h3)[1]/a").click()
            del(x)


