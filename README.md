# Socket testing with pyhton and docker

### This project has 83 continers in total one running a python app and the rest an SSH server. (SSH servers start from 0)
### And we are socket testing that SSH port on all containers.

#

### To use this project just clone the repo.
## To build just:
```bash
docker compose build
```

## To run just:
```bash
docker compose up
```
> To stop running execution (CRTL+C or CMD+C)

## To remove all containers:
```bash
docker compose down
```
> #### Note: The example was with 100+ container but my personal computer could not take it.
> #### Try adding more if you like. 
> #### To do so; change values in `compose.yaml` file, the environment variable and then comment or uncomment services as required.