import pyaudio

p = pyaudio.PyAudio()

# Get the number of available audio devices
num_devices = p.get_device_count()

# Iterate over each audio device
for i in range(num_devices):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}")
    print(f"  Index: {device_info['index']}")
    print(f"  Default Sample Rate: {device_info['defaultSampleRate']}")
    print(f"  Max Input Channels: {device_info['maxInputChannels']}")
    print(f"  Max Output Channels: {device_info['maxOutputChannels']}")
    print(f"  Default Low Input Latency: {device_info['defaultLowInputLatency']}")
    print(f"  Default Low Output Latency: {device_info['defaultLowOutputLatency']}")
    print(f"  Default High Input Latency: {device_info['defaultHighInputLatency']}")
    print(f"  Default High Output Latency: {device_info['defaultHighOutputLatency']}")
    print(f"  Host API Type: {device_info['hostApi']}")
    print()

p.terminate()
