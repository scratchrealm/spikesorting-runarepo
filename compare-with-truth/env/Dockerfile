FROM spikeinterface/mountainsort4-base:1.0.0

RUN pip install pandas

# todo: mountainsort4 should not depend on requests - see _mdaio_impl.py
RUN pip install requests

RUN pip install spikeinterface==0.92.0

RUN pip install pynwb
RUN git clone https://github.com/catalystneuro/nwb-conversion-tools /nwb-conversion-tools \
    && cd /nwb-conversion-tools \
    && pip install .

RUN git clone https://github.com/flatironinstitute/spikeforest2 /spikeforest2 \
    && cd /spikeforest2 \
    && pip install .
# old kachery is needed by spikeforest2_utils -- but we're going to move away from that package - this is temporary
RUN pip install kachery

RUN pip install packaging