# IDS721-Project2-Docker-Example

This snippet of code can tell you the current time.

- build docker image(do it after `docker login`)

   ```docker build --tag cccyaa/ids721-project2-docker:latest .```
  
- list docker images

  ```docker image ls```

- build image app

  ```#docker build --tag=app .```

- push docker image

  ```./push_docker.sh```
  
  
- pull and run

  ```docker pull cccyaa/ids721-project2-docker:latest```
  
  ```docker run -it cccyaa/ids721-project2-docker:latest python app.py```

  
