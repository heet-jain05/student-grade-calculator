def validate_score(value):
    score = int(value)

    if score < 0 or score > 100:
        raise ValueError(
            "Score must be between 0 and 100"
        )

    return score