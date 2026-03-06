from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database for restaurants
restaurants = [
    {"id": 1, "name": "Spicy Biryani", "cuisine": "Indian"},
    {"id": 2, "name": "Cheesy Pizza", "cuisine": "Italian"},
    {"id": 3, "name": "Sushi World", "cuisine": "Japanese"}
]

@app.route('/')
def home():
    return "Welcome to JourneyBites Backend!"

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants)

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant['id'] == restaurant_id:
            return jsonify(restaurant)
    return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    data = request.get_json()
    new_id = max(r['id'] for r in restaurants) + 1 if restaurants else 1
    new_restaurant = {
        "id": new_id,
        "name": data.get("name"),
        "cuisine": data.get("cuisine")
    }
    restaurants.append(new_restaurant)
    return jsonify(new_restaurant), 201

if __name__ == '__main__':
    # Run backend on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
