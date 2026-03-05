

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
Apply / find your API key at: https://openetdata.org/

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
