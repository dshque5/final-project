import configuration
import requests

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=order_body)

def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION,
                      params={"t": track_number})
    
    