import os
from tabnanny import verbose
from spikeinterface import extractors as se
from spikeinterface import sorters as ss

def main():
    recording, sorting = se.read_mearec('/input/recording.h5')
    # sorter = ss.Mountainsort4Sorter(recording=recording, output_folder='/output', verbose=True)
    # sorter.run()
    sorter_params = {}
    ss.run_mountainsort4(
        recording=recording, output_folder='/output',
        verbose=True, raise_error=True,
        **sorter_params
    )

if __name__ == '__main__':
    main()