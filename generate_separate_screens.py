import os
from PIL import Image, ImageDraw

os.makedirs("generated_outputs", exist_ok=True)

def create_phone(title="Android App", w=320, h=480):
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Phone Body
    draw.rounded_rectangle([0, 0, w-1, h-1], radius=22, fill="#1E293B", outline="#0F172A", width=3)
    # Screen
    draw.rounded_rectangle([8, 8, w-9, h-9], radius=15, fill="#F8FAFC")
    # Top Status Bar
    draw.rounded_rectangle([8, 8, w-9, 36], radius=15, fill="#0284C7")
    draw.rectangle([8, 22, w-9, 36], fill="#0284C7")
    # Camera pill
    draw.rounded_rectangle([w//2 - 28, 12, w//2 + 28, 22], radius=5, fill="#0F172A")
    # App Bar
    draw.rectangle([8, 36, w-9, 72], fill="#0369A1")
    draw.text((20, 46), title, fill="#FFFFFF")
    return img, draw

# ================= 1. LIFECYCLE (2 screens: Start/Resume & Pause/Stop) =================
# 1A: Active Screen
img_lc1, d_lc1 = create_phone("Activity Lifecycle")
d_lc1.text((50, 130), "Activity Lifecycle Demo", fill="#334155")
d_lc1.rounded_rectangle([35, 180, 285, 280], radius=8, fill="#0F172A", outline="#38BDF8")
d_lc1.text((45, 195), "Logcat Events:", fill="#38BDF8")
d_lc1.text((45, 220), "D: onCreate()", fill="#4ADE80")
d_lc1.text((45, 240), "D: onStart()", fill="#4ADE80")
d_lc1.text((45, 260), "D: onResume()", fill="#38BDF8")
# Toast
d_lc1.rounded_rectangle([50, 360, 270, 405], radius=18, fill="#1E293B")
d_lc1.text((105, 375), "onResume()", fill="#FFFFFF")
img_lc1.save("generated_outputs/lifecycle_screen1.png")

# 1B: Paused/Destroyed Screen (Home Pressed)
img_lc2, d_lc2 = create_phone("Lifecycle - Background")
d_lc2.text((40, 110), "Home Button Pressed (Background)", fill="#64748B")
d_lc2.rounded_rectangle([35, 150, 285, 270], radius=8, fill="#0F172A", outline="#F59E0B")
d_lc2.text((45, 165), "Logcat Events:", fill="#F59E0B")
d_lc2.text((45, 190), "D: onPause()", fill="#FCD34D")
d_lc2.text((45, 210), "D: onStop()", fill="#FCD34D")
d_lc2.text((45, 235), "D: onDestroy() (if closed)", fill="#EF4444")
# Toast
d_lc2.rounded_rectangle([50, 360, 270, 405], radius=18, fill="#1E293B")
d_lc2.text((105, 375), "onStop()", fill="#FCD34D")
img_lc2.save("generated_outputs/lifecycle_screen2.png")


# ================= 2. REG, LOGIN, SHARED (3 SEPARATE SCREENS) =================
# 2A: Registration Screen (MainActivity)
img_reg, d_reg = create_phone("Register Activity")
d_reg.text((95, 95), "Create Account", fill="#0F172A")
d_reg.text((35, 125), "Username:", fill="#475569")
d_reg.rounded_rectangle([35, 145, 285, 185], radius=6, fill="#FFFFFF", outline="#94A3B8")
d_reg.text((45, 157), "student_alex", fill="#0F172A")

d_reg.text((35, 195), "Password:", fill="#475569")
d_reg.rounded_rectangle([35, 215, 285, 255], radius=6, fill="#FFFFFF", outline="#94A3B8")
d_reg.text((45, 227), "•••••••• (pass123)", fill="#0F172A")

d_reg.rounded_rectangle([35, 280, 285, 320], radius=6, fill="#0284C7")
d_reg.text((115, 292), "REGISTER", fill="#FFFFFF")

d_reg.rounded_rectangle([45, 370, 275, 415], radius=18, fill="#1E293B")
d_reg.text((65, 385), "Registration Successful", fill="#4ADE80")
img_reg.save("generated_outputs/reg_screen.png")

# 2B: Login Screen (LoginActivity)
img_log, d_log = create_phone("Login Activity")
d_log.text((115, 95), "User Login", fill="#0F172A")
d_log.text((35, 125), "Enter Username:", fill="#475569")
d_log.rounded_rectangle([35, 145, 285, 185], radius=6, fill="#FFFFFF", outline="#94A3B8")
d_log.text((45, 157), "student_alex", fill="#0F172A")

d_log.text((35, 195), "Enter Password:", fill="#475569")
d_log.rounded_rectangle([35, 215, 285, 255], radius=6, fill="#FFFFFF", outline="#94A3B8")
d_log.text((45, 227), "••••••••", fill="#0F172A")

d_log.rounded_rectangle([35, 280, 285, 320], radius=6, fill="#10B981")
d_log.text((130, 292), "LOGIN", fill="#FFFFFF")

d_log.rounded_rectangle([45, 370, 275, 415], radius=18, fill="#1E293B")
d_log.text((95, 385), "Login Successful!", fill="#38BDF8")
img_log.save("generated_outputs/login_screen.png")

# 2C: SharedPreferences Inspection Screen
img_sp, d_sp = create_phone("SharedPreferences Data")
d_sp.text((50, 95), "Local Storage: 'MyPrefs.xml'", fill="#0F172A")
d_sp.rounded_rectangle([25, 130, 295, 290], radius=10, fill="#FEF3C7", outline="#F59E0B", width=2)
d_sp.text((40, 145), "MODE_PRIVATE Storage State:", fill="#92400E")
d_sp.line([(35, 170), (285, 170)], fill="#FCD34D", width=1)
d_sp.text((40, 185), "Key: KEY_USER", fill="#B45309")
d_sp.text((40, 205), "Value: \"student_alex\"", fill="#1E293B")
d_sp.text((40, 235), "Key: KEY_PASS", fill="#B45309")
d_sp.text((40, 255), "Value: \"pass123\"", fill="#1E293B")

d_sp.rounded_rectangle([30, 320, 290, 420], radius=8, fill="#EFF6FF", outline="#93C5FD")
d_sp.text((40, 335), "Verification Logic:", fill="#1E3A8A")
d_sp.text((40, 360), "enteredUser.equals(savedUser) &", fill="#2563EB")
d_sp.text((40, 380), "enteredPass.equals(savedPass)", fill="#2563EB")
d_sp.text((40, 400), "&rarr; MATCH FOUND!", fill="#16A34A")
img_sp.save("generated_outputs/shared_screen.png")


# ================= 3. TOGGLE IMAGE (State 1: image1 & State 2: image2) =================
# 3A: State 1 (image1)
img_tg1, d_tg1 = create_phone("Toggle Image - State 1")
d_tg1.rounded_rectangle([45, 95, 275, 275], radius=12, fill="#E0F2FE", outline="#0284C7", width=2)
# Sun & Hill
d_tg1.ellipse([180, 115, 230, 165], fill="#F59E0B")
d_tg1.polygon([(65, 270), (140, 160), (210, 270)], fill="#10B981")
d_tg1.polygon([(145, 270), (205, 190), (265, 270)], fill="#059669")
d_tg1.text((85, 285), "Displaying: image1 (Day)", fill="#0369A1")

d_tg1.rounded_rectangle([60, 330, 260, 375], radius=8, fill="#6366F1")
d_tg1.text((105, 345), "TOGGLE IMAGE", fill="#FFFFFF")
d_tg1.text((70, 410), "Status: isFirstImage = true", fill="#64748B")
img_tg1.save("generated_outputs/toggle_screen1.png")

# 3B: State 2 (image2)
img_tg2, d_tg2 = create_phone("Toggle Image - State 2")
d_tg2.rounded_rectangle([45, 95, 275, 275], radius=12, fill="#0F172A", outline="#38BDF8", width=2)
# Moon & Stars
d_tg2.ellipse([180, 115, 230, 165], fill="#F8FAFC")
d_tg2.ellipse([170, 110, 220, 160], fill="#0F172A") # crescent cut
d_tg2.text((75, 130), "★", fill="#FDE047")
d_tg2.text((120, 170), "★", fill="#FDE047")
d_tg2.text((85, 285), "Displaying: image2 (Night)", fill="#38BDF8")

d_tg2.rounded_rectangle([60, 330, 260, 375], radius=8, fill="#6366F1")
d_tg2.text((105, 345), "TOGGLE IMAGE", fill="#FFFFFF")
d_tg2.text((70, 410), "Status: isFirstImage = false", fill="#64748B")
img_tg2.save("generated_outputs/toggle_screen2.png")


# ================= 4. SPINNER (Closed vs Opened Dropdown) =================
# 4A: Closed State
img_sp1, d_sp1 = create_phone("Spinner (Closed)")
d_sp1.text((35, 110), "Select Course:", fill="#0F172A")
d_sp1.rounded_rectangle([35, 140, 285, 185], radius=6, fill="#FFFFFF", outline="#0284C7", width=2)
d_sp1.text((50, 154), "BCA - Computer Apps", fill="#0F172A")
d_sp1.polygon([(260, 158), (274, 158), (267, 168)], fill="#0284C7")
d_sp1.text((35, 230), "Tap spinner to open list...", fill="#64748B")
img_sp1.save("generated_outputs/spinner_screen1.png")

# 4B: Opened Dropdown Popup
img_sp2, d_sp2 = create_phone("Spinner (Opened)")
d_sp2.text((35, 100), "Select Course:", fill="#0F172A")
d_sp2.rounded_rectangle([35, 125, 285, 165], radius=6, fill="#F1F5F9", outline="#94A3B8")
d_sp2.text((50, 137), "Select...", fill="#64748B")

# Popup dropdown
d_sp2.rounded_rectangle([35, 170, 285, 350], radius=8, fill="#FFFFFF", outline="#0284C7", width=2)
courses = ["MCA - Masters in CS  ✔", "BCA - Bachelor of Apps", "B.Tech - Comp Science", "M.Tech - Data Science"]
y = 185
for c in courses:
    if "✔" in c:
        d_sp2.rectangle([37, y-7, 283, y+27], fill="#E0F2FE")
        d_sp2.text((45, y), c, fill="#0369A1")
    else:
        d_sp2.text((45, y), c, fill="#334155")
    d_sp2.line([(37, y+28), (283, y+28)], fill="#E2E8F0", width=1)
    y += 40

d_sp2.rounded_rectangle([45, 380, 275, 425], radius=18, fill="#1E293B")
d_sp2.text((65, 395), "Selected: MCA - Masters in CS", fill="#38BDF8")
img_sp2.save("generated_outputs/spinner_screen2.png")


# ================= 5. ARRAY ADAPTER LISTVIEW (Default & Clicked) =================
# 5A: ListView normal
img_lv1, d_lv1 = create_phone("ListView Normal")
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple"]
y = 90
for f in fruits:
    d_lv1.rectangle([10, y, 310, y+42], fill="#FFFFFF")
    d_lv1.text((30, y+14), f, fill="#1E293B")
    d_lv1.line([(10, y+42), (310, y+42)], fill="#E2E8F0", width=1)
    y += 43
d_lv1.text((35, 380), "Click any item to select...", fill="#64748B")
img_lv1.save("generated_outputs/listview_screen1.png")

# 5B: ListView item clicked with Toast
img_lv2, d_lv2 = create_phone("ListView Clicked")
y = 90
for f in fruits:
    if f == "Orange":
        d_lv2.rectangle([10, y, 310, y+42], fill="#BAE6FD")
        d_lv2.text((30, y+14), f + " (Selected)", fill="#0369A1")
    else:
        d_lv2.rectangle([10, y, 310, y+42], fill="#FFFFFF")
        d_lv2.text((30, y+14), f, fill="#1E293B")
    d_lv2.line([(10, y+42), (310, y+42)], fill="#E2E8F0", width=1)
    y += 43

d_lv2.rounded_rectangle([45, 380, 275, 425], radius=18, fill="#1E293B")
d_lv2.text((80, 395), "Selected: Orange (Pos: 2)", fill="#38BDF8")
img_lv2.save("generated_outputs/listview_screen2.png")


# ================= 6. EXPLICIT INTENT (Sender & Receiver Separate) =================
# 6A: Sender Activity (MainActivity)
img_ex1, d_ex1 = create_phone("Explicit Intent - Sender")
d_ex1.text((50, 100), "MainActivity (Sender)", fill="#0F172A")
d_ex1.text((35, 135), "Enter Your Name:", fill="#475569")
d_ex1.rounded_rectangle([35, 160, 285, 200], radius=6, fill="#FFFFFF", outline="#94A3B8")
d_ex1.text((45, 172), "Rinshad", fill="#0F172A")

d_ex1.rounded_rectangle([35, 230, 285, 275], radius=6, fill="#0284C7")
d_ex1.text((70, 245), "GO TO SECOND ACTIVITY", fill="#FFFFFF")

d_ex1.rounded_rectangle([30, 320, 290, 420], radius=8, fill="#EFF6FF", outline="#93C5FD")
d_ex1.text((40, 335), "Intent Code Executing:", fill="#1E3A8A")
d_ex1.text((40, 360), "Intent i = new Intent(", fill="#2563EB")
d_ex1.text((40, 380), "  MainActivity.this, Second.class);", fill="#2563EB")
d_ex1.text((40, 400), "i.putExtra(\"USER_NAME\", \"Rinshad\");", fill="#0369A1")
img_ex1.save("generated_outputs/intent_sender.png")

# 6B: Receiver Activity (SecondActivity)
img_ex2, d_ex2 = create_phone("Explicit Intent - Receiver")
d_ex2.text((45, 100), "SecondActivity (Receiver)", fill="#059669")
d_ex2.rounded_rectangle([30, 140, 290, 220], radius=10, fill="#ECFDF5", outline="#10B981", width=2)
d_ex2.text((65, 165), "Welcome, Rinshad!", fill="#065F46")
d_ex2.text((50, 190), "(Data received from Intent)", fill="#047857")

d_ex2.rounded_rectangle([30, 280, 290, 400], radius=8, fill="#FEF3C7", outline="#F59E0B")
d_ex2.text((40, 300), "Extraction Code:", fill="#92400E")
d_ex2.text((40, 330), "Intent i = getIntent();", fill="#B45309")
d_ex2.text((40, 355), "String n = i.getStringExtra(", fill="#B45309")
d_ex2.text((40, 375), "    \"USER_NAME\");", fill="#B45309")
img_ex2.save("generated_outputs/intent_receiver.png")

print("All detailed separate output screens generated successfully!")

