import requests
from api_requests.access_token import get_access_token


class Preconditions:
    # token = "Bearer " + req_post.json()["access_token"]
    headers_req = {
        "Authorization": "Bearer " + get_access_token.json()["access_token"],
        "Content-Type": "application/json"
        }

    def create_new_record(self, object_api_name, record_type, name):
        new_account_json = {
            "Name": name,
            "RecordTypeId": record_type,
            }
        create_record = requests.post(f"https://ap4.salesforce.com/services/data/v48.0/sobjects/{object_api_name}",
                                      headers=self.headers_req, json=new_account_json)
        print(create_record.json())
        # input("Press any key")

    def verify_account_created(self):
        params_req = {"q": "SELECT Name From Account "
                           "WHERE Name='test_api_acc_name' "
                           "AND Rating='Warm' "
                           "AND Support_Plan_Expiration_Date__c=2012-02-05 "
                           "AND Has_Support_Plan__c=true"
                      }
        get_records_query = requests.get("https://ap4.salesforce.com/services/data/v48.0/query",
                                         headers=self.headers_req, params=params_req)
        print(get_records_query.json()['totalSize'])


if __name__ == '__main__':
    Preconditions().create_new_record(object_api_name='Account', record_type='0126F000001YvgZQAS',
                                      name='test_api_acc_name')
