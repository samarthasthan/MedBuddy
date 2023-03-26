
from fastapi import APIRouter
import spacy
import pandas as pd
import cv2
import easyocr
import spacy
import re

import pytesseract
import shutil
import os
import random

from PIL import Image
import pandas as pd
import cv2
import easyocr
import spacy
import re
import random
import pytesseract
import shutil
import os
import random
from PIL import Image





router = APIRouter(
    tags=['scanner'],
)

df = pd.read_csv('/Users/samarthasthan/Desktop/aiml/train_Dataset_health.csv')

#Drugs Names
all_drugs = df['drugName'].unique().tolist()
all_drugs = [x.lower() for x in all_drugs]

#model directory
dir = '/Users/samarthasthan/Desktop/aiml/model'

def extract2(path):

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise=cv2.medianBlur(gray,3)
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img,paragraph='False')
    ftext=pd.DataFrame(result)

    text3 = ftext[1][2]

    data = []
    ent_dict = {}
    processed_token = []
    for token in text3.split():
        token = ''.join(e.lower() for e in token if e.isalnum())
        processed_token.append(token)
        review = ' '.join(processed_token)
    visited_item = []
    entities = []
    for token in review.split():
      if token in all_drugs:
        for i in re.finditer(token,review):
            entity = (i.span()[0], i.span()[1], 'DRUG')
            entities.append(entity)

    ent_dict['entities'] = entities
    train_item2 = (review, ent_dict)
    data.append(train_item2)

    print("Loading from",dir) #model directory gdrive
    nlp2 = spacy.load(dir)
    for i, _ in data[0:1]:
      doc = nlp2(i)
      a = ('Entities', [(ent.text, ent.label_) for ent in doc.ents])
      b = ('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
    
    return a



pytesseract.pytesseract.tesseract_cmd=r'tesseract-ocr-setup-4.00.00dev.exe'

df = pd.read_csv('/Users/samarthasthan/Desktop/aiml/train_Dataset_health.csv')

all_drugs = df['drugName'].unique().tolist()
all_drugs = [x.lower() for x in all_drugs]

#model directory
dir = "/Users/samarthasthan/Desktop/aiml/model"
def extract(path):
    text = pytesseract.image_to_string(Image.open(path))

    def process_review(review):
        processed_token = []
        for token in review.split():
            token = ''.join(e.lower() for e in token if e.isalnum())
            processed_token.append(token)
        return ' '.join(processed_token)
    
    def format(text):
        dataa = []
        ent_dict = {}
        review = process_review(text)
        entities = []
        for token in review.split():
            if token in all_drugs:
                for i in re.finditer(token,review):
                    entity = (i.span()[0], i.span()[1], 'DRUG')
                    entities.append(entity)

        ent_dict['entities'] = entities
        train_item2 = (review, ent_dict)
        dataa.append(train_item2)
        return dataa
      
    a = format(text)
  
    print("Loading from",dir) #model directory gdrive
    nlp2 = spacy.load(dir)
    for i, _ in a:
      doc = nlp2(i)
      a = ([ent.text for ent in doc.ents])
      b = ('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
    
    return a

ft = extract('/Users/samarthasthan/Desktop/aiml/12.jpg')
print(ft)

''''@router.get('/scan')
async def scanner():
    print("processing")
    ft = extract('/Users/samarthasthan/Desktop/aiml/12.jpg')
    return ft'''