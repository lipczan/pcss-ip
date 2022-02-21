FROM python:3.8

WORKDIR /app
#COPY requirements.txt requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

EXPOSE 5000

#FROM scratch
#COPY --from=builder /app/myapp /myapp
#ENTRYPOINT [ "/myapp" ]