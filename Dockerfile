FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7
MAINTAINER sih4sing5hong5

WORKDIR /opt
COPY . .
RUN pip3 install -r requirements.txt

CMD gunicorn -w 2 -b 0.0.0.0:5000 --log-level debug hokbu:app
