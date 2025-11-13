#Second File
#Here we are going to record the audio from the patient and then we will transcribe that audio into text using GROQ Whisper model

#Step 1: Setup Audio Recorder ((ffmpeg & portaudio))
#ffmpeg , portaudio , pyaudio 
#ffmpeg is used to handle audio/image/video processing 
#portaudio is used to handle audio input/output from microphone/speakers
#pyaudio is used to record and play audio in python


import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


# In logging library it help to show which type of logging we have to show as INFO , DEBUG , ERROR
# Now we have to show INFO type of logging in the given format as time - level - message
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer() # It's the object of the Recognizer use to store the audio data from the microphone of the patient
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")  # This acts as an cout statement for clear and easy understanding
            recognizer.adjust_for_ambient_noise(source, duration=1) # This is use to adjust the background noise for 1 second or we can change it also
            logging.info("Start speaking now...")        
            
            # Record the audio
            # This will listen the audio from the microphone source with timeout and phrase_time_limit
            # timeout (int): Maximum time to wait for a phrase to start (in seconds). Agar koi awaaz na aaye to itne second ke baad recording band kar dega
            # phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_filepath="patient_voice_test.mp3"
record_audio(file_path=audio_filepath)

#Step2: Setup Speech to text–STT–model for transcription
# Here is the code to transcribe audio using GROQ Whisper model
# using Whisper used to convert audio into text 

import os
from groq import Groq

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")   # Fetching API form .env file in variable named GROQ_API_KEY
stt_model="whisper-large-v3"   # This is an Speech to text model from GROQ

def transcribe_with_groq(stt_model,audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)            #creating client object of Groq class with api_key 
    audio_file=open(audio_filepath, "rb")        # opening the audio file in read binary mode

    # API call to GROQ Whisper STT model for transcription
    # Sending the audio file to the model for transcription
    transcription=client.audio.transcriptions.create(   
            model=stt_model,               # Model Name
            file=audio_file,               # Audio file to be transcribed
            language="en"                  # Language of the audio file
    )

    return transcription.text


