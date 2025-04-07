package com.example.mogger

import android.os.Bundle
import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.os.Build
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.annotation.RequiresApi
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.example.mogger.ui.theme.MoggerTheme


@RequiresApi(Build.VERSION_CODES.Q)
private val REQUIRED_PERMISSIONS = arrayOf(
    Manifest.permission.ACCESS_FINE_LOCATION,
    Manifest.permission.ACTIVITY_RECOGNITION
)

private val REQUEST_CODE_PERMISSIONS = 1001

@RequiresApi(Build.VERSION_CODES.Q)
private fun checkAndRequestPermissions(ctx: Context, activity: ComponentActivity) {
    val missing = REQUIRED_PERMISSIONS.filter {
        ContextCompat.checkSelfPermission(ctx, it) != PackageManager.PERMISSION_GRANTED
    }

    if (missing.isNotEmpty()) {
        ActivityCompat.requestPermissions(activity, missing.toTypedArray(), REQUEST_CODE_PERMISSIONS)
    } else {
        Toast.makeText(ctx, "All permissions granted!", Toast.LENGTH_SHORT).show()
        startSensorLogging() // we'll define this in step 2
    }
}

fun startSensorLogging() {
    TODO("Not yet implemented")
}


class MainActivity : ComponentActivity() {
    @RequiresApi(Build.VERSION_CODES.Q)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        checkAndRequestPermissions(this, this)

        setContent {
            MoggerTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting(
                        name = "Android",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }

    @Deprecated("Deprecated in Java")
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)

        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (grantResults.all { it == PackageManager.PERMISSION_GRANTED }) {
                Toast.makeText(this, "Permissions granted!", Toast.LENGTH_SHORT).show()
                startSensorLogging()
            } else {
                Toast.makeText(this, "Permissions denied. App won't work.", Toast.LENGTH_LONG).show()
            }
        }
    }

}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    MoggerTheme {
        Greeting("Android")
    }
}