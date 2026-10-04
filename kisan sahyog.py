# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:16:39 2026

@author: HP
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import csv
from datetime import datetime

# Voice library
try:
    import speech_recognition as sr
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False


# =========================================================
# KISAN SAHAYAK
# Bilingual Agricultural Assistance System
# =========================================================

window = tk.Tk()
window.title("Kisan Sahayak")
window.geometry("850x700")
window.minsize(750, 600)

# -------------------- COLORS --------------------

BG = "#F4F8F1"
GREEN = "#2E7D32"
DARK_GREEN = "#1B5E20"
LIGHT_GREEN = "#E8F5E9"
BUTTON = "#4CAF50"
TEXT = "#263238"
WHITE = "#FFFFFF"
ORANGE = "#F57C00"
RED = "#C62828"

window.configure(bg=BG)


# -------------------- USER DATA --------------------

user_data = {
    "language": "English",
    "crop": "",
    "problem_options": [],
    "description": "",
    "soil": "",
    "duration": "",
    "spread": "",
    "affected_area": "",
    "photo": ""
}


# -------------------- SCREEN MANAGEMENT --------------------

def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()


def make_title(title, subtitle=""):
    tk.Label(
        window,
        text=title,
        font=("Arial", 26, "bold"),
        bg=BG,
        fg=DARK_GREEN
    ).pack(pady=(25, 5))

    if subtitle:
        tk.Label(
            window,
            text=subtitle,
            font=("Arial", 13),
            bg=BG,
            fg=TEXT
        ).pack(pady=(0, 20))


def nav_buttons(back_function, back_text, home_text):
    frame = tk.Frame(window, bg=BG)
    frame.pack(pady=20)

    tk.Button(
        frame,
        text=back_text,
        font=("Arial", 11),
        width=12,
        command=back_function
    ).pack(side="left", padx=10)

    tk.Button(
        frame,
        text=home_text,
        font=("Arial", 11),
        width=12,
        command=home_screen
    ).pack(side="left", padx=10)


# =========================================================
# HOME / LANGUAGE SCREEN
# =========================================================

def home_screen():
    clear_screen()

    tk.Label(
        window,
        text="🌾 KISAN SAHAYAK",
        font=("Arial", 30, "bold"),
        bg=BG,
        fg=DARK_GREEN
    ).pack(pady=(70, 10))

    tk.Label(
        window,
        text="AI Agricultural Assistance System",
        font=("Arial", 16),
        bg=BG,
        fg=TEXT
    ).pack(pady=5)

    tk.Label(
        window,
        text="Choose your language / अपनी भाषा चुनें",
        font=("Arial", 18, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(pady=45)

    tk.Button(
        window,
        text="🇬🇧  English",
        font=("Arial", 15, "bold"),
        width=24,
        height=2,
        bg=BUTTON,
        fg=WHITE,
        command=lambda: start_language("English")
    ).pack(pady=10)

    tk.Button(
        window,
        text="🇮🇳  हिंदी",
        font=("Arial", 15, "bold"),
        width=24,
        height=2,
        bg=BUTTON,
        fg=WHITE,
        command=lambda: start_language("Hindi")
    ).pack(pady=10)

    tk.Label(
        window,
        text="Crop assistance • Voice • Photo • Field assistance request",
        font=("Arial", 10),
        bg=BG,
        fg="#607D8B"
    ).pack(pady=40)


def start_language(language):
    user_data["language"] = language
    crop_screen()


# =========================================================
# CROP SCREEN
# =========================================================

def crop_screen():
    clear_screen()

    lang = user_data["language"]

    if lang == "English":
        title = "Which crop are you growing?"
        crops = ["Wheat", "Rice", "Cotton", "Mustard", "Tomato"]
        back = "← Back"
        home = "⌂ Home"
    else:
        title = "आप कौन-सी फसल उगा रहे हैं?"
        crops = ["गेहूँ", "धान", "कपास", "सरसों", "टमाटर"]
        back = "← वापस"
        home = "⌂ होम"

    make_title(
        "🌾 KISAN SAHAYAK" if lang == "English"
        else "🌾 किसान सहायक",
        title
    )

    for crop in crops:
        tk.Button(
            window,
            text=crop,
            font=("Arial", 14),
            width=25,
            height=1,
            bg=WHITE,
            fg=TEXT,
            command=lambda c=crop: select_crop(c)
        ).pack(pady=6)

    nav_buttons(home_screen, back, home)


def select_crop(crop):
    user_data["crop"] = crop
    problem_screen()


# =========================================================
# PROBLEM SCREEN
# =========================================================

def problem_screen():
    clear_screen()

    lang = user_data["language"]

    if lang == "English":
        title = "What are you observing in your crop?"
        options = [
            "Yellow leaves",
            "Wilting",
            "Spots on leaves",
            "Leaves curling",
            "Insects visible",
            "Slow growth",
            "Plant/stem becoming weak"
        ]
        description_label = "Describe the problem in your own words:"
        placeholder = "Example: Leaves are turning yellow from the bottom..."
        continue_text = "Continue →"
        back = "← Back"
        home = "⌂ Home"
    else:
        title = "आप अपनी फसल में क्या देख रहे हैं?"
        options = [
            "पत्तियाँ पीली होना",
            "पौधे का मुरझाना",
            "पत्तियों पर धब्बे",
            "पत्तियाँ मुड़ना",
            "कीड़े दिखाई देना",
            "धीमी वृद्धि",
            "पौधे/तने का कमजोर होना"
        ]
        description_label = "अपनी समस्या अपने शब्दों में लिखें:"
        placeholder = "उदाहरण: नीचे से पत्तियाँ पीली हो रही हैं..."
        continue_text = "आगे बढ़ें →"
        back = "← वापस"
        home = "⌂ होम"

    make_title(
        "Describe the problem" if lang == "English"
        else "समस्या बताएं",
        title
    )

    tk.Label(
        window,
        text=f"Crop: {user_data['crop']}",
        font=("Arial", 13, "bold"),
        bg=BG,
        fg=DARK_GREEN
    ).pack(pady=5)

    # Scrollable-ish options area
    options_frame = tk.Frame(window, bg=BG)
    options_frame.pack(pady=10)

    selected = {}

    for option in options:
        var = tk.BooleanVar()

        tk.Checkbutton(
            options_frame,
            text=option,
            variable=var,
            font=("Arial", 12),
            bg=BG,
            anchor="w",
            width=32
        ).pack(anchor="w", pady=2)

        selected[option] = var

    tk.Label(
        window,
        text=description_label,
        font=("Arial", 12, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(pady=(15, 5))

    text_box = tk.Text(
        window,
        height=4,
        width=65,
        font=("Arial", 11)
    )
    text_box.pack()

    def save_problem():
        user_data["problem_options"] = [
            option for option, var in selected.items()
            if var.get()
        ]

        user_data["description"] = text_box.get(
            "1.0", tk.END
        ).strip()

        if not user_data["problem_options"] and not user_data["description"]:
            if lang == "English":
                messagebox.showwarning(
                    "Information needed",
                    "Please select an observation or describe the problem."
                )
            else:
                messagebox.showwarning(
                    "जानकारी आवश्यक",
                    "कृपया कोई समस्या चुनें या अपनी समस्या लिखें।"
                )
            return

        details_screen()

    # Voice button
    if VOICE_AVAILABLE:
        tk.Button(
            window,
            text="🎤 Speak / बोलकर बताएं",
            font=("Arial", 11, "bold"),
            command=lambda: voice_input(text_box)
        ).pack(pady=8)
    else:
        tk.Label(
            window,
            text="Voice input requires the speech-recognition package.",
            font=("Arial", 9),
            bg=BG,
            fg="#777777"
        ).pack(pady=5)

    tk.Button(
        window,
        text=continue_text,
        font=("Arial", 13, "bold"),
        bg=BUTTON,
        fg=WHITE,
        width=20,
        command=save_problem
    ).pack(pady=10)

    nav_buttons(problem_back, back, home)


def problem_back():
    crop_screen()


# =========================================================
# VOICE INPUT
# =========================================================

def voice_input(text_box):
    if not VOICE_AVAILABLE:
        return

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            if user_data["language"] == "Hindi":
                messagebox.showinfo(
                    "Voice Input",
                    "अब अपनी समस्या हिंदी में बोलें।"
                )
                audio = recognizer.listen(source, timeout=7)
                text = recognizer.recognize_google(
                    audio,
                    language="hi-IN"
                )
            else:
                messagebox.showinfo(
                    "Voice Input",
                    "Please describe your crop problem."
                )
                audio = recognizer.listen(source, timeout=7)
                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                )

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

    except Exception as error:
        messagebox.showwarning(
            "Voice input",
            "Voice could not be understood. Please try again or type the problem."
        )


# =========================================================
# DETAILS SCREEN
# =========================================================

def details_screen():
    clear_screen()

    lang = user_data["language"]

    if lang == "English":
        title = "Tell us a little more"
        soil_q = "How does the soil feel?"
        soil_options = [
            "Very dry",
            "Slightly dry",
            "Moist/normal",
            "Very wet",
            "I don't know"
        ]

        duration_q = "When did you first notice the problem?"
        duration_options = [
            "Today",
            "2–3 days ago",
            "Within the last week",
            "More than a week ago",
            "I don't know"
        ]

        spread_q = "Is the problem spreading?"
        spread_options = [
            "No / stopped",
            "Slowly",
            "Quickly",
            "I am not sure"
        ]

        area_q = "Approximately how much of the field is affected?"
        area_options = [
            "A few plants",
            "Less than 10%",
            "10–25%",
            "25–50%",
            "More than 50%",
            "Almost the entire field"
        ]

        continue_text = "Assess problem →"
        back = "← Back"
        home = "⌂ Home"

    else:
        title = "थोड़ी और जानकारी दें"
        soil_q = "मिट्टी हाथ से कैसी महसूस होती है?"
        soil_options = [
            "बहुत सूखी",
            "थोड़ी सूखी",
            "नम/सामान्य",
            "बहुत गीली",
            "पता नहीं"
        ]

        duration_q = "समस्या पहली बार कब दिखाई दी?"
        duration_options = [
            "आज",
            "2–3 दिन पहले",
            "पिछले एक सप्ताह में",
            "एक सप्ताह से अधिक पहले",
            "पता नहीं"
        ]

        spread_q = "क्या समस्या फैल रही है?"
        spread_options = [
            "नहीं / रुक गई है",
            "धीरे-धीरे",
            "तेजी से",
            "पता नहीं"
        ]

        area_q = "लगभग खेत के कितने हिस्से में समस्या है?"
        area_options = [
            "कुछ पौधे",
            "10% से कम",
            "10–25%",
            "25–50%",
            "50% से अधिक",
            "लगभग पूरा खेत"
        ]

        continue_text = "समस्या का आकलन →"
        back = "← वापस"
        home = "⌂ होम"

    make_title(
        title,
        f"{'Crop' if lang == 'English' else 'फसल'}: {user_data['crop']}"
    )

    # Soil
    tk.Label(
        window,
        text=soil_q,
        font=("Arial", 13, "bold"),
        bg=BG
    ).pack(pady=(5, 5))

    soil_var = tk.StringVar()
    soil_menu = tk.OptionMenu(
        window,
        soil_var,
        *soil_options
    )
    soil_menu.config(width=30, font=("Arial", 11))
    soil_menu.pack(pady=3)

    # Duration
    tk.Label(
        window,
        text=duration_q,
        font=("Arial", 13, "bold"),
        bg=BG
    ).pack(pady=(15, 5))

    duration_var = tk.StringVar()
    duration_menu = tk.OptionMenu(
        window,
        duration_var,
        *duration_options
    )
    duration_menu.config(width=30, font=("Arial", 11))
    duration_menu.pack(pady=3)

    # Spread
    tk.Label(
        window,
        text=spread_q,
        font=("Arial", 13, "bold"),
        bg=BG
    ).pack(pady=(15, 5))

    spread_var = tk.StringVar()
    spread_menu = tk.OptionMenu(
        window,
        spread_var,
        *spread_options
    )
    spread_menu.config(width=30, font=("Arial", 11))
    spread_menu.pack(pady=3)

    # Affected area
    tk.Label(
        window,
        text=area_q,
        font=("Arial", 13, "bold"),
        bg=BG
    ).pack(pady=(15, 5))

    area_var = tk.StringVar()
    area_menu = tk.OptionMenu(
        window,
        area_var,
        *area_options
    )
    area_menu.config(width=30, font=("Arial", 11))
    area_menu.pack(pady=3)

    def continue_assessment():
        user_data["soil"] = soil_var.get()
        user_data["duration"] = duration_var.get()
        user_data["spread"] = spread_var.get()
        user_data["affected_area"] = area_var.get()

        assessment_screen()

    tk.Button(
        window,
        text=continue_text,
        font=("Arial", 13, "bold"),
        bg=BUTTON,
        fg=WHITE,
        width=25,
        command=continue_assessment
    ).pack(pady=18)

    nav_buttons(problem_screen, back, home)


# =========================================================
# ASSESSMENT ENGINE
# =========================================================

def calculate_assessment():

    problem_text = " ".join(
        user_data["problem_options"]
    ).lower()

    description = user_data["description"].lower()

    combined = problem_text + " " + description

    possible_issue = "General crop health issue"
    action = (
        "Observe the affected crop carefully and follow "
        "recommended crop-management practices for your area."
    )
    avoid = (
        "Do not apply unknown chemicals or excessive "
        "fertilizer without identifying the problem."
    )

    # Basic rule-based assessment
    if (
        "wilting" in combined
        or "मुरझाना" in combined
    ):
        possible_issue = "Possible water-related stress"
        action = (
            "Check soil moisture and irrigation conditions. "
            "Observe whether the affected area is increasing."
        )

    elif (
        "yellow" in combined
        or "पीली" in combined
    ):
        possible_issue = "Possible nutrient or growing-condition stress"
        action = (
            "Check soil moisture and overall crop condition. "
            "Follow locally recommended nutrient-management practices."
        )

    elif (
        "spot" in combined
        or "धब्ब" in combined
    ):
        possible_issue = "Possible plant health or fungal-related issue"
        action = (
            "Inspect affected leaves carefully. "
            "If the problem spreads, seek advice from a local "
            "agriculture expert before applying any treatment."
        )

    elif (
        "insect" in combined
        or "कीड़े" in combined
    ):
        possible_issue = "Possible pest-related problem"
        action = (
            "Inspect the affected plants and check whether insects "
            "are spreading. Seek local agricultural guidance before "
            "using any pesticide."
        )

    # Severity assessment
    severity_score = 0

    if user_data["spread"] in ["Quickly", "तेजी से"]:
        severity_score += 3
    elif user_data["spread"] in ["Slowly", "धीरे-धीरे"]:
        severity_score += 1

    if user_data["affected_area"] in [
        "More than 50%",
        "Almost the entire field",
        "50% से अधिक",
        "लगभग पूरा खेत"
    ]:
        severity_score += 3

    elif user_data["affected_area"] in [
        "25–50%",
        "25–50%"
    ]:
        severity_score += 2

    elif user_data["affected_area"] in [
        "10–25%",
        "10–25%"
    ]:
        severity_score += 1

    if user_data["duration"] in [
        "More than a week ago",
        "एक सप्ताह से अधिक पहले"
    ]:
        severity_score += 1

    if severity_score >= 5:
        severity = "High"
    elif severity_score >= 2:
        severity = "Moderate"
    else:
        severity = "Low"

    return possible_issue, action, avoid, severity


# =========================================================
# ASSESSMENT SCREEN
# =========================================================

def assessment_screen():
    clear_screen()

    lang = user_data["language"]

    issue, action, avoid, severity = calculate_assessment()

    if lang == "English":

        title = "🤖 Preliminary Assessment"

        if severity == "High":
            severity_text = "HIGH — Further assistance recommended"
        elif severity == "Moderate":
            severity_text = "MODERATE — Continue monitoring"
        else:
            severity_text = "LOW — Continue observing"

        result = (
            f"Possible issue:\n{issue}\n\n"
            f"Severity:\n{severity_text}\n\n"
            f"What you can do:\n{action}\n\n"
            f"What you should avoid:\n{avoid}\n\n"
            "Important:\n"
            "This is a preliminary educational assessment, "
            "not a confirmed agricultural diagnosis."
        )

        assistance_text = "🚜 Request Field Assistance"
        photo_text = "📷 Add Crop Photo"
        back_text = "← Back"
        home_text = "⌂ Home"

    else:

        title = "🤖 प्रारंभिक आकलन"

        if severity == "High":
            severity_text = "HIGH — आगे कृषि सहायता लेना उचित है"
        elif severity == "Moderate":
            severity_text = "MODERATE — फसल की निगरानी जारी रखें"
        else:
            severity_text = "LOW — फसल पर नज़र रखें"

        result = (
            f"संभावित समस्या:\n{issue}\n\n"
            f"गंभीरता:\n{severity_text}\n\n"
            f"आप क्या कर सकते हैं:\n{action}\n\n"
            f"क्या नहीं करना चाहिए:\n{avoid}\n\n"
            "महत्वपूर्ण:\n"
            "यह केवल प्रारंभिक शैक्षिक आकलन है। "
            "यह कृषि विशेषज्ञ द्वारा पुष्टि किया गया निदान नहीं है।"
        )

        assistance_text = "🚜 खेत सहायता का अनुरोध"
        photo_text = "📷 फसल की फोटो जोड़ें"
        back_text = "← वापस"
        home_text = "⌂ होम"

    make_title(title)

    result_box = tk.Text(
        window,
        height=15,
        width=78,
        font=("Arial", 11),
        wrap="word"
    )
    result_box.pack(pady=10)

    result_box.insert(tk.END, result)
    result_box.config(state="disabled")

    # Photo selection
    tk.Button(
        window,
        text=photo_text,
        font=("Arial", 11),
        command=choose_photo
    ).pack(pady=5)

    # Field assistance
    tk.Button(
        window,
        text=assistance_text,
        font=("Arial", 12, "bold"),
        bg=ORANGE,
        fg=WHITE,
        width=30,
        command=field_assistance_screen
    ).pack(pady=10)

    nav_buttons(details_screen, back_text, home_text)


# =========================================================
# PHOTO SELECTION
# =========================================================

def choose_photo():
    file_path = filedialog.askopenfilename(
        title="Select crop photo",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        user_data["photo"] = file_path

        messagebox.showinfo(
            "Photo Added",
            "Crop photo has been added to this assessment."
        )


# =========================================================
# FIELD ASSISTANCE REQUEST
# =========================================================

def field_assistance_screen():
    clear_screen()

    lang = user_data["language"]

    if lang == "English":
        title = "🚜 Request Field Assistance"
        labels = [
            "Your Name",
            "Mobile Number",
            "Village",
            "District",
            "Field / Khasra Number (optional)",
            "Additional information"
        ]
        submit_text = "Submit Request"
        back_text = "← Back"
        home_text = "⌂ Home"
    else:
        title = "🚜 खेत सहायता का अनुरोध"
        labels = [
            "आपका नाम",
            "मोबाइल नंबर",
            "गाँव",
            "जिला",
            "खेत / खसरा नंबर (वैकल्पिक)",
            "अतिरिक्त जानकारी"
        ]
        submit_text = "अनुरोध भेजें"
        back_text = "← वापस"
        home_text = "⌂ होम"

    make_title(title)

    entries = []

    for i, label in enumerate(labels):

        tk.Label(
            window,
            text=label,
            font=("Arial", 11, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(pady=(5, 2))

        if i == len(labels) - 1:
            entry = tk.Text(
                window,
                height=3,
                width=60,
                font=("Arial", 10)
            )
        else:
            entry = tk.Entry(
                window,
                width=55,
                font=("Arial", 11)
            )

        entry.pack(pady=2)
        entries.append(entry)

    def submit_request():

        values = []

        for i, entry in enumerate(entries):

            if isinstance(entry, tk.Text):
                value = entry.get("1.0", tk.END).strip()
            else:
                value = entry.get().strip()

            values.append(value)

        # Basic required information
        if not values[0] or not values[1] or not values[2]:
            if lang == "English":
                messagebox.showwarning(
                    "Information needed",
                    "Please enter your name, mobile number and village."
                )
            else:
                messagebox.showwarning(
                    "जानकारी आवश्यक",
                    "कृपया नाम, मोबाइल नंबर और गाँव भरें।"
                )
            return

        # Save request locally
        try:
            with open(
                "field_assistance_requests.csv",
                "a",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    user_data["crop"],
                    user_data["affected_area"],
                    values[5]
                ])

            if lang == "English":
                messagebox.showinfo(
                    "Request Submitted",
                    "Your field assistance request has been recorded."
                )
            else:
                messagebox.showinfo(
                    "अनुरोध दर्ज",
                    "आपका खेत सहायता अनुरोध दर्ज कर लिया गया है।"
                )

            home_screen()

        except Exception as error:
            messagebox.showerror(
                "Error",
                "Could not save the request."
            )

    tk.Button(
        window,
        text=submit_text,
        font=("Arial", 13, "bold"),
        bg=ORANGE,
        fg=WHITE,
        width=25,
        command=submit_request
    ).pack(pady=15)

    nav_buttons(
        assessment_screen,
        back_text,
        home_text
    )


# =========================================================
# START APPLICATION
# =========================================================

home_screen()

window.mainloop()