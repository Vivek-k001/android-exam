package com.example.imagetoggleapp;

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
            imageView.setImageResource(isFirstImage ? R.drawable.image2 : R.drawable.image1);
            isFirstImage = !isFirstImage;
        });
    }
}
