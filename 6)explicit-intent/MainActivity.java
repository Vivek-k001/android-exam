package com.example.exam;

import android.content.Intent;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        EditText et = findViewById(R.id.etName);
        Button btn = findViewById(R.id.btnSend);

        btn.setOnClickListener(v -> {
            Intent i = new Intent(this, SecondActivity.class);
            i.putExtra("USER", et.getText().toString());
            startActivity(i);
        });
    }
}
