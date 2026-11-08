import re

new_explicit = '''code_p6 = """// 1. SENDER (MainActivity.java)
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
}"""'''

for f_name in ['build_pdf.py', 'build_pdf_dark.py']:
    with open(f_name, 'r') as f:
        content = f.read()
    content = re.sub(r'code_p6 = """.*?"""', new_explicit, content, flags=re.DOTALL)
    with open(f_name, 'w') as f:
        f.write(content)

print("Updated build_pdf scripts successfully!")
