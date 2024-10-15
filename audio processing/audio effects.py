from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file(r"D:\SEM 3 Subjects\Python\audio processing\harvard.wav")

# Add fade in effect
audio_fade_in = audio.fade_in(2000)  # 2 seconds

# Export audio file with fade in effect
audio_fade_in.export('audio_file_fade_in.wav', format='wav')
