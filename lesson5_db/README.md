postgresql docker:
    https://www.dbvis.com/thetable/how-to-set-up-postgres-using-docker/
 
    docker pull postgres

    docker volume create postgres_data

    docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres


get IP for wsl:
    wsl hostname -I


postgres sample
	https://neon.tech/postgresql/postgresql-getting-started/postgresql-sample-database
	https://neon.tech/postgresql/postgresql-getting-started/load-postgresql-sample-database
