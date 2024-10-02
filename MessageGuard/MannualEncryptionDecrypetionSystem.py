import streamlit as st
import random

st.title("Message Guard")
st.subheader("Turn Messages into Mystery: Encrypt, Decrypt, Safeguard.")
code=st.text_input("Enter Message Here")
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
button1=st.button("Code")
button2=st.button("Decode")
if button1:
       lst=[]      
       a=code.split(" ")
       for message in a:
          if len(message)>= 3:
                message=message[1:]+message[0]
                a=str( random.choice(alphabets)+random.choice(alphabets) +random.choice(alphabets))
                b=str( random.choice(alphabets)+random.choice(alphabets) +random.choice(alphabets))
                c=a+message+b
                lst.append(c)
          else:
                a=message[::-1]
                lst.append(a) 
       st.info(" ".join(lst))

if button2:
      lst=[]
      a=code.split(" ")
      for message in a:
            if len(message)>=3:
                  orignal=message[3:-3]
                  orignal=orignal[-1]+orignal[:-1]
                  lst.append(orignal)
            else :
                  orignal=message[::-1]
                  lst.append(orignal)
      st.info(" ".join(lst))