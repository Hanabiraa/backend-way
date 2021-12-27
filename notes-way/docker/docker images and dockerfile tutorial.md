# This article continue official [docker tutorial for beginners](https://docker-curriculum.com/) and my own *docker beginner tutorial* and *docker web app tutorial*

## Some theoretical information

Docker images are the basis of containers. In the previous example, we pulled the Busybox image from the registry and asked the Docker client to run a container based on that image. 

1. `docker images` - for list of images that are available locally
2. `docker search` - for search images in docker hub
3. `docker build <path>` - build image

i.e.
```
$ docker images

REPOSITORY                      TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
prakhar1989/catnip              latest              c7ffb5626a50        2 hours ago         697.9 MB
prakhar1989/static-site         latest              b270625a1631        21 hours ago        133.9 MB
python                          3-onbuild           cf4002b2c383        5 days ago          688.8 MB
martin/docker-cleanup-volumes   latest              b42990daaca2        7 weeks ago         22.14 MB
ubuntu                          latest              e9ae3c220b23        7 weeks ago         187.9 MB
busybox                         latest              c51f86c28340        9 weeks ago         1.109 MB
hello-world                     latest              0a6ba66e537a        11 weeks ago        960 B
```

- `TAG` - refers to a particular snapshot of the image
- `IMAGE ID` - unique identifier for that image

For simplicity, you can think of an image akin to a git repository - images can be committed with changes and have multiple versions. If you don't provide a specific version number, the client defaults to `latest`. For example, you can pull a specific version of `ubuntu` image

```
$ docker pull ubuntu:18.04
```

To get a new Docker image you can either get it from a registry (such as the Docker Hub) or create your own. There are tens of thousands of images available on Docker Hub. You can also search for images directly from the command line using `docker search`.

## Important theoretical information

An important distinction to be aware of when it comes to images is the difference between base and child images.

> **Base images** are images that have no parent image, usually images with an OS like ubuntu, busybox or debian.

> **Child images** are images that build on base images and add additional functionality.

Then there are official and user images, which can be both base and child images.

> **Official images** are images that are officially maintained and supported by the folks at Docker. These are typically one word long. In the list of images above, the `python`, `ubuntu`, `busybox` and `hello-world` images are official images.

> **User images** are images created and shared by users like you and me. They build on base images and add additional functionality. Typically, these are formatted as `user/image-name`.

## Our First Image

Now that we have a better understanding of images, it's time to create our own. Our goal in this section will be to create an image that sandboxes a simple Flask application. For the purposes of this workshop, I've already created a fun little Flask app that displays a random cat .gif every time it is loaded

```
$ git clone https://github.com/prakhar1989/docker-curriculum.git
$ cd docker-curriculum/flask-app
```

The next step now is to create an image with this web app. As mentioned above, all user images are based on a base image. Since our application is written in Python, the base image we're going to use will be Python 3.

## Dockerfile

> A `Dockerfile` is a simple text file that contains a list of commands that the Docker client calls while creating an image. It's a simple way to automate the image creation process. The best part is that the commands you write in a Dockerfile are almost identical to their equivalent Linux commands. This means you don't really have to learn new syntax to create your own dockerfiles.

The application directory does contain a Dockerfile but since we're doing this for the first time, we'll create one from scratch. To start, create a new blank file in our favorite text-editor and save it in the same folder as the flask app by the name of Dockerfile.

```
FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]
```

1. We start with specifying our base image. Use the `FROM` keyword to do that:
```
FROM python:3
```

2. The next step usually is to write the commands of copying the files and installing the dependencies. First, we set a working directory and then copy all the files for our app.
```
# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .
```

3. Now, that we have the files, we can install the dependencies:
```
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
```

4. The next thing we need to specify is the port number that needs to be exposed. Since our flask app is running on port 5000, that's what we'll indicate:
```
EXPOSE 5000
```

5. The last step is to write the `command` for running the application, which is simply - `python ./app.py`. We use the `CMD` command to do that:
```
CMD ["python", "./app.py"]
```
The primary purpose of CMD is to tell the container which command it should run when it is started. With that, our Dockerfile is now ready. 

## Building

Now that we have our `Dockerfile`, we can build our image. The docker build command does the heavy-lifting of creating a Docker image from a `Dockerfile`

The docker build command is quite simple:
- `-t` - tag name

*My name on DockerHub is hanabira*
```
$ docker build -t hanabira/catnip .
```

lets check:
```
$ docker images

REPOSITORY                TAG       IMAGE ID       CREATED              SIZE
hanabira/catnip           latest    5a7aa32cb4b5   About a minute ago   927MB
python                    3         a5d7930b60cc   6 days ago           917MB
prakhar1989/static-site   latest    f01030e1dcf3   5 years ago          134MB
```

and run it:

```
$ docker run -p 8888:5000 hanabiraa/catnip 

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
```

![](./assets/img/catgif.webp)