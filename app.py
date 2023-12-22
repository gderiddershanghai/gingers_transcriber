import streamlit as st
from whisper_transcribe import transcribe
from save_video import save_uploaded_file

def main():
    st.title("Video Transcription")

    uploaded_file = st.file_uploader("Upload your video", type=["mp4"])

    # Initialize transcript_file_path outside of the if-statement
    transcript_file_path = None

    if uploaded_file is not None:
        video_path = save_uploaded_file(uploaded_file)
        st.session_state['video_path'] = video_path

    if 'video_path' in st.session_state and st.button("Generate Transcription"):
        transcript_file_path = transcribe(st.session_state['video_path'])
        if transcript_file_path:  # Check if transcription was successful
            with open(transcript_file_path, 'r') as file:
                st.session_state['transcription_text'] = file.read()

    if 'transcription_text' in st.session_state:
        confirmed_transcription = st.text_area("Edit the transcription if needed:", st.session_state['transcription_text'], height=500)
        if st.button("Save Transcription") and transcript_file_path:
            with open(transcript_file_path, 'w') as file:
                file.write(confirmed_transcription)
            st.session_state['transcription_text'] = confirmed_transcription
            st.session_state['save_clicked'] = True
            st.success("Transcription saved.")

    if st.session_state.get('save_clicked', False) and transcript_file_path:
        # Use the string variable directly instead of file object
        st.download_button(
            label="Download Transcription",
            data=st.session_state['transcription_text'],
            file_name="transcription.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
