from diart import SpeakerDiarization, VoiceActivityDetection
from diart.sources import MicrophoneAudioSource
from diart.inference import StreamingInference
from diart.sinks import RTTMWriter
import torch

# Initialize VoiceActivityDetection pipeline
class CustomVoiceActivityDetection(VoiceActivityDetection):
    def __init__(self, checkpoint_path):
        super().__init__()
        # Assuming there's a method to get the model, e.g., self.pipeline.model
        self.model = self._load_model_from_checkpoint(checkpoint_path)
    
    def _load_model_from_checkpoint(self, checkpoint_path):
        # Create the model or get the pipeline model
        model = self.pipeline.model  # Or however the model is referenced internally
        # Load the pre-trained weights from the checkpoint
        checkpoint = torch.load(checkpoint_path)
        model.load_state_dict(checkpoint['state_dict'])  # Adjust this if necessary
        return model

# Use your pre-trained checkpoint
checkpoint_path = "/home/rteam2/m15kh/rttm-viewer/epoch=99-step=2000.ckpt"
pipeline = CustomVoiceActivityDetection(checkpoint_path)

mic = MicrophoneAudioSource()
inference = StreamingInference(pipeline, mic, do_plot=True)
inference.attach_observers(RTTMWriter(mic.uri, "output/vad.rttm"))

# Start inference
prediction = inference()
