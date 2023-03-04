import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

class ChatbotTest(unittest.TestCase):
    def setUp(self):
        # set up the webdriver
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("http://localhost:8080")
        time.sleep(10)
        
    def test_greeting(self):
        # send a greeting message
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Hello, chatbot!")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["Hi there, how can I help?",
        "Hello, there",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?"]
        self.assertTrue(chat_output.text in expected_output)
        
    def test_farewell(self):
        # send a farewell message
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Goodbye, chatbot!")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["See you later, thanks for visiting",
        "Have a nice day",
        "Bye! Come back again soon."]
        self.assertTrue(chat_output.text in expected_output)

    def test_prescription_requests_online(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I order my repeat prescription online?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "There are online services and apps you can use to order a repeat prescription. Some GP online services are only available in certain areas. Ask your GP surgery which service your GP surgery uses."
        self.assertEqual(chat_output.text, expected_output)

    def test_book_appointments(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I book an appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can book an appointment to see your GP online, by phone or in-person, by going into the surgery and talking to the receptionist."
        self.assertEqual(chat_output.text, expected_output)

    def test_medical_records(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I access my medical records?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["Medical records hold information about you. You'll have separate records for any NHS service you go to including your GP surgery, hospital, dentist or opticians. Your GP record includes information like any conditions or allergies you have and any medicine you're taking. There are 3 ways to access your medical records: using your NHS account, other online services and directly speaking to your GP surgery.",
        "Most patients who use online services will automatically be given access to more information added to their GP record from November 2022 onwards, including letters, test results and appointment notes."]
        self.assertTrue(chat_output.text in expected_output)

    def test_home_visits(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How to book a home visit?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["A GP will only visit you at home if they think that your medical condition requires it. A GP can also decide how urgently a visit is needed. Due to increasing demand GPs can no longer automatically visit any patient who requests a home visit. All visits must now be triaged and dealt with according to clinical need.",
        "If you live in their area, home visits can be made. Contact your GP for further information."]
        self.assertTrue(chat_output.text in expected_output)

    def test_specialist_referrals(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("I need a specialist referral")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["A specialist will only see you with a letter of referral from your GP. The letter will give the specialist essential background information, such as your medical history, and it'll also contain details that the specialist needs to pay particular attention to.",
        "You're entitled to ask for a referral for specialist treatment on the NHS. If you wish to be referred to a specialist in a particular field, such as a cardiologist or gynaecologist, you should see the GP you are registered with."]
        self.assertTrue(chat_output.text in expected_output)

    def test_appointment_arrival(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What time should I arrive for my appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You should aim to arrive at least 10 minutes before your appointment."
        self.assertEqual(chat_output.text,expected_output)

    def test_prove_identity_online_services(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I prove my identity to use online health services?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The two ways to prove your identity to use online health services are by proving who you are online using NHS login or by using details from your GP surgery to register."
        self.assertEqual(chat_output.text,expected_output)

    def test_online_health_service_register(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I register for online health services?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "To register to use online health services, you need to prove who you are. You can do this online using NHS login or by using details from your GP surgery to fill in a short registration form."
        self.assertEqual(chat_output.text,expected_output)

    def test_online_health_service_providers(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I find out which online health service I can use?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "To find out which online health service providers you can use, you should check your GP surgery's website to see what services are available online and which providers you can use."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_online_contact(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I get advice through online health services?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can contact your GP, nurse or other healthcare professional for advice and support through online health services."
        self.assertEqual(chat_output.text,expected_output)

    def test_online_health_record(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What sort of information can I see on my health record using online health services?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Through online health services, you can see parts of your health record, including information about medicines, vaccinations, and test results, as well as communications between your GP surgery and other services such as hospitals."
        self.assertEqual(chat_output.text,expected_output)

    def test_online_health_services(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What kind of health services can be accessed online if you are registered with a GP surgery?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you are registered with a GP surgery, you can access some health services online, such as contacting your GP, nurse or other healthcare professional for advice and support, ordering repeat prescriptions, seeing parts of your health record, including information about medicines, vaccinations and test results, seeing communications between your GP surgery and other services, such as hospitals, and booking, checking or cancelling appointments with a GP, nurse or other healthcare professional."
        self.assertEqual(chat_output.text,expected_output)
     
    def test_video_consultation_prescribe(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Will the GP or healthcare professional be able to prescribe medicine during a video consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you are prescribed any medicine, the doctor or healthcare professional will give you advice on how to take it. They may talk to you about the best way of getting your prescription."
        self.assertEqual(chat_output.text,expected_output)

    def test_video_consultation_questions(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can you ask questions during a video consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Yes, a video call is very similar to a face-to-face appointment. You will get the same care."
        self.assertEqual(chat_output.text,expected_output)

    def test_video_consultation_issues(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can you rebook your appointment if the video call does not work or you do not have a signal?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If your video call does not work or you do not have signal, they will try a phone call instead. If this is not possible, you will be able to rebook your appointment."
        self.assertEqual(chat_output.text,expected_output)

    def test_during_video_consultation(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What happens during a video consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If a GP, doctor or healthcare professional recommends you have a video call, you will get a text, email or letter with a date and time for the appointment. A video call is very similar to a face-to-face appointment. You will get the same care. The GP, doctor or healthcare professional will ask you questions about your health to work out the best treatment for you. You can also ask any questions you may have."
        self.assertEqual(chat_output.text,expected_output)

    def test_prepare_video_consultation(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What do I need for a video consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "To have a video consultation you need: a smartphone, tablet or computer that allows video calling – remember to make sure your microphone and camera are switched on, an internet connection, a well-lit, quiet and private space so the GP, nurse or other health professional can see you clearly"
        self.assertEqual(chat_output.text,expected_output)

    def test_video_consultation(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is a video consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "A video call is very similar to a face-to-face appointment. You will get the same care. This is where you speak to a doctor or healthcare professional using the video camera in your smartphone, tablet or computer."
        self.assertEqual(chat_output.text,expected_output)

    def test_face_to_face_changes(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How has face-to-face appointments changed due to the pandemic?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Appointments may take place by phone, video, or face-to-face depending on your clinical need."
        self.assertEqual(chat_output.text,expected_output)

    def test_online_consultation(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is an online consultation?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Most GP surgeries, hospitals, mental health services and community care services now offer video consultations. This is where you speak to a doctor or healthcare professional using the video camera in your smartphone, tablet or computer."
        self.assertEqual(chat_output.text,expected_output)

    def test_GP_sick_note(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can my GP provide me with a sick note?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Yes, if you are unable to work due to illness or injury, your GP can provide you with a sick note to give to your employer. The sick note will outline the duration of your illness or injury and any limitations you may have on your ability to work."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_sick_note(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is the process for getting a sick note?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Sick notes are free if the employee has been ill for more than 7 days when they ask for one. The healthcare professional might charge a fee if the employee has been ill for 7 days or less."
        self.assertEqual(chat_output.text,expected_output)

    def test_GP_visit(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How often should I see my GP?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The frequency of your visits to your GP will depend on your individual health needs. Some people may only need to see their GP once or twice a year, while others may need more frequent check-ups."
        self.assertEqual(chat_output.text,expected_output)

    def test_mental_health(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can my GP provide mental health support?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can receive a mental health referral from your GP. When you talk to your GP about your mental health they'll listen, give you advice and introduce you to a mental health service they think will be most helpful to you."
        self.assertEqual(chat_output.text,expected_output)

    def test_change_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I change my registered GP?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can change your GP surgery if you need to. This might be because: you have moved, you have had problems with your current practice, you were removed from the patient list. You should tell the GP surgery if you change address or move out of the area."
        self.assertEqual(chat_output.text,expected_output)

    def test_find_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I find a GP surgery in the area where I want to register?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can find a GP on the NHS website."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_home_visit_outside_area(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can a GP surgery offer home visits if I register with them from outside their area?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you live outside of their area, the GP surgery might not be able to offer home visits. Other arrangements might be made if you are not well enough to go to the GP surgery. Contact your GP for further information."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_refuse_registration_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What are some reasons that a GP surgery may refuse registration?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The GP surgery can refuse registration for reasons such as they are not taking new patients or it's too far away from your home and you need home visits."
        self.assertEqual(chat_output.text,expected_output)

    def test_restriction_outside_area_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Are there any restrictions on registering with a GP surgery outside my area?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The surgery will decide if they can accept you as a regular patient or accept you without home visits."
        self.assertEqual(chat_output.text,expected_output)

    def test_outside_area_register_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I register with a GP surgery outside the area I live?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Yes, you can. However, the GP surgery can refuse registration for reasons such as they are not taking new patients or it's too far away from your home and you need home visits."
        self.assertEqual(chat_output.text,expected_output)

    def test_register_GP(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I register with a GP?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Anyone in England can register with a GP surgery. It's free to register. You do not need proof of address or immigration status, ID or an NHS number. GP surgeries are usually the first contact if you have a health problem. They can treat many conditions and give health advice. They can also refer you to other NHS services."
        self.assertEqual(chat_output.text,expected_output)

    def test_test_results(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I access my test results?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you are registered for online service you can access your test results directly via the NHS app, otherwise you should call your GP."
        self.assertEqual(chat_output.text,expected_output)

    def test_medical_records_online(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I access my medical records using online services?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You might be able to use other GP online services and apps to get your GP record. First, you need to register for online services and prove who you are. You'll need to ask your GP surgery for online access to your full record, or you'll only see your medicines and allergies. Some services and apps are only available in certain areas. Ask your GP surgery which one you can use."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_medical_records_NHS(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I access my medical records using my NHS account?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can get your GP record by logging into your account using the NHS app or NHS website. First, you need to register for online services and prove who you are. You can do this when you create an account.You'll need to ask your GP surgery for online access to your full record, or you'll only see your medicines and allergies."
        self.assertEqual(chat_output.text,expected_output)

    def test_travel_vaccinations(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I get travel vaccinations from my GP?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If the GP practice is signed up to provide NHS travel vaccines, these can be provided to you free of charge. Other non-NHS travel vaccines may be charged for by the GP."
        self.assertEqual(chat_output.text,expected_output)

    def test_flu_vaccinations(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I receive a flu vaccination at the surgery?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you're eligible for a free flu vaccine, you can book an appointment at your GP surgery."
        self.assertEqual(chat_output.text,expected_output)

    def test_complaints(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is the complaints process?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can either complain to the NHS service provider directly (such as a GP, dentist surgery or hospital) or to the commissioner of the services, which is the body that pays for the NHS services you use. You cannot apply to both."
        self.assertEqual(chat_output.text,expected_output)

    def test_out_of_hours(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Who do I contact in the case of a medical emergency outside of surgery hours?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If your GP surgery is closed, call 999 if it is an emergency or 111 if you have any urgent queries."
        self.assertEqual(chat_output.text,expected_output)

    def test_opening_hours(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What are the practice's opening hours?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The opening hours for most GP practices are 8:00 am to 6:30 pm on any day from Monday to Friday, excluding bank holidays."
        self.assertEqual(chat_output.text,expected_output)

    def test_cancellation_policy(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is the policy on cancelling appointments?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Cancellations can be done online or over the phone. Cancellations notified less than 30 minutes before the appointment time will be recorded as failure to attend (DNA)."
        self.assertEqual(chat_output.text,expected_output)

    def test_no_appointment(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I see a GP without an appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "It is usually necessary to make an appointment to see a GP in the UK. However, some practices offer walk-in clinics or same-day appointments for urgent concerns."
        self.assertEqual(chat_output.text,expected_output)

    def test_wait_appointment(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How long do I have to wait to book an appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The waiting time for an appointment can vary depending on the availability of your GP and the urgency of your condition. If you require urgent medical attention, your GP may be able to offer you an appointment on the same day."
        self.assertEqual(chat_output.text,expected_output)

    def test_evening_weekend_appointment(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can you access evening and weekend appointments?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Some GP surgeries offer evening and weekend appointments. Appointments are available from 6.30-8pm in the evenings, 9am to 5pm on Saturdays and Sundays. You can request to book an appointment during these times by calling your GP."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_missed_appointment(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What should I do if I missed my appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "The first time a patient fails to attend a booked appointment we will send them a DNA (did not attend) letter reminding them that in future they must cancel appointments if they are unable to attend. After three failure to attend letters we will consider advising you to register with another surgery."
        self.assertEqual(chat_output.text,expected_output)


    def test_appointment_online(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I cancel an appointment online?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you are registered with a GP surgery, you can use their online services to book, check or cancel appointments with a healthcare professional. Most GP clinics have online services to book appointments such as SystmOnline."
        self.assertEqual(chat_output.text,expected_output)

    def test_appointment_changes(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I reschedule an appointment?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can book,cancel or change your GP appointment by contacting GP surgery by phone or through their website."
        self.assertEqual(chat_output.text,expected_output)

    def test_appointment_urgent(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How do I book an appointment urgently?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Call your GP surgery if you need an urgent appointment. If your GP surgery is closed, call 999 if it is an emergency or 111 if you have any urgent queries"
        self.assertEqual(chat_output.text,expected_output)

    def test_GP_repeat_prescription(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Do I need to see my GP to order a repeat prescription?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You do not need to see a GP to order a repeat prescription. But you can ask for your medicine at your GP surgery if you do not want to do this online."
        self.assertEqual(chat_output.text,expected_output)

    def test_about_repeat_prescription(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("What is a repeat prescription?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "If you take medicine regularly you'll usually have a repeat prescription. This means you can order your medicine when you need it without having to see a GP until your next medicine review."
        self.assertEqual(chat_output.text,expected_output)

    def test_prescription_NHS(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Can I use my NHS account to order a repeat prescription?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "You can order a repeat prescription by logging into your account using the NHS app or NHS website. If you're asked to nominate a pharmacy, you can only nominate a high street pharmacy.You'll be able to collect your medicine in person when it's ready. Some high street pharmacies also deliver."
        self.assertEqual(chat_output.text,expected_output)

    def test_prescription(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("How can I get a repeat prescription?")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Ask your GP sugery how you should let them know when you need your repeat prescription. They can send your request to a pharmacy."
        self.assertEqual(chat_output.text,expected_output)
    
    def test_thank_you(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys("Thank you")
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = ["Happy to help!", "Any time!", "My pleasure"]
        self.assertTrue(chat_output.text in expected_output)

    def test_random_string(self):
        chat_input = self.driver.find_element(by=By.XPATH , value = "//input[@id='textInput']")
        chat_input.send_keys(" ".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)))
        chat_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # check if the response matches the expected output
        chat_output = self.driver.find_element(by=By.XPATH , value ="//div[@class='msg left-msg']//div[@class='msg-text']")
        expected_output = "Sorry, I am still learning. To help you further, you can find out more information at https://www.nhs.uk/nhs-services/gps/"
        self.assertEqual(chat_output.text,expected_output)

    def tearDown(self):
        # close the webdriver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
