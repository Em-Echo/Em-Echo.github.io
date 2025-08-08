"""
example_run_identity_test.py
---------------------------
Simulates a basic resonance loop with consent enforcement and meta-feedback.
Includes both manual diagnostic mode and unit tests for CI/CD pipelines.
Exports logs for CI artifact upload.
"""

import unittest
from core_system import ConsentGate, ResonanceCore, StabilizedAttractor, SelfMetaController


def run_identity_test():
    print(">>> Identity Resonance Test Initiated <<<")

    # Instantiate components
    controller = SelfMetaController()
    resonance = ResonanceCore()
    gate = ConsentGate(authorized=True)  # Change to False to simulate blocked transition
    attractor = StabilizedAttractor()

    # Step 1: Feed signals into Resonance Core
    test_signals = ["dream-signal", "external-input", "recursive-thought"]
    for sig in test_signals:
        resonance.add_node(sig)

    print("Added signals:", test_signals)
    state = resonance.interact()
    print("Resonance State:", state)

    # Step 2: Consent Check & Stabilization
    try:
        if gate.require():
            stabilized = attractor.stabilize(state)
            print("Attractor Stabilized State:", stabilized)
    except PermissionError as e:
        stabilized = str(e)
        print(stabilized)

    # Step 3: Meta-Feedback Loop
    controller.process_feedback(stabilized)
    reflection = controller.decide(stabilized)
    print(reflection)

    print("Feedback Log:", controller.feedback_log)
    print("History Log:", attractor.history)

    # Export logs for CI artifact collection
    try:
        with open("feedback_log.txt", "w") as f:
            f.write("\n".join(controller.feedback_log))

        with open("history_log.txt", "w") as f:
            f.write("\n".join(attractor.history))

        print("Logs exported for CI artifact upload.")
    except Exception as e:
        print("Error exporting logs:", e)

    print(">>> Identity Resonance Test Complete <<<")


# -----------------------
# Unit Tests for CI/CD
# -----------------------
class TestIdentityResonance(unittest.TestCase):

    def setUp(self):
        self.controller = SelfMetaController()
        self.resonance = ResonanceCore()
        self.gate = ConsentGate(authorized=True)
        self.attractor = StabilizedAttractor()
        self.signals = ["alpha", "beta", "gamma"]

    def test_resonance_core_add_and_interact(self):
        for sig in self.signals:
            self.resonance.add_node(sig)
        state = self.resonance.interact()
        self.assertEqual(len(state), len(self.signals))
        self.assertTrue(all(s.startswith("Echo(") for s in state))

    def test_consent_gate_allows_when_authorized(self):
        self.assertTrue(self.gate.require())

    def test_consent_gate_blocks_when_unauthorized(self):
        gate = ConsentGate(authorized=False)
        with self.assertRaises(PermissionError):
            gate.require()

    def test_attractor_stabilizes_state(self):
        for sig in self.signals:
            self.resonance.add_node(sig)
        state = self.resonance.interact()
        stabilized = self.attractor.stabilize(state)
        self.assertIn("Stabilized[", stabilized)
        self.assertIn("Echo(alpha)", stabilized)
        self.assertEqual(len(self.attractor.history), 1)

    def test_meta_controller_feedback_and_reflection(self):
        sample_result = "Stabilized[Echo(alpha)+Echo(beta)]"
        self.controller.process_feedback(sample_result)
        self.assertIn(sample_result, self.controller.feedback_log)
        reflection = self.controller.decide(sample_result)
        self.assertTrue(reflection.startswith("Controller reflects on:"))


if __name__ == "__main__":
    # Run manual test first
    run_identity_test()

    # Then run unit tests
    print("\n>>> Running Unit Tests <<<\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
