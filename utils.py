# Fonctions utilitaires comme le surlignage, etc.
import re
from difflib import SequenceMatcher

def appliquer_regles_personnalisees(texte):
    texte_corrige = texte
    # Ajoute ici toutes tes règles...
    texte_corrige = re.sub(r'أَلِفْ', 'ا', texte_corrige)
    texte_corrige = re.sub(r'لَامْ', 'لَ', texte_corrige)
    texte_corrige = re.sub(r'مِيمْ', 'مِ', texte_corrige)
    texte_corrige = re.sub(r'رَا', 'رَ', texte_corrige)
    texte_corrige = re.sub(r'صَادْ', 'صَ', texte_corrige)
    texte_corrige = re.sub(r'كَافْ', 'كَ', texte_corrige)
    texte_corrige = re.sub(r'هَا', 'هَ', texte_corrige)
    texte_corrige = re.sub(r'يَا', 'يَ', texte_corrige)
    texte_corrige = re.sub(r'عَيْن',  'ع', texte_corrige)
    texte_corrige = re.sub(r'عَيْنِ ', 'عِ' , texte_corrige)
    texte_corrige = re.sub(r'طَا', 'طَ', texte_corrige)
    texte_corrige = re.sub(r'سِينْ', 'سِ', texte_corrige)
    texte_corrige = re.sub(r'حَا', 'حَ', texte_corrige)
    texte_corrige = re.sub(r'قَافْ', 'قَ', texte_corrige)
    texte_corrige = re.sub(r'نُونْ', 'نُ', texte_corrige)

    texte_corrige = re.sub(r'أَلِفْ لَامْ مِيمْ رَا', 'الٓمٓر',texte_corrige)
    texte_corrige = re.sub(r'أَلِفْ لَامْ مِيمْ', 'الٓمٓ', texte_corrige)
    texte_corrige = re.sub(r'أَلِفْ لَامْ رَا', 'الٓر', texte_corrige)
    texte_corrige = re.sub(r'كَافْ هَا يَا عَيْنْ صَادْ', 'كٓهيعٓصٓ', texte_corrige)
    texte_corrige = re.sub(r'طَاهَا', 'طه', texte_corrige)
    texte_corrige = re.sub(r'طَا سِينْ مِيمْ', 'طسٓمٓ', texte_corrige)
    texte_corrige= re.sub(r'طَا سِينْ', 'طسٓ', texte_corrige)
    texte_corrige = re.sub(r'يَاسِينْ', 'يسٓ', texte_corrige)
    texte_corrige = re.sub(r'صَادْ', 'صٓ', texte_corrige)
    texte_corrige = re.sub(r'حَامِيمْ', 'حمٓ', texte_corrige)
    texte_corrige = re.sub(r'عَيْنْ سِينْ قَافْ', 'عٓسٓقٓ', texte_corrige)
    return texte_corrige

def surligner_erreurs(reference, transcription):
    output = ""
    matcher = SequenceMatcher(None, reference, transcription)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            output += reference[i1:i2]
        else:
            output += f"<span style='background-color:red; color:white;'>{reference[i1:i2]}</span>"
    return output
