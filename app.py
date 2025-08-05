import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
# ISSUE FIXED: Import the correct class for transcript fetching
from youtube_transcript_api import YouTubeTranscriptApi
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

   

# ISSUE FIXED: Added {transcript} placeholder for proper string formatting
prompt = """You are Youtube Transcript Summarizer.
You will be given a Youtube video transcript.
Your task is to summarize the transcript of the video.
You will return the summary in 270 Words or less.
Here is the transcript:
{transcript}
"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        # ISSUE FIXED: Use the correct methods that are actually available
        # Based on the available methods: 'fetch' and 'list'
        # This appears to be an instance-based API, not static methods
        api = YouTubeTranscriptApi()
        
        # Try to get the transcript using the available methods
        try:
            # Method 1: Try using list and fetch
            transcript_list = api.list(video_id)
            transcript_text = api.fetch(video_id)
        except:
            # Method 2: Try direct fetch
            transcript_text = api.fetch(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i.text  # Changed from i["text"] to i.text

        return transcript

    except Exception as e:
        # ISSUE FIXED: Remove the debug info and provide cleaner error handling
        st.error(f"Error fetching transcript: {str(e)}")
        st.info("Make sure the YouTube video has captions/subtitles available.")
        raise e
    
def summarize_transcript(transcript , prompt):
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        # ISSUE FIXED: Properly format the prompt with transcript content
        # OLD CODE: response = llm.invoke(prompt, {"transcript": transcript})
        # NEW CODE: Format the prompt string first, then invoke
        formatted_prompt = prompt.format(transcript=transcript)
        response = llm.invoke(formatted_prompt)
        # ISSUE FIXED: Access content attribute directly from response object
        summary = response.content
        return summary
    except Exception as e:
        raise e 
    
st.title("YouTube Transcript to Detailed Notes Converter")
st.markdown("#### Made By Ayush Singh")  # Added signature
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# After image display, add these lines to always show the summary if available
if "summary" in st.session_state:
    st.markdown("## Detailed Notes:")
    st.write(st.session_state["summary"])

# Changed: Separate detailed notes generation remains the same and stores summary in session state.
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = summarize_transcript(transcript_text, prompt)
        st.session_state["summary"] = summary  # Persist summary for Q&A
        st.markdown("## Detailed Notes:")
        st.write(summary)

# NEW FEATURE: Q&A Section moved outside the detailed notes block so it persists across interactions
st.markdown("## Q&A Section")
question = st.text_input("Ask your question about the detailed notes:")
if st.button("Get Answer"):
    if "summary" not in st.session_state:
        st.error("Please generate detailed notes first.")
    else:
        summary = st.session_state["summary"]
        qa_prompt = (
            "You are a helpful Q&A assistant. Based on the detailed notes below, "
            "answer the following question.\n\n"
            "Detailed Notes:\n" + summary + "\n\nQuestion: " + question
        )
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        answer = llm.invoke(qa_prompt).content
        st.markdown("### Answer:")
        st.write(answer)