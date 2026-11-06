package com.example.spinnercomponent;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        Spinner s = findViewById(R.id.spinner);
        String[] c = {"MCA", "BCA", "B.Tech", "M.Tech"};

        s.setAdapter(new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, c));

        s.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> p, View v, int pos, long id) {
                Toast.makeText(MainActivity.this, c[pos], Toast.LENGTH_SHORT).show();
            }
            @Override public void onNothingSelected(AdapterView<?> p) {}
        });
    }
}
