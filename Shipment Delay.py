
# coding: utf-8

# In[35]:

a = open("C:/Users/saiad/Desktop/IE Project/reviews_Electronics_split_9/reviews_Electronics_3.txt").read()


# In[2]:

import re
import nltk


# In[36]:

sents = nltk.sent_tokenize(a)


# In[10]:

mystring = ("feature", "delivered late", "delayed", "Shipment delayed","arrived early","late delivered",
             "")
text = str()
for line in sents:
    if any(x in line for x in mystring):
    #if mystring in line:
          text = text + line


# In[38]:

with open('C:/Users/saiad/Desktop/IE Project/Output/reviews_Electronics_3.txt', 'w') as f:
    f.writelines(text)


# In[36]:

b = open("C:/Users/saiad/Desktop/IE Project/Output/output3.txt").read()


# In[18]:

import re
c = re.findall(r"asin..\s['\w]+",b)
d = re.findall(r"title':\s['\w\s&-]+",b)


# In[23]:

with open('C:/Users/saiad/Desktop/IE Project/Output/output1.txt', 'w') as f:
    f.writelines(c)


# In[37]:

d = b.replace("title","\n")


# In[38]:

with open('C:/Users/saiad/Desktop/IE Project/Output/output3.txt', 'w') as f:
    f.writelines(d)


# Code to extract the dates

datesextr = open("C:/Users/saiad/Desktop/IE Project/Output/combined_shipment_electronics_neg.txt").read()

datesextrs = re.findall(r'(reviewTime":\s"[\d\s,]+)',datesextr)

with open('C:/Users/saiad/Desktop/IE Project/Output/combined_shipment_electronics_neg_dates.txt', 'w') as f:
    f.writelines(datesextrs)




