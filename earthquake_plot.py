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
            date_str = parts[0] + " " + parts[1]
            timestamp = datetime.strptime(date_str, "%Y.%m.%d %H:%M:%S")
            latitude = float(parts[2])
            longitude = float(parts[3])
            depth = float(parts[4])
            magnitude = float(parts[6])
            location = " ".join(parts[8:])
            data.append((timestamp, magnitude, depth, location))
        except Exception:
            continue
    return pd.DataFrame(data, columns=["Time", "Magnitude", "Depth", "Location"])

def plot_graph(df):
    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.plot(df["Time"], df["Magnitude"], marker='o', color='orange')
    plt.title("Güncel Depremler (Kandilli Rasathanesi)")
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
        plot_graph(df)
        time.sleep(60)
    except KeyboardInterrupt:
        print("Program durduruldu.")
        break
    except Exception as e:
        print("Hata:", e)
        time.sleep(60)

