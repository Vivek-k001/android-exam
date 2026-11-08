package com.example.exam;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

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
}
