# This article cover official [docker tutorial for beginners](https://docker-curriculum.com/)

## What is docker?

> **Docker is a tool that allows** developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows **users to package an application with all of its dependencies into a standardized unit for software development**. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.

 ### what is container?
 >  VMs are great at providing full process isolation for applications: there are very few ways a problem in the host operating system can affect the software running in the guest operating system, and vice-versa. But this isolation comes at great cost — the computational overhead spent virtualizing hardware for a guest OS to use is substantial.

> Containers take a different approach: **by leveraging the low-level mechanics of the host operating system, containers provide most of the isolation of virtual machines at a fraction of the computing power**.


## Some commands and their explanation

1. `docker pull` - command fetches the image from the Docker registry and saves it to our system
2. `docker image` - to see a list of all images on your system
3. `docker run` - run container
> **Hint:** running with flags -it like these: 
> ```
> $ docker run -it <name>
> ```
> **these flags attaches us to an interactive *tty* in the container**. Now we can run as many commands in the container as we want.
4. `docker ps` - show all containers that are currently running
5. `docker <docker command> --help` - for list of all flags this command support
6. `docker rmi` - delete images that you no longer need by running
7. `docker rm <id>` - delete container by id
> **Hint:** use this for deletes all containers that have a status of exited (not images)
> ```
> $ docker rm $(docker ps -a -q -f status=exited)
> ```
> `-q` flag returns only IDs and `-f` filter output based on condition provided

> **Hint:** One last thing that'll be useful is the `--rm` flag that can be passed to `docker run` which **automatically deletes the container once it's exited from**. *For one off docker runs, `--rm` flag is very useful.*

**For this effect (like `docker rm <IDs>`.) you can use:**
```
$ docker container prune
```
**And get output like these:**
```
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
...
```
## A little about containers

Even if you use `rm -rf bin` and break all the commands, the next time you start you will be able to work in the system again as if it were not there.
**Since Docker creates a new container every time, everything should start working again.**

## Terminology
* **Images** - the blueprints of our application which form the basis of containers
* **Containers** - created from Docker images and run the actual application
* **Docker Daemon** - the background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system which clients talk to
* **Docker Client** - the command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as *Kitematic* which provide a GUI to the users.
* **Docker Hub** - a registry of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.
