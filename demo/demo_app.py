import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from demo_ai import get_ai_2 as get_ai, train_ai, map

from flask import jsonify
from web.app import get_app
app = get_app()

AI_MIN_OK = 22
AI_MAX_OK = 28
AI_LOC = 25
AI_SCL = 2.2

ai_model = get_ai()
train_ai(ai_model, AI_MIN_OK, AI_MAX_OK, AI_LOC, AI_SCL, batch_size=32, epochs=4)

@app.route('/api/predict/<value>')
def api_predict(value):
    try:
        value = float(value)
        mapped = map(value, AI_MIN_OK, AI_MAX_OK, 0, 1)

        pred = ai_model.predict([[mapped]])[0]

        ok = pred[0] > pred[1]
        confidence = max(pred[0], pred[1])

        result = "ok" if ok else "not ok"
        return jsonify({ 
            "status": "ok", 
            "result": result, 
            "confidence": f'{(confidence * 100):2.0f}%'
        })

    except Exception as e:
        print(str(e))
        return jsonify({ "status": "error", "message": "Internal server error" })

app.run()