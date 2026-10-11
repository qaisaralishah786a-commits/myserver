from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  stringify = "Hello! Mera server bilkul theek kaam kar raha hai aur 24/7 live hai."
  return stringify


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
