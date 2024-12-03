# planet-eo
Examples of Planet API
## Using docker
1. Build the container
```bash
docker build . --file .devcontainer/Dockerfile -t planet
```

2. Start the container
```bash
docker run --rm -i -t -p 8888:8888 -w /app --mount type=bind,src="$(pwd)",target=/app planet
```

3. Start jupyter lab
```bash
jupyter lab --allow-root --ip=0.0.0.0
```

4. In browser go to:
```bash
http://127.0.0.1:8888/lab
```

5. In Jupyter Lab open the notebook:  `ps_search_preview_dld.ipynb`
