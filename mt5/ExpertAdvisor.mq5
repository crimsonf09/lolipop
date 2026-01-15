#include <Wininet.dll>

void OnTick()
{
   string url = "http://127.0.0.1:8000/trade/predict";
   string payload = "{\"price\":1.234,\"rsi\":25}";
   char result[];
   int res = WebRequest(
      "POST", url,
      "Content-Type: application/json\r\n",
      NULL,
      5000,
      payload,
      result,
      NULL
   );

   string response = CharArrayToString(result);

   if (StringFind(response, "BUY") > 0)
      OrderSend(Symbol(), OP_BUY, 0.1, Ask, 10, 0, 0);
}
