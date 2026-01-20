url= "http://wwww.google.com"

if url.startswith("http://") or url.startswith("https://"):
    if url.endswith(".com") or url.endswith(".co"):
        print("valid url")
    else:
        print("not valid")
else:
    print("invalid")