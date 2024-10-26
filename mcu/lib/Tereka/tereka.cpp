#include "tereka.h"


Preferences     tereka::fs;
Adafruit_Mahony tereka::filter;
MPU9250         tereka::imu;
float           tereka::q_raw[4],
                tereka::q_filt[4];


void tereka::update_q_raw() {
    tereka::q_raw[0] = tereka::imu.getQuaternionW();
    tereka::q_raw[3] = tereka::imu.getQuaternionX();
    tereka::q_raw[2] = tereka::imu.getQuaternionY();
    tereka::q_raw[1] = tereka::imu.getQuaternionZ();
}


void tereka::update_q_filt() {
    float   gx, gy, gz,
            ax, ay, az,
            mx, my, mz;

    gx = tereka::imu.getGyroX()*TEREKA_RADS_TO_DPS;
    gy = tereka::imu.getGyroY()*TEREKA_RADS_TO_DPS;
    gz = tereka::imu.getGyroZ()*TEREKA_RADS_TO_DPS;
    ax = tereka::imu.getAccX();
    ay = tereka::imu.getAccY();
    az = tereka::imu.getAccZ();
    mx = tereka::imu.getMagX();
    my = tereka::imu.getMagY();
    mz = tereka::imu.getMagZ();

    tereka::filter.update(
        gx, gy, gz,
        ax, ay, az,
        mx, my, mz
    );
    tereka::filter.getQuaternion(
        tereka::q_filt + 0,
        tereka::q_filt + 3,
        tereka::q_filt + 2,
        tereka::q_filt + 1
    );
}


void tereka::transmit_data() {
    for(uint8_t i = 0; i < 4; ++i) {
        Serial.print(String(tereka::q_raw[i], 5));
        Serial.print(',');
    }
    for(uint8_t i = 0; i < 4; ++i) {
        Serial.print(String(tereka::q_filt[i], 5));
        Serial.print(',');
    }
    Serial.print('\n');
}


void tereka::calibrate() {
    for(uint8_t i = 0; i < 3; ++i) {
        digitalWrite(TEREKA_PIN_BUZZER, HIGH);
        digitalWrite(TEREKA_PIN_LED, HIGH);
        delay(200);
        digitalWrite(TEREKA_PIN_BUZZER, LOW);
        digitalWrite(TEREKA_PIN_LED, LOW);
        delay(200);
    }
    delay(3000);
    tereka::imu.calibrateAccelGyro();

    for(uint8_t i = 0; i < 3; ++i) {
        digitalWrite(TEREKA_PIN_BUZZER, HIGH);
        digitalWrite(TEREKA_PIN_LED, HIGH);
        delay(200);
        digitalWrite(TEREKA_PIN_BUZZER, LOW);
        digitalWrite(TEREKA_PIN_LED, LOW);
        delay(200);
    }
    delay(3000);
    tereka::imu.calibrateMag();

    tereka::fs.putFloat(TEREKA_FSKEY_ACCBIASX, tereka::imu.getAccBiasX());
    tereka::fs.putFloat(TEREKA_FSKEY_ACCBIASY, tereka::imu.getAccBiasY());
    tereka::fs.putFloat(TEREKA_FSKEY_ACCBIASZ, tereka::imu.getAccBiasZ());
    tereka::fs.putFloat(TEREKA_FSKEY_GYRBIASX, tereka::imu.getGyroBiasX());
    tereka::fs.putFloat(TEREKA_FSKEY_GYRBIASY, tereka::imu.getGyroBiasY());
    tereka::fs.putFloat(TEREKA_FSKEY_GYRBIASZ, tereka::imu.getGyroBiasZ());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGBIASX, tereka::imu.getMagBiasX());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGBIASY, tereka::imu.getMagBiasY());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGBIASZ, tereka::imu.getMagBiasZ());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGSCLEX, tereka::imu.getMagScaleX());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGSCLEY, tereka::imu.getMagScaleY());
    tereka::fs.putFloat(TEREKA_FSKEY_MAGSCLEZ, tereka::imu.getMagScaleZ());

    for(uint8_t i = 0; i < 3; ++i) {
        digitalWrite(TEREKA_PIN_BUZZER, HIGH);
        digitalWrite(TEREKA_PIN_LED, HIGH);
        delay(200);
        digitalWrite(TEREKA_PIN_BUZZER, LOW);
        digitalWrite(TEREKA_PIN_LED, LOW);
        delay(200);
    }
}


void tereka::set_calibration_data() {
    tereka::imu.setAccBias(
        tereka::fs.getFloat(TEREKA_FSKEY_ACCBIASX, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_ACCBIASY, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_ACCBIASZ, 0.0)
    );
    tereka::imu.setGyroBias(
        tereka::fs.getFloat(TEREKA_FSKEY_GYRBIASX, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_GYRBIASY, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_GYRBIASZ, 0.0)
    );
    tereka::imu.setMagBias(
        tereka::fs.getFloat(TEREKA_FSKEY_MAGBIASX, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_MAGBIASY, 0.0),
        tereka::fs.getFloat(TEREKA_FSKEY_MAGBIASZ, 0.0)
    );
    tereka::imu.setMagScale(
        tereka::fs.getFloat(TEREKA_FSKEY_MAGSCLEX, 1.0),
        tereka::fs.getFloat(TEREKA_FSKEY_MAGSCLEY, 1.0),
        tereka::fs.getFloat(TEREKA_FSKEY_MAGSCLEZ, 1.0)
    );
}


void tereka::setup() {
    Serial.begin(115200);
    Wire.begin();
    tereka::fs.begin("TEREKA");
    delay(200);

    pinMode(TEREKA_PIN_BUZZER, OUTPUT);
    pinMode(TEREKA_PIN_LED, OUTPUT);

    tereka::imu.setup(TEREKA_MPU9250_ADDRESS);
    filter.begin(TEREKA_UPDATE_FREQ_HZ);
}


void tereka::loop() {
    bool is_updated = tereka::imu.update();
    delay(TEREKA_UPDATE_PERIOD_MS);

    if(is_updated) {
        tereka::update_q_raw();
        tereka::update_q_filt();
        tereka::transmit_data();
    }
}