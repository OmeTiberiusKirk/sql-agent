FROM postgres:17

WORKDIR /home

RUN apt update && apt install -y git make gcc postgresql-server-dev-17
RUN git clone https://github.com/pgvector/pgvector.git && cd pgvector && make && make install

EXPOSE 5432