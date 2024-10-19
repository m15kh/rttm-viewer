from diart import SpeakerDiarization, VoiceActivityDetection
from diart.sources import MicrophoneAudioSource
from diart.inference import StreamingInference
from diart.sinks import RTTMWriter

pipeline = VoiceActivityDetection()
mic = MicrophoneAudioSource()
inference = StreamingInference(pipeline, mic, do_plot=True)
inference.attach_observers(RTTMWriter(mic.uri, "output/vad.rttm"))
prediction = inference()