import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r"D:\SEM 3 Subjects\Python\audio processing\harvard.wav")

# Write audio file
sf.write('new_audio_file.wav', audio, sample_rate)

