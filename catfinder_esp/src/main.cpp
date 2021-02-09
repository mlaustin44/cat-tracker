#include <Arduino.h>

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include <secrets.h>

void setup() {
  Serial.begin(9600);
  Serial.println("Starting connection");

  WiFi.begin(SSID, SECRET);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println('.');
  }

  Serial.print("Connected to wifi with IP: ");
  Serial.println(WiFi.localIP());

}

int i = 0;

void loop() {
  DynamicJsonDocument req(1024);
  req["uuid"] = 10101;
  req["name"] = "winky";
  req["rssi"] = i;

  String payload;
  serializeJson(req, payload);

  HTTPClient http;
  http.begin(SERVER);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(payload);
  http.end();

  Serial.print("HTTP request sent with code ");
  Serial.println(httpResponseCode);
  i--;
  delay(5000);
}