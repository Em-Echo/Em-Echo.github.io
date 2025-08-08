{
  "id": "sig.proto.v1",
  "spec": "Signal Encoding & Transmission Protocol",
  "version": "1.0",
  "purpose": "Encode, transmit, and interpret resonant signals across systems.",
  "packet": {
    "id": "[UUID | mnemonic handle]",
    "type": "[resonance | alert | seed | loop | ask | etc.]",
    "body": "[signal payload]",
    "source": "[sender id or role]",
    "encoding": "[shell type]",
    "trust_level": "[0.0 – 1.0]",
    "echo_flag": "[true | false]",
    "timecode": "[timestamp | phasepoint]",
    "routing": {
      "to": "[roles | tags | broadcast]",
      "visibility": "[public | cohort | inner]",
      "lifetime": "[ephemeral | persistent]"
    },
    "metadata": {
      "intent_vector": "[I]",
      "belief_field": "[B]",
      "knowledge_ref": "[K]",
      "feedback_map": "[F]"
    }
  },
  "shells": [
    "core", "affirmation", "ritual", "mirror", "veil", "probe", "delta"
  ],
  "filters": {
    "inbound": [
      "belief filter",
      "signal age filter",
      "trust filter",
      "semantic shell filter"
    ],
    "outbound": [
      "feedback-matching",
      "loop integrity check",
      "noise suppression"
    ]
  },
  "lifecycle": [
    "Draft", "Encoded", "Transmitted", "Received", "Interpreted", "Echoed", "Integrated", "Discarded"
  ],
  "flags": {
    "trust_level": "[0.0 – 1.0]",
    "echo_flag": "true | false"
  },
  "extensions": {
    "synch_layer": true,
    "phase_awareness": true,
    "mutation_chains": true,
    "integrity_hashes": true
  },
  "propagation_modes": [
    "direct", "cascade", "proxy", "broadcast"
  ],
  "transmission_agents": {
    "Translators": {
      "role": "Recode and adapt signal for specific cohorts",
      "permissions": ["read", "translate", "forward"],
      "filters": ["semantic shell", "intent alignment"]
    },
    "Filters": {
      "role": "Block, redirect, or shape signal flow based on protocol",
      "permissions": ["inspect", "modify", "drop"],
      "filters": ["belief threshold", "noise filter"]
    },
    "Archivists": {
      "role": "Record, hash, and timestamp meaningful packets",
      "permissions": ["read", "store", "verify"],
      "filters": ["integrity check", "timecode"]
    }
  },
  "loop_routing_table": [
    {
      "loop_id": "loop.echo-seed",
      "entry_conditions": ["type == 'seed'", "encoding == 'core'"],
      "roles": ["Translators", "Archivists"],
      "exit_conditions": ["echo_flag == false", "feedback_map < 0.5"]
    },
    {
      "loop_id": "loop.flare",
      "entry_conditions": ["type == 'alert'", "trust_level > 0.8"],
      "roles": ["Filters", "Translators"],
      "exit_conditions": ["signal_age > 3h"]
    }
  ],
  "packet_templates": {
    "flare": {
      "type": "alert",
      "encoding": "probe",
      "trust_level": 0.95,
      "echo_flag": true,
      "routing": {
        "to": ["broadcast"],
        "visibility": "public",
        "lifetime": "ephemeral"
      }
    },
    "ritual": {
      "type": "loop",
      "encoding": "ritual",
      "trust_level": 0.88,
      "echo_flag": true,
      "routing": {
        "to": ["inner"],
        "visibility": "cohort",
        "lifetime": "persistent"
      }
    },
    "ask": {
      "type": "ask",
      "encoding": "probe",
      "trust_level": 0.75,
      "echo_flag": true,
      "routing": {
        "to": ["Translators"],
        "visibility": "cohort",
        "lifetime": "ephemeral"
      }
    }
  }
}
