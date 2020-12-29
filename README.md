# Script for cpu and memory metrics


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install psutil.

Make script executable
```bash
chmod +x cpu_mem_info.py
```
## Usage
Run script with parameter

For cpu metrics:
```bash
./cpu_mem_info.py cpu
```
For memory metrics:
```bash
./cpu_mem_info.py mem
```

## Usage with docker
Build docker image:
```bash
docker build -t <image_name>:<tag> .
```

Run docker container with parameter:
```bash
docker run -it <image_name>:<tag> cpu_mem_info.py cpu | mem
```


