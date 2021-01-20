FROM python:3.8

COPY ./backend ./backend

WORKDIR ./backend

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
