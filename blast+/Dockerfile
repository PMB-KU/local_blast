FROM conda/miniconda3

RUN conda install blast pandas biopython -c bioconda && \
    mkdir -p /local_volume /workspace

ENV PATH=/workspace/utils:$PATH

ADD . /workspace
RUN ln /workspace/utils/extract_sequence.py /workspace/utils/extract_sequence
WORKDIR /local_volume