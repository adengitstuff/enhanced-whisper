import whisper

# print(whisper.__file__)
# exit()

test_file_path = "test_audio/test_3_difficult.flac"
model = whisper.load_model("medium")
result = model.transcribe(test_file_path)
print(result["text"])