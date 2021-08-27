# container-101-bakery


# Docker Basic Commnad

    $ docker run -dp 80:80 docker/getting-started
    $ docker image ls
    $ docker container ls
    $ docker container stop (Container ID |NAMES)
    $ docker stop (Container ID |NAMES)
    $ docker ps
    $ docker ps -a
    $ docker start  (Container ID |NAMES)
    $ docker ps
    $ docker ps -a
    $ docker rm (Container ID |NAMES)
    $ docker images
    $ docker rmi (Container ID |NAMES)
    $ docker exec -it (Container ID |NAMES) bash 
    $ docker run --name abcdemo -dp 82:80 docker/getting-started 
    $ docker attach abcdemo
    $ docker stop (from another terminal)
    $ docker inspect (Container ID |NAMES)


## Reference

[*Docker 101 Tutorial*](https://www.docker.com/101-tutorial)

[*docker base command*](https://docs.docker.com/engine/reference/commandline/docker/)

---

# Docker Image / Dockerfile
    $ docker build . --tag=bakeryhello
    $ docker build . --tag=bakeryhello/simplified -f=Dockerfile_simplified    
    $ docker build . --tag=bakeryhello/fat -f=Dockerfile_fat
    $ docker run --rm -it -w /code -p 8000:8000 bakeryhello sh -c "sh"
    $ docker run --rm -it -w /code -p 8000:8000 bakeryhello/simplified sh -c "sh"
    $ docker run --rm -it -w /code -p 8000:8000 bakeryhello/fat sh -c "sh"
    
        $ /code/manage.py migrate
        $ /code/manage.py load_initial_data
        $ /code/manage.py runserver 0.0.0.0:8000
        



## Reference:

[*Best practices for writing Dockerfiles*](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#minimize-the-number-of-layers)

# DockerHub

    $ docker login
    $ docker tag bakeryhello/simplified  aboutwilliam/bakeryhello:simplified.1
    $ docker push aboutwilliam/bakeryhello:simplified.1