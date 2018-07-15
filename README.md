# WebSpider

1. Get an image from 'bingojyb/webspider' docker repository and to create the container by the following command:

        docker run -d -p 4000:80 -v &(pwd)/images:/images bingojyb/webspider:main

   In this command, '-p 4000:80' maps the host port 4000 to the container port 80, a HTTP port for communication and messages.    '-v &(pwd)/images:/images' mounts the 'images' directory created in Dockerfile to '/images' in the container for the            downloaded images.

2. Use the swarm mode and make the host be swarm manager by

        docker swarm init [--advertise-addr ip]
  
3. Run the following command on the manager

        docker swarm join-token worker
  
4. Run the output of the above command on workers to join the swarm

5. Deploy the script according to 'docker-compose.yml' file by

        docker stack deploy -c docker-compose.yml spider
  
6. Verify the deployment on multiple Debian machines by

        docker service ls
