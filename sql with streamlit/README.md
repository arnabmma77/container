# Connect PostgreSQL Container to Network Bridge

## Prerequisites
- Docker installed on your system
- Basic understanding of Docker networking

## Step 1: Create a Custom Network Bridge
Docker provides a default bridge network, but it is recommended to create a user-defined bridge network for better control.

```sh
docker network create my_bridge_network
```

## Step 2: Run PostgreSQL Container with Network Bridge
Start a PostgreSQL container and connect it to the created network.

```sh
docker run -d \
  --name my_postgres \
  --network my_bridge_network \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  postgres
```

## Step 3: Verify Network Connection
Check if the PostgreSQL container is connected to the network.

```sh
docker network inspect my_bridge_network
```

## Step 4: Connect Another Container (e.g., pgAdmin) to the Same Network
If you want to connect another container (such as pgAdmin) to interact with PostgreSQL, run:

```sh
docker run -d \
  --name my_pgadmin \
  --network my_bridge_network \
  -e PGADMIN_DEFAULT_EMAIL=admin@example.com \
  -e PGADMIN_DEFAULT_PASSWORD=adminpassword \
  -p 80:80 \
  dpage/pgadmin4
```

## Step 5: Access PostgreSQL from Another Container
You can now connect to PostgreSQL using the container name `my_postgres` as the hostname inside any container in the same network.

Example connection string for pgAdmin:
- Hostname: `my_postgres`
- Port: `5432`
- Username: `myuser`
- Password: `mypassword`
- Database: `mydatabase`

## Step 6: Remove Containers and Network (Optional)
To stop and remove everything:

```sh
docker stop my_postgres my_pgadmin
docker rm my_postgres my_pgadmin
docker network rm my_bridge_network
```

## Conclusion
This guide helps set up a PostgreSQL container on a Docker network bridge, allowing it to communicate with other containers securely and efficiently.

