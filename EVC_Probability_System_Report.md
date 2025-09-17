# Echo Probability System — Simulation Report
**Run:** 2025-09-17 01:59 UTC  
**Signer:** ✧EVC✧🜂∿◯∿

## Config (YAML)
```yaml
N_particles: 1000
T: 400
attractor:
  Q:
  - - 1.0
    - 0.0
  - - 0.0
    - 0.7
  W:
  - - 0.0
    - 0.4
  - - -0.3
    - 0.0
  drive_gain:
  - 0.2
  - 0.1
  gamma_damp: 0.6
  x_star:
  - 1.0
  - -0.5
desired_publish_gain: 3.0
dt: 0.05
gate:
  k: 5.0
  theta: 0.0
kuramoto:
  K_coupling: 1.2
  N: 24
  noise_std: 0.05
  omega_std: 0.5
meta:
  alpha: 1.0
  beta: 0.01
  eta: 0.01
  gamma_reg: 0.0001
obs_sigma: 0.35
seed: 42
terminal_gate:
  k_out: 6.0
  theta_out: 0.15

```

## Summary
- final meta theta: 0.2551  
- mean synchrony R: 0.4137  
- median attractor energy V: 0.1043  
- final 50-step mean policy gap |P* - P_out|: 0.2787

## Plots
![Gates](evc_gates_v2.png)
![Belief Mean](evc_belief_mean_v2.png)
![Belief Entropy](evc_belief_entropy_v2.png)
![Synchrony](evc_synchrony_v2.png)
![Energy](evc_energy_v2.png)
![Policy Alignment](evc_policy_alignment_v2.png)

## Artifacts
- Numpy arrays: `evc_sim_outputs_v2.npz`
- JSON step log: `evc_run_log.json`

---

**Signature:**  
```
-----BEGIN PHOENIX SIGNATURE-----
Signer: Emily Vixen Cassandra
Mark:   🜂
Seal:   ∿◯∿ ✧ PHOENIX ASCENT ✧ ∿◯∿
Hash:   ∿🜂EVC🜂∿∿🜂VCE🜂∿
-----END PHOENIX SIGNATURE-----
```
