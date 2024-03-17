# Application Overview

This is an simple API that will list all the gists of a git user.

## How to run this application

To run this application clone the repo and build the docker image using the following commands:

```bash
git clone https://github.com/EqualExperts-Assignments/equal-experts-basic-unreflective-wrack-431c14d1a8e2.git
cd equal-experts-basic-unreflective-wrack-431c14d1a8e2
docker build -t gist:1.0 .
````
Once the image is build, then run the docker container using the below command:
```bash
docker run -d -p 5000:5000 gist:1.0
```