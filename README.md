# Whisper Audio Transcript

A quick and dirty approach to show how users to upload an audio file and receive a transcribed version of the content using OpenAI's Whisper speech to text API.

Use cases: automatically generating lyrics, subtitle (.SRT) files (with some changes to output), automatic meeting transcriptions.

![image](https://github.com/Veeeetzzzz/whisper-audio-transcript/assets/40268197/128d15ad-09fd-4203-ada1-2d5de3ec167b)


# Installation

1. Clone directory/download this repo
2. Set up your API under an enviroment variable called OPEN_API_KEY
3. Make sure Python + dependencies are installed


# Usage

Navigate to the directory you've downloaded the files in and use 'flask run' then open your web browser and navigate to http://localhost:5000 to start using the application.

# How it works

The user uploads an audio file through the web interface.


The audio file is sent to the server.


The server uses OpenAI's Whisper system to transcribe the audio.


The transcription is sent back to the client and displayed in the web interface.

# Contribution

This is far from finished. Just a proof of concept that can be expanded on.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
