from user_profile import build_user_profile
from fraud_detection import optimize_fraud_rule
from transaction_routing import optimize_route

#transaction data
transactions = [
    {'amount': 50.0, 'location': 'home', 'time_of_day': 12, 'recipient': 'friend', 'is_fraud': False},
    {'amount': 1000.0, 'location': 'abroad', 'time_of_day': 2, 'recipient': 'unknown', 'is_fraud': True},
    {'amount': 200.0, 'location': 'work', 'time_of_day': 9, 'recipient': 'vendor', 'is_fraud': False},
    {'amount': 500.0, 'location': 'abroad', 'time_of_day': 15, 'recipient': 'family', 'is_fraud': False},
    {'amount': 1500.0, 'location': 'home', 'time_of_day': 23, 'recipient': 'unknown', 'is_fraud': True},
]

#creating a user profile
profile = build_user_profile(transactions)
print("User Profile:", profile)

best_rule = optimize_fraud_rule(transactions, profile) #runs the Genetic Algorithm to find the smartest fraud detection rule for specific banking habits
print("Optimized Fraud Rule (weights):", [round(w, 2) for w in best_rule]) #finds the best weights for amount, location, time of day

best_route, min_risk, _ = optimize_route() #runs the Particle Swarm Optimization algorithm to find the safest possible path for money to travel through the banking network
print("Optimized Transaction Route:", best_route) #outputs the best path through the network
print("Minimum Risk:", round(min_risk, 2))

new_tx = {'amount': 1200.0, 'location': 'abroad', 'time_of_day': 3, 'recipient': 'unknown'} # test transaction

risk_score = (new_tx['amount'] / profile['avg_amount'] * best_rule[0]) + \
             (1 if new_tx['location'] not in profile['common_locations'] else 0) * best_rule[1] + \
             (1 if new_tx['time_of_day'] > 20 or new_tx['time_of_day'] < 6 else 0) * best_rule[2] # calculate risk score for new transaction

if risk_score > 1.5: #detects high & low risk
    print("High Risk Detected! Suggesting optimized secure route.")
else:
    print("Low Risk. Transaction looks safe.")

print("\nAlgoSafe Optimizer Demo Finished")
