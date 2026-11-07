package com.example.exam;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class LoginActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_login);

        EditText u = findViewById(R.id.lu);
        EditText p = findViewById(R.id.lp);
        Button btn = findViewById(R.id.lbtn);

        btn.setOnClickListener(v -> {
            SharedPreferences sp = getSharedPreferences("MyPrefs", MODE_PRIVATE);
            String savedU = sp.getString("U", "");
            String savedP = sp.getString("P", "");

            if (u.getText().toString().equals(savedU) && p.getText().toString().equals(savedP)) {
                Toast.makeText(this, "Login Success", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "Login Failed", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
