# SDS2-2026-Build-Forward
# Supercharging SDS2: Leveraging AI to Build Custom SDS2 Solutions

Welcome to the official resource page for my 2026 conference presentation! Thank you for attending. Below you will find the scripts we reviewed today, the slide deck, and the exact prompts you can use to start automating your own SDS2 workflows.

---

## 📥 Presentation Files & Downloads

* **Fixed_Ladder_Custom_Member.py** - The fully functional fixed ladder script from the live demo.
* **Add_Material_Parametric.py** - The simple plate-addition script.
* **Supercharging_SDS2_Presentation.pdf** - A copy of today's slide deck.

*(Note: To download a file, click on it in the file list above, then click the "Download raw file" button usually located near the top right of the code box).*

---

## 🧠 AI Prompting Best Practices

The SDS2 .NET API is highly specialized. To get working code from Claude or Gemini, you must guide them strictly. Remember these three golden rules:

1.  **Stop Guessing, Start Guiding:** Always assign the AI a persona first (e.g., "Act as an expert SDS2 API developer").
2.  **Few-Shot Prompting:** Never ask the AI to build from scratch. Always paste a working SDS2 Python script into the prompt as a structural template to prevent hallucinated code.
3.  **Manage Your Context Window:** Start a brand new chat for every new parametric. Do not let the AI's memory get cluttered with old, broken code or unrelated conversations.

---

## 🛠️ The Master "Few-Shot" Prompt Template

Copy and paste this directly into your AI tool of choice. Just be sure to insert your own working reference script at the very bottom!

> **Act as an expert SDS2 parametric developer using Python 3 and the SDS2 .NET API. Your goal is to write a complete, functional Custom Member script for a vertical Fixed Ladder.**
> 
> **The Fixed Ladder must connect between two work points (bottom and top). Please include the following requirements:**
> 
> **1. Dialog Box/Parameters: Include variables for Rung Spacing (default 12 inches), Rail Material (default Flat Bar), Rung Material (default Round Bar), and Ladder Width (default 24 inches).**
> **2. Side Rails: Generate two vertical side rails extending from the bottom work point to the top work point, offset by half the ladder width from the center line.**
> **3. Rungs: Generate horizontal rungs connecting the two side rails. Use a loop to space them evenly based on the Rung Spacing parameter, starting from the bottom work point.**
> 
> **To ensure you use the exact correct SDS2 .NET API syntax, UI layout, and update logic, use the following working Custom Member script as your structural template. Do not invent generic Python geometry; adapt this specific SDS2 class structure to build the ladder.**
> 
> **Here is the working reference script:**
> 
> **[PASTE YOUR WORKING HANDRAIL OR PURLIN SCRIPT HERE]**

---

## 🤝 Let's Connect

If you use these tools to build something incredible, I want to hear about it! 

* **LinkedIn:** [Insert Your LinkedIn URL Here]
* **Email:** [Insert Your Email Address Here]
