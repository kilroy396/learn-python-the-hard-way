# A docker based set of notes for "Learning Jupyter"

Jupyter notebook examples come from "Learning Jupyter" by Dan Toomey, published by Packt Publishing 2016

The container specified is large.  It supports Python, Scala, R, Spark, Mesos Stack.

Alternatively use some of the alternative jupter/*-notebook containers on [http://hub.docker.com](https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=jupyter&starCount=0)

To start the containerised notebook:
```
$ docker container run -d  --restart always -p 8888:8888 -v “$(pwd)“:/home/jovyan/mapped-notebooks --name jupyter-notebook jupyter/all-spark-notebook
```

You will then need to browse to [http://localhost:8888](http://128.0.0.1:8888)

You will be prompted for a token.  This can be retrieved by doing the following.

```
$ docker exec -it jupyter-notebook /bin/bash
$ jupyter notebook list
```

The token is contained in the output, and it can then by copyed to the dialogue box.

When finished

```
docker container stop jupyter-notebook
docker container rm jupyter-notebook
```
