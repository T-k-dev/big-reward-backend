from flask import Flask, request, jsonify
   import requests
   import os
   from dotenv import load_dotenv

   # Load environment variables
   load_dotenv()

   app = Flask(__name__)
   FLASK_SECRET = os.getenv("FLASK_SECRET")
   BOT_TOKEN = os.getenv("BOT_TOKEN")

   @app.route('/track-click', methods=['POST'])
   def track_click():
       data = request.json
       user_id = data.get('user_id')
       if user_id:
           # Send a message to the user
           url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
           payload = {
               "chat_id": user_id,
               "text": "The 'Check' button was clicked!"
           }
           requests.post(url, json=payload)
           return jsonify({"status": "success"})
       return jsonify({"status": "error", "message": "User ID not provided"}), 400

   if __name__ == '__main__':
       app.run(debug=True)
