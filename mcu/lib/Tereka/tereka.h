#ifndef __TEREKA_H__
#define __TEREKA_H__

#include <Arduino.h>
#include <Preferences.h>
#include "MPU9250.h"
#include "Adafruit_AHRS.h"

#define TEREKA_MPU9250_ADDRESS  0x68
#define TEREKA_UPDATE_PERIOD_MS 33
#define TEREKA_UPDATE_FREQ_HZ   30
#define TEREKA_RADS_TO_DPS      57.29577951F
#define TEREKA_PIN_BUZZER       32
#define TEREKA_PIN_LED          33

#define TEREKA_FSKEY_ACCBIASX   "j129"
#define TEREKA_FSKEY_ACCBIASY   "coa2"
#define TEREKA_FSKEY_ACCBIASZ   "ap29"
#define TEREKA_FSKEY_GYRBIASX   "2ikf"
#define TEREKA_FSKEY_GYRBIASY   "6n2o"
#define TEREKA_FSKEY_GYRBIASZ   "dg12"
#define TEREKA_FSKEY_MAGBIASX   "xe75"
#define TEREKA_FSKEY_MAGBIASY   "28d4"
#define TEREKA_FSKEY_MAGBIASZ   "q89i"
#define TEREKA_FSKEY_MAGSCLEX   "vzl2"
#define TEREKA_FSKEY_MAGSCLEY   "aewq"
#define TEREKA_FSKEY_MAGSCLEZ   "9pa9"

namespace tereka {
    extern Preferences      fs;
    extern Adafruit_Mahony  filter;
    extern MPU9250          imu;
    extern float            q_raw[4],
                            q_filt[4];

    void update_q_raw();
    void update_q_filt();
    void transmit_data();

    void calibrate();
    void set_calibration_data();
    
    void setup();
    void loop();
}

#endif