def configure_server(host, port, **metadata):
    print(f"host : {host}")
    print(f"port : {port}")

    if metadata:
        for key,value in metadata.items():
            print(f"{key}:{value}")


configure_server("localhost", 8080, environment="development")
