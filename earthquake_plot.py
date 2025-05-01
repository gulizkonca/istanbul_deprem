import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

def get_earthquake_data():
    url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
    response = requests.get(url)
    response.encoding = 'iso-8859-9'

    soup = BeautifulSoup(response.text, 'html.parser')
    pre_tag = soup.find('pre')
    lines = pre_tag.text.strip().split('\n')[6:]

    data = []
    for line in lines:
        parts = line.split()
        try:
            timestamp = datetime.strptime(parts[0] + " " + parts[1], "%Y.%m.%d %H:%M:%S")
            latitude = float(parts[2])
            longitude = float(parts[3])
            depth     = float(parts[4])
            magnitude = float(parts[6])
            location  = " ".join(parts[8:])
            data.append((timestamp, latitude, longitude, magnitude, depth, location))
        except Exception:
            continue

    return pd.DataFrame(data, columns=[
        "Time", "Latitude", "Longitude", "Magnitude", "Depth", "Location"
    ])

def plot_graph(df):
    plt.clf()
    plt.figure(figsize=(12, 6))
    plt.plot(df["Time"], df["Magnitude"], marker='o', linestyle='-', color='orange')

    # Her bir noktayı etiketle
    for _, row in df.iterrows():
        plt.annotate(
            row["Location"],
            xy=(row["Time"], row["Magnitude"]),
            xytext=(5, 5),               # yazıyı noktanın sağ üstüne offsetler
            textcoords="offset points",
            fontsize=8,
            rotation=30,                 # gerekirse eğim verin
            alpha=0.7
        )

    plt.title("Son 6 Saatte Marmara Bölgesi Depremleri")
    plt.xlabel("Zaman")
    plt.ylabel("Büyüklük (Mw)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.pause(1)

plt.ion()
while True:
    try:
        df = get_earthquake_data()
        df = df[df["Time"] > datetime.now() - pd.Timedelta(hours=6)]

        # Marmara Bölgesi bounding box
        lat_min, lat_max = 39.5, 42.0
        lon_min, lon_max = 26.0, 33.0
        df_marmara = df[
            (df.Latitude.between(lat_min, lat_max)) &
            (df.Longitude.between(lon_min, lon_max))
        ]

        plot_graph(df_marmara)
        time.sleep(60)
    except KeyboardInterrupt:
        print("Program durduruldu.")
        break
    except Exception as e:
        print("Hata:", e)
        time.sleep(60)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

def get_earthquake_data():
    url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
    response = requests.get(url)
    response.encoding = 'iso-8859-9'

    soup = BeautifulSoup(response.text, 'html.parser')
    pre_tag = soup.find('pre')
    lines = pre_tag.text.strip().split('\n')[6:]

    data = []
    for line in lines:
        parts = line.split()
        try:
            timestamp = datetime.strptime(parts[0] + " " + parts[1], "%Y.%m.%d %H:%M:%S")
            latitude = float(parts[2])
            longitude = float(parts[3])
            depth     = float(parts[4])
            magnitude = float(parts[6])
            location  = " ".join(parts[8:])
            data.append((timestamp, latitude, longitude, magnitude, depth, location))
        except Exception:
            continue

    return pd.DataFrame(data, columns=[
        "Time", "Latitude", "Longitude", "Magnitude", "Depth", "Location"
    ])

def plot_graph(df):
    plt.clf()
    plt.figure(figsize=(12, 6))
    plt.plot(df["Time"], df["Magnitude"], marker='o', linestyle='-', color='orange')

    # Her bir noktayı etiketle
    for _, row in df.iterrows():
        plt.annotate(
            row["Location"],
            xy=(row["Time"], row["Magnitude"]),
            xytext=(5, 5),               # yazıyı noktanın sağ üstüne offsetler
            textcoords="offset points",
            fontsize=8,
            rotation=30,                 # gerekirse eğim verin
            alpha=0.7
        )

    plt.title("Son 6 Saatte Marmara Bölgesi Depremleri")
    plt.xlabel("Zaman")
    plt.ylabel("Büyüklük (Mw)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.pause(1)

plt.ion()
while True:
    try:
        df = get_earthquake_data()
        df = df[df["Time"] > datetime.now() - pd.Timedelta(hours=6)]

        # Marmara Bölgesi bounding box
        lat_min, lat_max = 39.5, 42.0
        lon_min, lon_max = 26.0, 33.0
        df_marmara = df[
            (df.Latitude.between(lat_min, lat_max)) &
            (df.Longitude.between(lon_min, lon_max))
        ]

        plot_graph(df_marmara)
        time.sleep(60)
    except KeyboardInterrupt:
        print("Program durduruldu.")
        break
    except Exception as e:
        print("Hata:", e)
        time.sleep(60)
