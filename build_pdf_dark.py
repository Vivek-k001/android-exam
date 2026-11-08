import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

pdf_filename = "Android_Exam_Ultimate_Guide_Dark.pdf"

def draw_dark_background(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFillColor(colors.HexColor("#0F172A"))
    canvas_obj.rect(0, 0, doc_obj.pagesize[0], doc_obj.pagesize[1], stroke=0, fill=1)
    canvas_obj.restoreState()

doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=letter,
    leftMargin=28,
    rightMargin=28,
    topMargin=24,
    bottomMargin=24
)

styles = getSampleStyleSheet()

prog_title_style = ParagraphStyle(
    'ProgTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=17,
    textColor=colors.HexColor("#38BDF8"),
    spaceAfter=3
)

body_text = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11.5,
    textColor=colors.HexColor("#CBD5E1")
)

story_text = ParagraphStyle(
    'StoryText',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor("#93C5FD")
)

code_style = ParagraphStyle(
    'CodeStyle',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=6.8,
    leading=8.6,
    textColor=colors.HexColor("#F8FAFC")
)

memory_trick_style = ParagraphStyle(
    'MemTrick',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor("#FDE047")
)

img_label_style = ParagraphStyle(
    'ImgLabel',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9.5,
    alignment=1,
    textColor=colors.HexColor("#7DD3FC")
)

def make_code_box(code_str, width=320):
    escaped = code_str.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace(' ', '&nbsp;')
    p = Paragraph(escaped, code_style)
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1E293B")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#334155")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

def make_story_box(story_html, width=556):
    p = Paragraph(story_html, story_text)
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1E293B")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#2563EB")),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

def make_memory_box(mem_html, width=556):
    p = Paragraph(mem_html, memory_trick_style)
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1E293B")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D97706")),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

def make_two_images_column(img_path1, label1, img_path2, label2, w=105, h=152):
    i1 = Image(img_path1, width=w, height=h)
    p1 = Paragraph(label1, img_label_style)
    i2 = Image(img_path2, width=w, height=h)
    p2 = Paragraph(label2, img_label_style)
    
    t = Table([[i1], [p1], [Spacer(1, 4)], [i2], [p2]], colWidths=[w])
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    return t

story = []

# ================= PAGE 1: ACTIVITY LIFECYCLE =================
story.append(Paragraph("1. Activity Life Cycle (State Callbacks)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Monitoring application states as the user enters, leaves, and resumes the app.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The Life of an Actor on Stage:</b><br/>"
    "• <b>onCreate():</b> Born & dressed backstage (Load layout).<br/>"
    "• <b>onStart():</b> Stage curtains open (Activity visible on screen).<br/>"
    "• <b>onResume():</b> Spotlight on! Performing live (User interacts with UI).<br/>"
    "• <b>onPause():</b> A quick interruption; phone rings (Another activity in front).<br/>"
    "• <b>onStop():</b> Curtains close (App goes to background/home).<br/>"
    "• <b>onRestart():</b> Waiting backstage before coming back.<br/>"
    "• <b>onDestroy():</b> Show is over forever; actor goes home (Freed from memory)."
))
story.append(Spacer(1, 4))

code_p1 = """package com.example.exam;

import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(this, "onCreate()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onStart() {
        super.onStart();
        Toast.makeText(this, "onStart()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onResume() {
        super.onResume();
        Toast.makeText(this, "onResume()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onPause() {
        super.onPause();
        Toast.makeText(this, "onPause()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onStop() {
        super.onStop();
        Toast.makeText(this, "onStop()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onRestart() {
        super.onRestart();
        Toast.makeText(this, "onRestart()", Toast.LENGTH_SHORT).show();
    }
    @Override protected void onDestroy() {
        super.onDestroy();
        Toast.makeText(this, "onDestroy()", Toast.LENGTH_SHORT).show();
    }
}"""

img_col_1 = make_two_images_column(
    "generated_outputs/lifecycle_screen1.png", "State 1: App Active (onResume)",
    "generated_outputs/lifecycle_screen2.png", "State 2: Background (onStop)",
    w=108, h=152
)

table_p1 = Table([[make_code_box(code_p1, width=428), img_col_1]], colWidths=[438, 118])
table_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p1)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Mnemonic:</b> <b>C-S-R-P-S-R-D</b> &rarr; <b>C</b>ome <b>S</b>oon, <b>R</b>un <b>P</b>romptly, <b>S</b>top <b>R</b>unning <b>D</b>ude! Every method must call <code>super.onXxx()</code>."))


# ================= PAGE 2: REGISTRATION & LOGIN WITH SHAREDPREFERENCES =================
story.append(PageBreak())
story.append(Paragraph("2. Registration, Login & SharedPreferences (3 Separate Views)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Multi-screen user registration, persistent key-value storage, and validation login.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The Secret Diary & The Bouncer:</b><br/>"
    "• <b>Registration Screen:</b> Write your secret password with a pen (<code>edit().putString()</code>), snap it shut (<code>apply()</code>).<br/>"
    "• <b>SharedPreferences File:</b> The locked diary stored in phone's private storage (<code>MODE_PRIVATE</code>).<br/>"
    "• <b>Login Screen:</b> The Bouncer opens the diary (<code>getString()</code>), checks your password, and says <i>'Welcome!'</i>."
))
story.append(Spacer(1, 4))

code_p2 = """// 1. REGISTER ACTIVITY (MainActivity.java)
package com.example.exam;

btn.setOnClickListener(v -> {
    SharedPreferences sp = getSharedPreferences("MyPrefs", MODE_PRIVATE);
    sp.edit()
      .putString("U", u.getText().toString())
      .putString("P", p.getText().toString())
      .apply();
    
    Toast.makeText(this, "Registered!", Toast.LENGTH_SHORT).show();
    startActivity(new Intent(this, LoginActivity.class));
});

// 2. LOGIN ACTIVITY (LoginActivity.java)
package com.example.exam;

btn.setOnClickListener(v -> {
    SharedPreferences sp = getSharedPreferences("MyPrefs", MODE_PRIVATE);
    String savedU = sp.getString("U", "");
    String savedP = sp.getString("P", "");
    
    if (u.getText().toString().equals(savedU) && 
        p.getText().toString().equals(savedP)) {
        Toast.makeText(this, "Login Success", Toast.LENGTH_SHORT).show();
    } else {
        Toast.makeText(this, "Login Failed", Toast.LENGTH_SHORT).show();
    }
});"""

i_reg = Image("generated_outputs/reg_screen.png", width=70, height=105)
p_reg = Paragraph("1. Register Screen", img_label_style)
i_log = Image("generated_outputs/login_screen.png", width=70, height=105)
p_log = Paragraph("2. Login Screen", img_label_style)
i_sp = Image("generated_outputs/shared_screen.png", width=70, height=105)
p_sp = Paragraph("3. SharedPrefs Storage", img_label_style)

img_col_2 = Table([[i_reg], [p_reg], [Spacer(1, 2)], [i_log], [p_log], [Spacer(1, 2)], [i_sp], [p_sp]], colWidths=[80])
img_col_2.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))

table_p2 = Table([[make_code_box(code_p2, width=452), img_col_2]], colWidths=[464, 92])
table_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p2)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Formula:</b> <b>Get &rarr; Edit &rarr; Put &rarr; Apply</b> to write | <b>Get &rarr; getString()</b> to read."))


# ================= PAGE 3: TOGGLE IMAGE =================
story.append(PageBreak())
story.append(Paragraph("3. Toggle Image (Dynamic View Switching)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Toggling between two distinct image drawable resources upon button click.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The Two-Way Light Switch:</b><br/>"
    "• Think of a wall switch (<code>boolean isFirstImage = true;</code>).<br/>"
    "• Flip the switch once &rarr; Sun sets, Moon rises (<code>setImageResource(R.drawable.image2)</code>) and mark switch down (<code>false</code>).<br/>"
    "• Flip it again &rarr; Moon sets, Sun rises (<code>setImageResource(R.drawable.image1)</code>) and mark switch up (<code>true</code>)."
))
story.append(Spacer(1, 4))

code_p3 = """package com.example.exam;

public class MainActivity extends AppCompatActivity {
    private boolean isFirstImage = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);
        Button btnToggle = findViewById(R.id.btnToggle);

        btnToggle.setOnClickListener(v -> {
            if (isFirstImage) {
                imageView.setImageResource(R.drawable.image2);
                isFirstImage = false;
            } else {
                imageView.setImageResource(R.drawable.image1);
                isFirstImage = true;
            }
        });
    }
}"""

img_col_3 = make_two_images_column(
    "generated_outputs/toggle_screen1.png", "State 1: image1 (Day)",
    "generated_outputs/toggle_screen2.png", "State 2: image2 (Night)",
    w=108, h=152
)

table_p3 = Table([[make_code_box(code_p3, width=428), img_col_3]], colWidths=[438, 118])
table_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p3)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Core Method:</b> <code>imageView.setImageResource(R.drawable.image_name);</code> accompanied by inverting the boolean flag."))


# ================= PAGE 4: SPINNER COMPONENT =================
story.append(PageBreak())
story.append(Paragraph("4. Spinner Component (Dropdown Selection)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Populating and handling selection events on a dropdown Spinner using ArrayAdapter.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The Restaurant Waiter:</b><br/>"
    "• <b>String[] array:</b> The dishes prepared in the kitchen (Data Source).<br/>"
    "• <b>Spinner:</b> The customer's table (UI View).<br/>"
    "• <b>ArrayAdapter:</b> The Waiter who bridges the kitchen to the table.<br/>"
    "• <b>onItemSelected():</b> The customer taps a dish, and the waiter serves it with a Toast."
))
story.append(Spacer(1, 4))

code_p4 = """package com.example.exam;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        Spinner s = findViewById(R.id.spinner);
        String[] c = {"MCA", "BCA", "B.Tech", "M.Tech"};

        s.setAdapter(new ArrayAdapter<>(this, 
            android.R.layout.simple_spinner_dropdown_item, c));

        s.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> p, View v, int pos, long id) {
                Toast.makeText(MainActivity.this, c[pos], Toast.LENGTH_SHORT).show();
            }
            @Override public void onNothingSelected(AdapterView<?> parent) {}
        });
    }
}"""

img_col_4 = make_two_images_column(
    "generated_outputs/spinner_screen1.png", "State 1: Spinner Closed",
    "generated_outputs/spinner_screen2.png", "State 2: Dropdown Opened & Chosen",
    w=108, h=152
)

table_p4 = Table([[make_code_box(code_p4, width=428), img_col_4]], colWidths=[438, 118])
table_p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p4)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Spinner Flow:</b> <b>Array &rarr; ArrayAdapter &rarr; setAdapter &rarr; setOnItemSelectedListener</b>."))


# ================= PAGE 5: ARRAY ADAPTER WITH LISTVIEW =================
story.append(PageBreak())
story.append(Paragraph("5. ListView with ArrayAdapter (List Scrolling & Item Clicks)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Binding an array of strings to a scrollable ListView and detecting clicked row positions.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The Supermarket Fruit Shelves:</b><br/>"
    "• <b>String[] fruits:</b> Fruit boxes sitting in the store inventory.<br/>"
    "• <b>ListView:</b> The vertical shopping shelves displayed to customers.<br/>"
    "• <b>ArrayAdapter:</b> The shelf-stacker who puts each fruit on a uniform plate (<code>simple_list_item_1</code>).<br/>"
    "• <b>onItemClick():</b> Shopper touches a fruit, and the system announces what was chosen."
))
story.append(Spacer(1, 4))

code_p5 = """package com.example.exam;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        ListView lv = findViewById(R.id.listView);
        String[] fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes"};

        // 1. Adapter bridges String array -> ListView rows
        lv.setAdapter(new ArrayAdapter<>(this, 
            android.R.layout.simple_list_item_1, fruits));

        // 2. Row Click Listener
        lv.setOnItemClickListener((p, v, pos, id) -> 
            Toast.makeText(this, fruits[pos], Toast.LENGTH_SHORT).show()
        );
    }
}"""

img_col_5 = make_two_images_column(
    "generated_outputs/listview_screen1.png", "State 1: Full ListView",
    "generated_outputs/listview_screen2.png", "State 2: Row Clicked (Toast)",
    w=108, h=152
)

table_p5 = Table([[make_code_box(code_p5, width=428), img_col_5]], colWidths=[438, 118])
table_p5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p5)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Key Difference:</b> ListView uses <code>setOnItemClickListener()</code> while Spinner uses <code>setOnItemSelectedListener()</code>."))


# ================= PAGE 6: EXPLICIT INTENT =================
story.append(PageBreak())
story.append(Paragraph("6. Explicit Intent (Screen-to-Screen Navigation & Data Passing)", prog_title_style))
story.append(Paragraph("<b>Concept:</b> Directly launching a specific target activity and transferring string extras between them.", body_text))
story.append(Spacer(1, 3))

story.append(make_story_box(
    "<b>📖 Story — The VIP Courier with Named Envelope:</b><br/>"
    "• <b>Envelope (Intent):</b> Addressed directly from <code>this</code> to <code>SecondActivity.class</code>.<br/>"
    "• <b>putExtra(\"KEY\", val):</b> Slipping the secret message into the envelope before mailing.<br/>"
    "• <b>startActivity():</b> Dispatching the courier off to deliver.<br/>"
    "• <b>getIntent().getStringExtra():</b> Opening the envelope at House #2 to read the message."
))
story.append(Spacer(1, 4))

code_p6 = """// 1. SENDER (MainActivity.java)
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText etName = findViewById(R.id.etName);
        Button btnSend = findViewById(R.id.btnSend);
        btnSend.setOnClickListener(v -> {
            String name = etName.getText().toString();
            Intent intent = new Intent(MainActivity.this, SecondActivity.class);
            intent.putExtra("USER", name);
            startActivity(intent);
        });
    }
}

// 2. RECEIVER (SecondActivity.java)
public class SecondActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        TextView tvWelcome = findViewById(R.id.tvWelcome);
        Intent intent = getIntent();
        String name = intent.getStringExtra("USER");
        tvWelcome.setText("Welcome, " + name + "!");
    }
}"""

img_col_6 = make_two_images_column(
    "generated_outputs/intent_sender.png", "Screen 1: Sender Activity",
    "generated_outputs/intent_receiver.png", "Screen 2: Receiver Activity",
    w=108, h=152
)

table_p6 = Table([[make_code_box(code_p6, width=428), img_col_6]], colWidths=[438, 118])
table_p6.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(table_p6)
story.append(Spacer(1, 4))
story.append(make_memory_box("💡 <b>Sender 3 P's:</b> <b>P</b>repare <code>new Intent(...)</code> &rarr; <b>P</b>ack <code>putExtra(...)</code> &rarr; <b>P</b>ush <code>startActivity()</code>.<br/><b>Receiver 2 G's:</b> <b>G</b>et <code>getIntent().getStringExtra()</code> &rarr; <b>G</b>ive to <code>setText()</code>."))

doc.build(story, onFirstPage=draw_dark_background, onLaterPages=draw_dark_background)
print(f"Rebuilt {pdf_filename} successfully!")
