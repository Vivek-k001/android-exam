package com.example.explicitintent;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_second);

        TextView tv = findViewById(R.id.tvWelcome);
        String name = getIntent().getStringExtra("USER");
        tv.setText("Welcome, " + name + "!");
    }
}
