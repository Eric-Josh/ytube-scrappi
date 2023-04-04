from flask import Flask

# Import api routes
from src.scrapper import scrapper_blueprint
from src.reqforwarder import forwarder_blueprint
from src.autoSuggestKeyword import autosuggest_blueprint
from src.converter import converter_blueprint
from src.m3u8ToMp4 import m3u8ToMp4_blueprint
from src.HLSToMp4 import HLSToMp4_blueprint

app = Flask(__name__)
# Register blueprint
app.register_blueprint(scrapper_blueprint)
app.register_blueprint(forwarder_blueprint)
app.register_blueprint(autosuggest_blueprint)
app.register_blueprint(converter_blueprint)
app.register_blueprint(m3u8ToMp4_blueprint)
app.register_blueprint(HLSToMp4_blueprint)

@app.route('/')
def home():
    return 'Silence is Gold!'

if __name__ == "__main__":
    app.run(debug=True)