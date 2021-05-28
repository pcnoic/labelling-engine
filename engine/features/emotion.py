import text2emotion as te

# Returns dict of 5 emotion features
def emotion_extraction(data):
    return te.get_emotion(data)
