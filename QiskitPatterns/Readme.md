# Quantum Machine Learning – Qiskit Patterns Demo

This repository contains an implementation of the **Qiskit patterns workflow** for Quantum Machine Learning (QML).  
The project demonstrates how to **map classical data to a quantum problem, optimize for execution, run on Qiskit Runtime primitives, and analyze results**.

The code follows the **4-step Qiskit pattern**:

1. **Map classical inputs to a quantum problem**  
2. **Optimize the problem for quantum execution**  
3. **Execute using Qiskit Runtime Primitives**  
4. **Analyze and post-process results**

---

## 📖 Workflow Walkthrough

### 🔹 Step 1: Map Classical Inputs
- Load training data (`dataset_graph7.csv`) containing 128 samples with 14 features and binary labels (+/-1).  
- Select a subset of the training data for demonstration.  
- Define a **custom quantum feature map** using parameterized circuits (`RY`, `RZ`, `RX` rotations with CZ entanglement).  
- Encode two classical data points into parameterized circuits.  
- Construct an **overlap circuit** to compare the two data encodings.

### 🔹 Step 2: Optimize for Quantum Execution
- (Optional) Use **Qiskit Runtime service** to select the least busy backend.  
- Transpile circuits with an optimization pass manager for efficient execution.  

### 🔹 Step 3: Execute with Qiskit Runtime Primitives
- Evaluate the overlap circuit using the **StatevectorSampler** primitive.  
- Run with `10,000` shots for statistical accuracy.  

### 🔹 Step 4: Analyze and Post-process
- Extract measurement counts.  
- Compute the probability of measuring the all-zeros state (`|0⟩`).  

---

## 🛠️ Tools & Dependencies

- [Qiskit](https://qiskit.org/)  
- Python 3.x  
- pandas, numpy (for handling classical data)  

---


