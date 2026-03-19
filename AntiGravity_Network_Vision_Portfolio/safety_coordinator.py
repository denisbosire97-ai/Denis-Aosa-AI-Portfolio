import time
import logging
from typing import Dict, Any, Tuple

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class AntiGravitySafetyBrain:
    """
    Integrates System Networking checks with YOLOv8 & MediaPipe Computer Vision results
    to enforce OSHA safety logic continuously.
    """

    def __init__(self, target_max_latency_ms: int = 20):
        # URLLC constraint (5G Private Network Requirement)
        self.target_max_latency_ms = target_max_latency_ms
        
        # OSHA Critical hazard taxonomy
        self.critical_hazards = [
            "forklift_reversing", 
            "forklift_proximity", 
            "suspended_load", 
            "trip_wire", 
            "unsecured_scaffolding"
        ]

    def verify_network_health(self, current_latency_ms: float) -> bool:
        """Evaluates whether the 5G Network is maintaining URLLC stability."""
        if current_latency_ms > self.target_max_latency_ms:
            logging.error(f"NETWORK DEGRADATION: Current latency {current_latency_ms}ms exceeds " 
                          f"the {self.target_max_latency_ms}ms 5G lifecycle threshold.")
            return False
        return True

    def process_frame_data(self, telemetry_data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Ingests frame perception data (Mocked output of YOLOv8-Nano & MediaPipe)
        and outputs the 'Stop & Assess' HUD trigger boolean.
        """
        # 1. 5G Network Latency Verification
        network_latency = telemetry_data.get("network_latency_ms", 999)
        if not self.verify_network_health(network_latency):
             return True, "SYSTEM WARNING: Latency High. Proceed with extreme caution."

        # 2. YOLOv8-Nano OSHA Object Detection Logic
        detected_objects = telemetry_data.get("yolo_objects_detected", [])
        for obj in detected_objects:
            if obj in self.critical_hazards:
                warn_msg = f"OSHA ALERT (HUD RED): Critical {obj.replace('_', ' ').upper()} detected in path."
                logging.warning(warn_msg)
                return True, warn_msg

        # 3. MediaPipe Ergonomic Posture Logic (OSHA Lifting Protocol)
        spine_angle = telemetry_data.get("mediapipe_spine_angle", 90)
        knee_angle = telemetry_data.get("mediapipe_knee_angle", 180)
        
        # If bending drastically at the waist (spine < 45 deg) without bending knees (knees > 160 deg)
        if spine_angle < 45 and knee_angle > 160:
            warn_msg = "ERGONOMIC ALERT (HUD ORANGE): Improper lifting posture. Bend knees, keep back straight."
            logging.warning(warn_msg)
            return True, warn_msg
            
        return False, "Clear. Environment stable."

# ====== TEST SIMULATION ======
if __name__ == "__main__":
    brain = AntiGravitySafetyBrain()
    
    print("--- SIMULATING PERFECT 5G CONDITIONS ---")
    safe_scenario = {
        "network_latency_ms": 12.5, # Excellent 5G time
        "yolo_objects_detected": ["pallet", "cone"],
        "mediapipe_spine_angle": 85,
        "mediapipe_knee_angle": 170
    }
    brain.process_frame_data(safe_scenario)

    print("\n--- SIMULATING FORKLIFT PROXIMITY EVENT ---")
    hazard_scenario = {
        "network_latency_ms": 14.1,
        "yolo_objects_detected": ["forklift_reversing"],
        "mediapipe_spine_angle": 90,
        "mediapipe_knee_angle": 180
    }
    brain.process_frame_data(hazard_scenario)
    
    print("\n--- SIMULATING WIFI 6 DEGRADATION ---")
    lag_scenario = {
        "network_latency_ms": 65.0, # Lag spike typically fatal in CV pipelines
        "yolo_objects_detected": [],
        "mediapipe_spine_angle": 90,
        "mediapipe_knee_angle": 180
    }
    brain.process_frame_data(lag_scenario)
