import numpy as np

def build_user_profile(transactions):
    #user profile of normal user behavior from non-fraudulent transactions.
    amounts = [t['amount'] for t in transactions if not t['is_fraud']] #add amounts only from non-fraudulent transactions
    avg_amount = np.mean(amounts) if amounts else 1.0  # avoid error division by zero, use 1.0 as default
    common_locations = set(t['location'] for t in transactions if not t['is_fraud']) #set of locations from non-fraudulent transactions
    
    return {
        'avg_amount': avg_amount,
        'common_locations': common_locations
    }
