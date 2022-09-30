# This is a sample Python script.
import swagger_client
from swagger_client import LisApi

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':

    import time
    import swagger_client
    from swagger_client.rest import ApiException
    from pprint import pprint
    api_instance = swagger_client.DownloadApi()
    syst = swagger_client.SystemsApi()
    systems = syst.query(sy="@coords:[41.8781 87.6298 1000 mi] " )
    # convert systems to ids
    # body = list(map(lambda x: x['id'], systems))
    body = [56]  # list[int] | ID of levee system(s)
    full = True  # bool | add all avaliable features to zip (optional)

    try:
        api_response = api_instance.download_dataset_csv_zip_post(body, full=full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_dataset_csv_zip_post: %s\n" % e)
