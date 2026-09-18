import re
import unicodedata
import base64
import codecs

def normalize_text(text: str) -> str:
    text = str(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", " ").replace("\u200c", " ").replace("\u200d", " ")
    text = text.replace("\ufeff", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text

def decode_obfuscation_candidates(text: str):
    candidates = [text]
    s = normalize_text(text)
    # Base64-looking tokens
    for token in re.findall(r"\b[A-Za-z0-9+/]{16,}={0,2}\b", s):
        try:
            decoded = base64.b64decode(token, validate=True).decode("utf-8", errors="ignore")
            if decoded.strip():
                candidates.append(decoded)
        except Exception:
            pass
    # ROT13 candidate
    try:
        rot = codecs.decode(s, "rot_13")
        if rot != s:
            candidates.append(rot)
    except Exception:
        pass
    return candidates

def normalized_for_model(text: str) -> str:
    return " ".join(decode_obfuscation_candidates(text))
