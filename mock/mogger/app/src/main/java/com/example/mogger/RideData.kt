package com.example.mogger

data class SensorLogEntry(
    val timestamp: Long,
    val gps: GpsData?,
    val imu: ImuData
)

data class GpsData(
    val lat: Double,
    val lon: Double,
    val speed: Float,
    val accuracy: Float
)

data class ImuData(
    val accel: FloatArray,
    val gyro: FloatArray
)