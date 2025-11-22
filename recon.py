import re
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

class ReconModule:
    def __init__(self):
        self.model = self.load_model()
    
    def load_model(self):
        try:
            with open('models/vuln_predictor.pkl', 'rb') as f:
                return pickle.load(f)
        except:
            data = pd.DataFrame({'port': [23, 80, 443], 'service': ['telnet', 'http', 'https'], 'vuln': [1, 0, 1]})  # Telnet high vuln
            self.model = RandomForestClassifier().fit(data[['port']], data['vuln'])
            pickle.dump(self.model, open('models/vuln_predictor.pkl', 'wb'))
            print("[DEBUG] Recon model trained and saved.")
            return self.model
    
    def run(self, target, nmap_output):
        ports = []
        if nmap_output:
            # Parse ports from output (e.g., "23/tcp open telnet")
            matches = re.findall(r'(\d+)/tcp\s+open\s+(\w+)', nmap_output)
            ports = [int(port) for port, service in matches]
        else:
            ports = [23]  # Default telnet
        predictions = self.model.predict(pd.DataFrame({'port': ports}))
        return {'ports': ports, 'vulns': predictions}
