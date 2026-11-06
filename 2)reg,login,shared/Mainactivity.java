package com.example.loginregisterapp;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        EditText u = findViewById(R.id.u);
        EditText p = findViewById(R.id.p);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(v -> {
            SharedPreferences sp = getSharedPreferences("MyPrefs", MODE_PRIVATE);
            sp.edit()
              .putString("U", u.getText().toString())
              .putString("P", p.getText().toString())
              .apply();

            Toast.makeText(this, "Registered!", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(this, LoginActivity.class));
        });
    }
}
