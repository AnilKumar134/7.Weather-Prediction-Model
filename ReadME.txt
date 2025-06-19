Weather Prediction Project

Python Version:
- 3.10.0


How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the Streamlit server.py:
   streamlit run server.py

---

Known Issues & Recommendations:

- TensorFlow Installation:
  After installing TensorFlow, you might face compatibility issues with numpy.
  Solution: Install a compatible numpy version by running:
  pip install "numpy<2"

- Protobuf Compatibility:
  TensorFlow and Streamlit sometimes have conflicts with the protobuf package.
  Solution: If you encounter protobuf-related errors, try uninstalling protobuf:
  pip uninstall protobuf
  Reinstall only if necessary.

- VS Code File Location Issue:
  If VS Code cannot locate files when running the app, try these steps:
  - Open your project folder in VS Code by Shift + Right Click on the folder, then select Open with Code.
  - Alternatively, you can use Jupyter Notebook or open the folder via a PowerShell window.

---
