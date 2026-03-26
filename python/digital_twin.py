import time
import random
from web3 import Web3
import os

# Connect to local blockchain (Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
if not w3.is_connected():
    print("Failed to connect to blockchain. Running in mock mode.")
    mock_mode = True
else:
    mock_mode = False

# Contract ABI and address (assuming deployed)
contract_address = '0x...'  # Replace with actual address
contract_abi = [...]  # Load from artifacts/SupplyChain.json
if not mock_mode:
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

class Order:
    def __init__(self, id, name, description, stage='Init'):
        self.id = id
        self.name = name
        self.description = description
        self.stage = stage
        self.timestamp = time.time()


class Shipment:
    def __init__(self, order_id, from_stage, to_stage, state='pending'):
        self.order_id = order_id
        self.from_stage = from_stage
        self.to_stage = to_stage
        self.state = state  # pending, in_transit, delivered


class DigitalTwin:
    def __init__(self):
        self.orders = []
        self.shipments = []

    def add_order(self, name, description):
        order_id = len(self.orders) + 1
        order = Order(order_id, name, description)
        self.orders.append(order)
        # Sync to blockchain if not mock
        if not mock_mode:
            # Call addMedicine
            pass
        return order

    def advance_stage(self, order_id, new_stage):
        order = next((o for o in self.orders if o.id == order_id), None)
        if order:
            order.stage = new_stage
            shipment = Shipment(order_id, order.stage, new_stage, 'in_transit')
            self.shipments.append(shipment)
            # Sync to blockchain
            if not mock_mode:
                # Call appropriate function like RMSsupply, etc.
                pass
            time.sleep(random.uniform(0.5, 2))  # Simulate time
            shipment.state = 'delivered'

    def sync_from_blockchain(self):
        if mock_mode:
            return
        # Fetch MedicineStock from contract
        for i in range(1, contract.functions.medicineCtr().call() + 1):
            med = contract.functions.MedicineStock(i).call()
            # Update local orders
            pass

    def simulation_loop(self):
        print("Starting Digital Twin Simulation...")
        while True:
            # Add random orders
            if random.random() < 0.1:
                self.add_order(f"Medicine {len(self.orders)+1}", "Description")
            # Advance random orders
            for order in self.orders:
                if order.stage != 'sold':
                    stages = ['RawMaterialSupply', 'Manufacture', 'Distribution', 'Retail', 'sold']
                    current_index = stages.index(order.stage) if order.stage in stages else 0
                    if current_index < len(stages) - 1 and random.random() < 0.05:
                        self.advance_stage(order.id, stages[current_index + 1])
            self.sync_from_blockchain()
            print(f"Orders: {len(self.orders)}, Shipments: {len(self.shipments)}")
            time.sleep(1)
            

if __name__ == "__main__":
    dt = DigitalTwin()
    dt.simulation_loop()
