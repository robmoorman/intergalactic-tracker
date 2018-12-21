#! /bin/env python
#
# Copyright 2018 Rob Moorman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import binascii
import json
import os

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from flask import Flask, Response, jsonify, render_template, request

app = Flask(__name__)

DEBUG = os.getenv("DEBUG", True)
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 8080)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/blocks/", methods=["GET"])
def blocks():
    return render_template("blocks.html")


@app.route("/transactions/", methods=["GET"])
def transactions():
    return render_template("transactions.html")


@app.route("/addresses/", methods=["GET"])
def addresses():
    return render_template("addresses.html")


@app.route("/api/wallet/", methods=["GET"])
def api_wallet():
    seed = Random.new().read
    private_key = RSA.generate(1024, seed)
    public_key = private_key.publickey()

    return jsonify({
        "public_key": binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'),
        "private_key": binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    })


@app.route("/healthcheck/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
