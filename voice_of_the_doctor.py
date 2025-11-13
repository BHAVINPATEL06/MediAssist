#Third File
# Here we are going to convert the text output from the GROQ LLM model into voice using TTS model


#gTTS - Google Text to Speech
# Step1A: Setup Text-to-Speech TTS-Model (gTTS)
import os
# from gtts import gTTS

# # Converting text to speech using gTTS
# def text_to_speect_with_gtts_old(input_text,output_filepath):
#     language='en'  # Language in which you want to convert

#     # Here we are creating the gTTS object which will convert the text into speech
#     # We are passing the text, language and slow=False (which means the speech will be in normal speed)
#     audioobj = gTTS(
#         text = input_text, 
#         lang=language,
#         slow = False 
#     )

#     audioobj.save(output_filepath)  # Saving the converted audio in the output_filepath

# # input_text will be given and gTTS will convert that text into speech and save it in the output_filepath
# input_text="Hello, I am your virtual doctor. How can I assist you today?"

# # output_filepath="gtts_testing.mp3" we can give any name to the output file
# text_to_speect_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")



# # # Step1B: Setup Text-to-Speech TTS-Model (elevenLabs)
# import os
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVEN_LABS_APIKEY = os.environ.get("ELEVEN_LABS_API_KEY")  # Fetching API form .env file in variable named ELEVEN_LABS_API_KEY
# print(bool(ELEVEN_LABS_APIKEY), len(ELEVEN_LABS_APIKEY or ""))

# def text_to_speech_with_elevenlabs_old(input_text,output_filepath):
#     client = ElevenLabs(api_key=ELEVEN_LABS_APIKEY)  # Creating client object of ElevenLabs class with api_key

#     # Here we are generating the audio using the ElevenLabs TTS model
#     # By passing the text, voice in which we want output, output_format and model name which we want to use
#     audio = client.text_to_speech.convert(
#         text = input_text,
#         voice_id = "21m00Tcm4TlvDq8ikWAM",
#         output_format = "mp3_22050_32",
#         model_id = "eleven_turbo_v2"
#     )

#     elevenlabs.save(audio,output_filepath) # Saving the converted audio in the output_filepath
    
# input_text will be given and elevenLabs will convert that text into speech and save it in the output_filepath
# input_text="Hello, I am your virtual doctor. How can I assist you today?"
# text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath="elevenlabs_testing.mp3")










# Step2: Use Model for Text output to voice
import subprocess   #subprocess is used interact with Command Line Interface(CLI) from python script
import platform     # platform module is used to get information about the system (like Windows, Linux, MacOS)

# def text_to_speect_with_gtts(input_text,output_filepath):
#     language='en'  # Language in which you want to convert

#     # Here we are creating the gTTS object which will convert the text into speech
#     # We are passing the text, language and slow=False (which means the speech will be in normal speed)
#     audioobj = gTTS(
#         text = input_text, 
#         lang=language,
#         slow = False 
#     )

#     audioobj.save(output_filepath)  # Saving the converted audio in the output_filepath
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")
# input_text will be given and gTTS will convert that text into speech and save it in the output_filepath
#output_filepath="gtts_testing.mp3" we can give any name to the output file
# text_to_speect_with_gtts(input_text=input_text, output_filepath="gtts_autoplay_testing.mp3")






def text_to_speech_with_elevenlabs(input_text,output_filepath):
    client = ElevenLabs(api_key=ELEVEN_LABS_APIKEY)  # Creating client object of ElevenLabs class with api_key

    # Here we are generating the audio using the ElevenLabs TTS model
    # By passing the text, voice in which we want output, output_format and model name which we want to use
    audio = client.text_to_speech.convert(
        text = input_text,
        voice_id = "21m00Tcm4TlvDq8ikWAM",
        output_format = "mp3_22050_32",
        model_id = "eleven_turbo_v2"
    )

    elevenlabs.save(audio,output_filepath) # Saving the converted audio in the output_filepath
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
# input_text will be given and elevenLabs will convert that text into speech and save it in the output_filepath
input_text="Hello this is an autoplay file please autoplay?"
text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")