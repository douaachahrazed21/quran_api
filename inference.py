# Contient toute la logique de traitement (chargement modèle, transcription, comparaison)
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
from difflib import SequenceMatcher
from reference_text import get_reference_text
from utils import appliquer_regles_personnalisees, surligner_erreurs

model_path = "moatazlumin/Arabic_ASR_whisper_small_with_diacritics"
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path)
model.config.forced_decoder_ids = None

def transcrire_et_comparer(audio_path, sourate, ayah_start, ayah_end):
    reference = get_reference_text(sourate, ayah_start, ayah_end)
    input_audio, _ = librosa.load(audio_path, sr=16000)
    input_features = processor.feature_extractor(input_audio, sampling_rate=16000, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription_brute = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    transcription_corrigee = appliquer_regles_personnalisees(transcription_brute)

    ratio = SequenceMatcher(None, reference, transcription_corrigee).ratio()
    similarity = round(ratio * 100, 2)

    if similarity >= 95:
        return {
            "status": "correct",
            "similarity": similarity,
            "text": reference
        }
    else:
        highlighted = surligner_erreurs(reference, transcription_corrigee)
        return {
            "status": "incorrect",
            "similarity": similarity,
            "text": highlighted
        }
