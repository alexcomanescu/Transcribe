# Transcribe

Transcribe audio recordings (e.g. therapy sessions) with speaker labels, then export to a formatted Word document with color-coded speakers.

## What it does

1. **`transcribe.py`** — Uploads an audio file to [AssemblyAI](https://www.assemblyai.com/), transcribes it with speaker diarization (Speaker A, B, …), and saves a timestamped `.txt` transcript next to the audio file.
2. **`txt_to_docx.py`** — Converts that transcript `.txt` into a `.docx` with a title, metadata, and each speaker’s lines in a distinct color.

## Requirements

- Python 3.7+
- [AssemblyAI](https://www.assemblyai.com/) API key (free tier available)

## Setup

### 1. Clone or download this project

### 2. Create a virtual environment (recommended)

```bash
conda create -n whisper-env python=3.11
conda activate whisper-env
```

### 3. Install dependencies

```bash
pip install assemblyai python-docx
```

### 4. API key

- Get an API key from the [AssemblyAI dashboard](https://www.assemblyai.com/dashboard).
- In this folder, create a file named **`aai_api_key.txt`**.
- Paste your API key on a single line and save.  
  (See `aai_api_key.txt.example` for instructions; the real key file is gitignored.)

## Usage

### Transcribe an audio file

```bash
python transcribe.py path\to\your_recording.m4a
```

Supported formats include `.m4a`, `.mp3`, `.wav`, etc. A file named `your_recording_transcript.txt` will be created in the same folder.

### Convert transcript to Word

```bash
python txt_to_docx.py path\to\your_recording_transcript.txt
```

This creates `your_recording_transcript.docx` in the same folder. To specify the output path:

```bash
python txt_to_docx.py your_recording_transcript.txt Session1.docx
```

## Configuration

- **Language / model** — Edit `transcribe.py`: `language_code` (e.g. `"ro"` for Romanian) and `speech_models` (e.g. `["universal-2"]`). See [AssemblyAI docs](https://www.assemblyai.com/docs) for options.
- **Document title / styles** — Edit `txt_to_docx.py` to change the Word title, colors, or layout.

## Project structure

| File / folder        | Purpose |
|----------------------|--------|
| `transcribe.py`      | Audio → transcript (.txt) via AssemblyAI |
| `txt_to_docx.py`     | Transcript (.txt) → formatted .docx |
| `aai_api_key.txt`    | Your API key (create this; do not commit) |
| `aai_api_key.txt.example` | Instructions for the API key file |

Transcripts, `.docx` outputs, and audio files are listed in `.gitignore` so they are not committed by default.

## License

Use and modify as you like. AssemblyAI usage is subject to their [terms and pricing](https://www.assemblyai.com/pricing).
