"""
Main module of the server file
"""
# local modules
import config
import os

# Get the application instance
app = config.app

# # Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yaml")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
