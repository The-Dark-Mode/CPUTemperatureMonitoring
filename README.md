# CPU Temperature Monitoring
Monitors the temperature of your linux system and displays it as a clean webpage.

## Setup:
`sudo apt install python3 python3-flask -y`

`python3 app.py`

### Run on Startup
1. **Create a Systemd Service File**

   ```bash
   sudo nano /etc/systemd/system/sensors-app.service
   ```

3. **Add the Service Configuration**

   In the file, add the following content:

   ```ini
   [Unit]
   Description=Sensors Flask App
   After=network.target

   [Service]
   User=root
   WorkingDirectory=/path/to/folder
   ExecStart=/usr/bin/python3 /path/to/folder/app.py
   Restart=always

   # Environment variables (if any)
   Environment="FLASK_APP=app.py"
   Environment="FLASK_ENV=production"

   [Install]
   WantedBy=multi-user.target
   ```

4. **Reload Systemd Daemon**

   ```bash
   sudo systemctl daemon-reload
   ```

6. **Enable the Service to Run on Boot**

   ```bash
   sudo systemctl enable sensors-app.service
   ```

7. **Start the Service Now**

   ```bash
   sudo systemctl start sensors-app.service
   ```

8. **Check the Service Status**

   ```bash
   sudo systemctl status sensors-app.service
   ```

9. **Logs for Debugging**

   If you need to check the logs for your Flask app or the service, you can view the service logs using:

   ```bash
   journalctl -u sensors-app.service -f
   ```

   This will show the live log output.


### Additional Considerations:
- **Virtual Environment**: If you're running the Flask app inside a Python virtual environment, you'll need to modify the `ExecStart` directive to activate the virtual environment. For example:

   ```ini
   ExecStart=/bin/bash -c 'source /path/to/folder/venv/bin/activate && /path/to/folder/venv/bin/python /path/to/folder/app.py'
   ```
