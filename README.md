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
pip install streamlit python-dotenv langchain-google-genai youtube-transcript-api
```

3. Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Setup

### Getting Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `.env` file

### Environment Variables

Create a `.env` file with the following structure:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the displayed URL (usually `http://localhost:8501`)

3. Enter a YouTube video URL in the input field

4. Click "Get Detailed Notes" to generate AI-powered summary

5. Use the Q&A section to ask questions about the generated notes

## Project Structure

```
New folder/
├── app.py              # Main Streamlit application
├── .env               # Environment variables (create this)
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (optional)
```

## Dependencies

- `streamlit`: Web app framework
- `python-dotenv`: Environment variable management
- `langchain-google-genai`: Google Generative AI integration
- `youtube-transcript-api`: YouTube transcript extraction

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
2. Ensure your API key is correctly set
3. Verify the YouTube video has captions available
4. Create an issue in the repository

---

⭐ If you found this project helpful, please give it a star!
