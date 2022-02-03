import time
import numpy as np
import kachery_client as kc
import spikeinterface.extractors as se

import sortingview as sv
from nwb_conversion_tools.utils.spike_interface import write_recording

kc.enable_ephemeral()
recording = sv.LabboxEphysRecordingExtractor('sha1://a205f87cef8b7f86df7a09cddbc79a1fbe5df60f/2014_11_25_Pair_3_0.json')
sorting_true = sv.LabboxEphysSortingExtractor('sha1://c656add63d85a17840980084a1ff1cdc662a2cd5/2014_11_25_Pair_3_0.firings_true.json')

print(recording.get_num_frames() / recording.get_sampling_frequency() / 60)
print(recording.get_num_channels())


timer = time.time()
X = recording.get_traces()
print('1::::::::::::::::::::::::::::', time.time() - timer)
np.save('input/test.npy', X)
print('2::::::::::::::::::::::::::::', time.time() - timer)

write_recording(
    recording,
    save_path="input/recording.nwb",
    compression=None,
    compression_opts=None
)
print('3::::::::::::::::::::::::::::', time.time() - timer)