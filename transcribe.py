import assemblyai as aai
import sys
import os
from datetime import timedelta

# ─── CONFIG ───────────────────────────────────────────────────────────────────
API_KEY_FILE = "aai_api_key.txt"  # This file should contain your AssemblyAI API key
# ──────────────────────────────────────────────────────────────────────────────


def load_api_key(path: str = API_KEY_FILE) -> str:
    """Load the AssemblyAI API key from a local file."""
    if not os.path.exists(path):
        print(f"Error: API key file not found: {path}")
        print("Create this file and put your AssemblyAI API key on a single line.")
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        key = f.read().strip()

    if not key:
        print(f"Error: API key file {path} is empty.")
        sys.exit(1)

    return key

def format_timestamp(ms):
    """Convert milliseconds to HH:MM:SS format."""
    seconds = ms // 1000
    return str(timedelta(seconds=seconds))

def transcribe(audio_path):
    if not os.path.exists(audio_path):
        print(f"Error: File not found: {audio_path}")
        sys.exit(1)

    print(f"Uploading {audio_path}...")

    aai.settings.api_key = load_api_key()

    config = aai.TranscriptionConfig(
        language_code="ro",             # Romanian
        speaker_labels=True,            # Speaker diarization
        speech_models=["universal-2"],  # Model supporting many languages incl. Romanian
    )

    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_path)

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        sys.exit(1)

    print("Transcription complete. Saving output...")

    # Build output file path next to the input file
    base = os.path.splitext(audio_path)[0]
    output_path = base + "_transcript.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"TRANSCRIPT: {os.path.basename(audio_path)}\n")
        f.write("=" * 60 + "\n\n")

        current_speaker = None
        for utterance in transcript.utterances:
            speaker = f"Speaker {utterance.speaker}"
            timestamp = format_timestamp(utterance.start)

            # Add a blank line between speaker changes for readability
            if speaker != current_speaker:
                if current_speaker is not None:
                    f.write("\n")
                f.write(f"[{timestamp}] {speaker}:\n")
                current_speaker = speaker

            f.write(f"{utterance.text}\n")

    print(f"\nDone! Transcript saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py path\\to\\your_file.m4a")
        print("Example: python transcribe.py C:\\Meetings\\call1.m4a")
        sys.exit(1)

    transcribe(sys.argv[1])