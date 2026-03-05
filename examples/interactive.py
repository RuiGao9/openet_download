import os
from openet_download import download_et_timeseries

def main():
    api_key = os.getenv("OPENET_API_KEY")  # recommended
    if not api_key:
        api_key = input("Enter your OpenET API key: ").strip()

    lon = float(input("Longitude (e.g., -120.176088): ").strip())
    lat = float(input("Latitude (e.g., 36.848983): ").strip())
    interval = input("Interval (daily/monthly): ").strip().lower()
    start = input("Start date (YYYY-MM-DD): ").strip()
    end = input("End date (YYYY-MM-DD): ").strip()
    out_dir = input("Output folder name/path: ").strip()

    out = download_et_timeseries(
        lon=lon, lat=lat,
        start=start, end=end,
        interval=interval,        # type: ignore[arg-type]
        out_dir=out_dir,
        api_key=api_key,
        plot=True,
        show_plot=True,
    )

    print("Saved CSV:", out["csv"])
    print("Saved figure:", out["figure"])

if __name__ == "__main__":
    main()