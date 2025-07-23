```
1. List all running containers
docker ps

2. List all containers irrespective of state.
docker ps -a

3. List all containers with file size
docker ps -s

4. List IDs of running containers
docker ps -q

5.List IDs of running containers irrespective of state.
docker ps -aq

6. Filter container list
docker ps -f name=<string>

7.Filter container  on basis of status
docker ps -af status=running

8. Create new container from Docker image
docker create <image_name>

9. Create new container from Docker image with fixed name
docker create --name <container_name> <image_name>

10. Start a container
docker start <container_id or container_name>

11. Stop running container
docker stop <container_id or container_name>

12. Restart container
docker restart <container_id or container_name>

13. Pause running container
docker pause <container_id or container_name>

14. Resume paused container
docker unpause <container_id or container_name>

15. Run container
docker run <image_name>

16. Delete container on exited status
docker run --rm <container>
The --rm option removes the filesystem of the container once it is stopped or when the container exits automatically

17. Run container in detached modes
docker run -d <image_name>

18. Run container with assigned name
docker run -d --name <container_name> <image_name>

19. List running processes in container
docker top <container_name or container_id>

20. Map ports of container
docker run --name <container_name> -d -p <host_post>:<container_port> <image_name>

21. Rename container
docker rename <old_name> <new_name>

22. Run container in interactive mode
docker run -it <image_name> /bin/bash

22. Get inside running container
docker exec -it <contaner_id or container_name> /bin/bash

23.Start container and keep it running
docker run -dt <image_name>

24. Copy file from container to host
docker cp <container_id or container_name>:<source_file_path> <destination_path>

25. Copy file from host to container
docker cp <host_file_path> <container_id or container_name>:<target_file_path>

26. Stop Container
docker stop <container_name or container_id>

27. Remove container
docker rm <container_name or container_id>

28. Remove container after it exits
docker run --rm <image_name>

29. Delete stopped containers
docker container prune

30. Delete stopped and running containers
docker rm -f $(docker ps -a -q)
docker container rm -f $(docker ps -a -q)

31. Create Docker images from existing containers
docker commit <container_id or container_name> <new_image_name>
docker container commit <container_id or container_name> <new_image_name>

32. Set environment variables in container
docker run --env ENV_VAR1=value1 --env ENV_VAR1=value2 --name <container_name> <image_name>

33. Set environment variables in container from file
docker run --env-file <path_to_the_file> --name <container_name> <image_name>

34. Docker image commands
1)List all images
docker images
2) List all images including dangling images
docker images -a
3)list image id's.
docker images -q
4)Build image from a docker file
docker build -t <image_name> <context_dir>
If your Dockerfile is not in your current directory, you can specify it by adding the --file option
docker build -f </path/to/dockerfilename>  -t <image_name> .
5) Build image with different tag
docker build -t <image_name>:<tag or version> .
6) Build image using custom-named Dockerfile
docker build -f <custom_docker_file_name> -t <image_name> .
7) save image as tar
docker save imageName > newimagename.tar
8) load the image
docker load -i newimagename.tar

To be continued....
