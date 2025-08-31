# heiferhelper
Moooooooo

## Docker
Depending on permissions for the docker group, you may need to run the Docker commands using sudo. Install Docker in order to developer with containers or create full image builds.

### Develop Using Docker
This will allow you to run the application within a Docker container for your dev environment eliminating the need for a virtual environment. Files are watched and the app will restart automatically just as any other dev env.
`sudo docker compose watch`

### Building Docker Image
For deployment purposes. 
1. Build the image utilizing the Dockerfile in the project's root: `docker build -t heiferhelper .`
2. Run it: `docker run -d --name moo -p 8000:8000 heiferhelper`