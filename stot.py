# First, you need to install the SpeechRecognition library.
# Open your command prompt or terminal and run:
# py -m pip install SpeechRecognition

# Note: This script requires an audio file named 'audio.wav' in the same folder.
# You can create a short voice recording and save it as a .wav file,
# or use an online tool to convert any audio file to the .wav format.

import speech_recognition as sr

def transcribe_audio_file(filename):
    """
    Transcribes a given audio file to text.

    Args:
        filename (str): The path to the .wav audio file.

    Returns:
        str: The transcribed text from the audio file.
    """
    # 1. Initialize a recognizer instance
    recognizer = sr.Recognizer()

    # 2. Open the audio file
    # The 'with' statement ensures the file is properly closed after reading.
    try:
        with sr.AudioFile(filename) as source:
            # The recognizer records the data from the file into an AudioData object.
            print("Reading audio file...")
            audio_data = recognizer.record(source)
            print("Processing audio...")

            # 3. Use Google's Web Speech API to recognize the audio
            # This sends the audio data to Google's servers for processing.
            # It requires an active internet connection.
            try:
                # The recognize_google() method performs the speech recognition.
                text = recognizer.recognize_google(audio_data)
                return text
            # Handle cases where the API could not understand the audio
            except sr.UnknownValueError:
                return "Google Web Speech API could not understand the audio."
            # Handle cases where the API is unreachable or there are network issues
            except sr.RequestError as e:
                return f"Could not request results from Google Web Speech API; {e}"

    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found. Please make sure it's in the same directory as the script."

# --- Example Usage ---
if __name__ == "__main__":
    # The name of the audio file you want to transcribe.
    # IMPORTANT: You must have a file with this name in the same folder.
    audio_filename = "audio.wav"

    # Transcribe the audio file
    transcribed_text = transcribe_audio_file(audio_filename)

    # Print the result
    print("\n" + "="*50 + "\n")
    print("Transcribed Text:")
    print(transcribed_text)
    print("\n" + "="*50)


