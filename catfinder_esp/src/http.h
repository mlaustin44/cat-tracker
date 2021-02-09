#include <secrets.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <Arduino.h>

#include <vector>

int send_reading(String UUID, String name, int RSSI);
int get_frequency();
std::vector<String> get_targets();
