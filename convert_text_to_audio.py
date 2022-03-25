from gtts import gTTS
import warnings
import os
warnings.filterwarnings('ignore')


# The text that you want to convert to audio
mytext = 'right'  # first "right" then replace by "left"
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("right.mp3")
  
# Playing the converted file
os.system("start right.mp3")