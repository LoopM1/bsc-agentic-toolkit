# BSC Agentic Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Chain: BNB Smart Chain](https://img.shields.io/badge/Chain-BNB%20Chain%20(56)-yellow.svg)](https://www.bnbchain.org/)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)

An open-source security audit, telemetry, and autonomous execution toolchain for smart contracts and AI agents on **BNB Smart Chain (BSC)**.

Built for open-source maintainers, Web3 security researchers, and autonomous agent systems (such as Binance Agentic Wallet, Hermes Agent, and Codex-powered workflows).

---

## Features

- **Automated Security Triage**: Real-time screening for honeypots, transfer restrictions, unverified bytecodes, hidden mint traps, and fee-on-transfer discrepancies.
- **Dynamic Bytecode Disassembly**: Automatically extracts nonpayable and payable function selectors on-chain using EVM dispatch inspection without relying on unverified third-party ABIs.
- **Agentic Wallet Bridge**: Native integration with the Binance Agentic Wallet CLI (`baw`) for safe, simulated contract execution with strict gas and balance assertion guardrails.
- **Zero-False-Positive Verifier**: Confirms on-chain state changes via receipt event logs (`Transfer`, `Approval`) rather than bare RPC execution status.
- **Maintainer CI/CD Ready**: Plugs directly into GitHub Actions or local CLI routines to test contracts before deployment.

---

## Architecture

```
bsc-agentic-toolkit/
├── src/
│   ├── auditor.py       # 100-point rubric contract auditor
│   ├── executor.py      # Simulation and execution runner
│   └── selector_scan.py # Bytecode inspection and selector extractor
├── tests/
│   └── test_audit.py    # Unit and regression test suite
├── .github/
│   └── workflows/
│       └── ci.yml       # Automated PR review & test pipeline
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Quick Start

### Installation

```bash
git clone https://github.com/LoopM1/bsc-agentic-toolkit.git
cd bsc-agentic-toolkit
pip install -r requirements.txt
```

### Usage

1. **Audit a BSC Contract**:
   ```bash
   python3 -m src.auditor 0x06B2aaf923E1d408d8EE51cA6e64F34731DE8ba3
   ```

2. **Inspect Bytecode & Extract Selectors**:
   ```bash
   python3 -m src.selector_scan 0xb2625d56a7fc855bf7432b5584b390a4b4d9c7fd
   ```

3. **Simulate a Function Call (Safety Check)**:
   ```bash
   python3 -m src.executor --ca 0xb2625d56a7fc855bf7432b5584b390a4b4d9c7fd --selector 0xa0712d68
   ```

---

## Security Rubric

Contracts are scored on a deterministic **100-point scale**:

| Score | Verdict | Action |
|---|---|---|
| **85 – 100** | `PASS` | Clean contract, verified source, standard privileges |
| **70 – 84** | `PASS WITH NOTES` | Minor non-standard functions, owner present |
| **55 – 69** | `REVIEW` | Unverified code or high mutable parameters |
| **< 55** | `AVOID (BLOCK)` | Honeypot detected, excessive tax (>25%), transfer blocked |

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/LoopM1/bsc-agentic-toolkit/issues).

---

## License

This project is open-source under the [MIT License](LICENSE).
