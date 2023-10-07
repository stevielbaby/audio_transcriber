import os
import whisper
import subprocess

folder_path = "/Users/steviel/python_projects/whisper/app/voice_notes/WMA"
name_schema = input("Enter the name schema for the output files: ")

# Verify that the source directory exists
if not os.path.exists(folder_path):
    print(f"Error: The directory {folder_path} does not exist.")
    exit(1)

# Get a list of all audio files in the folder
files = [file for file in os.listdir(folder_path) if file.lower().endswith((".wma", ".mp3", ".m4a"))]

# If there are no audio files in the directory, exit the script
if not files:
    print(f"Error: No audio files found in {folder_path}.")
    exit(1)

# Create the output folders if they don't exist
mp3_output_folder = "/Users/steviel/python_projects/whisper/app/voice_notes/mp3"
os.makedirs(mp3_output_folder, exist_ok=True)

transcriptions_output_folder = "/Users/steviel/python_projects/whisper/app/transcriptions"
os.makedirs(transcriptions_output_folder, exist_ok=True)

# Check if FFmpeg is installed
try:
    subprocess.check_output(["ffmpeg", "-version"])
except subprocess.CalledProcessError:
    print("Error: FFmpeg is not installed or not in the system path.")
    exit(1)

# Check if the whisper model exists
try:
    model = whisper.load_model("base")
except Exception as e:
    print(f"Error: Failed to load the whisper model. {e}")
    exit(1)

for i, file in enumerate(files):
    # Generate output file path
    output_file = f"{name_schema}_{i+1}.txt"
    transcription_output_path = os.path.join(transcriptions_output_folder, output_file)

    input_file_path = os.path.join(folder_path, file)

    # If the file is a .wma or .m4a file, convert it to .mp3
    if file.lower().endswith((".wma", ".m4a")):
        mp3_file_path = os.path.join(mp3_output_folder, f"{file.rsplit('.', 1)[0]}.mp3")
        try:
            subprocess.run(["ffmpeg", "-i", input_file_path, "-c:a", "libmp3lame", mp3_file_path], check=True)
            print(f"Converted {input_file_path} to {mp3_file_path}")

            # Delete the original audio file
            try:
                os.remove(input_file_path)
                print(f"Deleted {input_file_path}")
            except Exception as e:
                print(f"Error: Failed to delete {input_file_path}. {e}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to convert {input_file_path} to {mp3_file_path}. {e}")
            continue
    # If the file is already a .mp3 file, no conversion is necessary
    elif file.lower().endswith(".mp3"):
        mp3_file_path = input_file_path

    # Transcribe the MP3 file
    try:
        result = model.transcribe(mp3_file_path)
        print(f"Transcribed {mp3_file_path}")
    except Exception as e:
        print(f"Error: Failed to transcribe {mp3_file_path}. {e}")
        continue

    # Write the transcription to a text file
    try:
        with open(transcription_output_path, "w") as f:
            f.write(result["text"])
        print(f"Saved transcription to {transcription_output_path}")
    except Exception as e:
        print(f"Error: Failed to write transcription to {transcription_output_path}. {e}")

print("Conversion and transcription completed.")
