from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')    
    emotion_result = emotion_detector(text_to_analyze)

    if emotion_result['dominant_emotion'] is None:
        response_message = "Invalid text! Please try again!"
    else:
        response = {
            "anger": emotion_result['anger'],
            "disgust": emotion_result['disgust'],
            "fear": emotion_result['fear'],
            "joy": emotion_result['joy'],
            "sadness": emotion_result['sadness'],
            "dominant_emotion": emotion_result['dominant_emotion']
        }
        response_message = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, \
            'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. \
            The dominant emotion is {response['dominant_emotion']}."
        )
    return response_message

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=500)