# import requests
# from collections import Counter
# import time

# url = "https://apis.zopper.com/accounts/login"
# counts = Counter()


# files = {
#     "username": (None, "samsung_max_croma_admin"),
#     "password": (None, "samsung_max_croma_admin"),
# }


# throttle_seconds = 0.05  # set to 0 for fastest, increase to slow down

# for i in range(1, 101):
#     try:
#         r = requests.post(url, files=files, timeout=10)
#         status = r.status_code
#         counts[status] += 1
#         print(f"{i:3d} -> {status}")
#     except requests.exceptions.Timeout:
#         counts["timeout"] += 1
#         print(f"{i:3d} -> TIMEOUT")
#     except requests.exceptions.RequestException as e:
#         counts["error"] += 1
#         print(f"{i:3d} -> ERROR ({e.__class__.__name__})")
#     if throttle_seconds:
#         time.sleep(throttle_seconds)

# print("\nSummary:", dict(counts))


import requests
from collections import Counter
import time
import re

url = "https://apis.zopper.com/accounts/login"
counts = Counter()

USERNAME = "samsung_max_croma_admin"
PASSWORD = "samsung_max_croma_admin"

files = {
    "username": (None, USERNAME),
    "password": (None, PASSWORD),
}

throttle_seconds = 0.05  # set to 0 for fastest, increase to slow down
TIMEOUT = 10
REDACT_PASSWORD = True  # set False only if you really want raw password printed
MAX_PRINT_BODY = 1000    # max chars to print for bodies (request/response)

session = requests.Session()

# Precompile simple regex to find the password value in multipart body (as bytes)
password_bytes = PASSWORD.encode("utf-8")
# we'll replace the raw password bytes with b"REDACTED"
replacement_bytes = b"REDACTED"

for i in range(1, 101):
    # prepare request so we can print the exact request that will be sent
    req = requests.Request("POST", url, files=files)
    prepped = session.prepare_request(req)

    try:
        resp = session.send(prepped, timeout=TIMEOUT, allow_redirects=True)
        status = resp.status_code
        counts[status] += 1
        print(f"{i:3d} -> {status}")

        if status != 200:
            print("\n===== NON-200 RESPONSE - DETAILS =====")
            # --- Request line + headers ---
            print("----- REQUEST -----")
            print(f"{prepped.method} {prepped.url}")
            for k, v in prepped.headers.items():
                print(f"{k}: {v}")

            # --- Request body (possibly bytes) ---
            body = prepped.body
            if body is None:
                print("(no body)")
            else:
                # Body can be bytes or str; convert to bytes then decode safely for printing
                try:
                    if isinstance(body, str):
                        bbody = body.encode("utf-8", errors="replace")
                    else:
                        bbody = body
                except Exception:
                    bbody = bytes(str(body), "utf-8", errors="replace")

                if REDACT_PASSWORD and password_bytes in bbody:
                    bbody = bbody.replace(password_bytes, replacement_bytes)

                try:
                    decoded_body = bbody.decode("utf-8", errors="replace")
                except Exception:
                    decoded_body = repr(bbody)

                # Truncate long bodies for readability
                if len(decoded_body) > MAX_PRINT_BODY:
                    print(decoded_body[:MAX_PRINT_BODY])
                    print("... (truncated)")
                else:
                    print(decoded_body)

            # --- Response summary + headers + truncated body ---
            print("\n----- RESPONSE -----")
            print(f"Status: {resp.status_code}")
            for k, v in resp.headers.items():
                print(f"{k}: {v}")
            text = resp.text or ""
            if len(text) > MAX_PRINT_BODY:
                print(text[:MAX_PRINT_BODY])
                print("... (truncated)")
            else:
                print(text)
            print("===== END DETAILS =====\n")

    except requests.exceptions.Timeout:
        counts["timeout"] += 1
        print(f"{i:3d} -> TIMEOUT")
    except requests.exceptions.RequestException as e:
        counts["error"] += 1
        print(f"{i:3d} -> ERROR ({e.__class__.__name__}): {e}")

    if throttle_seconds:
        time.sleep(throttle_seconds)
