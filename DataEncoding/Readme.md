# Quantum Data Encoding Methods

This repository provides an overview and practical examples of **quantum feature encoding methods**, which are essential for embedding classical data into quantum states. These methods are commonly used in **Quantum Machine Learning (QML)** and **Variational Quantum Algorithms (VQAs)**.

---

## 📖 Methods of Encoding

### 1. Basis Encoding
Encodes classical bits directly into computational basis states.

### 2. Amplitude Encoding
Maps a normalized classical vector into the amplitudes of a quantum state.

### 3. Angle Encoding
Encodes classical data into rotation angles of quantum gates.

### 4. Phase Encoding
Uses phase shifts of quantum states to represent classical data.

### 5. Dense Angle Encoding
A variant of angle encoding where multiple data dimensions are compactly encoded into fewer qubits.

---

## 📊 Encoding with Built-in Feature Maps

Quantum SDKs (like **Qiskit**) provide built-in **feature maps** for efficient embedding:

- **Encoding at arbitrary points**
- **Efficient SU2 Feature Map**
- **Z Feature Map**
- **ZZ Feature Map**
- **Pauli Feature Map**
- **Gallery of Pauli Feature Maps**

---

## 🔍 Review of Built-in Feature Maps
This section summarizes the advantages and limitations of various feature maps, focusing on trade-offs between:
- Expressivity  
- Circuit depth  
- Hardware efficiency  

---

## ⚡ Hardware-Efficient Feature Mapping
Optimized encodings designed for near-term quantum devices, balancing:
- Low gate count  
- Shallow circuit depth  
- Noise resilience  

---
