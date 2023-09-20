FROM python:3.7

RUN pip install cairosvg --default-timeout=10000 --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --trusted-host=pypi.python.org

WORKDIR /app

COPY render.py render.py

ENTRYPOINT [ "python", "render.py" ]
