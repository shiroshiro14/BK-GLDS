package com.example.glds;

import static android.content.ContentValues.TAG;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


public class StatusPanel extends AppCompatActivity {
    private String current_valve;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.status_panel);

        ImageView pipe_logo = findViewById(R.id.pipe_logo);
        TextView pipe_status = findViewById(R.id.pipe_status);
        EditText valve_status = findViewById(R.id.valve_status);
        EditText pressure = findViewById(R.id.pressure);
        EditText gas_level = findViewById(R.id.gas_level);


        valve_status.setEnabled(false);
        gas_level.setEnabled(false);
        pressure.setEnabled(false);

        Button lock_btn = findViewById(R.id.lock_btn);

        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference speaker = database.getReference("2/data");
        DatabaseReference relay = database.getReference("11/data");
        DatabaseReference gas = database.getReference("23/data");

        speaker.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String value = snapshot.getValue(String.class);
                pressure.setText(value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.w(TAG, "Failed to read value.", error.toException());
            }
        });

        relay.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String value = snapshot.getValue(String.class);
                current_valve = value;
                valve_status.setText(value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.w(TAG, "Failed to read value.", error.toException());
            }
        });

        gas.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String value = snapshot.getValue(String.class);
                gas_level.setText(value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.w(TAG, "Failed to read value.", error.toException());
            }
        });

        /*switch(current_valve) {
            case "OPEN":
                lock_btn.setText("LOCK VALVE");
                lock_btn.setBackgroundColor(Color.parseColor("#FF0000"));
                break;
            case "LOCKED":
                lock_btn.setText("RELEASE VALVE");
                lock_btn.setBackgroundColor(Color.parseColor("#00FF00"));
                break;
        }*/

        lock_btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                switch(current_valve) {
                    case "LOCKED":
                        relay.setValue("OPEN");
                        lock_btn.setText("LOCK VALVE");
                        lock_btn.setBackgroundColor(Color.parseColor("#FF0000"));
                        break;
                    case "OPEN":
                        relay.setValue("LOCKED");
                        lock_btn.setText("RELEASE VALVE");
                        lock_btn.setBackgroundColor(Color.parseColor("#00FF00"));
                        break;
                }
            }
        });
    }
}