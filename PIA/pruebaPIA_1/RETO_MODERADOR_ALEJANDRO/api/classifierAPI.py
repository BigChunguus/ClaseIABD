import re

OFFENSIVE_WORDS = [
    "idiota", "tonto", "imbécil", "estúpido", "gilipollas",
    "pendejo", "bobo", "capullo", "mierda"
]

offensive_pattern = re.compile(
    r'\b(?:' + '|'.join(re.escape(word) for word in OFFENSIVE_WORDS) + r')\b',
    flags=re.IGNORECASE
)

def clean_message(texto):
    """Reemplaza palabras ofensivas por '[MENSAJE CENSURADO]'."""
    cleaned_message = offensive_pattern.sub("[MENSAJE CENSURADO]", texto)
    return cleaned_message
