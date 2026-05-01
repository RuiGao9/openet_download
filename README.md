[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18880781.svg)](https://doi.org/10.5281/zenodo.18880781)
![Stars](https://img.shields.io/github/stars/RuiGao9/openet_download?style=social)<br>

# A lightweight Python package to download OpenET evapotranspiration (ET) time-series data (daily or monthly) using the OpenET API

## Features
- Download OpenET **ET time series** for a **point** (longitude/latitude)
- Supports **daily** or **monthly** interval
- Choose OpenET model 
    - `Ensemble`
    - `DisALEXI`
    - `eeMETRIC`
    - `geeSEBAL`
    - `PT-JPL`
    - `SIMS`
    - `SSEBop`
- Automatically saves:
  - a **CSV** time-series file
  - a **PNG** time-series plot

## Get an OpenET API Key
Apply/find your API key at: https://openetdata.org/

## Installation
```
pip install "git+https://github.com/RuiGao9/openet_download.git" 
```

## How to Use This Repository for ET Downloading
After installation, open main_run.ipynb and update the settings shown below to match your inputs.
```python
YOUR_API_KEY = "APPLY FOR AN API KEY AT https://openetdata.org/"
model = "Ensemble"
longitude = -120.414164
latitude = 37.375004
interval = "daily"
dir_out = r"C:\GitHub\openet_download\outputs"
start_date = "2024-10-01"
end_date = "2025-09-30"
plot = "True"
show_plot = "True"
```

- `YOUR_API_KEY`, you applied from  https://openetdata.org/
- `model`, one type model listed in the **Features** above
- `longitude` and `latitude`, the location where you want to get ET values
- `interval`, either **"daily"** or **"monthly"**
- `dir_out`, a folder path for results saving
- `start_date` and `end_date`, the start and end dates of the time series
- `plot`, either **True** or **False** showing if you want to save the plot after running the program
- `show_plot`, either **True** or **False** showing if you want to see the plot after running the program
<br>Note, `show_plot` won't show the plot if `plot` is **False**.

## Citation
Rui Gao, Safeeq, M., & Viers, J. (2026). A lightweight Python package to download OpenET evapotranspiration (ET) time-series data (daily and monthly) using the OpenET API (0.1.0). Zenodo. https://doi.org/10.5281/zenodo.18880781

**BibTeX:**
```bibtex
@misc{gao2026openet_download,
  author        = {Rui Gao, Mohammad Safeeq, and Joshua H. Viers},
  title         = {A lightweight Python package to download OpenET evapotranspiration (ET) time-series data (daily or monthly) using the OpenET API},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18880781},
  url          = {https://doi.org/10.5281/zenodo.18880781}
}
```

## Repository update information
- Creation date: 2026-03-05
- Last update: 2026-03-05

## Contact inforamtion if issues were found
Rui Gao: Rui.Ray.Gao@gmail.com or RuiGao@ucmerced.edu
