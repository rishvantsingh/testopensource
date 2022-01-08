FROM python:3-alpine

WORKDIR /usr/local/cotu

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
