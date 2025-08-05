# YouTube Transcript to Detailed Notes Converter

A Streamlit web application that converts YouTube video transcripts into detailed notes and provides an interactive Q&A feature using Google's Generative AI.

## Features

- 🎥 Extract transcripts from YouTube videos
- 📝 Generate detailed notes (270 words or less) using AI
- ❓ Interactive Q&A system based on generated notes
- 🖼️ Display video thumbnails
- 💾 Persistent session state for notes and Q&A
- 🔑 Secure API key management with environment variables

## Prerequisites

- Python 3.7 or higher
- Google API Key for Generative AI
- Internet connection for API calls

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "New folder"
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (for local development):

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Setup

### Getting Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. For local development: Copy the key and add it to your `.env` file
4. For Streamlit Cloud: Add it as a secret in your app settings

### Environment Variables

**Local Development:**
Create a `.env` file with:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

**Streamlit Cloud Deployment:**
Add `GOOGLE_API_KEY` in the app's secrets management section.

## Usage

### Local Development

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. Open your web browser and navigate to the displayed URL (usually `http://localhost:8501`)

### Streamlit Cloud Deployment

1. Push your code to GitHub
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your `GOOGLE_API_KEY` in the app secrets
4. Your app will be available at the provided URL

5. Enter a YouTube video URL in the input field

6. Click "Get Detailed Notes" to generate AI-powered summary

7. Use the Q&A section to ask questions about the generated notes

## Project Structure

```
New folder/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (local only)
└── README.md          # Project documentation
```

## Dependencies

- `streamlit`: Web app framework
- `python-dotenv`: Environment variable management
- `langchain-google-genai`: Google Generative AI integration
- `youtube-transcript-api`: YouTube transcript extraction

## Deployment on Streamlit Cloud

1. Push your repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Set the main file path to `app.py`
5. Add your `GOOGLE_API_KEY` in the app secrets section
6. Deploy the app

## Features in Detail

### Transcript Extraction

- Supports YouTube videos with available captions/subtitles
- Automatic video ID extraction from YouTube URLs
- Error handling for videos without transcripts

### AI Summarization

- Uses Google's Gemini 1.5 Flash model
- Generates concise summaries (270 words or less)
- Maintains context and key information

### Interactive Q&A

- Ask questions about the generated notes
- Persistent session state across interactions
- Context-aware responses based on the summary

## Error Handling

The application includes comprehensive error handling for:

- Missing API keys
- Invalid YouTube URLs
- Videos without available transcripts
- API connection issues

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Known Issues

- Only works with YouTube videos that have captions/subtitles available
- Requires stable internet connection for API calls
- Summary length is limited to 270 words

## Future Enhancements

- Support for multiple languages
- Batch processing of multiple videos
- Export notes to different formats (PDF, TXT)
- Advanced filtering and search within notes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Ayush Singh**

## Support

If you encounter any issues or have questions, please:

1. Check the error messages in the application
2. Ensure your API key is correctly set in Streamlit Cloud secrets
3. Verify the YouTube video has captions available
4. Create an issue in the repository

---

⭐ If you found this project helpful, please give it a star!
