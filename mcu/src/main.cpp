// #define __CALIBRATE__
#include "tereka.h"

void setup() {
    tereka::setup();

    #ifdef __CALIBRATE__
        tereka::calibrate();
    #endif
    tereka::set_calibration_data();
}

void loop() {
    tereka::loop();
}