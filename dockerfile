FROM python:3.10.14-slim


WORKDIR /app



COPY ./requirements.txt ./


RUN pip install -r requirements.txt 

COPY ./ ./


EXPOSE 8501



ENTRYPOINT ["streamlit", "run", "front.py", "--server.port=8501", "--server.address=0.0.0.0"]