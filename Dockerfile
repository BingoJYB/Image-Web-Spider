FROM debian:9

# Create a directory for the output of images and grant right
RUN mkdir ./images && chmod 777 -R ./images

# Copy the current directory contents into the container at /app
ADD . /app

# Install necessary tools
RUN apt update
RUN yes | apt install python3-pip cron
RUN pip3 install asyncio aiohttp aiofiles

# Make port 80 available to the world outside this container
EXPOSE 80

# Use cron to run script every 5 minutes
RUN (crontab -l ; echo "*/5    *   *   *   * python3 /app/Main.py /app/img_url" ; echo)| crontab -

# Run cron when the container launches
ENTRYPOINT ["/usr/sbin/cron", "-f"]
