import rx.operators as ops
import diart.operators as dops
from diart.sources import MicrophoneAudioSource
from diart.blocks import SpeakerSegmentation, OverlapAwareSpeakerEmbedding, VoiceActivityDetection

# Load the pre-trained VAD model
vad = VoiceActivityDetection.from_pretrained("pyannote/voice-activity-detection")
mic = MicrophoneAudioSource()

# Function to interpret VAD output (you can tweak this based on the model's output structure)
def interpret_vad_output(vad_output):
    if vad_output == 1:  # Assuming the model returns 1 for speech
        return "Speech Detected"
    else:
        return "Silence or Noise Detected"

# Real-time audio stream processing
stream = mic.stream.pipe(
    # Reformat stream into smaller chunks (e.g., 1 second duration, 0.1 second shift)
    dops.rearrange_audio_stream(sample_rate=44100, duration=1.0, shift=0.1),
    
    # Apply the VAD model to each chunk of audio
    ops.map(lambda wav: vad(wav)),
    
    # Map VAD output to a human-readable format
    ops.map(interpret_vad_output)
)

# Subscribe to the stream and print VAD detection result in real-time
stream.subscribe(on_next=lambda result: print(result))

# Start reading from the microphone
mic.read()
