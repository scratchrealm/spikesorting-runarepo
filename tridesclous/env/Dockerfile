FROM spikeinterface/tridesclous-base:1.6.4

RUN pip install pandas

RUN pip install spikeinterface==0.92.0

RUN pip install pynwb
RUN git clone https://github.com/catalystneuro/nwb-conversion-tools /nwb-conversion-tools \
    && cd /nwb-conversion-tools \
    && pip install .
RUN pip install packaging