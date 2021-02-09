#include <Arduino.h>

#include <WiFi.h>
#include <vector>

#include <secrets.h>
#include <http.h>

void setup() {
  Serial.begin(9600);
  Serial.println("Starting connection");

  WiFi.begin(CFG_SSID, CFG_SECRET);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println('.');
  }

  Serial.print("Connected to wifi with IP: ");
  Serial.println(WiFi.localIP());

}

int i = 0;

void loop() {
  Serial.println("Trying to get frequency");
  int f = get_frequency();
  Serial.printf("Frequency result: %d\n", f);
  Serial.println("Trying to get targets");
  std::vector<String> v = get_targets();
  Serial.printf("Got %d targets \n", v.size());
  for (String s : v) {
    Serial.println(s);
  }
  delay(5000);
}