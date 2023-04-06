import numpy as np
import pydub
import sksound.sounds as sks

# carrega o arquivo de áudio
audio_file = pydub.AudioSegment.from_file(
    "caminho\do\arquivo\sujo.wav", format="wav")

# converte para matriz numpy
audio_array = np.array(audio_file.get_array_of_samples())

# aplica a redução de ruído
clean_audio = sks.nr.reduce_noise(
    audio_array, noise_clip=audio_array, verbose=False)

# salva o arquivo de áudio limpo
clean_audio = pydub.AudioSegment(clean_audio.tobytes(
), frame_rate=audio_file.frame_rate, sample_width=audio_file.sample_width, channels=audio_file.channels)
clean_audio.export("caminho\do\novo\arquivo_limpo.wav", format="wav")
