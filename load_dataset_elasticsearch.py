import random, time
from elasticsearch import Elasticsearch

es = client = Elasticsearch(
    "https://deployment.es.us-central1.gcp.cloud.es.io:9243",
    api_key="API_KEY==",
)

index_name = "logs-apache.access-default"

def get_Elasticsearch_http():
    res = es.search(index=index_name, size=100, body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    result_list = []
    for hit in res['hits']['hits']:
        with open('load.txt', 'w') as file:
            for hit in res['hits']['hits']:
                #ip_from = '8.8.8.8'  # O 'from' é fixo como no exemplo
                #ip_to = f"{generate_ip()}:{generate_port()}"
                #ip_from = hit['_source']['source']['ip']
                try:
                    city_name = hit['_source']['source']['geo']['city_name'].lower()
                    country_iso_code = hit['_source']['source']['geo']['country_iso_code'].lower()
                    ip_to = '128.201.254.243'
                    color = generate_color()
                    line = f"window['raven'].add_to_data_to_table({{'from':'{city_name},{country_iso_code}','to':'{ip_to}'}},{{'line':{{'from':'{color}','to':'{color}'}}}},2000,['line','multi-output','single-output'])\n"
                    file.write(line)
                except:
                    #lat = hit['_source']['source']['geo']['location']['lat']
                    #lon = hit['_source']['source']['geo']['location']['lon']
                    country_iso_code = hit['_source']['source']['geo']['country_iso_code'].lower()
                    ip_to = '128.201.254.243'
                    color = generate_color()
                    line = f"window['raven'].add_to_data_to_table({{'from':'{country_iso_code}','to':'{ip_to}'}},{{'line':{{'from':'{color}','to':'{color}'}}}},2000,['line','multi-output','single-output'])\n"
                    file.write(line)

def generate_color():
    return f"#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}"

while True:
    get_Elasticsearch_http()
    time.sleep(5)
