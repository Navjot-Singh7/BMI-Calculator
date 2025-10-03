# 🏋️ BMI Calculator

A modern, sleek BMI (Body Mass Index) calculator built with Python and ttkBootstrap, featuring real-time calculations and a beautiful dark theme interface.

## ✨ Features

- **Real-time BMI Calculation** - Instant updates as you adjust values
- **Modern Dark Theme** - Easy on the eyes with ttkBootstrap's "darkly" theme
- **Precise Controls** - Fine-tuned weight adjustment with ±1kg and ±0.1kg buttons
- **Interactive Height Slider** - Smooth height selection from 100cm to 250cm
- **Clean Visual Design** - Large, readable display with intuitive layout

## 🛠️ Tech Stack

- **Python 3** - Core programming language
- **Tkinter** - Standard GUI framework
- **ttkBootstrap** - Modern styling and themes
- **CustomTkinter** - Enhanced UI components

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install ttkbootstrap customtkinter
```

Running the Application

```bash
python main.py
```

The interface features:

· Large BMI Display - Clear, prominent result showing
· Weight Control Panel - Precise increment/decrement buttons
· Height Slider - Smooth adjustable height selector
· Modern Styling - Dark theme with green accent colors

🧮 How BMI is Calculated

```python
BMI = weight (kg) / (height (m) ** 2)
```

Example:

· Weight: 70 kg
· Height: 1.75 m
· BMI = 70 / (1.75 * 1.75) = 22.86

🎯 Key Features in Detail

Real-time Updates

· BMI recalculates instantly with every weight/height change
· Smooth slider interactions with live height display
· Visual feedback on all user interactions

Precision Controls

· ±1 kg buttons for larger adjustments
· ±0.1 kg buttons for fine-tuning
· Slider for continuous height selection

Responsive Design

· Clean, centered layout
· Large, readable fonts
· Intuitive button placement

🔧 Code Architecture

The application uses a modular class structure:

· App - Main application window and BMI logic
· ResultLabel - Large BMI display component
· InputFrame - Weight control panel
· HeightInput - Height slider with live display
· UnitSwitcher - Future unit conversion toggle

🌟 Future Enhancements

· Imperial units (pounds/feet) support
· BMI category indicators (Underweight, Normal, etc.)
· Weight history tracking
· Progress visualization
· Multiple user profiles

---

⭐ If you find this BMI calculator useful, please give it a star!

---

Built with attention to detail and user experience - Making health calculations accessible and visually appealing! 🎨✨