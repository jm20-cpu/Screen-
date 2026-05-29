from PIL import Image
import numpy as np

from ai_logic import generate_signal

def analyze_chart(image_path):

    img = Image.open(image_path)

    img = img.resize((224, 224))

    data = np.array(img)

    brightness = np.mean(data)

    volatility = np.std(data)

    result = generate_signal(
        brightness,
        volatility
    )

    return result
