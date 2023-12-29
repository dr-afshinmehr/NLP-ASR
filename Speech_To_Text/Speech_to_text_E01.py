import whisper as ws    # Import Require Libraries

mod = ws.load_model('medium')

audio_input = (r"audio\Recording.mp3")

result = mod.transcribe(audio_input)

print(result['text'])