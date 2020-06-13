#!/usr/bin/env python
# coding: utf-8

# In[1]:
import random
import string


# In[2]:


#all possible chatbot outputs
COMPLIMENTS = ['You are kind', 'You are very nice', 'I like your style', 'You are very funny', 'You make my day', 'You are very good looking']
LOVE = ['I love you', 'You are everything to me', 'I love everything about you', 'My love', "I can't live without you", 'ily <3']
INSULTS = ['You suck', "You're terrible", 'You irritate me', 'You are not very bright', 'You have a pea-sized brain', "You're a clown"]
QUESTION = ['Only you know the answer to that', 'The answer to that is top secret. Shh.', "We don't talk about that."]
ALL_CHOICES = ['Make up your mind with one', 'My mind cannot process more than one', 'I said pick one yo']
EXCLAIMS = ["Don't yell at me :(", 'You sound a little too excited to be talking to a computer', 'Wow! You sound pumped!']
OTHER = ['idk', 'I wish I could answer that', 'I am the wrong bot for that', 'Ask someone else because idk']


# In[3]:


#code from A3
def is_question(input_string): #tell whether input is question
    
    """ Parameters
        ----------
        input_string: string
        
        Returns
        ---------
        output: bool
    """
        
        
    if '?' in input_string: #if question, return True
        output = True
        
    else:
        output = False #if not a question, return false
        
    return output


# In[4]:


#tell whether input is exclaimed
def is_exclaiming(input_string): 
    
    """ Parameters
        ----------
        input_string: string
        
        Returns
        ---------
        output: bool
    """
    
    if '!' in input_string: #if exclaimed return True
        output = True
        
    else:
        output = False #if not return False
        
    return output


# In[5]:


#remove punctuation to better read input
def remove_punctuation(input_string):
    
    """ Parameters
        ----------
        input_string: string
        
        Returns
        ---------
        out_string: string
    """
    
    out_string = ''
    #index through input_string and removes punctuation
    for n in input_string:
        if n not in string.punctuation: 
            out_string += n #new string with no punctuation
            
    return out_string


# In[6]:


#makes input easier to understand for the chatbot
def prepare_text(input_string):
    
    """ Parameters
        ----------
        input_string: string
        
        Returns
        ---------
        out_list: list
    """
    
    #makes string all lowercase
    temp_string = input_string.lower()
   
    #removes punctuation
    temp_string = remove_punctuation(temp_string)
    
    #turns string into a list of words
    out_list = temp_string.split()
    
    return out_list


# In[8]:


#check if user wants compliment
def compliment(input_list):
    
    """ Parameters
        ----------
        input_list: list
        
        Returns
        ---------
        bool
    """
    
    if 'compliment' in input_list:
        return True
    else:
        return False


# In[9]:


#check if user wants insult
def insult(input_list):
    
    """ Parameters
        ----------
        input_list: list
        
        Returns
        ---------
        bool
    """
    
    if 'insult' in input_list:
        return True
    else:
        return False


# In[10]:


#check if user wants love remark
def love(input_list):
    
    """ Parameters
        ----------
        input_list: list
        
        Returns
        ---------
        bool
    """
    
    if 'love' in input_list:
        return True
    else:
        return False


# In[11]:


#checks if user wants to end conversation
def end_chat(input_list):
    
    """ Parameters
        ----------
        input_list: list
        
        Returns
        ---------
        bool
    """
    
    if 'quit' in input_list:
        return True
    else:
        return False


# In[12]:


#main function that runs chatbot
def izzy_bot():
    
    chat = True
    
    #intro
    print("Hello human! My name is Izzy and I am here to give you compliments, love remarks, or insults.")
    print("Please let me know whether you want a compliment, love remark, or insult.")
    print("If you get tired of me, just say 'quit', and I'll leave you alone.")
    
    #contains A3 code
    while chat:
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)
        
        #check if the input has an exclamation
        exclamation = is_exclaiming(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        #check if user wants compliment, return random compliment
        if compliment(msg):
            out_msg = random.choice(COMPLIMENTS)
         
        #check if user wants love msg, return random love msg
        if love(msg):
            out_msg = random.choice(LOVE)
    
        #check if user wants insult, return insult
        if insult(msg):
            out_msg = random.choice(INSULTS)
        
        #if compliment and love input, return random ALL_CHOICES
        if compliment(msg) and love(msg):
            out_msg = random.choice(ALL_CHOICES)
        
        #if compliment and insult input, return random ALL_CHOICES
        if compliment(msg) and insult(msg):
            out_msg = random.choice(ALL_CHOICES)
        
        #if love and insult input, return random ALL_CHOICES 
        if love(msg) and insult(msg):
            out_msg = random.choice(ALL_CHOICES)
            
        #if all options inputed, repeat process    
        if love(msg) and insult(msg) and compliment(msg):
            out_msg = random.choice(ALL_CHOICES)

        # no output yet, but question asked
        if not out_msg and question:
            out_msg = random.choice(QUESTION)
            
            
        #no 3 options lsited in input but exclamation used, return random EXCLAIMS
        if not out_msg and exclamation:
            out_msg = random.choice(EXCLAIMS)
            
        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(OTHER)

       
        #prints bot response according to input       
        print('OUTPUT:', out_msg)

        

        
          

        
            
        
    


# In[ ]:


#izzy_bot()


# In[ ]:




