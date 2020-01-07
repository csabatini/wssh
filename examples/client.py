#!/usr/bin/env python

if __name__ == '__main__':
    from wssh import client

    client.invoke_shell('wss://localhost:8443/remote')
