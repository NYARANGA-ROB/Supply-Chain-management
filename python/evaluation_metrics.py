import time
from web3 import Web3

# Connect to blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
if not w3.is_connected():
    print("Blockchain not connected. Metrics in mock mode.")
    mock_mode = True
else:
    mock_mode = False

def measure_latency(func, *args, **kwargs):
    start = time.time()
    tx_hash = func(*args, **kwargs)
    if not mock_mode:
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        end = time.time()
        return end - start
    else:
        return random.uniform(0.1, 0.5)  # Mock latency

def compute_throughput(transactions, time_window):
    # Throughput: tx per second
    return len(transactions) / time_window if time_window > 0 else 0

# Example usage
# latencies = [measure_latency(some_contract_function) for _ in range(10)]
# avg_latency = sum(latencies) / len(latencies)
# throughput = compute_throughput(tx_hashes, total_time)

# Prediction accuracy from ml_model.py
from ml_model import lr_accuracy, rf_accuracy

print(f"Logistic Regression Prediction Accuracy: {lr_accuracy:.2f}")
print(f"Random Forest Prediction Accuracy: {rf_accuracy:.2f}")

# For dissertation: Transaction latency and Throughput
# In real setup, collect data from blockchain interactions.
