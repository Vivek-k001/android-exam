package com.example.exam;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import androidx.appcompat.app.AppCompatActivity;

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
}
