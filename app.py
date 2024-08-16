from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/receive_lead', methods=['POST'])
def receive_lead():
    try:
        # Extract lead data from form-encoded payload
        lead_data = {
            'listingId': request.form.get('listingId'),
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'movingDate': request.form.get('movingDate'),
            'numBedroomsSought': request.form.get('numBedroomsSought'),
            'numBathroomsSought': request.form.get('numBathroomsSought'),
            'message': request.form.get('message'),
            # Add other fields as needed
        }

        # Process the lead (in this example, we're just printing it)
        print("Received lead:", json.dumps(lead_data, indent=2))

        # Here you would typically:
        # 1. Validate the data
        # 2. Store it in your database
        # 3. Trigger any necessary notifications or workflows

        # Respond with success
        return jsonify({"status": "success", "message": "Lead received successfully"}), 200

    except Exception as e:
        # Log the error and respond with an error message
        print(f"Error processing lead: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)