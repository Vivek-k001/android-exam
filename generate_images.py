import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("generated_outputs", exist_ok=True)

# Helper to draw a modern mobile phone frame
def create_phone_frame(width=340, height=520, title="Android App"):
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer phone body
    draw.rounded_rectangle([0, 0, width-1, height-1], radius=24, fill="#1E293B", outline="#0F172A", width=3)
    
    # Screen area
    draw.rounded_rectangle([10, 10, width-11, height-11], radius=16, fill="#F8FAFC")
    
    # Status bar
    draw.rounded_rectangle([10, 10, width-11, 40], radius=16, fill="#0284C7")
    draw.rectangle([10, 25, width-11, 40], fill="#0284C7") # flatten bottom of status bar
    
    # Notch/camera pill
    draw.rounded_rectangle([width//2 - 35, 14, width//2 + 35, 26], radius=6, fill="#0F172A")
    
    # App title bar
    draw.rectangle([10, 40, width-11, 80], fill="#0369A1")
    draw.text((25, 52), title, fill="#FFFFFF")
    
    return img, draw

# 1. Lifecycle Output (Showing Toast & Logcat style)
def gen_lifecycle():
    img, draw = create_phone_frame(title="Activity Lifecycle")
    # Screen content
    draw.text((60, 150), "Activity Lifecycle Demo", fill="#334155")
    
    # Toast notification simulation
    draw.rounded_rectangle([50, 360, 290, 410], radius=20, fill="#334155")
    draw.text((105, 376), "onResume()", fill="#FFFFFF")
    
    # Logcat box simulation below
    draw.rounded_rectangle([20, 210, 320, 320], radius=8, fill="#0F172A", outline="#38BDF8", width=1)
    draw.text((28, 220), "[Logcat Output]", fill="#38BDF8")
    draw.text((28, 240), "D/ActivityLifecycle: onCreate()", fill="#4ADE80")
    draw.text((28, 260), "D/ActivityLifecycle: onStart()", fill="#4ADE80")
    draw.text((28, 280), "D/ActivityLifecycle: onResume()", fill="#38BDF8")
    
    img.save("generated_outputs/out_lifecycle.png")

# 2. Login & SharedPreferences Output
def gen_login():
    img, draw = create_phone_frame(title="Login & SharedPrefs")
    
    # Welcome / Title
    draw.text((120, 110), "User Login", fill="#0F172A")
    
    # Inputs
    draw.rounded_rectangle([35, 145, 305, 185], radius=6, fill="#FFFFFF", outline="#94A3B8")
    draw.text((45, 157), "username: alex_99", fill="#1E293B")
    
    draw.rounded_rectangle([35, 195, 305, 235], radius=6, fill="#FFFFFF", outline="#94A3B8")
    draw.text((45, 207), "password: ••••••••", fill="#1E293B")
    
    # Button
    draw.rounded_rectangle([35, 255, 305, 295], radius=6, fill="#0284C7")
    draw.text((145, 267), "LOGIN", fill="#FFFFFF")
    
    # Toast notification
    draw.rounded_rectangle([55, 340, 285, 385], radius=18, fill="#1E293B")
    draw.text((95, 354), "Login Successful!", fill="#22C55E")
    
    # SharedPreferences note
    draw.rounded_rectangle([30, 410, 310, 480], radius=8, fill="#FEF3C7", outline="#F59E0B")
    draw.text((40, 420), "Saved in SharedPreferences:", fill="#92400E")
    draw.text((40, 440), "KEY_USER = alex_99", fill="#B45309")
    draw.text((40, 455), "KEY_PASS = pass123", fill="#B45309")
    
    img.save("generated_outputs/out_login.png")

# 3. Toggle Image Output
def gen_toggle():
    img, draw = create_phone_frame(title="Image Toggle")
    
    # Image frame (State A & State B demonstration)
    draw.rounded_rectangle([60, 110, 280, 280], radius=12, fill="#E0F2FE", outline="#0284C7", width=2)
    # Draw simple sun/mountain art
    draw.ellipse([190, 130, 240, 180], fill="#F59E0B") # Sun
    draw.polygon([(80, 275), (150, 180), (220, 275)], fill="#10B981") # Mountain
    draw.polygon([(160, 275), (220, 210), (270, 275)], fill="#059669")
    
    draw.text((105, 290), "Current: image1.png", fill="#0369A1")
    
    # Toggle Button
    draw.rounded_rectangle([70, 340, 270, 385], radius=8, fill="#6366F1")
    draw.text((115, 354), "TOGGLE IMAGE", fill="#FFFFFF")
    
    draw.text((45, 420), "Click changes to image2 (Night mode / Star)", fill="#64748B")
    img.save("generated_outputs/out_toggle.png")

# 4. Spinner Output
def gen_spinner():
    img, draw = create_phone_frame(title="Course Spinner")
    
    draw.text((35, 110), "Select Course:", fill="#0F172A")
    
    # Spinner dropdown closed
    draw.rounded_rectangle([35, 135, 305, 175], radius=6, fill="#FFFFFF", outline="#0284C7", width=2)
    draw.text((50, 147), "MCA - Computer Science", fill="#0F172A")
    draw.polygon([(280, 150), (292, 150), (286, 160)], fill="#0284C7")
    
    # Dropdown popup overlay
    draw.rounded_rectangle([35, 185, 305, 335], radius=6, fill="#FFFFFF", outline="#CBD5E1", width=1)
    courses = ["BCA - Bachelor of Apps", "MCA - Computer Science  ✔", "B.Tech - IT", "M.Tech - Data Science"]
    y = 195
    for c in courses:
        if "✔" in c:
            draw.rectangle([36, y-5, 304, y+25], fill="#E0F2FE")
            draw.text((45, y), c, fill="#0369A1")
        else:
            draw.text((45, y), c, fill="#334155")
        y += 35
        
    # Toast notification
    draw.rounded_rectangle([50, 380, 290, 425], radius=18, fill="#1E293B")
    draw.text((80, 395), "Selected: MCA - Computer Science", fill="#38BDF8")
    
    img.save("generated_outputs/out_spinner.png")

# 5. ListView with ArrayAdapter Output
def gen_listview():
    img, draw = create_phone_frame(title="Fruits ListView")
    
    fruits = ["Apple", "Banana", "Orange (Clicked)", "Mango", "Grapes", "Pineapple"]
    y = 100
    for f in fruits:
        if "Clicked" in f:
            draw.rectangle([12, y, 328, y+45], fill="#BAE6FD")
            draw.text((35, y+14), f, fill="#0369A1")
        else:
            draw.rectangle([12, y, 328, y+45], fill="#FFFFFF")
            draw.text((35, y+14), f, fill="#1E293B")
        draw.line([(12, y+45), (328, y+45)], fill="#E2E8F0", width=1)
        y += 46
        
    # Toast on item click
    draw.rounded_rectangle([50, 420, 290, 465], radius=18, fill="#1E293B")
    draw.text((95, 434), "Clicked: Orange", fill="#38BDF8")
    
    img.save("generated_outputs/out_listview.png")

# 6. Explicit Intent Output
def gen_explicit_intent():
    # Double screen graphic (Activity 1 -> Activity 2)
    w, h = 460, 350
    img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Phone 1 (MainActivity)
    draw.rounded_rectangle([10, 10, 210, 340], radius=14, fill="#F8FAFC", outline="#334155", width=2)
    draw.rectangle([10, 10, 210, 45], fill="#0284C7")
    draw.text((25, 20), "MainActivity", fill="#FFFFFF")
    
    draw.text((25, 70), "Enter Name:", fill="#475569")
    draw.rounded_rectangle([25, 95, 195, 130], radius=4, fill="#FFFFFF", outline="#94A3B8")
    draw.text((35, 105), "Rinshad", fill="#0F172A")
    
    draw.rounded_rectangle([25, 150, 195, 185], radius=6, fill="#0284C7")
    draw.text((55, 160), "GO TO SECOND", fill="#FFFFFF")
    
    # Arrow with Intent label
    draw.line([(212, 167), (248, 167)], fill="#E11D48", width=3)
    draw.polygon([(245, 160), (258, 167), (245, 174)], fill="#E11D48")
    draw.text((205, 135), "Intent", fill="#E11D48")
    draw.text((195, 180), "putExtra", fill="#E11D48")
    
    # Phone 2 (SecondActivity)
    draw.rounded_rectangle([250, 10, 450, 340], radius=14, fill="#F8FAFC", outline="#334155", width=2)
    draw.rectangle([250, 10, 450, 45], fill="#059669")
    draw.text((265, 20), "SecondActivity", fill="#FFFFFF")
    
    draw.rounded_rectangle([265, 110, 435, 170], radius=8, fill="#ECFDF5", outline="#10B981")
    draw.text((280, 130), "Welcome, Rinshad!", fill="#065F46")
    draw.text((265, 210), "getIntent().getStringExtra()", fill="#047857")
    
    img.save("generated_outputs/out_explicit_intent.png")

gen_lifecycle()
gen_login()
gen_toggle()
gen_spinner()
gen_listview()
gen_explicit_intent()
print("All preview output images generated successfully!")

