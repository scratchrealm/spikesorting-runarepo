FROM spikeinterface/mountainsort4-base:1.0.0

RUN pip install pandas

# todo: mountainsort4 should not depend on requests - see _mdaio_impl.py
RUN pip install requests

RUN pip install spikeinterface==0.92.0

RUN pip install mearec
COPY run.py /run.py

CMD [ "python",  "/run.py" ]