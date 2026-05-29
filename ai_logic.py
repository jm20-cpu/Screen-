import random

def generate_signal(brightness, volatility):

    confidence = random.randint(80, 95)

    signal = "BUY"

    if volatility > 70:
        signal = "SELL"

    trend = "Bullish"

    if signal == "SELL":
        trend = "Bearish"

    return {

        "signal": signal,

        "confidence": confidence,

        "trend": trend,

        "brightness": round(brightness, 2),

        "volatility": round(volatility, 2),

        "analysis": "Screenshot AI analysis completed"
    }
