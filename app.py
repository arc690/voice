from flask import Flask, request, jsonify
import autopep8

app = Flask(__name__)

@app.route('/fix_python_code', methods=['POST'])
def fix_python_code():
    data = request.get_json()
    code = data['code']
    
    try:
        fixed_code = autopep8.fix_code(code)
        return jsonify({'success': True, 'fixed_code': fixed_code})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
