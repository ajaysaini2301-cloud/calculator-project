from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Zero से भाग नहीं कर सकते'})
            result = num1 / num2
        else:
            return jsonify({'error': 'गलत ऑपरेशन'})

        return jsonify({'result': result})
    except:
        return jsonify({'error': 'गलत इनपुट!'})

if __name__ == '__main__':
    app.run(debug=True)