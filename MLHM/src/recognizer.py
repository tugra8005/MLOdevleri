from hmmlearn import hmm
import numpy as np
import os
import sys


def load_model(name, n_states):
    try:
        # Check if the data directory exists first
        data_path = 'data'
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"The directory '{data_path}' does not exist. Please create it.")

        # Paths for the matrices
        trans_file = os.path.join(data_path, f'{name}_transition.csv')
        emission_file = os.path.join(data_path, f'{name}_emission.csv')

        # Load the files
        trans_matrix = np.genfromtxt(trans_file, delimiter=',')
        emission_matrix = np.genfromtxt(emission_file, delimiter=',')

        # Handle genfromtxt failure (returns nan if file is missing or empty)
        if np.isnan(trans_matrix).any() or np.isnan(emission_matrix).any():
            raise ValueError(f"Could not read data from {name} CSVs. Check formatting.")

        # Initialize and configure the model
        model = hmm.CategoricalHMM(n_components=n_states)
        model.startprob_ = np.array([1.0] + [0.0] * (n_states - 1))
        model.transmat_ = trans_matrix
        model.emissionprob_ = emission_matrix
        
        return model        

    except FileNotFoundError as e:
        print(f"FILE ERROR: {e}", file=sys.stderr, flush=True)
        return None
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}", file=sys.stderr, flush=True)
        return None


def main():
    model_ev = load_model('ev', 2)
    if model_ev:
        test_data = np.array([[0, 1]]).T 
        logprob, sequence = model_ev.decode(test_data)
        print(f"Successfully decoded sequence: {sequence}")
        print(f"Log Probability: {logprob}")
        score = model_ev.score(test_data)
        print(f"Model Score: {score}")
    else:
        print("Model failed to load. Check the error messages above.")
       # Load the 4-state OKUL model
    model_okul = load_model('okul', 4)
    
    if model_okul and model_ev:
        score_ev = model_ev.score(test_data)
        score_okul = model_okul.score(test_data)
        
        print("\n--- FINAL CLASSIFICATION ---")
        print(f"EV Score:   {score_ev:.4f}")
        print(f"OKUL Score: {score_okul:.4f}")
        
        if score_ev > score_okul:
            print("Prediction: The word spoken was 'EV'")
        else:
            print("Prediction: The word spoken was 'OKUL'") 


if __name__ == '__main__':
    main()
