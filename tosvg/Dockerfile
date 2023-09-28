FROM python:2.7

RUN pip install Pillow==2.9.0 lxml==3.4.0 pylzma==0.4.6 pyswf==1.5.4 --default-timeout=10000 --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --trusted-host=pypi.python.org

WORKDIR /app

COPY render.py render.py

ENTRYPOINT [ "python", "render.py" ]
