#

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)





driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3641811861&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

password="123"

time.sleep(20)

email=driver.find_element_by_name("session_key")
email.send_keys("kaz@gmaill.com")


password=driver.find_element_by_name("session_password")
password.send_keys("kaz")


Signin=driver.find_element_by_class_name("btn-md btn-primary flex-shrink-0 cursor-pointersign-in-form__submit-btn--full-width")
Signin.click()

# or:

# password.send_keys(Keys.ENTER)

# To direct sign in ! 



#applying for a job :

#1) opening the job 

job=driver.find_element_by_Css_selector("#ember722 a") 
job.click()

#2) waiting for the options to be upload :

time.sleep(20)

#3) clicking on easy apply :

easy_apply=driver.find_element_by_id("ember1136")
easy_apply.click()

#4) waiting for the page to be uploaded :

time.sleep(20)

#5) filling the form :

email=driver.find_element_by_id("text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641413942-91851627-multipleChoice")
email.send_keys("kaz@gmaill.com")


phone_symbol=driver.find_element_by_id("text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641413942-91851619-phoneNumber-country")
phone_symbol.send_keys("25")

phone=driver.find_element_by_id("single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641413942-91851619-phoneNumber-nationalNumber")
phone.send_keys("32+6566226")


next=driver.find_element_by_id("ember1152")
next.click()

#6) waiting for the page to be uploaded :

time.sleep(20)


#7) fill the other form : 

next=driver.find_element_by_id("ember1152")
next.click()

#8) selecting additional option!

open_options=driver.find_element_by_id(
               "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641413942-91851603-multipleChoice"
                                      )
open_options.click()



# __________________________________________________________________________________________________________#



# Applying To All Jobs :


jobs=driver.find_elements_by_class_name("disabled ember-view job-card-container__link job-card-list__title")


for job in jobs:

    try :

    #1) opening the job 
        job.click()
        
        #2) waiting for the options to be upload :
        time.sleep(20)
        
        #3) clicking on easy apply :
        easy_apply=driver.find_element_class_name(
                                    "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary artdeco-button--disabled ember-view"
                                                )
        easy_apply.click()
        
        #4) waiting for the page to be uploaded :
        time.sleep(20)
        
        #5) filling the form 
        
        emails=driver.find_element_class_name("artdeco-text-input--input")
        emails.send_keys("Your Email")

        phone_symbol=driver.find_element_class_name("artdeco-text-input--input")
        phone_symbol.send_keys("Your Phone symbol")

        #6 submiting
        submit_button = driver.find_element_by_css_selector("footer button")
        submit_button.click()

        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        continue

    # here the exception will come when we dont find the submit directly , then we cancel it , so we lay on the depend buttom not on the next button 
    except NoSuchElementException:

        #restarting 
        cancel=driver.find_element_class_name("mercado-match")
        cancel.click()
        discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
        print("Complex application, skipped.")
        continue
    



driver.quit()

  

