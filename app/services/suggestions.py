def suggest_lifestyle_tips(metrics: dict) -> list:
    suggestions = []

    if metrics.get("water_glasses", 0) < 5:
        suggestions.append("Bugün pek su içmemişsin, bir bardak su içmeyi düşünebilirsin 💧")

    if metrics.get("sleep_hours", 8) < 6:
        suggestions.append("Uykusuzluk modunu etkileyebilir. Bu akşam erken yatmayı dene 😴")

    if metrics.get("coffee_cups", 0) > 3:
        suggestions.append("Bugün bolca kahve içmişsin, yarın biraz azaltmayı denemek ister misin? ☕")

    if metrics.get("screen_time_hours", 0) > 6:
        suggestions.append("Ekran süren yüksek, biraz yürüyüş iyi gelebilir 📵")

    if metrics.get("exercise_minutes", 0) < 15:
        suggestions.append("Bugün çok hareket etmemişsin. Kısa bir yürüyüş bile iyi gelebilir 🏃‍♂️")

    return suggestions
