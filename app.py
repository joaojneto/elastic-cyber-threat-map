from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

# Função para ler a primeira linha do arquivo e removê-la
def read_and_remove_line(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        return None
    
    # A primeira linha será retornada e o restante será reescrito no arquivo
    first_line = lines[0].strip()
    second_line = lines[1].strip()


    with open(file_path, 'w') as file:
        file.writelines(lines[2:])

    return first_line,second_line

@app.route('/')
def index():
    #return "Hello World! This is a version with error..."
    return render_template("index.html"), 200
    #raise Exception("Uuuuppppsss")

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Altere para o caminho do seu arquivo
        file_path = 'load.txt'
        line1,line2 = read_and_remove_line(file_path)
        
        line = line1 + "," + line2

        if line:
            return jsonify({"line": line})
        else:
            return jsonify({"error": "No more lines"}), 200
    except:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
