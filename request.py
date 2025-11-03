import requests
import json
from datetime import datetime

url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/e09ec359a2316b880761a869267fccf9?q=VTJGc2RHVmtYMS9hVTR5alpBcnFPZ1FkUVJUMkNObEt3NWsxYzQxOG1XTWZxVGl2bk9CSjZXZjZDYWsrOEdudWZyWGJYZmlQY3ZrUGRmcE5lY216akdYS0xFcGxqMTN2L01SZVhjNEZjOG9URldtYjYzd21JN3IvUURSU2RCU2NqWVhlZFZSNytubmpGV25qMW9oSWdCd0ljaThiVEtvcWZTYVdqaGw3S0FXbEtJR3RzMXZyMUlsNG5nY1VtemZsR1lXL2ovT2dJUXhkMUl0VHkrWmxRS2x2dEMvU3NFOVFpN1JVeVFGSnYrZGV3Smw5SVRlMnVLbWxpT0NlOFdXUnRTaHpFd0ZwVUQ1eVJvcHRvVElsTmt2WWxLNCsyc0RrVllVbXBDWU9mb2llbzVrd2VJRXF4VjRUTjZWemJ6YktMQ2V1NEtCRlR6SjZYbWNya0laM1RvVFhxekl1UUpWakozVjBFNVU0UlhZenFEalF4Sm1yM2h6bWpUdkF5N2JSMDdHZXNLbjdaKzdWWE1YS3RjUFhGMTVDRWNYUlB2akRXRWhMWjRmTTlvK29iZE5vVGRod0FXbUpnelRlK3V3all4RkFJdmZ3UytyaEdmTm8wRUVwRUI3cmhlR3JSVjQyL2dDVWFPL21yT2ZrOHFIM2luYnEzb1Ywc3l0VUlGeGlQRm1aWlY3TGx6ZEVtSVA1Yk5paWtSeTBaUHVTekQ0cUFRUk9YUnl3dWkwRitaMkJlUC9UbVVjMGN3WEdHdmdLeWVlaHhPbmZjQnpWNmpVTm9ZRDg5dm1BVTNDdnF3ZTl5S296eEsrYk9iSG1OL3ZWLzZZYmo0dzh4eTN3NjBsZ1dhMHliRUdGNTZzd3pSWGI4NWlyYzZ0TlFQOHdXdHlEQTA2V0U0bENFR3NwbktIUk5YS3FUYjdyR3pVTHYwMTdUUmliZkkxTWMvY1ZNcithNmlTb0pzb3BwM2ZDR29OQ1p5TGpQVnBncEhTcGFwemd1RmQ1REYyQmkzMloweEY5WTQxK2NVMU4rdWl4NE11ajd1dmZUZz09"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://lvr.land.moi.gov.tw/",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("success")
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("not json")
        data = {"error": "not json", "raw": response.text}

    filename = f"lvr_query_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
else:
    print("fail", response.status_code)
