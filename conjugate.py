import selenium
from selenium import webdriver
import nltk
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import googletrans
from tqdm import tqdm
from googletrans import Translator
import warnings


def conjugate():
    warnings.filterwarnings("ignore")
    tense = input("Enter the tense: ")
    tense = tense.capitalize()
    pronoun = input("Enter the pronoun: ")
    pronoun = pronoun+' '
    # pronoun = pronoun.lower()
    verb = input("Enter the verb to conjugate for: ")
    verb = verb.lower()

    t1 = time.time()
    path = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(path, options=options)

    driver.get("https://conjugator.reverso.net/conjugation-german.html")

    search = driver.find_element(By.ID, 'txtVerb')
    search.send_keys(verb)
    search.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-block-api")))

    print()

    results = element.text

    results = results.split('\n')

    index = results.index('KONJUNKTIV I')
    indikativ = results[:index]
    indikativ.remove('Advertising')
    prasens_index = indikativ.index('Präsens')
    prateritum_index = indikativ.index('Präteritum')
    futur1_index = indikativ.index('Futur I')
    plusq_index = indikativ.index('Plusquamperfekt')
    perfekt_index = indikativ.index('Perfekt')
    futur2_index = indikativ.index('Futur II')

    prasens = indikativ[prasens_index:prateritum_index]
    prateritum = indikativ[prateritum_index:futur1_index]
    futur1 = indikativ[futur1_index:perfekt_index]
    perfekt = indikativ[perfekt_index:plusq_index]
    plusq = indikativ[plusq_index:futur2_index]
    futur2 = indikativ[futur2_index:]

    if (tense == 'Prasens'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in prasens:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)
        else:
            for word in prasens:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)
    elif (tense == 'Prateritum'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in prateritum:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)
        else:
            for word in prateritum:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)

    elif (tense == 'Futur I'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in futur1:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)
        else:
            for word in futur1:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)
    elif (tense == 'Perfekt'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in perfekt:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)

        else:
            for word in perfekt:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)
    elif (tense == 'Plusquamperfekt'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in plusq:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)
        else:
            for word in plusq:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)
    elif (tense == 'Futur II'):
        if (pronoun == 'er ' or pronoun == 'sie ' or pronoun == 'es '):
            for word in futur2:
                if word.find('er/sie/es') != -1:
                    print("Conjugation: ", word)
        else:
            for word in futur2:
                if word.find(pronoun) != -1:
                    print("Conjugation: ", word)
    else:
        print("Input does not match any of the tenses.")
    t2 = time.time()
    print('Time elapsed: ', str(t2-t1), 'seconds')

conjugate()
