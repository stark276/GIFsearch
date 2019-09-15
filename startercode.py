from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    section = "WELCOME TO MY GIF SEARCH PROJECT"

    # TODO: Extract the query term from url using request.args.get()
    query = request.args.get("search")
    # TODO: Make 'params' dictionary containing:
     
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {'q': query,
        'key': 'JTN0N421L3KK',
        'limit': '10'}
    

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation ____
    r = requests.get("https://api.tenor.com/v1/search", params=params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    mygifs_json = r.json()

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    show_my_gifs = mygifs_json["Your Gifs"]

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'
    return render_template('index.html', 
        section = section,
        query =  query,
        show_my_gifs = show_my_gifs)


if __name__ == '__main__':
    app.run(debug=True)
