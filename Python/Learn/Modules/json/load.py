#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def main():
    data = ""
    with open("data.json", "r") as f:
        data = json.load(f)

    for key, value in data.items():
        print("key = '{}', value = '{}'".format(key, data[key]))

    


if __name__ == "__main__":
    main()

