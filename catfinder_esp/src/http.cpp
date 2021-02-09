#include <http.h>

int send_reading(String UUID, String name, int RSSI) {
  DynamicJsonDocument req(1024);
  req["uuid"] = UUID;
  req["name"] = name;
  req["rssi"] = RSSI;

  String payload;
  serializeJson(req, payload);

  String url = CFG_SERVER + String("/reading/") + CFG_NAME;

  HTTPClient http;
  http.begin(url);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(payload);
  http.end();

  Serial.print("HTTP request sent with code ");
  Serial.println(httpResponseCode);
  return httpResponseCode;
}

int get_frequency() {
  String url = CFG_SERVER + String("/config/frequency");

  HTTPClient http;
  http.begin(url);

  int httpResponseCode = http.GET();
  if (httpResponseCode == 200) {
    return http.getString().toInt();
  }
  return -1;
}

std::vector<String> get_targets() {
  String url = CFG_SERVER + String("/config/targets");

  HTTPClient http;
  http.begin(url);

  std::vector<String> r;

  int httpResponseCode = http.GET();
  if (httpResponseCode == 200) {
    StaticJsonDocument<256> doc;
    String raw = http.getString();
    DeserializationError err = deserializeJson(doc, raw);
    if (err) { Serial.println("Error deserializing json during get targets"); Serial.println(err.f_str()); }
    JsonArray arr = doc["targets"].as<JsonArray>();
    for (JsonVariant v : arr) {
      r.push_back(v.as<String>());
    }
  }
  return r;
}