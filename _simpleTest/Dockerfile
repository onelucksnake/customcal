# ------ RESULT ------
#  PYTHON 3.4  No
#  PYTHON 3.5  Yes
#  PYTHON 3.12 Yes
# ------ RESULT ------

# FROM python:3.4-alpine    
# FROM python:3.5-alpine
# FROM python:3.12-alpine

FROM python:3.5-alpine
USER 0
COPY  ./workenv /workenv
RUN cd /workenv && python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ && \
    python -m pip install setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
RUN cd /workenv && python setup.py check && python setup.py bdist_wheel && \
    python -m pip install dist/*.whl --force-reinstall
WORKDIR /usr/local/bin/
CMD  [ "python","/workenv/run/testScript.py" ]
