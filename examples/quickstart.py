from openet_download import download_et_timeseries

out = download_et_timeseries(
    lon=-120.176088,
    lat=36.848983,
    start="2016-01-01",
    end="2016-12-31",
    interval="daily",          # or "monthly"
    out_dir="my_named_folder",
    api_key=None,              # recommend env var OPENET_API_KEY
    plot=True,
    show_plot=False,
)

print("Saved CSV:", out["csv"])
print("Saved figure:", out["figure"])
print(out["data"].head())