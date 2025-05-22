# Récupération du texte de référence depuis l’API Al-Quran
import requests

def get_reference_text(sourah, ayah_start, ayah_end):
    text = ""
    for ayah in range(ayah_start, ayah_end + 1):
        url = f"https://api.alquran.cloud/v1/ayah/{sourah}:{ayah}/ar"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            text += data["data"]["text"] + " "
    return text.strip()
