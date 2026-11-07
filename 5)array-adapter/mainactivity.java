package com.example.exam;

import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        ListView lv = findViewById(R.id.listView);
        String[] fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes"};

        lv.setAdapter(new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, fruits));

        lv.setOnItemClickListener((p, v, pos, id) -> 
            Toast.makeText(this, fruits[pos], Toast.LENGTH_SHORT).show()
        );
    }
}
