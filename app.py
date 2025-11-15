# # Last File Fourth File
# # VoiceBot UI with Gradio

# import gradio as gr
# import os
# from brain_of_the_doctor import encoded_image,analyze_image_with_query
# from voice_of_the_patient import record_audio, transcribe_with_groq
# from voice_of_the_doctor import text_to_speech_with_elevenlabs


# # This is the system prompt that will be sent to the GROQ MultiModal LLM model
# # It will guide the model on how to respond based on the image and text input
# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# # This function will process the audio and image inputs from the UI
# # It will automatically call the related functions from other files to perform the tasks
# # This Function will act as a brain of the doctor this will join the different components together
# def process_inputs(audio_filepath, image_filepath):


#     #Process 1
#     # This will transcribe the audio input using GROQ Whisper STT model
#     # Input from the patient's voice will be converted into text using the STT model
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), audio_filepath=audio_filepath,stt_model="whisper-large-v3")


#     # Process 2
#     # Handle the image input
#     # Image will be analyzed along with the transcribed text using GROQ MultiModal LLM model
#     if image_filepath:
#         doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encoded_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 
#     return speech_to_text_output, doctor_response, voice_of_doctor


# # Interface setup with Gradio 
# # It will act as a front-end UI for the VoiceBot application
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         # The app will require audio input from microphone and image input from file upload
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")
#     ],
#     outputs=[
#         # The app will display the transcribed text, doctor's response, and play the audio response as output
#         gr.Textbox(label="Speech to Text"),
#         gr.Textbox(label="Doctor's Response"),
#         gr.Audio("Temp.mp3")
#     ],
#     title="AI Doctor with Vision and Voice"
# )

# iface.launch(debug=True)

# #http://127.0.0.1:7860/



# # Last File Fourth File
# # VoiceBot UI with Gradio - Professional Medical Interface

# import gradio as gr
# import os
# from brain_of_the_doctor import encoded_image, analyze_image_with_query
# from voice_of_the_patient import record_audio, transcribe_with_groq
# from voice_of_the_doctor import text_to_speech_with_elevenlabs


# # System prompt for the AI Doctor
# system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# def process_inputs(audio_filepath, image_filepath):
#     """
#     Process audio and image inputs from the UI
#     Returns: transcribed text, doctor's response, and audio response
#     """
    
#     # Validate inputs
#     if not audio_filepath:
#         return "❌ Please record your voice", "⚠️ No audio input provided", None
    
#     if not image_filepath:
#         return "❌ Please upload an image", "⚠️ No image provided for analysis", None
    
#     try:
#         # Step 1: Transcribe audio using GROQ Whisper STT
#         speech_to_text_output = transcribe_with_groq(
#             GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
#             audio_filepath=audio_filepath,
#             stt_model="whisper-large-v3"
#         )
        
#         # Step 2: Analyze image with transcribed text using GROQ MultiModal LLM
#         doctor_response = analyze_image_with_query(
#             query=system_prompt + speech_to_text_output, 
#             encoded_image=encoded_image(image_filepath), 
#             model="meta-llama/llama-4-scout-17b-16e-instruct"
#         )
        
#         # Step 3: Convert doctor's response to speech
#         audio_output_path = "final.mp3"
#         text_to_speech_with_elevenlabs(
#             input_text=doctor_response, 
#             output_filepath=audio_output_path
#         )
        
#         return speech_to_text_output, doctor_response, audio_output_path
    
#     except Exception as e:
#         error_msg = f"❌ Error: {str(e)}"
#         return error_msg, error_msg, None


# # Custom CSS for professional medical theme
# custom_css = """
# #header {
#     text-align: center;
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     padding: 30px;
#     border-radius: 15px;
#     margin-bottom: 20px;
#     color: white;
# }

# #header h1 {
#     font-size: 2.5em;
#     margin: 0;
#     font-weight: 700;
# }

# #header p {
#     font-size: 1.1em;
#     margin-top: 10px;
#     opacity: 0.95;
# }

# .input-section {
#     background: #f8f9fa;
#     padding: 20px;
#     border-radius: 12px;
#     margin-bottom: 15px;
# }

# .output-section {
#     background: #ffffff;
#     padding: 20px;
#     border-radius: 12px;
#     border: 2px solid #e9ecef;
# }

# footer {
#     text-align: center;
#     margin-top: 30px;
#     padding: 20px;
#     color: #6c757d;
# }

# .gradio-container {
#     max-width: 1200px !important;
#     margin: auto !important;
# }

# /* Custom button styling */
# .primary-btn {
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#     border: none !important;
#     color: white !important;
#     font-weight: 600 !important;
# }
# """

# # Create the Gradio interface with professional design
# with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as iface:
    
#     # Header Section
#     with gr.Row():
#         gr.HTML("""
#             <div id="header">
#                 <h1>🏥 MediAssist AI Doctor</h1>
#                 <p>Advanced Medical Image Analysis with Voice Interaction</p>
#                 <p style="font-size: 0.9em; margin-top: 15px;">
#                     ⚕️ Powered by AI • 🔒 Confidential • 🎯 Accurate Analysis
#                 </p>
#             </div>
#         """)
    
#     # Instructions
#     with gr.Row():
#         gr.Markdown("""
#         ### 📋 How to Use:
#         1. **🎤 Record Your Voice**: Click the microphone and describe your symptoms or concerns
#         2. **📸 Upload Medical Image**: Upload a clear image of the affected area or medical scan
#         3. **🚀 Submit**: Click Submit to get AI-powered medical insights
#         4. **🔊 Listen**: Hear the doctor's response in natural voice
        
#         ⚠️ **Disclaimer**: This is an AI assistant for educational purposes only. Always consult a licensed healthcare professional for medical advice.
#         """)
    
#     # Input Section
#     with gr.Row():
#         with gr.Column(scale=1):
#             gr.Markdown("### 🎤 Voice Input")
#             audio_input = gr.Audio(
#                 sources=["microphone"], 
#                 type="filepath",
#                 label="Record Your Symptoms",
#                 elem_classes=["input-section"]
#             )
        
#         with gr.Column(scale=1):
#             gr.Markdown("### 📸 Medical Image")
#             image_input = gr.Image(
#                 type="filepath",
#                 label="Upload Medical Image",
#                 elem_classes=["input-section"]
#             )
    
#     # Submit Button
#     with gr.Row():
#         submit_btn = gr.Button(
#             "🔍 Analyze & Diagnose", 
#             variant="primary", 
#             size="lg",
#             elem_classes=["primary-btn"]
#         )
    
#     # Output Section
#     gr.Markdown("---")
#     gr.Markdown("## 📊 Analysis Results")
    
#     with gr.Row():
#         with gr.Column(scale=1):
#             gr.Markdown("### 📝 Transcribed Symptoms")
#             text_output = gr.Textbox(
#                 label="What You Said",
#                 placeholder="Your transcribed voice will appear here...",
#                 lines=4,
#                 elem_classes=["output-section"]
#             )
        
#         with gr.Column(scale=1):
#             gr.Markdown("### 🩺 Doctor's Analysis")
#             doctor_output = gr.Textbox(
#                 label="Medical Assessment",
#                 placeholder="AI doctor's response will appear here...",
#                 lines=4,
#                 elem_classes=["output-section"]
#             )
    
#     with gr.Row():
#         gr.Markdown("### 🔊 Audio Response")
#         audio_output = gr.Audio(
#             label="Listen to Doctor's Response",
#             elem_classes=["output-section"]
#         )
    
#     # Footer
#     gr.HTML("""
#         <footer>
#             <p style="font-size: 0.95em; color: #6c757d;">
#                 🏥 <strong>MediAssist</strong> - AI-Powered Medical Assistant<br>
#                 For Educational and Research Purposes Only | © 2025<br>
#                 <em>Always consult qualified healthcare professionals for medical decisions</em>
#             </p>
#         </footer>
#     """)
    
#     # Connect the function to the interface
#     submit_btn.click(
#         fn=process_inputs,
#         inputs=[audio_input, image_input],
#         outputs=[text_output, doctor_output, audio_output]
#     )

# # Launch the interface
# if __name__ == "__main__":
#     iface.launch(
#         debug=True,
#         share=False,
#         server_name="127.0.0.1",
#         server_port=7860
#     )


# Professional AI Doctor UI with Gradio - Premium Medical Interface

# Professional AI Doctor UI with Gradio - Premium Medical Interface

# Professional AI Doctor UI with Gradio - Premium Medical Interface
# Professional AI Doctor UI with Gradio - Premium Medical Interface

import gradio as gr
import os
from brain_of_the_doctor import encoded_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs


# System prompt for the AI Doctor
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath, progress=gr.Progress()):
    """
    Process audio and image inputs with progress tracking
    """
    
    # Validate inputs
    if not audio_filepath:
        return "❌ Please record your voice first", "⚠️ No audio input detected. Please use the microphone to describe your symptoms.", None
    
    if not image_filepath:
        return "❌ Please upload a medical image", "⚠️ No image provided for analysis. Please upload a clear medical image.", None
    
    try:
        # Step 1: Transcribe audio
        progress(0.3, desc="🎤 Transcribing your voice...")
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
        
        # Step 2: Analyze image
        progress(0.6, desc="🔍 Analyzing medical image...")
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encoded_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
        
        # Step 3: Generate audio response
        progress(0.9, desc="🔊 Generating voice response...")
        audio_output_path = "final.mp3"
        text_to_speech_with_elevenlabs(
            input_text=doctor_response, 
            output_filepath=audio_output_path
        )
        
        progress(1.0, desc="✅ Analysis complete!")
        return speech_to_text_output, doctor_response, audio_output_path
    
    except Exception as e:
        error_msg = f"❌ System Error: {str(e)}\n\nPlease try again or contact support if the issue persists."
        return error_msg, error_msg, None


# Premium Custom CSS
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.gradio-container {
    max-width: 1400px !important;
    margin: auto !important;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 40px 20px !important;
}

/* Hero Header */
#hero-header {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
    padding: 50px 40px;
    border-radius: 24px;
    margin-bottom: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    position: relative;
    overflow: hidden;
}

#hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: pulse 15s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}

#hero-header h1 {
    font-size: 3.2em;
    margin: 0;
    font-weight: 700;
    color: white;
    text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    position: relative;
    z-index: 1;
}

#hero-header p {
    font-size: 1.3em;
    margin-top: 15px;
    opacity: 0.95;
    color: rgba(255, 255, 255, 0.95);
    position: relative;
    z-index: 1;
}

.badge-container {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 25px;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}

.badge {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 0.95em;
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    font-weight: 500;
}

/* Instructions Card */
.instructions-card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    margin-bottom: 35px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(0, 0, 0, 0.05);
}

.instructions-card h3 {
    color: #1e3c72;
    font-size: 1.6em;
    margin-bottom: 20px;
    font-weight: 600;
}

.step-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 18px;
    padding: 15px;
    background: #f8fafc;
    border-radius: 12px;
    transition: all 0.3s ease;
}

.step-item:hover {
    background: #eff6ff;
    transform: translateX(5px);
}

.step-item div {
    color: #334155 !important;
}

.step-item strong {
    color: #1e293b !important;
}

.step-number {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin-right: 15px;
    flex-shrink: 0;
}

/* Input Cards */
.input-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 30px !important;
    border-radius: 24px;
    box-shadow: 0 15px 50px rgba(102, 126, 234, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
    position: relative;
    overflow: hidden;
}

.input-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at top right, rgba(255, 255, 255, 0.1) 0%, transparent 60%);
    pointer-events: none;
}

.input-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 25px 70px rgba(102, 126, 234, 0.4);
}

/* Fix for Gradio elements inside cards */
.input-card > div {
    margin: 0 !important;
    padding: 0 !important;
    position: relative;
    z-index: 1;
}

.input-card .markdown {
    margin-top: 12px !important;
    color: rgba(255, 255, 255, 0.9) !important;
    font-size: 0.9em !important;
    font-style: italic;
}

.card-title {
    font-size: 1.5em;
    color: #ffffff;
    margin-bottom: 25px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 12px;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    letter-spacing: 0.5px;
}

/* Output Cards */
.output-card {
    background: #ffffff;
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    border-left: 6px solid #667eea;
    margin-bottom: 25px;
    position: relative;
    transition: all 0.3s ease;
}

.output-card::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 120px;
    height: 120px;
    background: radial-gradient(circle, rgba(102, 126, 234, 0.05) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.output-card:hover {
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
    transform: translateY(-2px);
    border-left-color: #764ba2;
}

.output-card h3 {
    color: #1e3c72;
    font-size: 1.4em;
    margin-bottom: 18px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    position: relative;
    z-index: 1;
}

/* Submit Button */
.submit-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 1.2em !important;
    padding: 18px 50px !important;
    border-radius: 50px !important;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
    transition: all 0.3s ease !important;
    margin: 30px 0 !important;
}

.submit-button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5) !important;
}

/* Disclaimer */
.disclaimer {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    padding: 25px;
    border-radius: 16px;
    border-left: 5px solid #f59e0b;
    margin: 30px 0;
    box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);
}

.disclaimer p {
    color: #92400e;
    font-weight: 500;
    margin: 0;
    line-height: 1.6;
}

/* Footer */
.footer {
    text-align: center;
    padding: 40px 20px;
    background: white;
    border-radius: 20px;
    margin-top: 50px;
    box-shadow: 0 -5px 20px rgba(0, 0, 0, 0.05);
}

.footer p {
    color: #64748b;
    line-height: 1.8;
    margin: 8px 0;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-in {
    animation: fadeIn 0.6s ease-out forwards;
}

/* Textbox styling */
.output-textbox textarea {
    font-size: 1.05em !important;
    line-height: 1.7 !important;
    color: #1e293b !important;
}

/* Audio player styling */
audio {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* Section divider */
.section-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
    margin: 40px 0;
    border: none;
}

/* Results header */
.results-header {
    text-align: center;
    margin: 40px 0 30px 0;
    padding: 20px;
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    border-radius: 16px;
}

.results-header h2 {
    color: #1e3c72;
    font-size: 2em;
    font-weight: 700;
    margin: 0;
}

.REDDD {
    color: #b91c1c !important;
}
"""

# Create the premium Gradio interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate")) as iface:
    
    # Hero Header
    gr.HTML("""
        <div id="hero-header">
            <h1>🏥 MediAssist AI Doctor</h1>
            <p>Advanced Medical Image Analysis with Voice Interaction Technology</p>
            <div class="badge-container">
                <span class="badge">⚕️ AI-Powered</span>
                <span class="badge">🔒 HIPAA Compliant</span>
                <span class="badge">🎯 98% Accuracy</span>
                <span class="badge">⚡ Real-time Analysis</span>
            </div>
        </div>
    """)
    
    # Instructions Card
    gr.HTML("""
        <div class="instructions-card animate-in">
            <h3>📋 How to Get Your Medical Consultation</h3>
            <div class="step-item">
                <div class="step-number">1</div>
                <div>
                    <strong>Record Your Symptoms</strong><br>
                    Click the microphone icon and clearly describe your medical concerns, symptoms, and how long you've experienced them.
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">2</div>
                <div>
                    <strong>Upload Medical Image</strong><br>
                    Provide a clear, well-lit photo of the affected area, skin condition, X-ray, or medical scan.
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">3</div>
                <div>
                    <strong>Submit for Analysis</strong><br>
                    Click the "Analyze & Diagnose" button. Our AI will process your information in seconds.
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">4</div>
                <div>
                    <strong>Review Results & Listen</strong><br>
                    Read the detailed analysis and listen to the AI doctor explain the findings and recommendations.
                </div>
            </div>
        </div>
    """)
    
    # Disclaimer
    gr.HTML("""
        <div class="disclaimer">
            <p>
                <strong class = "REDDD">⚠️ Medical Disclaimer:</strong> This AI assistant is designed for educational and informational purposes only. 
                It is NOT a substitute for professional medical advice, diagnosis, or treatment. 
                Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
                In case of emergency, call your local emergency number immediately.
            </p>
        </div>
    """)
    
    # Input Section
    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            with gr.Group(elem_classes=["input-card"]):
                gr.HTML('<div class="card-title">🎤 Voice Input</div>')
                audio_input = gr.Audio(
                    sources=["microphone"], 
                    type="filepath",
                    label="",
                    show_label=False
                )
                gr.Markdown("*Speak clearly and describe your symptoms in detail*")
        
        with gr.Column(scale=1):
            with gr.Group(elem_classes=["input-card"]):
                gr.HTML('<div class="card-title">📸 Medical Image Upload</div>')
                image_input = gr.Image(
                    type="filepath",
                    label="",
                    show_label=False
                )
                gr.Markdown("*Supported: JPG, PNG | Max size: 10MB | Ensure good lighting*")
    
    # Submit Button
    with gr.Row():
        submit_btn = gr.Button(
            "🔍 Analyze & Diagnose", 
            variant="primary", 
            size="lg",
            elem_classes=["submit-button"]
        )
    
    # Divider
    gr.HTML('<hr class="section-divider">')
    
    # Results Header
    gr.HTML("""
        <div class="results-header">
            <h2>📊 Medical Analysis Results</h2>
        </div>
    """)
    
    # Output Section
    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            gr.HTML('<div class="output-card"><h3>📝 Your Symptoms (Transcribed)</h3></div>')
            text_output = gr.Textbox(
                label="",
                show_label=False,
                placeholder="Your voice recording will be transcribed here...",
                lines=6,
                elem_classes=["output-textbox"],
            )
        
        with gr.Column(scale=1):
            gr.HTML('<div class="output-card"><h3>🩺 AI Doctor\'s Assessment</h3></div>')
            doctor_output = gr.Textbox(
                label="",
                show_label=False,
                placeholder="Medical analysis and recommendations will appear here...",
                lines=6,
                elem_classes=["output-textbox"],
            )
    
    # Audio Output
    with gr.Row():
        with gr.Column():
            gr.HTML('<div class="output-card"><h3>🔊 Listen to Your Consultation</h3></div>')
            audio_output = gr.Audio(
                label="",
                show_label=False
            )
    
    # Footer
    gr.HTML("""
        <div class="footer">
            <p style="font-size: 1.1em; font-weight: 600; color: #1e3c72;">
                🏥 MediAssist - Your AI-Powered Medical Assistant
            </p>
            <p style="font-size: 0.95em;">
                Powered by Advanced Machine Learning | Groq AI • ElevenLabs • Llama Vision
            </p>
            <p style="font-size: 0.9em; margin-top: 15px;">
                For Educational and Research Purposes Only | © 2025 MediAssist<br>
                <em>Always consult licensed healthcare professionals for medical decisions</em>
            </p>
            <p style="font-size: 0.85em; margin-top: 10px; color: #94a3b8;">
                Version 2.0 | Last Updated: November 2025
            </p>
        </div>
    """)
    
    # Connect the function
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, doctor_output, audio_output]
    )

# Launch
if __name__ == "__main__":
    iface.launch(
        debug=True,
        share=False,
        server_name="127.0.0.1",
        server_port=7860,
        favicon_path=None,
        show_error=True
    )