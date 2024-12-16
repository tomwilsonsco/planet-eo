# planet-eo
Examples of Planet API. 

The Jupyter notebooks import custom modules under `utils`, so need to run them from within the full repository directory.

## Setup for Windows users - Conda `environment.yml`
Windows users may find it easiest to use Conda.

1. Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) (if not already installed).

2. Clone this repository, open an Anaconda Prompt and `cd` to the repository directory.

3. Create the environment using the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```
4. Activate the environment:
   ```bash
   conda activate planet_eo
   ```
5. Start Jupyter Lab:
   ```
   jupyter lab
   ```
6. In Jupyter Lab open the example notebooks:
   - Planet Scope: `ps_search_preview_dld.ipynb`
   - Monthly Basemap: `basemaps_month_download.ipynb`

## Setup Using docker
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

4. Copy link in format below and open in browser:
```bash
http://127.0.0.1:8888/lab?token=abc123
```

5. In Jupyter Lab open the notebooks:  `ps_search_preview_dld.ipynb` or `basemaps_month_download.ipynb`
