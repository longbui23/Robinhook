{
	"info": {
		"_postman_id": "e448fd91-2acf-4168-8852-f1880fd4c993",
		"name": "Robinhook",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "40686892"
	},
	"item": [
		{
			"name": "TestAPI",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/prices/latest?symbol=AAPL&provider=yfinance",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"prices",
						"latest"
					],
					"query": [
						{
							"key": "symbol",
							"value": "AAPL"
						},
						{
							"key": "provider",
							"value": "yfinance"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "TestPrometheus",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:9090/api/v1/query?query=1%2B1&time=4",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "9090",
					"path": [
						"api",
						"v1",
						"query"
					],
					"query": [
						{
							"key": "query",
							"value": "1%2B1"
						},
						{
							"key": "time",
							"value": "4"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "Test Poll",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"symbols\": [\"AAPL\", \"MSFT\"],\r\n  \"interval\": 60,\r\n  \"provider\": \"alpha_vantage\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/prices/poll",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"prices",
						"poll"
					]
				}
			},
			"response": []
		}
	]
}