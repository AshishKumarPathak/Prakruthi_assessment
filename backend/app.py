from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows your React frontend to make requests to this backend

@app.route('/get-prakruthi', methods=['POST'])
def get_prakruthi():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Extract responses from the received data
    responses = data.get('responses', [])
    
    # Debug: Print received responses
    print("Received responses:", responses)
    
    # Process responses to determine Prakruthi
    prakruthi = process_responses(responses)
    
    # Debug: Print determined Prakruthi
    print("Determined Prakruthi:", prakruthi)
    
    # Return the Prakruthi as JSON
    return jsonify({'prakruthi': prakruthi})

def process_responses(responses):
    # Initialize counters for Vata, Pitta, and Kapha

    vata_score = 0
    pitta_score = 0
    kapha_score = 0
    total_score = 0
    
    # Define scoring for each question
    scoring_rules = [
        # Question 1
        { "Slim": (2, 0, 0), "Average": (0, 1, 0), "Heavy": (0, 0, 2) },
        # Question 2
        { "Dry": (2, 0, 1), "Oily": (0, 2, 0), "Normal": (0, 1, 2) },
        # # Question 3
        # { "Warm": (0, 2, 0), "Cold": (2, 0, 0), "Neutral": (1, 1, 1) },
        # # Question 4
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 5
        # { "Cold": (2, 0, 0), "Hot": (0, 2, 0), "Neutral": (1, 1, 1) },
        # # Question 6
        # { "Frequent": (2, 0, 0), "Occasional": (1, 1, 1), "Rarely": (0, 2, 0) },
        # # Question 7
        # { "Well": (2, 1, 0), "Moderately": (1, 1, 1), "Poorly": (0, 2, 0) },
        # # Question 8
        # { "Yes": (2, 0, 0), "No": (0, 2, 0), "Sometimes": (1, 1, 1) },
        # # Question 9
        # { "Good": (2, 0, 0), "Average": (1, 1, 1), "Poor": (0, 2, 0) },
        # # Question 10
        # { "Morning": (2, 0, 0), "Evening": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 11
        # { "Rich": (2, 0, 0), "Light": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 12
        # { "Regular": (2, 0, 0), "Irregular": (0, 2, 0), "Occasional": (1, 1, 1) },
        # # Question 13
        # { "Gain": (2, 0, 0), "Lose": (0, 2, 0), "Stable": (1, 1, 1) },
        # # Question 14
        # { "Frequent": (2, 0, 0), "Occasional": (1, 1, 1), "Rarely": (0, 2, 0) },
        # # Question 15
        # { "Strong": (2, 0, 0), "Weak": (0, 2, 0), "Average": (1, 1, 1) },
        # # Question 16
        # { "Well": (2, 0, 0), "Moderately": (1, 1, 1), "Poorly": (0, 2, 0) },
        # # Question 17
        # { "Yes": (2, 0, 0), "No": (0, 2, 0), "Sometimes": (1, 1, 1) },
        # # Question 18
        # { "Good": (2, 0, 0), "Average": (1, 1, 1), "Poor": (0, 2, 0) },
        # # Question 19
        # { "Yes": (2, 0, 0), "No": (0, 2, 0), "Sometimes": (1, 1, 1) },
        # # Question 20
        # { "Dry": (2, 0, 1), "Oily": (0, 2, 0), "Normal": (0, 1, 2) },
        # # Question 21
        # { "Anxious": (2, 0, 0), "Calm": (0, 2, 0), "Neutral": (1, 1, 1) },
        # # Question 22
        # { "Well": (2, 0, 0), "Moderately": (1, 1, 1), "Poorly": (0, 2, 0) },
        # # Question 23
        # { "Yes": (2, 0, 0), "No": (0, 2, 0), "Occasionally": (1, 1, 1) },
        # # Question 24
        # { "Frequently": (2, 0, 0), "Occasionally": (1, 1, 1), "Rarely": (0, 2, 0) },
        # # Question 25
        # { "Spicy": (2, 0, 0), "Mild": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 26
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 27
        # { "Overeat": (2, 0, 0), "Undereat": (0, 2, 0), "Balanced": (1, 1, 1) },
        # # Question 28
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 29
        # { "Yes": (2, 0, 0), "No": (0, 2, 0), "Occasionally": (1, 1, 1) },
        # # Question 30
        # { "Well": (2, 0, 0), "Moderately": (1, 1, 1), "Poorly": (0, 2, 0) },
        # # Question 31
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 32
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 33
        # { "Social": (2, 0, 0), "Solitary": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 34
        # { "Strong": (2, 0, 0), "Mild": (0, 2, 0), "Neutral": (1, 1, 1) },
        # # Question 35
        # { "Optimistic": (2, 0, 0), "Pessimistic": (0, 2, 0), "Neutral": (1, 1, 1) },
        # # Question 36
        # { "Light": (2, 0, 0), "Medium": (1, 1, 1), "Dark": (0, 2, 0) },
        # # Question 37
        # { "Cool": (2, 0, 0), "Warm": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 38
        # { "Frequently": (2, 0, 0), "Occasionally": (1, 1, 1), "Rarely": (0, 2, 0) },
        # # Question 39
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 40
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 41
        # { "Strong": (2, 0, 0), "Moderate": (1, 1, 1), "Weak": (0, 2, 0) },
        # # Question 42
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 43
        # { "Dry": (2, 0, 1), "Oily": (0, 2, 0), "Normal": (0, 1, 2) },
        # # Question 44
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 45
        # { "Light": (2, 0, 0), "Heavy": (0, 2, 0), "Medium": (1, 1, 1) },
        # # Question 46
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 47
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 48
        # { "Optimistic": (2, 0, 0), "Pessimistic": (0, 2, 0), "Neutral": (1, 1, 1) },
        # # Question 49
        # { "Light": (2, 0, 0), "Heavy": (0, 2, 0), "Medium": (1, 1, 1) },
        # # Question 50
        # { "Strong": (2, 0, 0), "Moderate": (1, 1, 1), "Weak": (0, 2, 0) },
        # # Question 51
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 52
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 53
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 54
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 55
        # { "Light": (2, 0, 0), "Heavy": (0, 2, 0), "Medium": (1, 1, 1) },
        # # Question 56
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 57
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
        # # Question 58
        # { "Light": (2, 0, 0), "Heavy": (0, 2, 0), "Medium": (1, 1, 1) },
        # # Question 59
        # { "Routine": (2, 0, 0), "Variety": (0, 2, 0), "Both": (1, 1, 1) },
        # # Question 60
        # { "High": (2, 0, 0), "Moderate": (1, 1, 1), "Low": (0, 2, 0) },
    ]
    
    # Validate if we have the correct number of responses
    if len(responses) != len(scoring_rules):
        raise ValueError("Number of responses does not match the number of questions")
    
    # Score responses
    for i, response in enumerate(responses):
        if response in scoring_rules[i]:
            vata_score += scoring_rules[i][response][0]
            pitta_score += scoring_rules[i][response][1]
            kapha_score += scoring_rules[i][response][2]
    
    # Calculate total score
    total_score = vata_score + pitta_score + kapha_score
    if total_score == 0:
        return {'Vata': 0, 'Pitta': 0, 'Kapha': 0, 'Balanced': 0}
    
    # Calculate percentages
    vata_percentage = (vata_score / total_score) * 100
    pitta_percentage = (pitta_score / total_score) * 100
    kapha_percentage = (kapha_score / total_score) * 100
    
    # Determine Prakruthi type
    if vata_score > pitta_score and vata_score > kapha_score:
        prakruthi_type = "Vata Prakruthi"
    elif pitta_score > vata_score and pitta_score > kapha_score:
        prakruthi_type = "Pitta Prakruthi"
    elif kapha_score > vata_score and kapha_score > pitta_score:
        prakruthi_type = "Kapha Prakruthi"
    else:
        prakruthi_type = "Balanced Prakruthi"

    # Return percentages and type
    return {
        'Vata': vata_percentage,
        'Pitta': pitta_percentage,
        'Kapha': kapha_percentage,
        'PrakruthiType': prakruthi_type
    }

if __name__ == '__main__':
    app.run(debug=True)